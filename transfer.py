# transfer provides the association between a team and a player
# when a player transfers from one team to another, an instance of Transfer is
# created

from datetime import date


class Transfer:
    transfer_date = date.today()

    def __init__(self, team, player, fee, transfer_date):
        self.team = team
        self.player = player
        self.fee = fee
        self.transfer_date = transfer_date

    def get_team(self):
        return self.team

    def get_player(self):
        return self.player

    def get_fee(self):
        return self.fee

    def get_transfer_date(self):
        return self.transfer_date
        

    


