# tasks.py

class TaskManager:
    def __init__(self, tasks=[]):
        self.tasks = tasks

    def add_task(self, task):
        try:
            self.tasks.append(task)
            return "Task added successfully."
        except Exception as e:
            return f"An error occurred: {e}"

    def get_tasks(self):
        try:
            if self.tasks:
                return "\n".join(self.tasks)
            else:
                return "No tasks available."
        except Exception as e:
            return f"An error occurred: {e}"
