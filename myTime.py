class myTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs
        
    def __add__(self, mt):
        if isinstance(mt, int):
            mt = myTime(0,0,mt)
        if not isinstance(mt, myTime):
            raise TypeError
        return self.__add_obj__(mt)

    def __add_obj__(self, mt):
        if not isinstance(mt, myTime):
            raise TypeError
        self.secs += mt.secs
        self.mins += mt.mins
        self.hrs += mt.hrs
        
        if (self.secs > 59):
            self.mins += self.secs//60
            self.secs = self.secs%60
        if (self.mins > 59):
            self.hrs += self.mins // 60
            self.mins = self.mins % 60

        return self

    def __sub__(self, mt):
        if isinstance(mt, int):
            mt = myTime(0,0, mt)

        if not isinstance(mt, myTime):
            raise TypeError
        return self.__sub_obj__(mt)

    def __sub_obj__(self, mt):
        self.secs -= mt.secs
        self.mins -= mt.mins
        self.hrs -= mt.hrs
        
        if (self.secs < 0):
            self.mins -= 1
            self.secs += 60
    
        if (self.mins <0):
            self.hrs -= 1
            self.mins += 60
        return self
            
    def __mul__(self, num):
        if not isinstance(num, int):
            raise TypeError
            
        self.secs *= num
        self.mins *= num
        self.hrs *= num
        
        if (self.secs > 59):
            self.mins += self.secs//60
            self.secs = self.secs%60
        if (self.mins > 59):
            self.hrs += self.mins // 60
            self.mins = self.mins % 60
        return self
            
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.hrs, self.mins, self.secs)
        
t1 = myTime(10,10,10)
t2 = myTime(11,1,1)
t3 = myTime(1, 1, 2)


print(t1)
print(t1 - 70)
print(t1 + 70)
print(t1*2-t2)
print(t3*100)