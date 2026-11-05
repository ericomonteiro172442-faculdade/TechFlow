Set-Content -Path "task_manager.py" -Value @"
class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, priority="Média"):
        task = {"id": self.next_id, "title": title, "status": "A Fazer", "priority": priority}
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_tasks(self):
        return list(self.tasks.values())

    def update_task_status(self, task_id, new_status):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = new_status
            return True
        return False

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
"@
# Metodo para criar tarefas implementado

# Metodos de leitura e atualizacao de status

# Metodo para remocao de tarefas
