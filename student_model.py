import re

class Student():
    __student_id = '*'
    __first_name = None
    __surname = None

    def get_student_id(self):
        return self.__student_id

    def get_first_name(self):
        return self.__first_name
    
    def get_surname(self):
        return self.__surname

    def set_student_id(self, student_id):
        p = re.compile('[^0-9]')
        if p.search(str(student_id)) is None:
            self.__student_id = student_id
        else:
            print('Student ID must be an integer value')
            return -1
    
    def set_first_name(self, first_name):
        p = re.compile('[^a-zA-Z\'-]|^[-\']|[-\']$')
        if p.search(first_name) is None:
            self.__first_name = first_name
        else:
            print('Invalid name')
            return -1

    def set_surname(self, surname):
        p = re.compile('[^a-zA-Z\'-]|^[-\']|[-\']$')
        if p.search(surname) is None:
            self.__surname = surname
        else:
            print('Invalid name')
            return -1
