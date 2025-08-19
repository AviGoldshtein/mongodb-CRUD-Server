class Soldier:
    def __init__(self, ID, first_name, last_name, phone_number, rank):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def to_dict(self):
        return {
            "ID": self.ID,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "rank": self.rank,
        }

    def __str__(self):
        return (
            f"ID: {self.ID}\n"
            f"first_name: {self.first_name}\n"
            f"last_name: {self.last_name}\n"
            f"phone_number: {self.phone_number}\n"
            f"rank: {self.rank}\n"
        )