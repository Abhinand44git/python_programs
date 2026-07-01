'''
class Student:
    def display(self):
        print("I am a student")
student = Student() #object creation
student.display()

class Employee:
    def __init__(self):
        print("Default Constructor is called")
employee = Employee()

class Car:
    color="Red" #class variable
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
car=Car("Pagani","Zonda")
print(car.brand,car.model,car.color)

car1=Car("Kia","Seltos")
print(car1.brand,car1.model,car1.color)

class Library:
    def __init__(self,name,location="Trivandrum",total_books=0):
        self.name = name
        self.location = location
        self.total_books = total_books
library=Library("cherry Tree")
print(library.name,library.location,library.total_books)
library1=Library("Solo Leveling","Seoul")
print(library1.name,library1.location,library1.total_books)

library2=Library("Tensura","Kyoto",400000)
print(library2.name,library2.location,library2.total_books)


#inheritance
#single_level inheritance
class User:#parent class or base class or super class
    def login(self):
        print("User logged in")

class Influencer(User):#child class or derived class or sub class
    def post_reels(self):
        print("Influencer posted a new reel")

influencer_user=Influencer()
influencer_user.login()
influencer_user.post_reels()

#Multi level inheritance
class Vehicle:
    def category(self,mode):
        print("Mode of transport: ",mode)

class Car(Vehicle):
    def vehicle_category(self,category,color):
        print("Type of Vehicle: ",category)
        print("Color of vahicle: ",color)

class ElectricCar(Car):
    def car_type(self,brand,category,variant,price):
        print("Brand Name: ",brand)
        print("Category: ",category)
        print("Variant: ",variant)
        print("Price of Car: ",price)

car_details=ElectricCar()
car_details.category("Road")
car_details.vehicle_category("Car","Purple")
car_details.car_type("Rimac","Electric","Nevera R",2200000)

#Multiple Inheritance
#try method resolution order
class ImageUpload:
    def upload_image(self,user_name,pic_name,):
        print(f"{user_name} posted {pic_name} successfully")

class ReelUpload:
    def upload_reels(self,user_name,reel_title,duration):
        print(f"{user_name} has uploaded a reel '{reel_title}' of {duration} seconds")

class Instagram(ImageUpload,ReelUpload):
    def user_analytics(self,user_name,owner,reaction):
        print(f"{user_name} is having a {owner} account with {reaction} reactions on posts uploaded today.")

user_details=Instagram()
user_details.upload_image("Rajesh","Good Morning.jpg")
user_details.upload_reels("Rajesh","Weekend Pary at Paragon",80)
user_details.user_analytics("Rajesh","Meta",345)

#try heirarchial and hybrid
class User:
    def __init__(self,user_name,email):
        self.user_name = user_name
        self.email = email

    def show_user(self):
        return f"Hello, {self.user_name}"

class AdminUser(User):
    def __init__(self, user_name, email,pin):
        User.__init__(self,user_name, email)
        self.pin = pin
    
    def show_admin(self):
        print("Admin PIN: ",self.pin)

class Customer(User):
    def __init__(self, user_name, email,balance):
        User.__init__(self,user_name, email)
        self.balance = balance

    def show_balance(self):
        print(f"{self.user_name} balance: {self.balance}")

class Guest(User):
    def __init__(self, user_name, email,expiry_days):
        User.__init__(self,user_name, email)
        self.expiry_days = expiry_days

    def show_expiry_days(self):
        print(f"{self.user_name} account expires in {self.expiry_days} days")

adm1 = AdminUser("Alex","alex@tmail.com","4356")
custm1 = Customer("Rita","ritaflorence@tmail.com",56734)
guest1 = Guest("Sid","Sidceaser@tmail.com",15)
print(adm1.show_user())
adm1.show_admin()
print(custm1.show_user())
custm1.show_balance()
print(guest1.show_user())
guest1.show_expiry_days()

#hybrid

class Device:
    def __init__(self,device_id,ip_address):
        self.device_id=device_id
        self.ip_address=ip_address

class Server(Device):
    def __init__(self, device_id, ip_address,cpu_cores,webhook_url):
        Device.__init__(self,device_id, ip_address)
        self.cpu_cores=cpu_cores
        self.webhook_url=webhook_url

    def send_critical_alert(self,message):
        print(f"ALERT TRIPPED Route: {self.webhook_url} | Payload: {message}")

    def show_server_details(self):
        print(f"Device ID: {self.device_id}\nIP Address: {self.ip_address}\nCPU Cores: {self.cpu_cores}")

class Switch(Device):
    def __init__(self, device_id, ip_address,port_count):
        Device.__init__(self,device_id, ip_address)
        self.port_count=port_count
    

class SmartSwtch(Switch,Server):
    def __init__(self, device_id, ip_address, port_count,cpu_cores,webhook_url):
        Switch.__init__(self,device_id, ip_address, port_count)
        Server.__init__(self,device_id,ip_address,cpu_cores,webhook_url)

    def monitor_traffic(self):
        alert=f"Intruder Detected"
        self.send_critical_alert(alert)

server=Server("Main Server","234.10.23.4",64,"https://api/hooks/123")
smartsw=SmartSwtch("sw-01", "192.168.1.1", 48,64,"https://api/hooks/123")
server.show_server_details()
print(smartsw.ip_address)
print(smartsw.port_count)
smartsw.monitor_traffic()

#polymorphism 2 types- method overloading,method overriding
print(len("Abhinand"))
print(len([10,59,39,40]))

class Calculator:
    def add(self,num1=0,num2=0,num3=0):
        return num1+num2+num3

calculate=Calculator()
print(calculate.add())
print(calculate.add(2))
print(calculate.add(4,6))
print(calculate.add(3,8,1))


#method overloading: same class,same method, different arguments

class Facebook:
    def login(self,email=None,password=None,phone_number=None):
        if email and password:
            print(f"Login through Email ID: {email}")
        elif phone_number and password:
            print(f"Login through Mobile Number: {phone_number}")
        else:
            print("Invalid Login")

facebook=Facebook()
facebook.login(email="yashraj@hotmail.com",password="qwerty12")
facebook.login(phone_number=8976852310,password="qwerty12")

class Payment:
    def pay(self,amount,method="cash"):
        if method=="cash":
            print(f"{amount} is collected via {method} method.")
        elif method=="upi":
            print(f"{amount} is collected via {method} method.")
        elif method=="card":
            print(f"{amount} is collected via {method} method.")

payment=Payment()
payment.pay(540)
payment.pay(350,method="upi")
payment.pay(620,method="card")
'''
#method overriding:different class, same method, same parameters
'''
manager has work and employee has work

class Employee:
    def work(self):
        print("Working as Employee")
    def skill(self):
        print("Python full Stack Intern")

class Manager(Employee):
    def work(self):
        super().work()
        print("Managing Team")

manager=Manager()
manager.work()
manager.skill()

class Order:
    def order_details(self,product_name,quantity):
        print(f"Order placed for {quantity} Qty {product_name}.")

class OnlineOrder(Order):
    def order_details(self, product_name, quantity,address):
        super().order_details(product_name, quantity)
        print(f"Order Delivered to {address}")

online_order=OnlineOrder()
online_order.order_details("Cinthol",4,"Bakery Junction")
'''
#abstraction: Hiding the implementation details from the user
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    def headlights_on(self):
        print("Headlights are set to low")

class Car(Vehicle):
    def start_engine(self):
        print("Car started using key.")
    def stop_engine(self):
        print("Engine stopped using key")

vehicle=Vehicle()
vehicle.start_engine()
vehicle.stop_engine()
vehicle.headlights_on()
'''
car=Car()
car.start_engine()
car.stop_engine()
car.headlights_on()
'''