# def greet_name(name):
#     def say_hello():
#         print("Hello",name)
#     say_hello()
# greet_name("Ali")


# def calculator(a, b):
#     def add():
#         print(a+b)
#     def tarh():
#             print(a-b)
#     def taqsim():
#             print(a//b)
#     def zarb():
#             print(a*b)
#     add()
#     tarh()
#     taqsim()
#     zarb()
# calculator(5,5)


# def power(n):
#     def inner(x):
#         return x ** n
#     return inner
# n = int(input())
# x = int(input())
# p = power(n)
# print(p(x))


# def discount(percent):
#     def inner(price):
#         res = price*(100-percent)/100
#         if res == int(res):
#             res=int(res)
#         return res
#     return inner
# x = int(input())
# n = int(input())
# d = discount(x)
# print(d(n))


# def count():
#     cnt = 0
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         return cnt
#     return inner

# c = count()
# print(c())
# print(c())
# print(c())



# def chek(password):
#     def inner(vvod):
#         return password==vvod
#     return inner
# passs = input()
# ch = chek(passs)
# print(ch(input()))
        

# def prefick(pref):
#     def inner(name):
#         return pref+" "+name
#     return inner
# x= input()
# n = input()
# c = prefick(x)
# print(c(n))


# def multi(n):
#     def inner(x):
#         return x*n
#     return inner
# n = int(input())
# x = int(input())
# c = multi(n)
# print(c(x))


# def acccul():
#     total = 0
#     def inner(x):
#         nonlocal total
#         total+=x
#         return total
#     return inner
# acc = acccul()
# print(acc(int(input())))
# print(acc(int(input())))
# print(acc(int(input())))



# def attempts(limit):
#     cnt =0 
#     def inner():
#         nonlocal cnt
#         if cnt<limit:
#             cnt+=1
#             print("Attempt", cnt)
#         else:
#             print("Acses dinied")
                
#     return inner
# limi = int(input())
# c = attempts(limi)
# c()
# c()
# c()
# c()



# def acc_balance(balance):
#     def deposit(accaunt):
#         nonlocal balance
#         balance+=accaunt
#         print(balance)
#     def withdraw(accaunt):
#         nonlocal balance
#         if accaunt>balance:
#             print("Not enought")
#         else:
#             balance-=accaunt
#     return deposit,withdraw
# x = int(input())
# deposit,withdraw = acc_balance(x)
# deposit(500)
# withdraw(300)
# withdraw(1500)


# ----------------------
# def  time_greeting(name, period):
#     def greet():
#         return f"Good {period},{name}"
#     return greet
# x = input()
# n = input()
# c = time_greeting(n,x)
# print(c())



# def logger():
#     res = []
#     def log(message):
#         res.append(message)
#         return res
#     return log
# log = logger()
# print(log(input()))
# print(log(input()))
# print(log(input()))



# def greet_name(name):
#     def say_hello():
#         print("Hello",name)
#     say_hello()
# greet_name("Ali")



# def print_receipt(items):
#     def line(name, price):
#         return f"{name}:{price}"
#     cnt = 0
#     for name,price in items.items():
#         print(line(name,price))
#         cnt+=price
#     print(f"total:{cnt}")



# def validate_password(pwd):
#     def has_digit():
#         for i in pwd:
#             if i.isdigit():
#                 return True
#         return False
#     def has_upper():
#         for i in pwd:
#             if i.isupper():
#                 return True
#         return False
#     return len(pwd) >=8 and has_digit() and has_upper()
# print(validate_password("Python123"))  # True
# print(validate_password("python123"))  # False

# def calc_average(numbers):
#     def total():
#         summ = 0
#         for i in numbers:
#             summ+=i
#         return summ
#     return total()/len(numbers)
# print(calc_average([1,2,3]))


# def validate_password(pwd):
#     def has_digit():
#         for i in pwd:
#             if i.isdigit():
#                 return True
#         return False
#     def has_upper():
#         for i in pwd:
#             if i.isupper():
#                 return True
#         return False
#     return len(pwd)>=8 and has_digit() and has_upper()
# print(validate_password("Python123"))  # True
# print(validate_password("python123"))  # False


# def make_table(n):
#     def row(i):
#         return f"{n}*{i}={n*i}"
#     for i in range(1,6):
#         print(row(i))
# make_table(7)


# def level1():
#     print("level 1")
#     def level2():
#         print("Level 2")
#     def level3():
#         print("level 3")
#     level2()
#     level3()
# level1()
            

# def discount_price(price, percent):
#     def calc_discount():
#         return price*(percent/100)
#     return price-calc_discount()
# print(discount_price(200, 10))
# # 180.0


# def power_creator(exp):
#     def square(base):
#         return base**exp
#     return square
# sq = power_creator(2)
# cb = power_creator(3)
# ft = power_creator(4)
# print(sq(2))
# print(cb(3))
# print(ft(4))



# def make_multiplier(n):
#     def doub(x):
#         return x*n
#     return doub
# sq = make_multiplier(2)
# ms = make_multiplier(3)
# print(sq(7))
# print(ms(7))



