# Name: Leonard Paya
# Date: 09/20/2025
#

# To be used when starting a project for the first time, and or adding a gitIgnore and or a
# simulation script. This is only to be used at the beginning of a project, and WILL OVERWRITE
# EXISTING PROJECTS AND FOLDERS with the same name.

# Current Functionality
#   - New Project (arg1 = "ProjectNameHere"): Creates a new project with a folder 
#                                    skeleton, an Intel Sim .do file, and a Git Ignore file. 
#   - Setup Intel Sim (arg1 = '-s'): Sets up the runsim.do file is used for Model Sim and Questa
#                                    Simulation tools
#   - Setup Git Ignore (arg1 = '-g'): Adds a Git Ignore file in the current working directory that 
#                                     targets temp files for: Quartus, Simulations, Vivado, Latex.

# Future Functionality:
#   - 

import os
import sys
import shutil


# Where arg 1 should be the tag, and arg2 is some String 
def main(arg1, arg2):
    if arg1 == "-n":
        setupFolders(arg2)
        setupGitIgnore()
        setupSim()

    if arg1 == "-s":
        setupSimIntel()

    if arg1== "-g":
        setupGitIgnore()
     
    
def getRootPath():
    thisFile = os.path.dirname(os.path.abspath(__file__))
    projectRoot = os.path.abspath(os.path.join(thisFile, ".."))
    return projectRoot

#Sets up the .do file for use with Questa and ModelSim. The output is a .do file under sim.
# Expected to be run inside the project folder, no catch 
def setupSim():
    status = ""

    templateFile = os.path.join(getRootPath(), "templates", "runsim.do")

    dest = os.path.join(os.getcwdw(), os.path.basename(templateFile))

    try:
        shutil.copyfile(templateFile, dest)
        status = "Successful"
    except FileNotFoundError:
        status = "Error: Simulation Template File not Found"
    except Exception as e:
        status = "An unexpected error occurred: {e}"

    print(f"Simulation File Setup: " + status)


# Sets up the Project Scaffolding. The output is a collection folders under the current working
# directory.
def setupFolders(projectName):
    path = os.path.join(projectName, "benchmarks")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(projectName, "description")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(projectName, "quartus")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(projectName, "sim", "modelsim")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(projectName, "src")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(projectName, "tb")
    os.makedirs(path, exist_ok=True)

    path = os.path.join(projectName, "vivado")
    os.makedirs(path, exist_ok=True)

# Sets up a Git Ignore file that excludes files that are not neccesary when using with Git.
# Saved under the current working directory.
def setupGitIgnore():
    

# The Script that runs main when this file is called.
if __name__ == "__main__":
    main()
