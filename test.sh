#!/bin/bash

# Script name: example.sh
# Description: A simple Bash script to demonstrate arguments and special characters.

# Print the script name
echo "Script name: $0"

# Print the number of arguments
echo "Number of arguments: $#"

# Print all arguments
echo "All arguments: $@"

# Print each argument
for arg in "$@"; do
    echo "Argument: $arg"
done

# Example of command substitution
echo "Current date: $(date)"

# Example of escaping special characters
echo "This is a dollar sign: \$"

# Example of redirection
echo "This will be saved to output.txt" > output.txt