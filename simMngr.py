# Name: Leonard Paya
# Date: 

# A CLI Tool that can easily create and manage projects for System Verilog. Also manages Simulation and tool management.

import os
import sys
import subprocess
import shutil

#defirectoryPath = "** /"
#ontents = os.listdir()

# Prompt User Input:
commands = {
    #"setup": setup,
    #"update": update,
    #"edit": edit,
    #"run": run,
    #"settings": settings,
    #"help":
}


    

# MISC:
def loading_bar(iteration, total, length = 50):
    percent = int((iteration / total) * 100)
    filled = int(length * iteration // total)
    bar = "█" * filled + "-" * (length - filled)
    sys.stdout.write(f"\r|{bar}| {percent}%")
    sys.stdout.flush()

print(f"simMngr-{sys.argv[1]}")
print(os.path.dirname(os.path.abspath(__file__)))
print(shutil.which("simMngr-{sys.argv[1]}"))

# For a CLI Tool, Still in development:
# def main():
#     if len(sys.argv) > 3:
#         print("Invalid function: Max number of arguments: 2")
#         print("Available built-in commands:", ", ".join(commands.keys()))
#         return
    
#     cmd = sys.argv[1]
#     args = sys.argv[2:]

#     exProgramName = f"simMngr-{cmd}"
#     path = shutil.which(exProgramName)
    
#     # If file not in path, check a specific folder (used in development)
#     if not path: 
#         currFileLocation = os.path.dirname(os.path.abspath(__file__))
#         possibleLoc = os.path.join(currFileLocation, "subCommands", exProgramName)
        
#         if os.path.isfile(possibleLoc) and os.access(possibleLoc, os.X_OK):
#             path = possibleLoc

#         # Deals with Windows and Unix system stuff...
#         if os.path.isfile(possibleLoc):
#             # On Windows: run with Python
#             if sys.platform.startswith("win") and possibleLoc.endswith(".py"):
#                 path = None
#                 subprocess.run([sys.executable, possibleLoc] + args)
#                 return
#             # On Unix: require executable bit
#             elif os.access(possibleLoc, os.X_OK):
#                 path = possibleLoc

#     # Final path check:
#     if path: 
#         subprocess.run([path] + args)
#     else: 
#         print(f"Unknown Command: {cmd}")
# main()
        



