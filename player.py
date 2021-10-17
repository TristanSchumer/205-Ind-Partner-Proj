class Player:
    age: int
    price: int

    def __init__(self, name):
        self.name = name
        self.age = Player.age
        self.price = Player.price
        self.position = Player.get_position
        self.nationality = Player.get_nationality
        self.team = set()

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_nationality(self):
        return self.nationality