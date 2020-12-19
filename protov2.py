import sys
import git
import os
import shutil
import csv
import pandas as pd
import statistics
import random
from threading import Thread

# conts
repo_dir = 'clone_repo'
repos_dir = 'clones_repo'

# deconstruct url to clone via ssh
url = str(sys.argv[1])  # https://github.com/bendag/TP1_IFT3913

# check if repo already exist, if true delete it.
if os.path.exists(repo_dir) and os.path.isdir(repo_dir):
    print('git repos already exist')
    if sys.platform == "linux" or sys.platform == "linux2":
        shutil.rmtree(repo_dir)
    if sys.platform == "win32":
        os.system('rmdir /S /Q "{}"'.format(repo_dir))
    print('repo remove')

# checkout repo
print('create repo')
git.Repo.clone_from(url, repo_dir)
my_repo = git.Repo('clone_repo')
commits = list(my_repo.iter_commits('HEAD'))

# get a sample of commit (10%)
def get_commits_sample(commits_list):
    sample_size = int(len(commits_list) * (10 / 100))
    return random.sample(commits_list, sa
def start_tp1(metric_software_name, path):
    os.system("java -jar " + metric_software_name + " " + path)

commits_sample = get_commits_sample(commits)    # random sample (10% of initial list)

# iterate in each commit of  the sample to get classes statistic
os.system('mkdir ' + repos_dir) 
threads = []

for commit in commits_sample:
    hex_id = commit.hexsha
    os.system('mkdir ' + repos_dir + '/' + hex_id) #create direcory for specific head id
    os.system('cp -a ' + repo_dir + ' ' + repos_dir + '/' + hex_id + '/') #copy clone_repo

    path = repos_dir + '/' + hex_id + '/' + repo_dir
    os.system("cd " + path + " && git reset --hard " + hex_id)

    # clone_path = repos_dir + '/' + hex_id + '/' + repo_dir
    # t = Thread(target=start_tp1, args=('TP1_IFT3913_project.jar', clone_path))
    # t.start()
    # threads.append(t)

# #join all threads
# for t in threads:
#     t.join()




print('all threads are done')








