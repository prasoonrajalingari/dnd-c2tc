import pyflowchart


def choosefruit(fruitname):  #changes testing
    if fruitname == 'apple':
        a= 5
        b= 5
        c = a+b
        print (f'{c}')
        print(f'you have choosen Apple')
    else:
        print(f'you have choosen {fruitname}')


def foo(a, b):
    if a:
        print("a")
        a = 'apple'
    else:
        for i in range(3):
            print("b")
            b= 'banana'
    choosefruit(b)
    return a 

foo(True,False)
