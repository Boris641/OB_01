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









