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


