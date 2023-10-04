#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("../filewrap"))

import filewrap

dirpath = str("demo-renamed")
filepath = str(dirpath + "/demo.txt")
filepathcopy = str(dirpath + "/democopy.txt")

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

gamma_lines = list([
    "This is line 9 of the demo.txt file.", 
    "This is line 10 of the demo.txt file.", 
    "This is line 11 of the demo.txt file."
])

filewrap.mkdir("demo")
filewrap.ren("demo", dirpath)

filewrap.mkfile("t", filepath)
filewrap.mkfile("t", filepathcopy)

filewrap.writelines(filepath, alpha_lines, beta_lines, "This is line 7 of the demo.txt file.", "This is line 8 of the demo.txt file.")
filewrap.writelines(filepathcopy, alpha_lines, beta_lines, "This is line 7 of the demo.txt file.", "This is line 8 of the demo.txt file.")

filewrap.appendlines(filepath, gamma_lines, "This is line 12 of the demo.txt file.", "This is line 13 of the demo.txt file.")
filewrap.appendlines(filepathcopy, gamma_lines, "This is line 12 of the demo.txt file.", "This is line 13 of the demo.txt file.")

filewrap.tar_wrap(dirpath)
filewrap.zip_wrap(dirpath)

print(f"Size of {filepath}:", filewrap.size(filepath), "Bytes")
print(f"Size of {dirpath}:", filewrap.size(dirpath), "Bytes")

filewrap.rpdir()
filewrap.rpfile("t", filepath, filepathcopy)

filewrap.rmfile(dirpath + ".tar.gz", dirpath + ".zip")
filewrap.rmall(dirpath)