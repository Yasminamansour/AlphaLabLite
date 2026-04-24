# helps print the view output as requested 
import re
def print_series(data, script_id):
    if data is None:
        print(f"No script found with id: {script_id}")
        return
    for var, value in data.items():
        if value is None:
            print(f"{var}: not found")
        elif len(value) > 4:
            print(f"{var}:\n\t[{value}]")
        else:
            print(f"{var}:\n\t{value}")
# extract the command and the arguments
def input_parse(string):
    res = re.findall(r'[^{}]+', string)
    return [item.strip() for item in res]
# reads commands 
def read_commands(lines=None):
    if lines is None:
        lines = []
        while True:
            try:
                lines.append(input())
            except KeyboardInterrupt:
                break
    result = {}
    for t in lines:
        chunk = t.split("=")
        result[chunk[0].strip()] = chunk[1].strip()
    return result
