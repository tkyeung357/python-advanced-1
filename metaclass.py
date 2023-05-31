import time 

class New_Meta(type):
    instances = []
    def __new__ (mcs, name, bases, dictionary):
        if "instantiation_time" not in dictionary:
            #equipping all newly instantiated classes with the  get_instantiation_time()
            dictionary['get_instantiation_time'] = mcs.get_instantiation_time

        #  The metaclass should have its own class variable (a list) 
        # that contains a list of the names of the classes instantiated by the metaclass .
        mcs.instances.append(name)

        obj = super().__new__(mcs, name, bases, dictionary)
        
        obj.instantiation_time= time.time()
        time.sleep(1)
        return obj

    def get_instantiation_time(self):
        return self.instantiation_time;

class my_class1(metaclass = New_Meta):
    pass
class my_class2(metaclass = New_Meta):
    pass
class my_class3(metaclass = New_Meta):
    pass
class my_class4(metaclass = New_Meta):
    pass

m1 = my_class1()
m2 = my_class2()
m3 = my_class3()
m4 = my_class4()

print(New_Meta.instances)
print("{} instantiation time is {}".format(str(m1.__class__), m1.get_instantiation_time()))
print("{} instantiation time is {}".format(str(m2.__class__), m2.get_instantiation_time()))
print("{} instantiation time is {}".format(str(m3.__class__), m3.get_instantiation_time()))
print("{} instantiation time is {}".format(str(m4.__class__), m4.get_instantiation_time()))

# def greetings(self):
#     print('Just a greeting function, but it could be something more serious like a check sum')

# class My_Meta(type):
#     def __new__(mcs, name, bases, dictionary):
#         if 'greetings' not in dictionary:
#             dictionary['greetings'] = greetings
#         obj = super().__new__(mcs, name, bases, dictionary)
#         return obj

# class My_Class1(metaclass=My_Meta):
#     pass

# class My_Class2(metaclass=My_Meta):
#     def greetings(self):
#         print('We are ready to greet you!')

# myobj1 = My_Class1()
# myobj1.greetings()
# myobj2 = My_Class2()
# myobj2.greetings()
