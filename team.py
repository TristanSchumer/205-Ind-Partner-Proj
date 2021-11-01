# team: the league has instances of team

class Team:
    def __init__(self, name, tranfser_budget: int, ranking, manager):
        self.name = name
        self.transfer_budget = tranfser_budget
        self.ranking = ranking
        self.manager = manager

    def to_string(self):
        s = '"' + self.name + '" ' + self.manager + ' ' + self.ranking
        return s

    def get_name(self):
        return self.name

    def get_transfer_budget(self):
        return self.transfer_budget

    def get_ranking(self):
        return self.ranking

    def get_manager(self):
        return self.manager

    # def __eq__(self, other):
    #     return self.transfer_budget == other.transfer_budget

    # def __hash__(self):
    #     return hash(self.transfer_budget)
