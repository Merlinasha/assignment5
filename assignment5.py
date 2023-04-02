#Challenge 1

class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
        print("The square of x is",self.x**2)
        print("The square of y is",self.y**2)
        print("The square of z is",self.z**2)
        sum=((self.x**2)+(self.y**2)+(self.z**2))
        print("The sum of the square numbers x,y and z is",sum)
        return sum
 
sqadd = Point(1,3,5)
sqadd.sqSum()


#Challenge 2

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("The addition of num1 and num2:",self.num1+self.num2)
    def sub(self):
        print("The subration of num1 and num2:", self.num1-self.num2)
    def mul(self):
        print("The multipliation of num1 and num2:", self.num1*self.num2)
    def div(self):
        print("The divion of num1 and num2:", self.num2/self.num1)
   
    
result= calculator(10,94)
result.add()
result.sub()
result.mul()
result.div()

#Challange3

class student:
    def __setname__(self,s1):
        self.__name=s1
    def __getname__(self):
        print("The student name is ",self.__name)
    def __setrollnumber__(self,r1):
        self.__rollnumber=r1
    def __getrollnumber__(self):
        print("The roll number of the student is ",self.__rollnumber)

stu1=student()
stu2=student()

stu1.__setname__(input("Enter the name:"))
stu2.__setname__(input("Enter the name:"))
print("The student:",stu1.__dict__)
print("The student:",stu2.__dict__)
stu1.__getname__()
stu2.__getname__()

no1 = student()
no2 = student()

no1.__setrollnumber__(input("Enter the rollnumber:"))
no2.__getrollnumber__(input("Enter the rollnumber:"))
print("The rollno of the student:",no1.__dict__)
print("The rollno of the student:",no2.__dict__)
no1.__getname__()
no2.__getname__()




#challenge 4

class Account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance

acc=Account("Ashish",5000)
print("Account:")
print(acc.title)
print(acc.balance)

class Savingaccount(Account):
    def __init__(self,title,balance,interestrate):
        self.title=title
        self.balance=balance
        self.interestrate=interestrate


savingacc=Savingaccount("Ashish",5000,5)
print("Saving Account:")
print(savingacc.title)
print(savingacc.balance)
print(savingacc.interestrate)






#challange 5

class Account:
    def __init__(self,title ,balance):
        self.title=title
        self.balance=balance

    def withdrawal(self,amount):
        self.amount=amount
        print("withdrawal({})".format(self.balance-self.amount))

    def deposit(self,amount):
        self.amount=amount
        print("Deposit({})".format(self.balance+self.amount))
        

    def getbalance(self):
        
        print("current balance:",format(self.balance))

acc = Account("Ashish",2000)

print(acc.title)
print(acc.balance)
print("--------------------")
acc.withdrawal(500)
acc.deposit(500)
acc.getbalance()
print("--------------------")


class Savingsaccount:
    def __init__(self,title,balance,interestrate):
        
        self.interestrate = interestrate

    def interestamount(self,interestrate,balance):
        interest=((interestrate*balance)/100)
        print
        print("Interest amount is:",interest)

sacc = Savingsaccount("Ashish",2000,5)
print("Interestrate:",sacc.interestrate)
sacc.interestamount(5,2000)