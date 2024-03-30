class Task():
    def __init__(self, description,status, deadline = 0):
        self.description = description
        self.status = status
        self.deadline = deadline

    def task(self, name):
        self.description = name
        print(f"Опишите задачу - {self.description}")
    def time(self, hour):
        if hour >= 0:
         self.deadline += hour
        print(f"Время на выполнение - {self.deadline}")
    def quality(self, announcement):
        if announcement >= 0:
            print(f"Задача выполнена")
        else:
            print(f"Задача не выполнена")
    def balance(self):
        print(f"Текущие задачи - {self.description}")

management = Task("Регистрация","Выполнена",4)

management.task(f"Регистрация")
management.time(0)
management.quality(0)
management.balance()

# Далее следует вариант от GPT-4:
class Task:
    def __init__(self, description, due_date, status=False):


        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_as_done(self):

        self.status = True

    def __str__(self):
        return f"{self.description} до {self.due_date} - {'Выполнено' if self.status else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):

        self.tasks.append(Task(description, due_date))

    def mark_done(self, description):

        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()

    def current_tasks(self):

        print("Текущие задачи:")
        for task in self.tasks:
            if not task.status:
                print(task)

# Пример использования
manager = TaskManager()
manager.add_task("Прочитать книгу", "2023-04-15")
manager.add_task("Написать код", "2023-04-16")
manager.add_task("Сходить в магазин", "2023-04-14")

manager.mark_done("Сходить в магазин")

manager.current_tasks()







