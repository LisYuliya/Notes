import os
import json

NOTES_FILE = "notes.json"

def create_note():
    note = {}
    note["title"] = input("Введите заголовок заметки: ")
    note["text"] = input("Введите текст заметки: ")
    
    while True:
        save = input("Хотите сохранить заметку? (y/n): ")
        if save.lower() == "y":
            if os.path.exists(NOTES_FILE):
                with open(NOTES_FILE, "r") as f:
                    notes = json.load(f)
            else:
                notes = []

            notes.append(note)

            with open(NOTES_FILE, "w") as f:
                json.dump(notes, f)

            print("Заметка сохранена.")
            break
        elif save.lower() == "n":
            break
        else:
            print("Неправильный ответ.")

    return note

def list_notes():
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)
    print ('Список заметок:')
    if not notes:
        print("Список заметок пуст.")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note['title']}")

        while True:
            choice = input("Введите номер заметки для чтения или нажмите Enter, чтобы вернуться: ")
            if choice == "":
                break
            try:
                note_index = int(choice) - 1
                if note_index < 0 or note_index >= len(notes):
                    print("Неверный номер заметки.")
                else:
                    print(f"Заголовок: {notes[note_index]['title']}")
                    print(f"Текст: {notes[note_index]['text']}")
                    break
            except ValueError:
                print("Неверный номер заметки.")
    print ('\n')


def edit_note():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
    else:
        notes = []

    note_index = int(input("Введите номер заметки, которую хотите изменить: ")) - 1

    if note_index >= 0 and note_index < len(notes):
        note = notes[note_index]
        note["title"] = input("Введите новый заголовок заметки: ")
        note["text"] = input("Введите новый текст заметки: ")
        notes[note_index] = note

        with open(NOTES_FILE, "w") as f:
            json.dump(notes, f)

        print("Заметка изменена.")
    else:
        print("Неправильный номер заметки.")

def delete_note():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
    else:
        notes = []

    note_index = int(input("Введите номер заметки, которую хотите удалить: ")) - 1

    if note_index >= 0 and note_index < len(notes):
        notes.pop(note_index)

        with open(NOTES_FILE, "w") as f:
            json.dump(notes, f)

        print("Заметка удалена.")
    else:
        print("Неправильный номер заметки.")

def main():
    while True:
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Изменить заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            note = create_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неправильный номер действия.")

if __name__ == "__main__":
    main()
