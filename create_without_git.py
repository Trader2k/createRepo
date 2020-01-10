import sys
import os
import inputs


def create():
    folderName = str(sys.argv[1])
    os.makedirs(inputs.dir_path + str(folderName))
    os.chdir(inputs.dir_path + str(sys.argv[1]))
    with open("README.md", "w") as text_file:
        text_file.write("==README==")
    with open(".gitignore", "w") as text_file:
        text_file.write("venv\n")
        text_file.write(".vscode")
    print("Succesfully created repository {}".format(folderName))


if __name__ == "__main__":
    create()
