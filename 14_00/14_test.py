class Partyanimal:
    x = 0
    name = ""
    
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    #def __del__(self):
     #   print('I am destructed', self.x)

#an = Partyanimal()
#an.party()
#an.party()
#an = 42
#print('an contains', an)

s = Partyanimal("Sally")
s.party()

j = Partyanimal("Jim")
j.party()
s.party()






        
        