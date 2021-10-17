import datetime
import transfer
import player

class League:
    league = None
    obj = Player()
    te

    @classmethod
    def get(self):
	    if self.league is None:
		    self.league = League()
		    return self.league

    def __init__(self):
	    self.players = set()
	    self.teams = set()
	    self.transfers = set()

    def add_player(self, player):
	    self.players.add(player)

    def get_players(self):
	    return self.players

    def add_teams(self, team):
	    self.teams.add(team)

    def get_teams(self):
	    return self.teams

    def find_player(self, name):
	    players = []
	    for p in self.players:
	    	if p.get_name() == name:
        	    players.append(p)
		return players

    def find_player_by_name(self, name):
	    for p in self.players:
		    if p.get_name() == name:
			    return p
	    return None

    def find_team_by_rank(self, rank):
	    for t in self.teams:
		    if t.get_ranking() == rank:
			    return t
	    return None

    # might not work right if we want to show both the previous team and new team
    def show_transfers(self):
	    for t in self.transfers:
		    s = t.get_player() + ' => ' + t.get_team() + 'for $'
		    print(s)

    # can we pass in a Player object instead of just the name of a player?
    def do_transfer(self, obj, new_team):
        prev_team = obj.get_team()
        print(prev_team)



