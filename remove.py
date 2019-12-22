import sys
import os
import shutil
import inputs
from github import Github

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        pass   
    
def remove():
    folderName = str(sys.argv[1])
    os.chdir(inputs.dir_path)
    user = Github(inputs.token).get_user()
    repo = user.get_repo(folderName)
    repo.delete()
    shutil.rmtree(folderName, onerror=onerror)


if __name__ == "__main__":
    remove()
