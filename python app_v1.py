vyidano_knig = 0

while True:
    print("\n--- Меню «Учёт книг» (v1) ---")
    print("1 — Выдать одну книгу")
    print("2 — Показать, сколько книг выдано")
    print("3 — Сбросить счётчик до 0")
    print("0 — Выход")

    komanda = input("Введите команду: ")

    if komanda == "1":
        vyidano_knig = vyidano_knig + 1
        print("Книга выдана.")
    elif komanda == "2":
        print("Сейчас выдано книг:", vyidano_knig)
    elif komanda == "3":
        vyidano_knig = 0
        print("Счётчик сброшен до 0.")
    elif komanda == "0":
        print("Работа программы завершена.")
        break
    else:
        print("Неизвестная команда")