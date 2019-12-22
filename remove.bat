:: ENTER PATH WHERE THE create.py an remove.py ARE LOCATED.
:: /D is needed to change drive selection (if not C:)
:: EXAMPLE-PATH: D:\Python_projects\createRepoFolder

cd /D <SCRIPT_PATH>

::---------------------------------------------------------
python remove.py %1