# def make_greeter(greeting):
#     def andi(name):
#         return f"{greeting} {name}"
#     return andi
# sq = make_greeter("Salom")
# print(sq("Ali"))


# def sndd(x):
#     def add(n):
#         return n+x
#     return add
# add5 = sndd(5)
# print(type(add5))
# print(add5.__name__)


# def smd(n):
#     def add(x):
#         return x+n
#     return add
# add5 = smd(5)
# print(add5.__closure__[0].cell_contents)


# def smd():
#     def  inner():
#         return "Hello"
#     return inner
# add5 = smd()
# print(add5.__closure__)


# 20-----------------------------------------------------------------------------------
# def make_converter(rate):
#     def add(n):
#         return n*rate
#     return add
# sq = make_converter(11)
# print(sq(100))


# def make_tag(tag):
#     def inn(hel):
#         return f"<{tag}>{hel}<{tag}>"
#     return inn
# sq = make_tag("c")
# print(sq("Hello"))



# def make_checker(min_len):
#     def add(n):
#         return len(n)>=min_len
#     return add
# sq = make_checker(8)
# print(sq("qwerty"))




# def make_in_range(low, high):
#     def add(number):
#         return low<=number<=high
#     return add
# sq = make_in_range(13,19)
# print(sq(15))


# def make_word_filter(banned):
#     def inn(word):
#         for i in banned:
#             word=word.replace(i,"***")
#             return word
#     return inn
# clean = make_word_filter({"this"})
# print(clean("this is bad word"))  



# def make_logger(prefix):
#     def message(word):
#         print( f"[{prefix}] {word}")
#     return message
# infa = make_logger("INFO")
# err = make_logger("ERROR")
# infa("started")
# err("opern")


# def counter():
#     cnt = 0
#     def inn():
#         nonlocal cnt
#         cnt+=1
#         return cnt
#     return inn
# sq = counter()
# print(sq())
# print(sq())
# print(sq())



# def counter():
#     cnt = 0
#     def inn():
#         nonlocal cnt
#         cnt+=1
#         return cnt
#     return inn
# sq = counter()
# sd = counter()
# print(sq())
# print(sq())
# print(sd())


# def counter(start=0, step=1):
#     cont = start
#     def inn():
#         nonlocal cont
#         cont+=step
#         return cont
#     return inn
# c=counter(10, 5)
# print(c(), c(), c()) 



# def make_countdown(n):
#     cnt = n
#     def minn():
#         nonlocal cnt
#         if cnt<=0:
#             return "Done"
#         cnnn=cnt
#         cnt-=1
#         return cnnn
#     return minn
# cd = make_countdown(3)
# print(cd(), cd(), cd(), cd())  



# def make_accumulator():
#     cnt = 0
#     def cnn(num):
#         nonlocal cnt
#         cnt+=num
#         return cnt
#     return cnn
# sq = make_accumulator()
# print(sq(10))
# print(sq(5))
# print(sq(20))


# def make_average():
#     tot = 0
#     avarage=0
#     def avare(number):
#         nonlocal tot,avarage
#         tot+=number
#         avarage+=1
#         return tot/avarage
#     return avare
# avg = make_average()
# print(avg(10))  # 10.0
# print(avg(20))  # 15.0
# print(avg(30))  # 20.0


# def make_limited(n):
#     cnt = 0
#     def minn():
#         nonlocal cnt
#         if cnt<n:
#             cnt+=1
#             return f"Click {cnt}" 
#         else:
#             return "Limit hgfhgf"
#     return minn
# click = make_limited(2)
# print(click())  # Click 1
# print(click())  # Click 2
# print(click())  # Limit reached



# def make_counter():
#     cnt = 0
#     def inc():
#         nonlocal cnt
#         cnt+=1
#     def dec():
#         nonlocal cnt
#         cnt-=1
#     def get():
#         nonlocal cnt
#         return cnt
#     return inc,dec,get

# inc, dec, get = make_counter()
# inc(); inc(); dec()
# print(get())  # 1



# def make(low,high):
#     def nn(number):
#         return low<=number<=high
#     return nn
# is_teen = make(13, 19)
# print(is_teen(15))  # True
# print(is_teen(25))  # False


# def outer():
#     x = 1
#     def inner():
#         print(x)
#     x = 2
#     inner()
# outer()  # ?



# def make():
#     count = 0
#     def inc():
#         nonlocal count
#         count += 1
#         return count
#     return inc

# f = make()
# f()  # UnboundLocalError



# st = ["wobil","djncjd","kdnv"]
# st.sort(lambda a:a[1])
# print(st)



# def stars(func):
#     def wrapper():
#         print("*****")
#         func()
#         print("*****")
#     return wrapper
# def hello_line(funcc):
#     def wrapper():
#         print("Hi")
#         funcc()
#     return wrapper
# @stars
# @hello_line
# def title():
#     print("Python")
# title()


def decorator(func):
    cnt = 0
    def wrapper():
        nonlocal cnt
        func()
        cnt+=1
        print(f"Cal {cnt}")
    return wrapper
@decorator
def resault():
    print("Hello")
resault()
resault()
resault()














        