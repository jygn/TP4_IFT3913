import sys
import git
import os
import shutil

#deconstruct url to clone via ssh
url = str(sys.argv[1])
dirpath = 'clone_repo'

#check if repo already exist, if true delete it.
if(os.path.exists(dirpath) and os.path.isdir(dirpath)):
    print('git repos already exist')
    shutil.rmtree(dirpath)
    print('repo remove')

#checkout repo
print('create repo')
git.Repo.clone_from(url, dirpath)

#count the number of commits to assign a hexadecimal version number
my_repo = git.Repo('clone_repo')
commits = list(my_repo.iter_commits('HEAD'))
count = len(commits)

version = hex(count)

print('id_version: ' + version)

#
