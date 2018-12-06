from db_project import Database
from student_model import Student

database = Database()
student = Student()

class Runner():

    def list_available_commands():
        commands = {
        1: 'add student',
        2: 'view all student(s)',
        3: 'search student(s) by first name',
        4: 'search student(s) by surname',
        5: 'update student',
        6: 'delete student'
        }

        for opt, command in commands.items():
            print(opt, command)


    def execute_command(option):

        if option == 1:
            student.set_first_name(input('Enter the first name of the student you wish to add:  '))
            student.set_surname(input('Enter the surname of the student you wish to add:  '))
            database.execute_query('add_student', student)
        elif option == 2:
            database.execute_query('view_students', student)
        elif option == 3:
            student.set_first_name(input('Enter the name you want to search by:  '))
            database.execute_query('select_first_name_equal', student)
        elif option == 4:
            student.set_surname(input('Enter the name you want to search by:  '))
            database.execute_query('select_surname_equal', student)
        elif option == 5:
            student.set_student_id(int(input('Enter the id of the student you wish to update:  ')))
            student.set_first_name(input('Enter new first name:  '))
            student.set_surname(input('Enter new surname:  '))
            database.execute_query('update_student', student)
        elif option == 6:
            student.set_student_id(int(input('Enter the id of the student you wish to delete:  ')))
            database.execute_query('delete_student', student)
        else:
            print('Invalid option, please use enter the number for one of the listed commands')
    
    list_available_commands()
    option = int(input('Input the number of the function you want to execute:  '))
    execute_command(option)



