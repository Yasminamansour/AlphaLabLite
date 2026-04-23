from typing import List
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from services import view, execute 
from helper import read_commands
app = FastAPI()
# to make it work i ran uvicorn api:app --reload
# on another command i ran the same command provided in the sheet
class ExecuteRequest(BaseModel):
    script: str 
@app.get("/") 
def get_rules():
    with open("rules.txt", "r") as f:
        return {"rules": f.read()}

@app.post("/execute")
def execute_endpoint(req: ExecuteRequest):
    commands = read_commands(req.script.split("\n"))
    id = execute(commands)
    return {"message":"Script successfully executed","result":id}

@app.get("/view/{script_id}")
# please note that i asked claude to help me with FastAPI syntax.
def view_endpoint(script_id: str, variables: List[str] = Query(default=[])):
    data = view(script_id, variables)
    if data is None:
        raise HTTPException(status_code=404, detail=f"No script found with id: {script_id}")
    return data
