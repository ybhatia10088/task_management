class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
