5#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 8 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი:  

#1. შექმენი კლასი car გაუკეთე 2 დეფაულტ ატრიბუტი , დაუმატე 2 მეთოდი, str და len. ასევე დინამიურად 2 შენს მიერ მოფიქრებული ატრბუტი.
# საბოლოოდ გამოჰქონდეს შესაბამისი მესიჯი.
# class car:
#     def __init__ (self,brend = 'bmw',year = '2015'):
#         self.brend = brend
#         self.year = year
#     def info (self):
#         return f'model is{self.brend} year is{self.year}'
#     def __str__(self):
#         return f'Car: {self.brend}'
         
#     def __len__(self):
#         return len(str(self.brend))
# car1 = car('mersedes','2020')
# setattr(car1,'model','m-1')
# setattr(car1,'color','blue')
# print(car1.info())
# print(car1.model)
# print(car1.color)
# print(len(car1))
# print(car1)
#2. დააიმპორტე მათემატიკის მოდული და იპოვე პოლიმორფიულდ ფართობები შემდეგი ფიგურებისთვის: წრე, კვადრატი, მართკუთხედი.
#გამოიტანე ყველას ფართობი, შესაბამისი მესიჯებით.
# from math import *
# class area :
#     def S (self):
#         pass
# class sqvear(area):
#     def __init__(self,side):
#         self.side = side
#     def S (self):
#         return self.side **2
# class reqtengular(area):
#     def __init__(self,side,second_side):
#         self.side = side
#         self.second_side = second_side
#     def S (self):
#         return self.side * self.second_side
# class sircle(area):
#     def __init__(self,radius):
#         self.radius = radius
#     def S (self):
#         return pi * self.radius **2
# circle1 = sircle(10)
# sqvear1 = sqvear(3)
# reqtengular1 = reqtengular(2,4)
# print(circle1.S(),reqtengular1.S(),sqvear1.S())

    
    
# 3. შექმენ პერსონ აიდის კლასი, სადაც დაახასიათებ სახელით, ასაკით , სქესით და ინფო მეთოდის მეშვეობით გამოიტან მომხმარებელზე ინფოს.
# class id:
#     def __init__(self,name,age,gender):
#         self.name = name 
#         self.age = age
#         self.gender = gender
#     def info (self):
#         return f'iformaishon name: {self.name} age: {self.age} gender: {self.gender}'
# person1 = id('Gela','16','man')
# print(person1.info())
# 4. შექმენი მშობელი კლასი გუნდი და შვილობილლი ფეხბურთისგუნდი, შექმენით Team კლასი, რომელსაც აქვს ფეხბურთელების სია. შექმენით FootballTeam კლასი, რომელიც მემკვიდრეობას იღებს Team კლასიდან.
# შექმენით Team კლასი, რომელსაც აქვს ფეხბურთელების სია. შექმენით FootballTeam კლასი, რომელიც მემკვიდრეობას იღებს Team კლასიდან. გამოიყენე super() ფუნქციაც.
# განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:
# class Team:
#     def __init__(self, name):          
#         self.name = name
#         self.players = []
#     def add_pl(self, added_pl):
#         self.players.append(added_pl)    
#     def pl_info (self):
#         print (self.name ,"players :", '. '.join(self.players) ) 
# class FootballTeam(Team):
#     def __init__(self, name,liga):
#         super().__init__(name)
#         self.liga = liga
#     def liga_info (self):
#         return f"Football : {self.name} liga : {self.liga} "
# team = FootballTeam('fc barselona', "mkaka")
# team.add_pl("leonelo mesi")
# team.add_pl('makaka 2')
# print(team.liga_info(),team.pl_info())
          

#5. მოიფიქრე და შექმენი წიგნების მართვის სისტემა. (ყოველივე მოიფიქრე შენით, შეგიძლია გამოიყენო 2 კლასი/ნებისმიერი მეთოდებით.)
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:
# class Book:
#     def __init__(self, title, author, ):
#         self.title = title
#         self.author = author
# class Book:
#     def __init__(self, title, author,isbn ):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#     def __str__(self):
#         return f"სათაური:{self.title} ავტორი:{self.author} გაერთიანულებული ნუმერაცია:{self.isbn} "
# class liber:
#     def __init__(self):
#         self.books = []
#     def add_book (self,book):
#         self.books.append(book)
#     def list_books (self):
#          return "\n".join(str(book) for book in self.books)
# book1 = Book("მე ბებია ილიკო ილარიონი",'ნოდარ დუმბაძე',"1234")
# book2 = Book("ვეფხვის ტყაოსანი",'შოთა რუსთაველი',"4321")
# libery = liber()
# libery.add_book(book1)
# libery.add_book(book2)
# print(libery.list_books())



#6. მოხმარებელთა მართვის სისტემა: შექმენით User კლასი, რომელიც მოიცავს სახელს, ასაკს და ელ.ფოსტას. დაამატეთ Admin კლასი, რომელიც მემკვიდრეობს User კლასიდან და აქვს მეთოდად დამატებითი უფლებები.
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:
# class User:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

# class User:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#     def info (self):
#         return f"name: {self.name} age: {self.age} email: {self.email}"
#     def grd (Self):
#         return f"welcom to our platporm {Self.name}"
# class admin(User):
#     def __init__(self,name,age,email,admin_pr):
#         super().__init__(name,age,email)
#         self.admin_pr = admin_pr
#     def info1 (self):
#         return f"{super().info()}, admin pr {self.admin_pr}"
#     def add_admin(self, user, permission):
#         return f"Admin {self.name} granted '{permission}' permission to {user.name}"
#     def remove_admin(self, user, permission):
#         return f"Admin {self.name} removed '{permission}' permission from {user.name}."
# user1 = User('mirza','15','makaka1@.gmail.com')
# admin1 = admin('makaka','16','makaka2008.@gmail.com','awrething')
# print(user1.info())
# print(admin1.info())
# print(admin1.info1())
# print(admin1.add_admin(user1,'edit'))
# print(admin1.remove_admin(user1,'delete'))

