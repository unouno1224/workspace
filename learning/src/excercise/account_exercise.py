class Account:
    num_cnt =0

    @classmethod
    def get_num_cnt(cls):
        return cls.num_cnt
    
    def __init__(self,name, money):
        self.user=name
        self.balance=money
        Account.num_cnt +=1

    def deposit(self,money):
        if money<0:
            return
        self.balance += money
        
    def withdraw(self,money):
        if money<0 or self.balance<money:
            return None,None
        self.balance -= money
        return money,self.balance

    def transfer(self,other,money):
        result = self.withdraw(money)
        if result:
            other.deposit(money)
            return True
        else:
            return False
    
    def __str__(self):
        return 'user : {}, balance : {}'.format(self.user, self.balance)

if __name__== "__main__":
    #객체 생성
    my_acnt = Account('greg', 5000)
    your_acnt = Account('john', 1000)

    #생성 확인
    print('object created')
    print(my_acnt)
    print(your_acnt)
    print()

    #인스턴스 메서드를 호출하는 방법
    #1. by object
    my_acnt.deposit(500)              #5
    #2. by class
    #Account.deposit(my_acnt, 500)    #6

    #deposit 확인
    print('deposit')
    print(my_acnt)
    print()

    #withdraw 함수 사용법
    print('withdraw')
    money,balance = my_acnt.withdraw(-1500)
    if money:
        print('withdrawn money : {}, balance : {}'.format(money,balance))
    else:
        print('Not enough to withdraw')
    print()

    #클래스 멤버에 접근하는 방법
    print('class member')
    #1.by class 
    print(Account.num_cnt)    
    #2.by object
    #print(my_acnt.num_acnt)
    print()

    #클래스 메서드를 호출하는 방법
    print('class method')
    #1.by class
    n_acnt = Account.get_num_cnt()
    #2.by object
    #n_acnt = my_acnt.get_num_cnt()
    
    print('The number of accounts : {}'.format(n_acnt))
    print()
    
    #메시지 패싱 
    print("message passing")
    print(my_acnt)
    print(your_acnt)
    res = my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)
    