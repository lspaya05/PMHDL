# Name: Leonard Paya
# Date: 09/20/2025

# A Function that displays functions to choose from, and what each function does.
import sys

def main():
    print(f"---------- Welcome to the .do File and Simulation Manager ----------")
    print(f"Options to Choose From: ")

    print(f"    * setup: Sets up the project, including the folder skeleton as well as the specific")
    print(f"             functions below. Must include a 'ProjectName'  typing method call")
    print(f"        -s: .")
    print(f"        -g: .")

    print(f"    * update: Updates src and tb file list in the the file 'runSim.do' that has been") 
    print(f"              set up.")
    print(f"        -n: .")
    print(f"        -n: .")
    print(f"        -n: .")

    print(f"    * edit: changes either the tb being run, or the simulation file to run.")
    print(f"        -tb: Changes the current testbench file to run, 2nd arguement is tb name.")
    print(f"        -sim: Changes the current simulation file to run, 2nd arguement is sim file name.")
    print(f"        -ts: calls the 2 functions abovem 2nd arg. is tb name, 3rd arg. is sim file name")

    print(f"    * sim: Displays current runSim.do file, including all of the option below.")
    print(f"        -src: shows only all the src files loaded.")
    print(f"        -tb: shows only all the tb files loaded.")
    print(f"        -sim: shows current tb being tested and the file name of the resulting wave.")

    print(f"    * list: Lists some collection of files that have been created.")
    print(f"        -w: Lists the '...wave.do' simulations that have been created and can be choosen from.")
    print(f"        -s: Lists the source Files that have been saved in 'runsim.do' script.")
    print(f"        -t: Lists the Testbench files that are not empty.")


    print(f"    * help: Displays a list of all the available functions")

if __name__ == "__main__":
    main()