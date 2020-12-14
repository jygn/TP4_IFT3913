import sys
import git
import os
import shutil
import csv
import subprocess

# deconstruct url to clone via ssh
url = str(sys.argv[1])
dirpath = 'clone_repo'

# check if repo already exist, if true delete it.
if os.path.exists(dirpath) and os.path.isdir(dirpath):
    print('git repos already exist')
    shutil.rmtree(dirpath)
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


with open('data_output.csv', 'w', newline='') as file:
    data = []

    for commit in commits:
        hex_id = commit.hexsha
        os.system("cd " + dirpath + " && git reset --hard " + hex_id)
        n_classes = files_counter(dirpath, ".java")
        data.append([hex_id, n_classes])

    writer = csv.writer(file)
    writer.writerow(["id_version", "n_classes"])
    writer.writerows(data)


# execute tp1 metric
def mediane_classe_BC(metric_software_name, dir_path):
    # os.system("java -jar " + metric_software_name + " " + dir_path)
    p = subprocess.Popen(["java", "-jar", metric_software_name, dir_path],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)  # this is for text communication
    p.stdin.write("1\n")


mediane_classe_BC('TP1_IFT3913_project.jar', dirpath)
