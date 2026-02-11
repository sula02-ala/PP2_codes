# def complex(real=3,imag=4):
#     print(f"The real part is {real}, and the imaginary part is {imag}") - простая функция

# dict_args = {'real': 5, 'imag':6}    
# for x in sorted(dict_args):
#     print(x,dict_args[x]) - ключ и значение
# print(dict_args)

# ex=(1,2,3,4,5)
# print(*ex) - Output: 1 2 3 4 5

# def complex(real=3,imag=4):
#     print(f"The real part is {real}, and the imaginary part is {imag}")

# dict_args = {'real': 5, 'imag':6} 

# complex(**dict_args) - Output : The real part is 5, and the imaginary part is 6

# def complex(real=3,imag=4):
#     print(f"The real part is {real}, and the imaginary part is {imag}")

# nums=(1,2)
# complex(*nums) - Output: The real part is 1, and the imaginary part is 2

# def kaspi_pay(money=1000, state="Need to pay a service fee",action="Convert money", mood="Sad"):
#     print(f"-I have only {money} tenge left, but i {state}")
#     print(f"Since I {state} ,I will lose {money} tenge")
#     print(f"But luckly, i do have {money} tenge in cash")
#     print(f"So, I need to {action} and I`m {mood}")

# kaspi_pay(money,state,action,mood) - Output: -I have only 1000 tenge left, but i Need to pay a service fee
# Since I Need to pay a service fee ,I will lose 1000 tenge
# But luckly, i do have 1000 tenge in cash
# So, I need to Convert money and I`m Sad (Данная функция берет значения в том порядке, в котором мы записали изначально, если записать 3000 в начале, функция возьмет не 1000, а 3000, тк мы обновили значение money)

# def korean_street_food(ramen_kind,*arguments,**keywords):
#     print("-Do you have any", ramen_kind, "?")
#     print(f"-We are sorry, we dont have such a {ramen_kind} ramen")
#     for arg in arguments:
#         print(arg)
#     print("-"*40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])    


# korean_street_food("Kimchi Soy Sauce Octopus Extra Spicy","Its very sad .....","Its very very sad", shopkeeper="Michael Sch",client="LH44",sketch="Korean Street Food")        


# def func(a,b):
#     return a+b

# f = lambda a,b : a+b

# a=5
# b=4

# print(func(a,b))
# print(f(a,b))


# def make_increment(n):
#     return lambda x: x+n

# f=make_increment(42)
# print(f(58)) - 42 идет в n, 58 - идет в х

# def hello(name):
#     return f'Hello {name}'

# say = hello
# print(say("andrei"))


def func():
    func.a =10

print(func.__dict__) #{}
func() #мы вызываем функцию, которая добавляет а в словарь
print(func.__dict__) #{'a':10}
func.b=16 #тоже самое что и функция def func()
