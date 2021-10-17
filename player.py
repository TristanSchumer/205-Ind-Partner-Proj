class Player:
    age: int
    price: int

    def __init__(self, name):
        self.name = name
        self.age = Player.age
        self.price = Player.price
        self.position = Player.get_position
        self.nationality = Player.get_nationality
        self.team = Player.get_team

    def to_string(self):
        s = self.name + ' age =' + str(self.age) + '; team =' + self.team + '; position =' + self.position + '; nationality =' + self.nationality + '; price =' + str(self.price)
        return s

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_nationality(self):
        return self.nationality

    def get_team(self):
        return self.team

    def get_age(self):
        return self.age

    def get_price(self):
        return self.price