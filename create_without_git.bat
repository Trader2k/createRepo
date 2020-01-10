:: ENTER PATH WHERE THE create.py an remove.py ARE LOCATED.
:: /D is needed to change drive selection (if not C:)

cd /D <SCRIPT_PATH>

::---------------------------------------------------------
python create_without_git.py %1

::---------------------------------------------------------
:: ENTER PATH WHERE YOUR PROJECTS ARE SAVED
:: e.g. C:\Users\<USERNAME>\Documents\Projects
cd <PROJECT_PATH>%1

::---------------------------------------------------------
:: OPENS VISUAL STUDIO CODE
code .