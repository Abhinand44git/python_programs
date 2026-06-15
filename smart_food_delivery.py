def calculate_food_amount(quantity,price):
    return quantity*price

def calculate_delivery_charge(distance):
    if distance<5:
        return 40
    else:
        return 80

def calculate_discount(bill_amount,premium_memebership_status):
    discount=0
    if premium_memebership_status and bill_amount>1000:
        discount=150
    return discount

def generate_bill(**bill_details):
    print("\n")
    print("-------FOOD ORDER BILL-------")
    print("\n")
    for key,value in bill_details.items():
        clean_key = key.replace("_"," ".title())
        print(f"{clean_key} : {value}")

def restaurant_details(restaurant_name="Imperial Kitchen"):
    print("Restaurant Name: ",restaurant_name)

def add_Extra_items(*items):
    print("---Extra Items Ordered---")
    if not items:
        print("No Extra Items Selected.")
    else:
        for item in items:
            print(f"{item}")

def customer_details(**details):
    for key,value in details.items():
        print(f"{key} : {value}")

def displayoffer():
    print("Offer: Free Soft Drink on Orders Above ₹1500")

def get_offer():
    return "Offer: Free Soft Drink on Orders Above ₹1500"

def search_food(menu,item):
    if item.strip().lower() in [menu_item.lower() for menu_item in menu]:
        return item
    return None

customer_name=input("Enter Customer Name: ")
mobile_number=int(input("Enter Mobile Number: "))
food_item_name=input("Enter Food Item Name: ")
quantity=int(input("Enter Quantity: "))
price_per_item=float(input("Enter Price Per Item: "))
delivery_distance=float(input("Enter Delivey Distance(in Km): "))
premium_or_not=input("Enter Premium Membership Status(True/False): ").strip().lower()
premium_membership = premium_or_not == "true"

food_amount=calculate_food_amount(quantity,price_per_item)
delivery_charge=calculate_delivery_charge(delivery_distance)
discount_amount=calculate_discount(food_amount,premium_membership)

final_bill_amount=food_amount+delivery_charge-discount_amount

generate_bill(
    Customer_Name=customer_name,
    Mobile=mobile_number,
    Item=food_item_name,
    Price=food_amount,
    Delivery_fee=delivery_charge,
    Discount=discount_amount,
    Final_Bill=final_bill_amount,
)
print("\n")
print(f"Datatype of Quantity: {type(quantity)}")
print(f"Datatype of Price: {type(price_per_item)}")
print(f"Datatype of Premium Member: {type(premium_membership)}")
print("\n")
print(f"Is Quantity Integer?: {isinstance(quantity,int)}")
print(f"Is Price A Float?: {isinstance(price_per_item,float)}")
print(f"Is Premium Member Status A Boolean?: {isinstance(premium_membership,bool)}")
print("\n")
print(f"ID of Food Amount: {id(food_amount)}")
print(f"ID of FInal Bill Amount: {id(final_bill_amount)}")
add_Extra_items("Raita","Garlic Dips","Extra Sev")
customer_details(location="Bakery Junction",Payment="UPI",Preffered_Restaurant="Yellow Chilli")
print_val = displayoffer()
print(f"Display offer shows{print_val}")
print(f"{get_offer()}")
menu_items=["Chicken Biryani","Butter Naan","Chicken Curry","Chicken 65"]

search_query="Chicken 65"
search_result= search_food(menu_items,search_query)

if search_result is not None:
    print(f"Food Search Result: {search_result}")
else:
    print(f"Food Search Result: Item not available")