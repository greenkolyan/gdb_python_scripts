#!/usr/bin/python3

import gdb
import os

while True:  
    file_name =str(input("Enter file prefix: "))
    try:
        filename_prefix = str(file_name)
        break
    except ValueError:
        print("Error! Please enter a valid value")


sections_out = gdb.execute('maintenance info sections', False, True)

split_text = sections_out.split('\n', maxsplit=-1)
split_text.pop(0)


# TODO: survive in case of an excepton
mydir = "dumps"

try:
    os.mkdir(mydir)
except OSError:
    print("Failed to create directory %s" % mydir)
else:
    print("The directory %s was created in a funny way" % mydir)

for e in split_text:
    new_e = e.split()
    memory = new_e[1]
    name = new_e[4]
    new_memory = memory.split('->')
    cmd_prefix = "dump binary memory dumps/" + filename_prefix
    memory_start = new_memory[0]
    memory_end = new_memory[1]
    dump_cmd = cmd_prefix + name + ".dump " +  memory_start + " " + memory_end
    print(dump_cmd)
    gdb.execute(dump_cmd)


