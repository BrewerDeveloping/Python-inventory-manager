from classes.inventory import Inventory
from classes.customer import Customer
import csv


class VideoStore:
    def __init__(self, name) -> None:
        self.name = name
        self.video = Inventory.load_inventory_from_csv()
        self.customer = Customer.load_customer_from_csv()
        #self.rented = Customer.grab_rented()
        
        
    #Option 1 of the menu
    def get_current_inventory(self):
        return self.video
    
    # Option 2 of the menu
    def get_all_customers(self):
        return self.customer
    
    def find_customer_by_id(self, customer_id):
        for customer in self.customer:
            if customer.customer_id == customer_id:
                return customer
        return None
    
    def find_video_by_id(self, video_id):
        for video in self.video:
            if video.id == video_id:
                return video
        return None
    
    # Option 3 of the menu
    def current_rented_video_by_customer_id(self, customer_id):
        customer = next((c for c in self.customer if c.customer_id == customer_id), None)
        if customer is None:
            print(f"No customer found with ID {customer_id}")
            return
        
        # now I need to see ifthe customer has any rentals
        if not customer.current_video_rentals:
            print(f"{customer.first_name} {customer.last_name} has no rentals currently.")
            return
        
        # show the titles that the customer has rented
        print(f"{customer.first_name} {customer.last_name} currently has the following rentals: ")
        for each_rental, rental_title in enumerate(customer.current_video_rentals):
            print(f"{each_rental + 1}. {rental_title}")
    
    # Option 4 of the menu
    def add_user(self):
        acc_type_prompt = """
        "sx" = standard account: max 1 rental out at a time
        "px" = premium account: max 3 rentals out at a time
        "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
        "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies
        """
        
        # Restriction to make sure no other text can be used other than the account type's lsited
        valid_acc_types = ['sx', 'px', 'sf', 'pf']
        customer_id = input("Enter the customer ID: ")
        
        # try to prevent duplicate ID's
        for customer in self.customer:
            if customer.customer_id == int(customer_id):
                print("A customer with that ID already exists.")
                return
        
        account_type = input(f"Here is a list of account type's {acc_type_prompt}\nEnter the account type for the customer: ")
        
        # now check against the valid account type list 
        if account_type not in valid_acc_types:
            print("Invalid account type. Please enter a valid account type from the list above.")
            return
        
        first_name = input("Enter customer's first name: ")
        last_name = input("Enter customer's last name: ")
        current_video_rentals = ""
        
         # need to create the new customer
        new_customer = Customer(customer_id, account_type, first_name, last_name, current_video_rentals)
        
        # adds the new customer to the custoemr list
        self.customer.append(new_customer)
        print(f"Customer {new_customer.first_name} {new_customer.last_name} has been added to the store.")
    
    # Option 5 of the menu
    def rent_video_by_customer_id(self):
        
        # first I need to get the customer's id
        customer_id = int(input("Enter the customer ID: "))
        customer = next((c for c in self.customer if c.customer_id == customer_id), None)
        if customer is None:
            print(f"No customer found with ID {customer_id}")
            return
        
        # Need to add the video ID's with titles so the user knows what to select from/
        print("Available videos:")
        for video in self.video:
            if int(video.copies_available) > 0:
                print(f"ID -- {video.id}  |  Title -- {video.title}")
        
        # Now I need to get the video ID
        video_id = int(input("Enter the video ID: "))
        video = next((v for v in self.video if v.id == video_id), None)
        if video is None:
            print(f"No video found with ID {video_id}")
            return
        
        # Now rent the video to the customer.
        if (customer.account_type in ['sf', 'pf'] and (video.rating in ['R'])):
            print(f"Sorry {customer.first_name} {customer.last_name} can't rent R rated movies because of account type!")
            return
        if (customer.account_type in ['sx', 'sf'] and len(customer.current_video_rentals) >= 1) or \
            (customer.account_type in ['px', 'pf'] and len(customer.current_video_rentals) >= 3):
                print(f"Sorry, {customer.first_name} {customer.last_name} has reached the maximum number of rentals for the account type!")
                return
        
        
        if int(video.copies_available) <= 0:
            print("This video is currently NOT available for rent.")
            return
        

        customer.current_video_rentals.append(video.title)
        video.copies_available = str(int(video.copies_available) - 1)
        print(f"{video.title} has been rented out to {customer.first_name} {customer.last_name}")
    
    # Option 6 of the menu
    def return_rental_by_customer_id(self, customer_id):
       # First, find the customer with the given ID
        customer = next((c for c in self.customer if c.customer_id == customer_id), None)
        if customer is None:
            print(f"No customer found with ID {customer_id}")
            return

        # Check if the customer has any rentals
        if not customer.current_video_rentals:
            print(f"{customer.first_name} {customer.last_name} has no rentals to return.")
            return

        # Ask the customer to select the rental to return
        rental_titles = customer.current_video_rentals
        print(f"{customer.first_name} {customer.last_name} currently has the following rentals:")
        for i, title in enumerate(rental_titles):
            print(f"{i + 1}. {title}")
        selection = input("Please select the rental to return (enter the corresponding number): ")

        # Validate the selection
        try:
            selection = int(selection)
            if selection < 1 or selection > len(rental_titles):
                raise ValueError()
        except ValueError:
            print("Invalid selection.")
            return

        # Return the selected rental
        rental_title = rental_titles[selection - 1]
        video = next((v for v in self.video if v.title == rental_title), None)
        if video is None:
            print(f"No video found with title '{rental_title}'")
            return
        customer.current_video_rentals = [title for title in rental_titles if title != rental_title]
        video.copies_available = str(int(video.copies_available) + 1)
        print(f"{rental_title} has been returned by {customer.first_name} {customer.last_name}")