import league
import team
import player

def main():
    league1 = league.League().get()

    team1 = "Liverpool"
    team2 = "Manchester United"
    team3 = "Chelsea"
    manager1 = "Jurgen Klopp"
    manager2 = "Ole Gunnar Solskjaer"
    manager3 = "Thomas Tuchel"

    team_1 = team.Team(team1, 100000000, 2, manager1)
    team_2 = team.Team(team2, 100000000, 5, manager2)
    team_3 = team.Team(team3, 100000000, 1, manager3)

    Salah = player.Player('Mohamed Salah', 27, 100000000, team_1)
 
    Ronaldo = player.Player('Cristiano Ronaldo', 31, 100000000, team_2)

    Kante = player.Player("N'Golo Kante", 21, 100000000, team_3)

    league1.add_player(Salah)
    league1.add_player(Ronaldo)
    league1.add_player(Kante)

    league1.add_teams(team_1)
    league1.add_teams(team_2)
    league1.add_teams(team_3)

    # prints every team in league with info
    for i in league1.get_teams():
        print(i.to_string())

    # prints each player in league with info
    for i in league1.get_players():
        print(i.to_string())

    # transfer example money
    print("%s transfer budget: %i" % (team_2.get_name(), team_2.transfer_budget))
    print("%s transfer budget: %i" % (team_3.get_name(), team_3.transfer_budget))
    league1.do_transfer(Ronaldo, team_3)  
    print("%s transfer budget: %i" % (team_2.get_name(), team_2.transfer_budget))
    print("%s transfer budget: %i" % (team_3.get_name(), team_3.transfer_budget))

    print("\n")
    # transfer example teams
    print("%s's current team: %s" % (Kante.get_name(), Kante.team.get_name()))
    league1.do_transfer(Kante, team_1)
    print("%s's current team: %s" % (Kante.get_name(), Kante.team.get_name()))
    
    print("\n")
    # failed transfer
    print("%s transfer budget: %i" % (team_1.get_name(), team_1.transfer_budget))
    print("%s transfer budget: %i" % (team_3.get_name(), team_3.transfer_budget))
    league1.do_transfer(Ronaldo, team_1)  
    print("%s transfer budget: %i" % (team_1.get_name(), team_1.transfer_budget))
    print("%s transfer budget: %i" % (team_3.get_name(), team_3.transfer_budget))
    

    

main()