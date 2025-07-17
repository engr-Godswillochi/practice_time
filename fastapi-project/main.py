from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


todos =[]

#get all todo
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#get a single todo
@app.get("/todos/{id}")
async def get_todo(id:int):
    for todo in todos:
        if todo.id == id:
            return {"todo": todo}
    return {"message": "no todos found"}

#create a todo
@app.post("/create")
async def creat(todo: Todo):
    todos.append(todo)
    return {"message": "todos added"}

#update a todo
@app.put("/update/{id}")
async def update_todo(id:int, todo_obj: Todo):
    for todo in todos:
        if todo.id == id:
            todo.id = id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "no todos found"}


#delete a todo
@app.delete("/delete/{id}")
async def delete_todo(id:int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message": "todo deleted"}
    return {"message": "no todos found"}
