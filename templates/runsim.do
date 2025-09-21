# -----     DO NOT EDIT UNLESS YOU KNOW WHAT YOU ARE DOING     ----- #
# ----- This is the a simple script to run ModelSim and Questa ----- #
# -----        Credit: University of Washington Department     ----- #
# -----          of Electrical and Computer Engineering.       ----- #

# Create work library
vlib work

# Compile Verilog
#     All Verilog files that are part of this design should have
#     their own "vlog" line below.

# SV Files here:

# TestBench Files here:

# Call vsim to invoke simulator
#     Make sure the last item on the line is the name of the
#     testbench module you want to execute.
vsim -voptargs="+acc" -t 1ps -lib work 

# Source the wave do file
#     This should be the file that sets up the signal window for
#     the module you are testing.
do 

# Set the window types
view wave
view structure
view signals

# Run the simulation
run -all
