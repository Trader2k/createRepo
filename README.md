# Project Creation Automation for WINDOWS

## Inspiration

This project is inspired by Kalle Halden (<https://github.com/KalleHallden)> AND Tim Eichinger (<https://github.com/eichingertim).> He had the idea to this project and made it working for MacOS.\
Check his repository out:<https://github.com/KalleHallden/ProjectInitializationAutomation> \
Check his repository out:<https://github.com/eichingertim/ProjectCreationAutomation>

Create automatically Repository, Folder, README.md and gitignore (venv, .vscode). For windows systems

## How to install

**BEFORE CLONING** make sure that you have already installed the newest version of python and you succesfully added it to your SYSTEM-PATH.

---

Goto your command-line (cmd) and navigate to the location where you want to clone this project. Then type:

``` bash
git clone "https://github.com/trader2k/createRepo"
cd createRepo
pip install -r requirements.txt
```

Then edit the three files
**create.bat** and
**remove.bat** and
**inputs.py** where necessary (marked and described with comments).

**IMPORTANT**: ADD createRepo-PATH to SYSTEM-PATH.

1. type **env** to your windows-search and hit enter. A dialog with system-properties should appear.
2. Click on the Button with **Environment Variables**
3. In the System Variables window, highlight **Path** in the upper section, and click **Edit**.
4. In the Edit System Variables window, click **New** and add the full path to the new created line.
5. Click **OK** in each open windows

## How to use it

### CREATE

To create a new project just open your command-line (cmd) and type in a command with the following syntax:

``` bash
create <ProjectName> <private/public>
```

### REMOVE

**USE WITH CAUTION - DELETING without question** \
To delete a Projekt and remove the repository open the command-line (cmd) and type in:

``` bash
remove <ProjektName>
```
