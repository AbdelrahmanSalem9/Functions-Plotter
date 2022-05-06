# Function Plotter Program

## Objective
Implements simple GUI program to plot user-entered function in specific plot range

## Description
Python code for reading input function from the user in simple gui window then try to parse the input for the plotting function 
that isbased on eval built-in function of python thats basically try to generate continuous values for the domain and plot it on another window
mainly the eval function works with single variable polynomial, trignometric functions from {sin,cos,tan} and logarithmic function with base 2 and 10 only

## Error check
the program support some invalid and missing user inputs like:
1. Missing function expression
2. Invalid function expression or complicated function can't be computed naively
3. Missing Min or Max inputs
4. Invalid Ranges for Min and Max inputs, (min > max)
addionlly the program support for both {**,^} exponent operators

# Files
the program consists of mainly four files
- app.py
- controller.py
- constant.py
- test.py

### 1-app.py
contains all the GUI components and user input parsing to the controller.py file that contain the input proccessing of error and may be extended for more features later additionally contain the plotting function

### 2-controller.py
contains the input user processing of error checks and any modification needed for the program

### 3-constant.py
contains all pre-defined variables from titles, font size, etc.

### 4-test.py
plot all valid pre-defined functions in the constant.py file for test check

# App Dependencies
 - pip install numpy
 - pip install matplotlib
 - pip install tk

# Notes
- The input function should be defined in continous range eg 1/x can't be defined with 0
- All snips of the program and test functions included in the img folder, I tried to test all possible functions randomly but due to eval function maybe unexpected happens with test some functions 

# Run
to run the app
- python app.py

to see the the test functions
- python test.py
 
 
 
 
 
 
