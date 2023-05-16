import csv

class Inventory:
    def __init__(self, id, title, rating, release_year, copies_available) -> None:
        self.id = int(id)
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available
        

    @classmethod
    def load_inventory_from_csv(cls):
        video_list = []
        with open('./data/inventory.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                new_video = cls(row['id'], row['title'], row['rating'], row['release_year'], row['copies_available'])
                video_list.append(new_video)
        return video_list
    
    # @classmethod
    # def find_video_by_id(cls, id):
    #     for video in cls.load_inventory_from_csv():
    #         if video.id == id:
    #             return video
    #     return None
    
    def __str__(self) -> str:
        return f"Title: {self.title} -- Copies in store: {self.copies_available}"