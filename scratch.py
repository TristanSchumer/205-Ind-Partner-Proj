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

    # print("Kante's age is", Kante.age)
    # print("Ronaldo's price is $", Ronaldo.price)
    # print("Salah's team is", Salah.team)

    league1.do_transfer(Kante, team_1)


main()