import edit_process
from print_data import print_data


def redactor_menu():
 
    begin = True
    while begin:
        
        print ('------ \n Введите число для соответствующей задачи или иное для выхода: ')
        print ('   0.\t Отобразить список')
        print ('   1.\t Добавить запись')


        program = int(input())
        print ()

        if program == 0:
            print_data()
            

        elif program == 1:
            edit_process.add_record()


        else:
            begin = False