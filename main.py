class User:
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access_level = 'user'


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


    def set_name(self, new_name):
        self.__name = new_name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Можно добавлять только экземпляры класса User.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def list_users(self):
        print("Список пользователей:")
        for user in self.__users:
            print(f"- ID: {user.get_id()}, Имя: {user.get_name()}, Уровень: {user.get_access_level()}")

admin = Admin(1, "Семен")

# Создаем пользователей
user_masha = User(2, "Маня")
user_vasya = User(3, "Вася")
user_katya = User(4, "Катерина")

admin.add_user(user_masha)
admin.add_user(user_vasya)
admin.add_user(user_katya)

admin.list_users()

# Удалим одного пользователя, например, с ID 3 (Вася)
admin.remove_user(3)

admin.list_users()