#7. შექმენი სოც.ქსელის პლატფორმის მართვის სისტემა: კლასი მომხმარებლით დაახასიათე მომხარებელი, და ერთი ატრიბუტი წარმოადგენდეს ლისტს:
# შემდეგნაირად:
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.friends = []
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.friends = []
#     def add (self,friend):
#         if friend not in self.friends:
#            self.friends.append(friend)
#     def get (self):
#         return self.friends
#     def info (self):
#         return f"name: {self.name} year old {self.age} "
# user1 = User('გელა','20')
# user2 = User("ნინო",'19')
# user1.add(user2)
# user2.add(user1)
# print(user1.info())
# print(user2.info())
# for friend in user1.get():
#     print(f"{friend.name}, {friend.age} years old") 
# for friend in user2.get():
#     print(f"{friend.name}, {friend.age} years old") 

# შექმენი მეგობრის დამატების მეთოდი მოცემულ კლასსში. დაამატე კლასი SocialMediaUser. წამოიღე მომკვიდრეობითი ატრიბუტები და დაამატე ერთი ატრიბური. გამოიტანე შესაბამისი შედეგი.
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.friends = []
#     def add (self,friend):
#         if friend not in self.friends:
#            self.friends.append(friend)
#     def get (self):
#         return self.friends
#     def info (self):
#         return f"name: {self.name} year old {self.age} "
# class SocialMediaUser(User):
#     def __init__(self, name, age,sbc_count = 0):
#         super().__init__(name, age)
#         self.sbc_count = sbc_count
#     def add_sbc (self):
#         self.sbc_count +=1
#     def info(self):
#         print(super().info(), 'followers : ',self.sbc_count)
# user1 = SocialMediaUser('გელა', 20)
# user2 = SocialMediaUser("ნინო", 19)
# user1.add(user2)
# user2.add(user1)
# user1.add_sbc()
# user1.add_sbc()
# user2.add_sbc()
# print(user1.info())
# print(user2.info())
# for friend in user1.get():
#     print(f"{friend.name}, {friend.age} years old")
# for friend in user2.get():
#     print(f"{friend.name}, {friend.age} years old")
#8. შექმენი ბანკის ანგრიშების მართვის სისტემბა:შექმენით BankAccount კლასი, რომელიც მოიცავს ანგარიშის ნომერს, ბალანსსა და დეპოზიტების/ამოღებების მეთოდებს. 
# ბალანსი უნდა იყოს private და უნდა შესაბამისი მეთოდებით უნდა შეგვეძლოს ანგარიშის გამოტანა, და მისი შეცვლა.
# class BankAccount:
#     def __init__(self, account_number):
#         self.__account_number = account_number  
#         self.__balance = 0
# class BankAccount:
#     def __init__(self, account_number):
#         self.__account_number = account_number  
#         self.__balance = 0  

#     def get_account_number(self):
#         return self.__account_number

#     def get_balance(self):
#         return self.__balance

#     def depo(self, amount):
#         if amount > 0:
#             self.__balance += amount  
#             print(f"Deposited {amount}. Now balance is {self.__balance}.")
#         else:
#             print("Error")

#     def get_money(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount  
#             print(f"money get {amount}. now balance is {self.__balance}.")
#         elif amount > self.__balance:
#             print("you dont have anought mone go work")
#         else:
#             print("Error")
# account = BankAccount(12345)
# account.depo(500)  
# account.get_money(200)  
# account.get_money(1000)  
# print(f" balance: {account.get_balance()}")  
#9. მოიფიქრე ოოპ-ის გამოყენების მაგალითი.
# class studen:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.grades = []
#     def add_gd (self,grade):
#         self.grades.append(grade)
#     def avrage (self):
#         if len(self.grades) > 0:
#             return sum(self.grades) / len(self.grades)
#         else :
#             print('you dont have any grades')
#     def info(self):
#         print(f"name:{self.name} age: {self.age} avrage grade {self.grades}")
# studen1 = studen('გელა','19')
# studen1.add_gd(50)
# studen1.add_gd(100)
# print(studen1.info())
# print(studen1.avrage())
#10. მოიფიქრე და დაახასიათე ნებისმიერი ობიექტი ოოპის მემკვიდრეობის მეშვოებით. გამოიყენე იერარქიული მემკვიდრეობა.
class animal:
    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound
class dog(animal):
    def __init__(self, name, age, sound,kind,collor):
        super().__init__(name, age, sound)
        self.kind = kind
        self.collor = collor
    def info (self):
        return  f'name: {self.name} age: {self.age} dog make sound {self.sound} and kind of {self.kind} color is {self.collor}'
class cat(animal):
    def __init__(self, name, age, sound,color):
        super().__init__(name, age, sound)
        self.color = color
    def info (self):
        return f'name: {self.name} age: {self.age} cat make sound {self.sound} and collor is {self.color}'
dog1 = dog('არჩი','6','ვაფ','ლაბლადორ','თეთრი')
cat1 = cat('მიაუ','3','მიაუ','კარაქის ფერი')
print(dog1.info())
print(cat1.info())