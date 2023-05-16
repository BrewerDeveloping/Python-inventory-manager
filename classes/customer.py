import csv

class Customer:
    
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals) -> None:
        self.customer_id = int(customer_id)
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals.split('/') if current_video_rentals else []
        
        
    @classmethod
    def load_customer_from_csv(cls):
        customer_list = []
        with open('./data/customers.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                new_customer = cls(row['customer_id'], row['account_type'], row['first_name'], row['last_name'], row['current_video_rentals'])
                customer_list.append(new_customer)
                # print(row)
        return customer_list
    
    def __str__(self) -> str:
        return f"Customer ID: {self.customer_id} -- Name: {self.first_name} {self.last_name} "