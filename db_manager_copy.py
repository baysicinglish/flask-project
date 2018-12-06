from db_project import Database
from student_model import Student

class Runner():

    def __init__(self):
        self.database = Database()
        self.student = Student()

    def list_available_commands(self):
        commands = {
        1: 'add student',
        2: 'view all students',
        3: 'search student(s) by first name',
        4: 'search student(s) by surname',
        5: 'update student',
        6: 'delete student',
        7: 'exit'
        }

        for opt, command in commands.items():
            print(opt, command)


    def execute_command(option):

        if option == 1:
            if student.set_first_name(input('Enter the first name of the student you wish to add:  ')) == -1: return -1
            if student.set_surname(input('Enter the surname of the student you wish to add:  ')) == -1: return -1
            database.add_student(student)
        elif option == 2:
            database.view_students()
        elif option == 3:
            if student.set_first_name(input('Enter the name you want to search by:  ')) == -1: return -1
            database.select_first_name_equal(student)
        elif option == 4:
            if student.set_surname(input('Enter the name you want to search by:  ')) == -1: return -1
            database.select_surname_equal(student)
        elif option == 5:
            if student.set_student_id(int(input('Enter the id of the student you wish to update:  '))) == -1: return -1
            if student.set_first_name(input('Enter new first name:  ')) == -1: return -1
            if student.set_surname(input('Enter new surname:  ')) == -1: return -1
            database.update_student(student)
        elif option == 6:
            if student.set_student_id(int(input('Enter the id of the student you wish to delete:  '))) == -1: return -1
            database.delete_student(student)
        elif option == 7:
            quit()
        else:
            print('Invalid option, please use enter the number for one of the listed commands')
    
    cont = True

    def yes_or_no(select):
        if select.lower() in ['n', 'no']:
            return False
        elif select.lower() in ['y', 'yes']:
            return True
        else:
            print('Input not recognised')
     
    database.main() 
    while cont is True:
        list_available_commands()
        try:
            option = int(input('Input the number of the function you want to execute:  '))
        except ValueError:
            print('Please enter a valid number')
            continue
        execute_command(option)
        select = input('Perform another action? Y/N:  ')
        cont = yes_or_no(select)




