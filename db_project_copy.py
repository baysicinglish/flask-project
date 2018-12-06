import sqlite3
from sqlite3 import Error as DbError
from student_model import Student

class Database():

    database = 'student_database.sqlite3'

    def connect(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except DbError as e:
            print(e)

        return None

    #def execute_query(self, query)-

    def create_table(self, conn, create_table_sql):
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
        except DbError as e:
            print(e)

    def add_student(self, student):
        try:
            conn = self.connect(self.database)
            cursor = conn.cursor()
            query = "INSERT INTO students (first_name, surname) VALUES (? ,?)"
            cursor.execute(query, (student.get_first_name(), student.get_surname()))
            conn.commit()
        except DbError as e:
            print(e)
        
        conn.close()

    def view_students(self):
        try:
            conn = self.connect(self.database)
            cursor = conn.cursor()
            query = "SELECT * FROM students"
            cursor.execute(query)
            students = cursor.fetchall()
            for row in students:
                print(row)

        except DbError as e:
            print(e)

        conn.close()

    def select_first_name_equal(self, student):
        try:
            conn = self.connect(self.database)
            cursor = conn.cursor()
            query = """SELECT * FROM students
            WHERE first_name = ?"""
            cursor.execute(query, (student.get_first_name(),))
            students = cursor.fetchall()
            for row in students:
                print(row)

        except DbError as e:
            print(e)

        conn.close()

    def select_surname_equal(self, student):
        try:
            conn = self.connect(self.database)
            cursor = conn.cursor()
            query = """SELECT * FROM students
            WHERE surname = ?"""
            cursor.execute(query, (student.get_surname(),))
            students = cursor.fetchall()
            for row in students:
                print(row)

        except DbError as e:
            print(e)

        conn.close()

    def update_student(self, student):
        try:
            conn = self.connect(self.database)
            cursor = conn.cursor()
            query = """UPDATE students
            SET first_name = ?, surname = ?
            WHERE student_id = ?"""
            cursor.execute(query, (student.get_first_name(), student.get_surname(), student.get_student_id()))
            conn.commit()

        except DbError as e:
            print(e)

        conn.close()

    def delete_student(self, student):
        try:
            conn = self.connect(self.database)
            cursor = conn.cursor()
            query = """DELETE
            FROM students
            WHERE student_id = ?"""
            cursor.execute(query, (student.get_student_id(),))
            conn.commit()

        except DbError as e:
            print(e)

        conn.close()


    def main(self):
        self.database = 'student_database.sqlite3'

        students_table = """ CREATE TABLE IF NOT EXISTS students (
            student_id integer PRIMARY KEY,
            first_name text NOT NULL,
            surname text NOT NULL
        ); """

        grades_table = """ CREATE TABLE IF NOT EXISTS grades (
            id integer PRIMARY KEY,
            exam text NOT NULL,
            score integer
        ); """

        #FOREIGN KEY (student_id) REFERENCES students (student_id)
        
        conn = self.connect(self.database)
        if conn is not None:
            #create student table
            self.create_table(conn, students_table)
            #create grades table
            self.create_table(conn, grades_table)
        else:
            print('Could not establish a connection to {}'.format(database))

        conn.close()
