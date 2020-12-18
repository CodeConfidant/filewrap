#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("../filewrap-os"))

import filewrap

dirpath = str("demo-renamed")
filepath = str(dirpath + "/demo.txt")

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
input("Press enter to continue:")

filewrap.ren("demo", dirpath)
input("Press enter to continue:")

filewrap.mkfile("t", filepath)
input("Press enter to continue:")

filewrap.writelines(filepath, alpha_lines, beta_lines, "This is line 7 of the demo.txt file.", "This is line 8 of the demo.txt file.")
input("Press enter to continue:")

filewrap.appendlines(filepath, gamma_lines, "This is line 12 of the demo.txt file.", "This is line 13 of the demo.txt file.")
input("Press enter to continue:")

filewrap.tar_wrap(dirpath)
filewrap.zip_wrap(dirpath)

filewrap.rpdir()

filewrap.rpfile("t", filepath)
input("Press enter to continue:")

filewrap.rmfile(filepath)
filewrap.rmdir(dirpath)
filewrap.rmfile(dirpath + ".tar.gz")
filewrap.rmfile(dirpath + ".zip")