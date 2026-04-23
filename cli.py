import sys
from transformation_impl import rules
from services import execute, view
from helper import read_commands, print_series
arg = sys.argv
if len(arg) < 2: #if the user did not enter any argument print the rules
    print(rules())
elif arg[1] == "execute": # if he enteted execute
    commands = read_commands() #prompyt him for the commands he woul like to excute 
    id = execute(commands) # execute and get the id 
    print(f"Script successfully executed: {id}") 
elif arg[1] == "view": 
    script_id = arg[3] #read id 
    variables = arg[4:] #read variables
    data = view(script_id, variables) #execute view command 
    print_series(data, script_id) # output 
