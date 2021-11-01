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

    Salah = player.Player('Mohamed Salah', 27, 100000000, team1)
 
    Ronaldo = player.Player('Cristiano Ronaldo', 31, 100000000, team2)

    Kante = player.Player("N'Golo Kante", 21, 100000000, team_3)

    league1.add_player(Salah)
    league1.add_player(Ronaldo)
    league1.add_player(Kante)

    league1.add_teams(team_1)
    league1.add_teams(team_2)
    league1.add_teams(team_3)

    # print("Kante's age is", Kante.age)
    # print("Ronaldo's price is $", Ronaldo.price)
    for i in league1.get_teams():
        print(i.to_string())

    for i in league1.get_players():
        print(i.to_string())
    # print(league1.get_players())
    # print(league1.get_teams())

    # league1.do_transfer(Kante, team_1)


main()