#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath('../filewrap'))

import filewrap

alpha_lines = list([ 
    'This is line 1 of the demo.txt file.', 
    'This is line 2 of the demo.txt file.', 
    'This is line 3 of the demo.txt file.'
])

beta_lines = list([     
    'This is line 4 of the demo.txt file.', 
    'This is line 5 of the demo.txt file.', 
    'This is line 6 of the demo.txt file.'
])

gamma_lines = list([
    'This is line 9 of the demo.txt file.', 
    'This is line 10 of the demo.txt file.', 
    'This is line 11 of the demo.txt file.'
])

filewrap.mkdir('demo')
filewrap.mkdir(f'demo/demo')
filewrap.ren('demo', 'demo-renamed')
filewrap.mkfile('t', 'demo-renamed/demo.txt')
filewrap.writelines('demo-renamed/demo.txt', alpha_lines, beta_lines, 'This is line 7 of the demo.txt file.', 'This is line 8 of the demo.txt file.')
filewrap.appendlines('demo-renamed/demo.txt', gamma_lines, 'This is line 12 of the demo.txt file.', 'This is line 13 of the demo.txt file.')
filewrap.copyfile('demo-renamed/demo', 'demo-renamed/demo.txt')
filewrap.copydir('demo-renamed/demo', 'demo-renamed')
filewrap.tar_wrap('demo-renamed')
filewrap.zip_wrap('demo-renamed')

print(f"Size of demo-renamed/demo.txt: {filewrap.size('demo-renamed/demo.txt')} Bytes")
print(f"Size of demo-renamed: {filewrap.size('demo-renamed')} Bytes")

filewrap.rpdir()
filewrap.rpfile('t', 'demo-renamed/demo.txt', 'demo-renamed/demo/demo.txt')

filewrap.rmfile('demo-renamed.tar.gz', 'demo-renamed.zip')
filewrap.rmall('demo-renamed')