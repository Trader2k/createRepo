:: ENTER PATH WHERE THE create.py an remove.py ARE LOCATED.
:: /D is needed to change drive selection (if not C:)
:: EXAMPLE-PATH: D:\Python_projects\createRepoFolder

cd /D <SCRIPT_PATH>

::---------------------------------------------------------
python create.py %1 %2

::---------------------------------------------------------
:: ENTER PATH WHERE YOUR PROJECTS ARE SAVED 
:: %1 IS IMPORTED AT THE END OF THE PATH
:: e.g. C:\Users\<USERNAME>\Documents\Projects

cd /D <PROJECT_PATH>%1

::---------------------------------------------------------
:: OPENS VISUAL STUDIO CODE
code .