book_names=[]
book_categories=("Biography","Fiction","Non-Fiction","History","Science")
unique_autors=set()
book_details={}

def collect_book_info():
    number_of_books=int(input("Enter the number of books present in library: "))
    for book in range(1,number_of_books+1):
        title=input("Enter Book Title: ")
        author=input("Enter Author Name: ")
        category=input("Enter Book Category: ")
        if category not in book_categories:
            print("Invalid Category")
            category="Non-Categorized"
        quantity=int(input("Enter Quantity Availble"))
        book_details[book]={
            "Title" : title,
            "Author" : author,
            "Categoty" : category,
            "Quantity" : quantity,
            "Status" : "Available"
        }
        book_names.append(title)
        unique_autors.add(author)

def display_available_books():
    print("\nAvailable Books")
    for book, data in book_details.items():
        if data["Quantity"]>0:
            print(f"{data['Ttila']} by {data['Author']} | Category: {data['Category']} | Quantity: {data['Quantity']}")
        else:
            print("Out of stock")

def sort_books():
    print("\nBooks Sorted Alphabetically")
    sorted_books=sorted(book_names)
    rank=1
    for title in sorted_books:
        print(f"{rank}. {title}")
        rank+=1

def search_books(title):
    if title in book_names:
        print(f"Book {title} is found in the library")
    else:
        print(f"Book {title} is not found in the library")

def issue_book(title):
    for book,data in book_details.items():
        if data["Title"]==title:
            if data["Quantity"]>0:
                data["Quantity"]-=1
                data["Status"]="Issued"
                print(f"Book {title} has been issued")
            else:
                print("Book is currently out of stock")
            return
    print(f"Book {title} not found")

def return_book(title):
    for book,data in book_details.items():
        if data["Title"]==title:
            data["Quantity"]+=1
            data["Status"]="Available"
            print(f"Book {title} has been returned")
            return
    print(f"Book {title} not found")

def count_books_per_category():
    print("Books count Per category")
    for category in book_categories:
        count=0
        for book, data in book_details.items():
            if data["Category"] == category:
                count+=1
        print(f"{category}: {count} book")

def generate_library_report():
    print("\n\tLibraby Report")
    total_books=len(book_details)
    total_quantity=0
    for book, data in book_details.items():
        total_quantity+=data["Quantity"]
    print("Total TItles: ",total_books)
    print("Total Books Availble: ",total_quantity)

def library_system():
    collect_book_info()

    display_available_books()
    sort_books()
    count_books_per_category()

    search_query=input("\nEnter book Title to search: ")
    search_books(search_query)

    issue_title=input("\nEnter book name to issue: ")
    issue_book()

    return_title=input("\nEnter book name to return: ")
    return_book(return_title)

    generate_library_report()

library_system()