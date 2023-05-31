import datetime

def execut_timestamp(action):
    def wrapper(*args):
        print("start at {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) )
        action(*args)
    return wrapper

@execut_timestamp
def hello_world():
    print("hello world")

@execut_timestamp
def add(a, b):
    print (a + b)

@execut_timestamp
def multi(a, b):
    print (a * b)

hello_world()
add(1,2)
multi(1,2)
hello_world()
add(3,2)
multi(3,2)
hello_world()
add(3,3)
multi(3,3)
hello_world()

def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()
        return internal_wrapper
    return wrapper

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)

@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')