import os

def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            file.write(note_text)
        print(f"Заметка '{note_name}' успешно создана!")
    except Exception as e:
        print(f"Ошибка при создании заметки: {e}")

def create_note():
    try:
        note_name = input("Введите название заметки: ").strip()
        if not note_name:
            print("Название заметки не может быть пустым!")
            return
        note_text = input("Введите текст заметки: ")
        build_note(note_text, note_name)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def read_note():
    try:
        note_name = input("Введите название заметки для чтения: ").strip()
        if not note_name:
            print("Название заметки не может быть пустым!")
            return
        if os.path.isfile(f"{note_name}.txt"):
            with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
                content = file.read()
            print(f"\n--- Заметка '{note_name}' ---\n{content}\n--- Конец заметки ---")
        else:
            print(f"Заметка '{note_name}' не найдена!")
    except Exception as e:
        print(f"Произошла ошибка при чтении заметки: {e}")

def edit_note():
    try:
        note_name = input("Введите название заметки для редактирования: ").strip()
        if not note_name:
            print("Название заметки не может быть пустым!")
            return
        if os.path.isfile(f"{note_name}.txt"):
            with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
                old_content = file.read()
            print(f"\nТекущий текст заметки:\n{old_content}")
            new_content = input("\nВведите новый текст заметки: ")
            with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
                file.write(new_content)
            print(f"Заметка '{note_name}' успешно обновлена!")
        else:
            print(f"Заметка '{note_name}' не найдена!")
    except Exception as e:
        print(f"Произошла ошибка при редактировании заметки: {e}")

def delete_note():
    try:
        note_name = input("Введите название заметки для удаления: ").strip()
        if not note_name:
            print("Название заметки не может быть пустым!")
            return
        if os.path.isfile(f"{note_name}.txt"):
            os.remove(f"{note_name}.txt")
            print(f"Заметка '{note_name}' успешно удалена!")
        else:
            print(f"Заметка '{note_name}' не найдена!")
    except Exception as e:
        print(f"Произошла ошибка при удалении заметки: {e}")

def display_notes():
    try:
        notes = [f for f in os.listdir() if f.endswith(".txt")]
        if not notes:
            print("Заметок не найдено!")
            return
        # Сортировка по длине содержимого (от короткой к длинной)
        sorted_notes = sorted(notes, key=lambda x: len(open(x, "r", encoding="utf-8").read()))
        print("\n--- Все заметки (по возрастанию длины) ---")
        for note in sorted_notes:
            content = open(note, "r", encoding="utf-8").read()
            print(f"\nНазвание: {note[:-4]}")
            print(f"Длина: {len(content)} символов")
            print(f"Текст: {content[:100]}{'...' if len(content) > 100 else ''}")
            print("-! * 40")
    except Exception as e:
        print(f"Произошла ошибка при отображении заметок: {e}")

def display_sorted_notes():
    try:
        notes = [f for f in os.listdir() if f.endswith(".txt")]
        if not notes:
            print("Заметок не найдено!")
            return
        # Сортировка по длине содержимого (от длинной к короткой)
        sorted_notes = sorted(
            notes,
            key=lambda x: len(open(x, "r", encoding="utf-8").read()),
            reverse=True
        )
        print("\n--- Все заметки (по убыванию длины) ---")
        for note in sorted_notes:
            content = open(note, "r", encoding="utf-8").read()
            print(f"\nНазвание: {note[:-4]}")
            print(f"Длина: {len(content)} символов")
            print(f"Текст: {content[:100]}{'...' if len(content) > 100 else ''}")
            print("-! * 40")
    except Exception as e:
        print(f"Произошла ошибка при сортировке заметок: {e}")

def main():
    while True:
        print("\n" + "="*50)
        print("УПРАВЛЕНИЕ ЗАМЕТКАМИ")
        print("="*50)
        print("1. Создать заметку")
        print("2. Прочитать заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Показать все заметки (по возрастанию длины)")
        print("6. Показать все заметки (по убыванию длины)")
        print("7. Выйти")
        print("-"*50)

        try:
            choice = input("Выберите действие (1-7): ").strip()

            if choice == "1":
                create_note()
            elif choice == "2":
                read_note()
            elif choice == "3":
                edit_note()
            elif choice == "4":
                delete_note()
            elif choice == "5":
                display_notes()
            elif choice == "6":
                display_sorted_notes()
            elif choice == "7":
                print("До свидания!")
                break
            else:
                print("Неверный выбор! Пожалуйста, выберите число от 1 до 7.")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()