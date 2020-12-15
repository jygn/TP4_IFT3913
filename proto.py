import sys
import git
import os
import shutil
import stat
import csv
import subprocess
import pandas as pd
import statistics

# deconstruct url to clone via ssh
url = str(sys.argv[1])  # https://github.com/bendag/TP1_IFT3913
dirpath = 'clone_repo'

# check if repo already exist, if true delete it.
if os.path.exists(dirpath) and os.path.isdir(dirpath):
    print('git repos already exist')
    # shutil.rmtree(dirpath)    # javais un bug avec windows10
    os.system('rmdir /S /Q "{}"'.format(dirpath))  # TODO voir si ca marche sous linux
    print('repo remove')

# checkout repo
print('create repo')
git.Repo.clone_from(url, dirpath)

# count the number of commits to assign a hexadecimal version number
my_repo = git.Repo('clone_repo')
commits = list(my_repo.iter_commits('HEAD'))


# Compte le nombre de fichier dans un directory selon l'extension
def files_counter(path, ext):
    files_nb = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                files_nb += 1

    return files_nb


# execute tp1 metric
def start_tp1(metric_software_name, path):
    # os.system("java -jar " + metric_software_name + " " + dir_path)
    p = subprocess.Popen(["java", "-jar", metric_software_name, path],
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         universal_newlines=True)  # this is for text communication
    p.stdin.write("1\n")
    p.stdin.close()
    p.stdout.close()
    p.wait()


# analyse CSV file
def get_csv_column(file_name, column_name):
    csv_data = pd.read_csv(file_name)
    t = csv_data[column_name].values
    return csv_data[column_name]


with open('data_output.csv', 'w', newline='') as file:
    data = []

    for commit in commits:
        hex_id = commit.hexsha
        os.system("cd " + dirpath + " && git reset --hard " + hex_id)

        start_tp1('TP1_IFT3913_project.jar', dirpath)
        classes_BC = get_csv_column('classes.csv', "classe_BC").values

        if not len(classes_BC):
            m_c_BC = "nan"
        else:
            m_c_BC = statistics.median(classes_BC)

        n_classes = files_counter(dirpath, ".java")
        data.append([hex_id, n_classes, m_c_BC])

    writer = csv.writer(file)
    writer.writerow(["id_version", "n_classes", "m_c_BC"])
    writer.writerows(data)
