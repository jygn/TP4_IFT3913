import math
import sys
import git
import os
import shutil
import csv
import pandas as pd
import statistics
import random

# deconstruct url to clone via ssh
url = str(sys.argv[1])  # https://github.com/bendag/TP1_IFT3913
dirpath = 'clone_repo'

# check if repo already exist, if true delete it.
if os.path.exists(dirpath) and os.path.isdir(dirpath):
    print('git repos already exist')
    if sys.platform == "linux" or sys.platform == "linux2":
        shutil.rmtree(dirpath)
    if sys.platform == "win32":
        os.system('rmdir /S /Q "{}"'.format(dirpath))
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


# analyse CSV file
def get_csv_column(file_name, column_name):
    csv_data = pd.read_csv(file_name)
    return csv_data[column_name]


def get_commits_sample(commits_list):
    sample_size = int(len(commits_list) * (10 / 100))
    return random.sample(commits_list, sample_size)


with open('data_output.csv', 'w', newline='') as file:
    data = []
    commits_sample = get_commits_sample(commits)  # random sample (10% of initial list)

    for commit in commits_sample:
        hex_id = commit.hexsha
        os.system("cd " + dirpath + " && git reset --hard " + hex_id)

        os.system("java -jar TP1_IFT3913_project.jar " + dirpath)    # run tp1
        classes_BC = get_csv_column('classes.csv', "classe_BC").values

        if not len(classes_BC):
            m_c_BC = 0
        else:
            m_c_BC = statistics.median(classes_BC)
            if math.isnan(m_c_BC):
                m_c_BC = 0

        n_classes = files_counter(dirpath, ".java")
        data.append([hex_id, n_classes, m_c_BC])

    writer = csv.writer(file)
    writer.writerow(["id_version", "n_classes", "m_c_BC"])
    writer.writerows(data)
