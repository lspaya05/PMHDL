# Project Manager for Hardware Description Languages

## Installation

## Current Functionality
To invoke the CLI, use `pmhdl` before calling a specific function. Below are some callable functions:

### General Functions
- `pmhdl`: Provides a list of commonly used functions and a very quick explaination of its use.

- `pmhdl help`: Provides a list of all used functions, and explains what each does.

- `pmhdl version`: Provides the current version, and describes the added functionality.

### Management Functions

- `pmhdl setup "ProjectName"`: 
  - `-s` | `--sim`: 
  - `-g` | `--gitignore`: 

- `pmhdl list`:
  - `-s` | `--sim`:
  - `-q` | `--quartus`:
  - `-v` | `--vivado`: 
  - `-w` | `--wave`: 

- `pmhdl update`:
  - `-s` | `--sim`:
  - `-q` | `--quartus`:
  - `-v` | `--vivado`:
  - `-tb` | `--testbench`: 

- `pmhdl sim`:
  - `-tb` | `--testbench`: 
  - `-w`  | `--wavefile`:  

- `pmhdl clean`: Removes uncessary Modelsim, Quartus, and Vivado files.

> [!CAUTION]
> Clean has not been tested extensively to not break any Quartus or Vivado Functionality.



## Future Functionality

## Known Issues

## Task to Complete

