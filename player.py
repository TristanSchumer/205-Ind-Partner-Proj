from team import Team
import team
class Player:
    age: int
    price: int
    team: str

    def __init__(self, name, age, price, team: Team):
        self.name = name
        self.age = age
        self.price = price
        self.position = Player.get_position
        self.nationality = Player.get_nationality
        self.team = team

    def to_string(self):
        return "Name: %s, Age: %i, Price: %i, Team: %s"% (self.get_name(), self.get_age(), self.get_price(), self.team.name)

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