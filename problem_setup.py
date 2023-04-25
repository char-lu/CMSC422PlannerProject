import sys

# Run this  before running the domain-independent planner to add (handempty) into initial state
# Ex: 
# python3 problem_setup.py problems/1/problem1.pddl problem.pddl
# Reads the problem1.pddl file and writes (handempty) into the problem init and writes file into problem.pddl ^
print(sys.argv[1])
print(sys.argv[2])

f = open(sys.argv[1], "r")
s =  f.readlines()
f.close()
f = open(sys.argv[2], "w+")
for line in s:
    if "(:init" in line:
        line = line + "        (handempty)\n"
    f.write(line)
f.close()