# =========================================================================
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# =========================================================================
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task(): # Создаём класс - массив заданий
    def __init__(self):
        self.my_tasks =[]

    def add_task(self, title, description, deadline): # Создаём метод - добавление задания
        self.my_tasks.append({'title': title, 'description': description, 'deadline': deadline, 'status': "Не выполнено"})

    def done_task(self, title):
        for my_task in self.my_tasks:
            if my_task['title'] == title:
                my_task['status'] == "Выполнено"
                print("")
                print(f'Задание "{title}" выполнено. УРА!')
 #           else:
 #               print("")
 #               print(f'Задание "{title}" не найдено.')

    def show_tasks(self):
        print("Список текущих задач:")
        for my_task in self.my_tasks:
            if my_task['status'] == "Не выполнено":
                print("")
                print(f"ЗАДАНИЕ: {my_task['title']}")
                print(f"ОПИСАНИЕ: {my_task['description']}")
                print(f"ВЫПОЛНИТЬ ДО: {my_task['deadline']}")

t = Task()
t.add_task("Заказать продукты", "Составить список продуктов, пополнить счёт для покупок, сделать заказ онлайн", "01.04.2024")
t.add_task("Пройти урок №1 по ООП", "Посмотреть видео урока, сделать домашку, сдать д/з", "01.04.2024")
t.add_task("Записаться к парикмахеру", "Проверить график работы мастера в боте, записаться на 5 апреля", "05.04.2024")
t.add_task("Позаботиться о кошке", "Вычесать шерсть, заказать корм, купить витамины", "29.03.2024")
t.add_task("Домашние дела", "Пропылесосить квартиру, приготовить еду, помыть окна", "04.04.2024")

t.show_tasks()

t.done_task("Пройти урок №1 по ООП")





