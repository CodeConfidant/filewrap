#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("../filewrap-os"))

import filewrap

# The string representing the file path of the demo directory that we want to create. 
dirpath = str("demo")

# The string representing the file path of the demo.txt file that we want to create.
filepath = str("demo.txt")

# Lists of strings to be written to the demo.txt file.
alpha_lines = list([ 
    "This is line 1 of the demo.txt file.", 
    "This is line 2 of the demo.txt file.", 
    "This is line 3 of the demo.txt file."
])

beta_lines = list([     
    "This is line 4 of the demo.txt file.", 
    "This is line 5 of the demo.txt file.", 
    "This is line 6 of the demo.txt file."
])

# Lists of strings to be appended to the end of the demo.txt file.
gamma_lines = list([
    "This is line 9 of the demo.txt file.", 
    "This is line 10 of the demo.txt file.", 
    "This is line 11 of the demo.txt file."
])

# Create a new directory called demo. 
filewrap.mkdir(dirpath)
input("Press enter to continue:")

# Create a new demo.txt file.
filewrap.mkfile("t", filepath)
input("Press enter to continue:")

# Rename the demo directory to demo-renamed. 
filewrap.ren(dirpath, "demo-renamed")
input("Press enter to continue:")

# Output to terminal the file/subdirectory names of the working directory.
filewrap.rpdir()

# Print a dictionary of information about the demo.txt file.
print("File Attributes:", filewrap.attrfile("rt", filepath), sep=" ")

# Write the strings from the alpha/beta lines lists as well as two additional strings to the demo.txt file.
filewrap.writelines("t", filepath, alpha_lines, beta_lines, "This is line 7 of the demo.txt file.", "This is line 8 of the demo.txt file.")
input("Press enter to continue:")

# Append the strings from the gamma lines list as well as two additional strings to the demo.txt file.
filewrap.appendlines("t", filepath, gamma_lines, "This is line 12 of the demo.txt file.", "This is line 13 of the demo.txt file.")
input("Press enter to continue:")

# Read and print the lines in the demo.txt file.
filewrap.rpfile("t", filepath)
input("Press enter to continue:")

# Delete the demo-renamed directory.
filewrap.rmdir("demo-renamed")

# Delete the demo.txt file. 
filewrap.rmfile(filepath)

# Delete objects.
del(dirpath, filepath, alpha_lines, beta_lines, gamma_lines)