from transformations import Fetch, SimpleMovingAverage, ExponentialMovingAverage, CrossAbove, ConstantSeries, RateOfChange, PortfolioSimulation
from db_helper import load_json, save_json
from helper import input_parse
import uuid
# run the matching function of each commadn
def run(s, store):
    if s[0] == "Fetch":
        return Fetch(s[1])
    elif s[0] == "SimpleMovingAverage":
        return SimpleMovingAverage(int(s[1]), store[s[2]])  
    elif s[0] == "ExponentialMovingAverage":
        return ExponentialMovingAverage(store[s[2]], float(s[1]))  
    elif s[0] == "CrossAbove":
        args = [a.strip() for a in s[1].split(",")]
        return CrossAbove(store[args[0]], store[args[1]])
    elif s[0] == "ConstantSeries":
        return ConstantSeries(store[s[2]], float(s[1]))
    elif s[0] == "RateOfChange":
        return RateOfChange(int(s[1]), store[s[2]])
    elif s[0] == "PortfolioSimulation":
        args = [a.strip() for a in s[2].split(",")]
        return PortfolioSimulation(int(s[1]), store[args[0]], store[args[1]], store[args[2]])
    else:
        raise ValueError(f"Unknown function: {s[0]}")
# excutes each commadn and store them in the json file, to make sure they are persistent.

def execute(command):
    store_json = load_json("output.json")
    script_id = str(uuid.uuid4()) #generate a unique id for the script
    store_json[script_id] = {}
    computed = {}  #containing the datasources we already handled 
    for name, value in command.items():
        s = input_parse(value) #parse the input 
        output = run(s, computed) #run commadn and store in output
        computed[name] = output #map the output to its corresponsing name, and store so it can be used later.
        store_json[script_id][name] = output
    save_json("output.json", store_json) #add script output to database
    return script_id

def view(script_id, variables):
    store = load_json("output.json") #takes output from database 
    if script_id not in store:
        return None
    result = store[script_id] # fetch the specific output of a script
    return {var: result.get(var) for var in variables} 

