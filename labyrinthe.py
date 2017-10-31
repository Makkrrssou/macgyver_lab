import random  

class Lab():
    def __init__(self):
        self.i=0
        self.j=0
        self.lab=dict()
        self.wall=["m",None]

    def build_wall(self):
        
        for self.i in range(0,16):
            for self.j in range (0,16):
                    if (self.i==0 and self.j==0) or (self.i==15 and self.j==15) :  #
                            self.lab[self.i,self.j]=None
                    else:
                            self.lab[self.i,self.j]==random.choice(self.wall)
                    self.j+=1
            self.i+=1
        return self.lab



##labi=Lab.build_wall()
##
##print(labi)
