# заметки
from datetime import datetime

notes = {} #пустой словарь для загрузки в него информации из файла
path = 'notes.txt' #путь к файлу

# 1 открытие файла
def open_file():
    with open(path, 'w+', encoding='UTF-8') as file:
        note = file.readlines()
    for i, note in enumerate(note, 1): #enumerate - создаем коды id
        notes[i] = note.strip().split(';')
    
# 2 сохранение файла
def save_file():
    data = []
    for note in notes.values():
        note = ';'.join(note)
        data.append(note)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

# 3 показать все заметки
def show_notes(pb: dict):
    if not notes:
        print(f'\nНет сохраненных заметок\n')
        print(f'Либо файл не был загружен\n')
        print(f'Для загрузки файла выберите пункт меню 1\n')
    else:
        for i, note in pb.items():
            print()
            print(f'ID: {i} \n{note[0]} \n{note[1]} \n{note[2]}')
        print()

# 4 создание заметки
def new_note():
    date_note = str(datetime.now())
   
    if not notes:
        print(f'Дата заметки: {date_note}')
        title = input('Введите заголовок заметки: ')
        text = input('Введите текст заметки: ')
        u_id = 1
        notes[u_id] = [date_note, title, text]
    else:
        print(f'Дата заметки: {date_note}')
        title = input('Введите заголовок заметки: ')
        text = input('Введите текст заметки: ')
        u_id = max(notes.keys()) + 1
        notes[u_id] = [date_note, title, text]
    return title

# 5 поиск заметки
def find_note():
    result = {}
    flag = 0
    word = input('Введите ключевое слово для поиска: ').lower()
    for i, note in notes.items():
        if word in ''.join(note).lower():
            result[i] = note
        else:
            flag += 1
    if flag > 0:
        print('==============================')
        print(f'\nПоиск не дал результатов\n')
        print('==============================')
    return result

# 6 выборка по дате
def find_note_date():
    result = {}
    flag = 0
    word = input('Введите дату в формате гггг-мм-дд: ').lower()
    for i, note in notes.items():
        if word in note[0].lower():
            result[i] = note
        else:
            flag += 1
    if flag > 0:
        print('==============================')
        print(f'\nПоиск не дал результатов\n')
        print(f'Либо введенная дата не соответствует формату гггг-мм-дд\n')
        print('==============================')
    return result

# 7 редактирование заметки
def edit_note():
    date_note = str(datetime.now())
    result = find_note()
    if not result:
        print()
    else:
        show_notes(result)
        u_id = int(input('Введите ID заметки, которую хотите изменить: '))
        if u_id in notes:
            old_date_note, old_title, old_text = notes[u_id]
            print(f'Дата изменений: {date_note}')
            title = input('Введите новый заголовок заметки: ')
            text = input('Введите новый тект заметки: ')
            notes[u_id] = [date_note if date_note else old_date_note, 
                        title if title else old_title, 
                        text if text else old_text]
            return title if title else old_title
        else:
            print('==============================')
            print(f'\nПоиск не дал результатов\n')
            print('==============================')

# 8 удаление заметки
def del_note():
    result = find_note()
    if not result:
        print()
    else:
        show_notes(result)
        u_id = int(input('Введите ID заметки, которую хотите удалить: '))
        if u_id in notes:
            name = notes.pop(u_id)
            return name[0]
        else:
            print('==============================')
            print(f'\nПоиск не дал результатов\n')
            print('==============================')

menu = '''\nГлавное меню
    1. Загрузить файл с заметками
    2. Сохранить файл с заметками
    3. Отобразить все заметки
    4. Создать заметку
    5. Найти заметку
    6. Выборка по дате
    7. Изменить заметку
    8. Удалить заметку
    9. Выход'''

while True:
    print (menu)
    choice = input('Выберите пункт меню: ')
    match choice:
        case '1': #Открыть файл
            open_file()
            print('==============================')
            print(f'\nФайл с заметками загружен\n')
            print('==============================')
        case '2': #Сохранить файл
            save_file()
            print('==============================')
            print(f'\nЗаметки сохранены в файл\n')
            print('==============================')
        case '3': #Показать все заметки
            print('==============================')
            show_notes(notes)
            print('==============================')
        case '4': #Создать заметку
            title = new_note()
            print('==============================')
            print(f'\nЗаметка создана\n')
            print(f'Для сохранения результата выберите пункт меню 2\n')
            print('==============================')
        case '5': #Найти заметку
            result = find_note()
            show_notes(result)
        case '6': #Выборка по дате
            result = find_note_date()
            show_notes(result)
        case '7': #Изменить заметку
            title = edit_note()
            if title :
                print('==============================')
                print(f'\nЗаметка успешно изменена\n')
                print(f'Для сохранения результата выберите пункт меню 2\n')
                print('==============================')
        case '8': #Удалить заметку
            name = del_note()
            if name :
                print('==============================')
                print(f'\nЗаметка удалена\n')
                print(f'Для сохранения результата выберите пункт меню 2\n')
                print('==============================')
        case '9': #Выход
            print(f'\nВнимание!')
            print(f'При выходе все не сохраненные изменения будут потеряны.\n')
            quit_program = str(input('Нажмите Enter, чтобы выйти, или n, чтобы остаться: '))
            if quit_program == 'n':
                print('==============================')
                print(f'\nДля сохранения результатов выберите пункт меню 2\n')
                print('==============================')
            else:
                print('==============================')
                print(f'\nДо свидания!\n')
                print('==============================')
                break
        case _:
            print('==============================')
            print(f'\nОшибка ввода. \nВыберите пункт меню от 1 до 9\n')
            print('==============================')