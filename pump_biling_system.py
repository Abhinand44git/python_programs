customer_name=input("Enter Customer Name: ")
vehicle_number=input("Enter Vehicle Number: ")
fuel_type=input("Enter Fuel Type: ")
liters_filled=int(input("Enter Liters Filled: "))
price_per_liter=float(input("Enter Price Per Liter: "))
premium_card=bool(input("Premium Card(True/False): "))

print("------- PETROL BILL-------")
print("Customer Name: ",customer_name)
print("Vehicle NUmber: ",vehicle_number)
print("Fuel Type: ",fuel_type)

total_fuel_price=liters_filled*price_per_liter
gst=total_fuel_price*0.05
final_bill_amount=total_fuel_price+gst

print("Fuel Amount: ",total_fuel_price)
print("GST Amount: ",gst)

final_bill_amount+=650 #oil change charge
final_bill_amount-=100 #discount of the day
final_bill_amount*=0.9 #service fee

print("Final Bill Amount: ",final_bill_amount)

if premium_card==True and final_bill_amount>3000:
    final_bill_amount-=200 #extra discount for premium members
print("Datatype of liters: ",type(liters_filled))
print("Datatype of premium card: ",type(premium_card))

print("Is liters float? ",isinstance(liters_filled,float))
print("Is premium card boolean? ",isinstance(premium_card,bool))
print("ID of Total Amount",id(total_fuel_price))
print("ID of Final Amount",id(final_bill_amount))