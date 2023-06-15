# Задача 38: Дополнить телефонный справочник возможностью изменения 
# и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

import os


def change_info(file_name): 
    os.system('CLS')
    with open(file_name, 'r') as data:
        phone_book = data.read()
        print(phone_book)
        
        index_del_data = int(input('Input number of a line to correction: ')) -1
        phone_book_lines = phone_book.split('\n')
        edit_phone_book_lines = phone_book_lines[index_del_data]
        elements = edit_phone_book_lines.split('\n')
        surname = input('Input a surname: ')
        phone_number = input('Input a number: ')
        num = elements[0]
        
        if len(surname) == 0:
            surname = elements[1]
        
        if len(phone_number) == 0:
            phone_number = elements[2]
            
        edited_line = f'{num} {surname} {phone_number}' 
        phone_book_lines[index_del_data] = edited_line
        print(f'The line {edit_phone_book_lines} was correctly edited as {edited_line}\n')
        
        with open(file_name, 'w') as f:
            f.write('\n'.join(phone_book_lines))
            

def delete_info(file_name):
    os.system('CLS')
    with open(file_name, 'r') as data:
        phone_book = data.read()
        print(phone_book)
        
    index_del_data = int(input('Input number of line to delete: ')) -1
    phone_book_lines = phone_book.split('\n')
    del_phone_book_lines = phone_book_lines[index_del_data]
    phone_book_lines.pop(index_del_data)
    
    print(f'The record {del_phone_book_lines} was deleted\n')
    
    with open(file_name, 'w') as data:
            data.write('\n'.join(phone_book_lines))