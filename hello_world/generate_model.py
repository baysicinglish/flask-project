class ModelGenerator():

    @staticmethod
    def make_class(class_name):
        print('class {}():'.format(class_name.title()))

    @staticmethod
    def make_constructor(list):
        print('\tdef __init__(self', end='')
        for arg in list:
            print(', ' +arg.lower(), end='')
        print('):')
        for arg in list:
            print('\t\tself.__{0} = {0}'.format(arg.lower()))
        print('')

    @staticmethod
    def make_getter_setter(list):
        
        for arg in list:
            print('\tdef set_{0}(self, {0}):\n\t\tself.__{0} = {0}\n'.format(arg.lower()))
            print('\tdef get_{0}(self):\n\t\treturn self.__{0}\n'.format(arg.lower()))

    @classmethod
    def create_model(cls, class_name, *args):
        cls.make_class(class_name)
        cls.make_constructor(args)
        cls.make_getter_setter(args)
