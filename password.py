def ask_password():
    right_password = "password"

    for _ in range(3):
        user_password = input()
        if user_password == right_password:
            print("Пароль принят")
            return
    print("В доступе отказано")

ask_password()