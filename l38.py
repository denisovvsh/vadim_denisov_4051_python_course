"""  
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""

import csv
import os

def find_contact_by_name(name, contacts):
    #Найти контакт по имени или фамилии
    for contact in contacts:
        if name.lower() in contact['name'].lower() or name.lower() in contact['surname'].lower():
            return contact
    return None

def update_contact(contact, new_data):
    #Обновить данные контакта
    contact.update(new_data)

def delete_contact(contacts, contact):
    #Удалить контакт из списка контактов
    contacts.remove(contact)

def add_contact(contacts, filename):
    new_name = input("Введите имя: ")
    new_surname = input("Введите фамилию: ")
    new_phone = input("Введите номер телефона: ")
    new_description_phone = input("Введите Описание контакта: ")
    new_contact = {'name': new_name, 'surname': new_surname, 'phone': new_phone, 'description': new_description_phone}
    contacts.append(new_contact)
    save_contacts_to_csv(contacts, filename)
    return True
    
def save_contacts_to_csv(contacts, filename):
    #Сохранить контакты в файл CSV
    fieldnames = ['name', 'surname', 'phone', 'description']
    with open(filename, 'w', encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def load_contacts_from_csv(filename):
    #Загрузить контакты из файла CSV
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                contacts.append(row)
    return contacts

#Загрузка контактов из файла CSV
filename = 'phonebook.csv'
contacts = load_contacts_from_csv(filename)

#Интерактивный ввод данных пользователя
action = input("Выберите действие (1 - изменить контакт, 2 - удалить контакт, 3 - добавить контакт): ")

if action == '1':
    name_to_find = input("Введите имя или фамилию для поиска контакта: ")
    contact_to_update = find_contact_by_name(name_to_find, contacts)
    if contact_to_update:
        new_name = input("Введите новое имя: ")
        new_surname = input("Введите новую фамилию: ")
        new_phone = input("Введите новый номер телефона: ")
        new_description_phone = input("Введите Описание контакта: ")
        update_contact(contact_to_update, {'name': new_name, 'surname': new_surname, 'phone': new_phone, 'description': new_description_phone})
        save_contacts_to_csv(contacts, filename)
        print("Контакт успешно изменен.")
    else:
        print("Контакт не найден.")

elif action == '2':
    name_to_find = input("Введите имя или фамилию для поиска контакта: ")
    contact_to_delete = find_contact_by_name(name_to_find, contacts)
    if contact_to_delete:
        delete_contact(contacts, contact_to_delete)
        save_contacts_to_csv(contacts, filename)
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")

elif action == '3':
    if add_contact(contacts, filename):
        print("Контакт успешно добавлен.")
    else:
        print("Ошибка добавления контакта!")
else:
    print("Некорректное действие.")
