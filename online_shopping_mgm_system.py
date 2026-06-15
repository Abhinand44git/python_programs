cart_products=[]
store_products={}
store_categories=("Cosmetics","Dairy Products","Home Appliance","Spices","Toileteries")
unique_brands=set()

def collect_product_details():
    total_price=0
    while True:
        product_name=input("Enter Product Name: ")
        if product_name.lower() == "checkout":
            break
        product_price=int(input("Enter Product Price: "))
        brand_name=input("Enter Brand Name: ")
        category=input("Enter Product Category: ")
        if category not in store_categories:
            print("Invalid Category")
            category="Uncategorized"

        store_products[product_name]={
            "Price" : product_price,
            "Category" : category,
            "Brand": brand_name
        }

        cart_products.append(product_name)

        unique_brands.add(brand_name)

        total_price+=product_price
    
    print(f"\nTotal items in cart:{len(cart_products)}")
    return total_price

def apply_discounts(total_price):
    if total_price>8000:
        return total_price*0.80
    elif total_price>5000:
        return total_price*0.85
    elif total_price>2000:
        return total_price*0.90
    else:
        print("No Discount Applicable.")
        return total_price

def sort_products():
    sorting_products=sorted(store_products.items(), key=lambda x: x[1]['Price'])
    rank=1
    for name,data in sorting_products:
        print(f"{rank}. {name} | Brand: {data['Brand']} | Price: {data['Price']}")
        rank+=1

def search_products(name):
    if name not in store_products:
        print(f"Product {name} is not found in the inventory.")
    else:
        details= store_products[name]
        print(f"Found, Product:{name} | Brand: {details['Brand']} | Price: {details['Price']}")
def generate_summary(final_bill):
    print("\n")
    print("\tPurchase Summary")
    print("\n")
    print("Items Ordered: ",*cart_products, sep=", ")
    print("Unique BrandsExplored: ",*unique_brands, sep=", ")
    print(f"Final Bill Amount: {final_bill}")

def show_shopping_system():
    raw_total=collect_product_details()
    final_bill=apply_discounts(raw_total)
    generate_summary(final_bill)
    sort_products()

    query=input("Enter product name to search: ")
    search_products(query)

show_shopping_system()