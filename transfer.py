# transfer provides the association between a team and a player
# when a player transfers from one team to another, an instance of Transfer is
# created
class Transfer:

    def __init__(self, team, player):
        self.team = team
        self.player = player
 
    def get_team(self):
        return self.team

    def get_player(self):
        return self.player

        

    


