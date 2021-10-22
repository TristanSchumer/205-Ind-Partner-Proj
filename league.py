import datetime
import transfer
import player

class League:
    league = None
    obj = Player("")

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

    # to do a transfer, we need two different teams, a player, the players price, and both of teams budgets to be affected by transfer
	# if a team doesnt have enough money for player, the budget cannot go through
    def do_transfer(self, obj, team):
		prev_team = obj.get_team()
		new_team = team
		player_price = obj.get_price()
		prev_team_budget = prev_team.get_transfer_budget()
		new_team_budget = new_team.get_transfer_budget()

		if new_team_budget <= player_price:
			print("%s does not have enough a large enough transfer budget to afford %s", new_team, obj.get_name())

		else:
			new_team_budget = new_team_budget - player_price
			prev_team_budget = prev_team_budget + player_price
			obj.team = new_team.get_name()
			# add player to teams set of players
			print("%s has transfered to %s from %s for %i", obj.get_name(), new_team.get_name(), prev_team.get_name(), obj.get_price())
    
		return None



