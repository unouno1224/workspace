class FourCal:
    def __init__ (self,first,second):
        self.result=0
        self.first = first
        self.second = second        
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
class MoreFourcal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result
    def div(self):
        try:
            result=self.first/self.second
        except:
            result=False
        return result
class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def give_money(self,other,money):
        self.money -=money
        other.get_money(money)
    def get_money(self,money):
        self.money+=money
    def show(self):
        print('{} : {}'.format(self.name, self.money))

if __name__ == "__main__":
    """ a=MoreFourcal(2,0)
    b=MoreFourcal(3,5)
    # a=FourCal(1,4)
    # b=FourCal(2,5)
    print (a.sum())
    print (b.sub())
    print (a.pow())
    print (a.div())
    print (b.div()) """
    
    g=Person('greg',5000)
    j=Person('john',3000)
    g.show()
    j.show()
    g.give_money(j,1000)
    g.show()
    j.show()
    print(dir())