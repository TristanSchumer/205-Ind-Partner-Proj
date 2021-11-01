# team: the league has instances of team

class Team:
    def __init__(self, name, tranfser_budget: int, ranking: int, manager):
        self.name = name
        self.transfer_budget = tranfser_budget
        self.ranking = ranking
        self.manager = manager

    def to_string(self):
        return "Team: %s, Transfer Budget: %i, Ranking: %i, Manager: %s"% (self.get_name(), self.get_transfer_budget(), self.get_ranking(), self.get_manager())

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
