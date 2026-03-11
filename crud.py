import helpers

def create_todo():
    return

def get_todo_by_id(todo_id):
    #make python read the todo file 
    tasks = helpers.read_db_file()

    #extract the task with same id and return
    for task in tasks:
        if task['id'] == todo_id:
            return task

def update_todo(todo_id, update_data):
    task = get_todo_by_id(todo_id) #read
    tasks = helpers.read_db_file()
    tasks.remove(task)

    #search for key in data
    if "title" in update_data:
        task['title']= update_data['title']#whats updated data

    if "description" in update_data:
        task['description']= update_data['description']

    tasks.append(task)
    helpers.write_db_file(tasks) #save

    return task


def  delete_todo(todo_id):
    task = get_todo_by_id(todo_id)
    tasks = helpers.read_db_file()
    tasks.remove(task)
    helpers.write_db_file(tasks) #save

