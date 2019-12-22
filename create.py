import sys
import os
import inputs
from github import Github

def create():
    folderName = str(sys.argv[1])
    public_private = str(sys.argv[2])
    os.makedirs(inputs.dir_path + str(folderName))
    user=Github(inputs.token).get_user()
    if (public_private == "private"):
        user.create_repo(folderName, private=True)
    if (public_private == "public"):
        user.create_repo(folderName)
    os.chdir(inputs.dir_path + str(sys.argv[1]))
    with open("README.md", "w") as text_file:
        text_file.write("==README==")
    with open(".gitignore", "w") as text_file:
        text_file.write("venv\n")
        text_file.write(".vscode")
    os.system("git init")
    os.system("git add README.md")
    os.system("git add .gitignore")
    os.system('git commit -m "first commit"')
    os.system("git remote add origin https://github.com/{0}/{1}.git".format(inputs.user,sys.argv[1]))
    os.system("git push -u origin master")
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
