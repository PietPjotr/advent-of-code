#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

# Assign the day number from the command line argument
day_number="$1"

# Define the main directory
main_directory="day_${day_number}"

# Check if the directory already exists
if [ -d "$main_directory" ]; then
    echo "Directory already exists for day ${day_number}."
    exit 1
fi

# Create the main directory
mkdir "$main_directory"

# Create the Python file
python_file="${main_directory}/${day_number}.py"
touch "$python_file"

# Add standard code to the Python file
echo "import sys
sys.path.append('..')
import my_parser as p" >> "$python_file"

# Create the 'inputs' directory
inputs_directory="${main_directory}/inputs"
mkdir "$inputs_directory"

# add a file named inp.txt and a file named test.txt to the inputs directory
touch "${inputs_directory}/inp.txt"
touch "${inputs_directory}/test.txt"

echo "Directory structure created for day ${day_number} in ${main_directory}."
