Set-Content -Path "test_task_manager.py" -Value @"
import pytest
from task_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    task = tm.add_task("Entregar pedido #102", "Alta")
    assert task["id"] == 1
    assert task["title"] == "Entregar pedido #102"
    assert len(tm.get_tasks()) == 1

def test_update_status():
    tm = TaskManager()
    task = tm.add_task("Conferir estoque")
    tm.update_task_status(task["id"], "Concluído")
    assert tm.get_tasks()[0]["status"] == "Concluído"

def test_delete_task():
    tm = TaskManager()
    task = tm.add_task("Remover rota antiga")
    assert tm.delete_task(task["id"]) is True
    assert len(tm.get_tasks()) == 0
"@
# Teste de atualizacao de status

# Teste de remocao de tarefas
