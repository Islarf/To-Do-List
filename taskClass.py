import json

class Task:
    id ="id"
    title = "title"
    description = "description"
    due_date = "due_date"
    priority = "priority"

    def displayTask(self):
        print("ID : " + str(self.id))
        print("Title: " + self.title)
        print("Description: " + self.description)
        print("Due Date: " + self.due_date)
        print("Priority: " + self.priority)

    def __init__(self, id):
        #Open the file
        with open('data/tasks.json', 'r') as file:
            taskFile = json.load(file)
            self.id = id #tasksFile[id][id]
            self.title = taskFile[id][self.title]
            self.description =  taskFile[id][self.description]
            self.due_date = taskFile[id][self.due_date]
            self.priority = taskFile[id][self.priority]
