from classes.video_store import VideoStore
from classes.customer import Customer

video_store = VideoStore('Blockbuster')

# print(video_store)
        
prompt = """
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View store customers
3. View customer rented videos
4. Add new customer
5. Rent Video
6. Return Video
7. Exit
"""

while(True):
    
    try:
        mode = int(input(prompt))
        
    except ValueError:
        print("Invalid input, please enter a valid response from the menu!")
        continue
    
    if mode == 1:
        inventory_list = video_store.get_current_inventory()
        for video in inventory_list:
            print(video)

    elif mode == 2:
        customer_list = video_store.get_all_customers()
        for customer in customer_list:
            print(customer)
    
    elif mode == 3:
        try:
            customer_id = int(input("Please enter the customer ID you wish to see current rented videos for:\n>"))
            
        except ValueError:
            print("That customer ID does not exist, please enter a valud Customer ID.")
            continue
        
        video_store.current_rented_video_by_customer_id(customer_id)
    
    elif mode == 4:
        video_store.add_user()
    elif mode == 5:
        video_store.rent_video_by_customer_id()
    
    elif mode == 6:
        try:
            customer_id = int(input("Enter a customer ID: "))
        except ValueError:
            print("Invalid ID, please enter a valid ID")
            continue

        video_store.return_rental_by_customer_id(customer_id)
    
    elif mode == 7:
        break
        