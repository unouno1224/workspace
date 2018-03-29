def func(li):
    li[0]= 'i am your father!'  #1

if __name__=="__main__":
    li = [1,2,3,4]
    func(li)
    print(li)


def func1(li):
    li= ['i am your father!', 2,3,4]
    print(li)
if __name__=="__main__":
    li = [1,2,3,4]
    func1(li)
    li.sort(reverse=True)
    print(li)

