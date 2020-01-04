#Perform operator overloading for triangle in a way that add function adds
#length of three sides and greater operator returns the side with highest length


class Triangle:
    def __init__(self,a=0,b=0,c=0):
        self.a=a
        self.b=b
        self.c=c

    def __add__(self,other):
        self.l=self.a+self.b+self.c
        print(self.l)

    def __gt__(self,other):
        if self.a>self.b and self.a>self.c:
            print("a has the highest length which is  ",self.a)

        elif self.b>self.a and self.b>self.c:
            print("b has the highest length which is  ",self.b)

        else:
            print("c has the highest length which is  ",self.c)
