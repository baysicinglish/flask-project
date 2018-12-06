from generate_model import ModelGenerator as generate

class User():
    def __init__(self, name, surname, email, username, password, admin=False):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__username = username
        self.__password = password
        self.__admin = admin

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_surname(self, surname):
        self.__surname = surname

    def get_surname(self):
        return self.__surname

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email
    
    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_admin(self, admin):
        self.__admin = admin

    def get_admin(self):
        return self.__admin

class Posts():
        def __init__(self, username, title, subheading, image, description):
                self.__username = username
                self.__title = title
                self.__subheading = subheading
                self.__image = image
                self.__description = description
                self.__published = False

        def set_post_id(self, post_id):
                self.__post_id = post_id

        def get_post_id(self):
                return self.__post_id

        def set_username(self, username):
                self.__username = username

        def get_username(self):
                return self.__username

        def set_title(self, title):
                self.__title = title

        def get_title(self):
                return self.__title

        def set_subheading(self, subheading):
                self.__subheading = subheading

        def get_subheading(self):
                return self.__subheading

        def set_image(self, image):
                self.__image = image

        def get_image(self):
                return self.__image

        def set_description(self, description):
                self.__description = description

        def get_description(self):
                return self.__description

        def set_published(self, published):
                self.__published = published

        def get_published(self):
                return self.__published

generate.create_model('Comments', 'author', 'post_id', 'rating', 'body', 'upvotes', 'downvotes')
#generate.make_getter_setter(['dog', 'cat'])
#generate.make_constructor(['dog', 'cat'])
