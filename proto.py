import sys
import git
import os
import shutil

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
git.Repo.clone_from(url, dirpath, no_checkout=True)

# count the number of commits to assign a hexadecimal version number
my_repo = git.Repo('clone_repo')
commits = list(my_repo.iter_commits('HEAD'))


# Compte le nombre de fichier selon son extension d'un dossier récursivement
def files_counter(path, ext):
    files_nb = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                files_nb += 1

    return files_nb


for commit in commits:
    hex_id = commit.hexsha
    os.system("cd " + dirpath + " && git reset --hard " + hex_id)
    n_classes = files_counter(dirpath, ".java")

