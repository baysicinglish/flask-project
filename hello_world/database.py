import sqlite3
from sqlite3 import Error as DbError
from models import User

class Database():

    def __init__(self):
        self.main()

    database = 'ratemy_database.sqlite3'

    def connect(self, db_file):
            try:
                conn = sqlite3.connect(db_file)
                return conn
            except DbError as e:
                print(e)

            return None

    def create_table(self, conn, create_table_sql):
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
        except DbError as e:
            print(e)

    def main(self):

        users_table = """ CREATE TABLE IF NOT EXISTS users (
            email text PRIMARY KEY,
            username text UNIQUE NOT NULL,
            password text NOT NULL,
            name text NOT NULL,
            surname text NOT NULL,
            admin boolean NOT NULL
        ); """

        posts_table = """ CREATE TABLE IF NOT EXISTS posts (
            post_id integer PRIMARY KEY autoincrement,
            username text NOT NULL,
            title text NOT NULL,
            subheading text,
            image text NOT NULL,
            description text,
            published boolean NOT NULL
        ); """

        comments_table = """ CREATE TABLE IF NOT EXISTS comments (
            author text NOT NULL,
            post_id integer NOT NULL,
            rating integer NOT NULL,
            body text NOT NULL,
            upvotes integer NOT NULL,
            downvotes integer NOT NULL
        ); """

        conn = self.connect(self.database)

        if conn is not None:
            self.create_table(conn, users_table)
            self.create_table(conn, posts_table)
            self.create_table(conn, comments_table)
        else:
            print('Could not establish a connection to {}'.format(database))

        conn.close()

    def execute_wrapper(func):
        def wrapper(self, *args):
            try:
                conn = self.connect(self.database)
                cursor = conn.cursor()
                func(self, conn, cursor, *args)
            except DbError as e:
                print(e)

            conn.close()

        return wrapper

    @execute_wrapper
    def create_user(self, conn, cursor, user):
            query = "INSERT INTO users (email, username, password, name, surname, admin) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (user.get_email(), user.get_username(), user.get_password(), user.get_name(), user.get_surname(), user.get_admin()))
            conn.commit()    
    
    @execute_wrapper
    def create_post(self, conn, cursor, post):
            query = "INSERT INTO posts (username, title, subheading, image, description, published) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (post.get_username(), post.get_title(), post.get_subheading(), post.get_image(), post.get_description(), post.get_published()))
            conn.commit()

    def return_posts(self):
        try:
            conn = self.connect(self.database)
            cursor = conn.cursor()
            query = "SELECT * FROM posts"
            cursor.execute(query)
            posts = cursor.fetchall()
            conn.close()
            return posts
        except DbError as e:
            print(e)
