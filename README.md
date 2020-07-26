# Mower Simulator

Technical test for the Junior ML Engineer position at BlaBlaCar (summer 2020).


## Description

The project contains a Python package `mowers` containing a lawn mowing simulator.
This package is fully unit tested within the folder `tests`.

In the root folder, you will find a python script using the package with input files located in `input` folder.
Feel free to add other input files in it in order to test the package.


## Get Started

### Installation

Make sure to have Python 3 installed on your computer (the project has been made with Python 3.7.4):
```
python3 --version
```


You can also make a virtual environment an run it, although no third tier party library has been used within this project.
```
python3 -m venv env
source env/bin/activate
```

### Usage

In order to run all unit tests, run the following command in the root folder of the project
```
python3 -m unittest discover -s tests -t tests
```

To test a specific input file and display the result, run the following command:
```
python3 main.py inputs/my_input_name.txt
```
Or just run this command to test all inputs within the `inputs` folder:
```
python3 main.py
```


## Possible improvements

This project could be improved by implementing the following ideas:
* Set a mower tracing in order to follow more precisely the mowers moves
* Implement an interface (a grid within terminal or in a graphical window)

