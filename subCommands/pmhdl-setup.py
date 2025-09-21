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
import sys
import os


# Where arg 1 should be the tag, and arg2 is some String 
def main(arg1, arg2):
    if arg1 == "-n":
        setupFolders(arg2)
        setupGitIgnore()
        setupSimIntel()

    if arg1 == "-s":
        setupSimIntel()

    if arg1== "-g":
        setupGitIgnore()
     
    
#Sets up the .do file for use with Questa and ModelSim. The output is a .do file under sim/modelsim.
def setupSimIntel():
    lines = [
        "# Create work library - DO NOT EDIT THE COMMENTS IN THIS FILE\n",
        "vlib work\n",
        "\n",
        "# Compile Verilog\n",
        "#     All Verilog files that are part of this design should have\n",
        "#     their own \"vlog\" line below.\n",
        "\n",
        "# SV Files here:\n",
        "\n",
        "# TestBench Files here:\n",
        "\n",
        "# Call vsim to invoke simulator\n",
        "#     Make sure the last item on the line is the name of the\n",
        "#     testbench module you want to execute.\n",
        "vsim -voptargs=\"+acc\" -t 1ps -lib work \n",
        "\n",
        "# Source the wave do file\n",
        "#     This should be the file that sets up the signal window for\n",
        "#     the module you are testing.\n",
        "do \n",
        "\n",
        "# Set the window types\n",
        "view wave\n",
        "view structure\n",
        "view signals\n",
        "\n",
        "# Run the simulation\n",
        "run -all\n",
    ]

    filePath = os.path.join("sim", "modelsim", "runSim.do")
    print(filePath)
    with open(filePath, "w") as file:
        file.writelines(lines)

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
    lines = [
        "# ========================\n",
        "# Global Ignores\n",
        "# ========================\n",
        "*.log\n",
        "*.jou\n",
        "*.tmp\n",
        "*.bak\n",
        "*~\n",
        "\n",
        "# ========================\n",
        "# Vivado-Specific Ignores\n",
        "# ========================\n",
        "/vivado/.Xil/\n",
        "/vivado/*.cache/\n",
        "/vivado/*.hw/\n",
        "/vivado/*.ip_user_files/\n",
        "/vivado/*.runs/\n",
        "/vivado/*.sim/\n",
        "/vivado/*.webtalk/\n",
        "/vivado/.Xil/\n",
        "/vivado/*.str\n",
        "/vivado/*_backup.xpr\n",
        "/vivado/*.dmp\n",
        "/vivado/*.restore\n",
        "\n",
        "# Optional: Ignore Vivado-generated project files if storing only sources\n",
        "/vivado/*.xpr\n",
        "/vivado/*.xpr.user\n",
        "/vivado/*.xgui\n",
        "/vivado/*.dcp\n",
        "/vivado/*.ltx\n",
        "/vivado/*.xml\n",
        "\n",
        "# ========================\n",
        "# Quartus-Specific Ignores\n",
        "# ========================\n",
        "/quartus/db/\n",
        "/quartus/incremental_db/\n",
        "/quartus/output_files/\n",
        "/quartus/*.rpt\n",
        "/quartus/*.qws\n",
        "/quartus/*.smsg\n",
        "/quartus/*.bak*\n",
        "/quartus/*.chg\n",
        "/quartus/*.pof\n",
        "/quartus/*.sof\n",
        "/quartus/*.sdf\n",
        "/quartus/*.jam\n",
        "/quartus/*.jic\n",
        "/quartus/*.summary\n",
        "/quartus/*.pin\n",
        "/quartus/*.qdf\n",
        "\n",
        "# ========================\n",
        "# Simulation Outputs\n",
        "# ========================\n",
        "/sim/modelsim/work/\n",
        "/sim/*.wlf\n",
        "/sim/modelsim/transcript\n",
        "/sim/modelsim/vsim.wlf\n",
        "/sim/modelsim.ini\n",
        "/sim/*.log\n",
        "/sim/*.vcd\n",
        "/sim/*.vpd\n",
        "/sim/*.svf\n",
        "\n",
        "# ========================\n",
        "# IDE / OS Misc\n",
        "# ========================\n",
        ".vscode/\n",
        ".idea/\n",
        "*.DS_Store\n",
        "Thumbs.db\n",
        "\n",
        "# ========================\n",
        "# Latex\n",
        "# ========================\n",
        "*.aux\n",
        "*.fdb_latexmk\n",
        "*.fls \n",
        "*.gz",
    ]

    with open(".gitignore", "w") as file:
        file.writelines(lines)

# The Script that runs main when this file is called.
if __name__ == "__main__":
    main()
