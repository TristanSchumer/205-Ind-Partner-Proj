import datetime
from team import Team
import transfer
import player

class League:
    league = None

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

    def find_team_by_name(self, name):
	    for t in self.teams:
		    if t.get_name() == name:
			    return True
	    return False

    def find_player_by_name(self, name):
	    for p in self.players:
		    if p.get_name() == name:
			    return True
	    return False

    def find_team_by_rank(self, rank):
	    for t in self.teams:
		    if t.get_ranking() == rank:
			    return t
	    return None

    def relegate(self):
	    self.teams.pop()
	    return None

    # to do a transfer, we need two different teams, a player, the players price, and both of teams budgets to be affected by transfer
	# if a team doesnt have enough money for player, the budget cannot go through
    def do_transfer(self, obj, team):
	    prev_team = obj.team
	    new_team = team
	    player_price = obj.price
		# need to figure out new way of setting transfer_budget
	    prev_team_budget = obj.team.transfer_budget
	    new_team_budget = new_team.transfer_budget

	    if new_team_budget < player_price:
		    print("%s does not have enough a large enough transfer budget to afford %s" % (new_team.get_name(), obj.get_name()))
		    # return False

	    else:
		    team.transfer_budget = new_team_budget - player_price
		    obj.team.transfer_budget = prev_team_budget + player_price
			
			# add player to teams set of players
		    print("%s has transfered to %s from %s for %i Euros" % (obj.get_name(), team.get_name(), obj.team.get_name(), obj.get_price()))
		   
		    
		    self.transfers.add("%s has transfered to %s from %s for %i Euros" % (obj.get_name(), team.get_name(), obj.team.get_name(), obj.get_price()))
		    obj.team = new_team

		    # return True
		
	    return None

    def incorrect_do_transfer(self, obj, team):
	    prev_team = obj.team
	    new_team = team
	    player_price = obj.price
		# need to figure out new way of setting transfer_budget
	    prev_team_budget = obj.team.transfer_budget
	    new_team_budget = new_team.transfer_budget
	    # print(new_team_budget, prev_team_budget)

	    if new_team_budget < player_price:
		    print("%s does not have enough a large enough transfer budget to afford %s" % (new_team.get_name(), obj.get_name()))
		    #return not None

	    else:
		    team.transfer_budget = new_team_budget - player_price
		    obj.team.transfer_budget = prev_team_budget + team.transfer_budget
			
			# add player to teams set of players
		    print("%s has transfered to %s from %s for %i Euros" % (obj.get_name(), team.get_name(), obj.team.get_name(), obj.get_price()))
		   
		
		    self.transfers.add("%s has transfered to %s from %s for %i Euros" % (obj.get_name(), team.get_name(), obj.team.get_name(), obj.get_price()))
		    obj.team = new_team

		    return None
		




