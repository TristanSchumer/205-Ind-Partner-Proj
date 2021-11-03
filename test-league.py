#from _typeshed import Self
import unittest
import league
import team
import player

class TestTransfer(unittest.TestCase):
    league = None

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')
        cls.league = league.League().get()

        # Create a few teams and players
        team1 = "Liverpool"
        team2 = "Manchester United"
        team3 = "Chelsea"
        team4 = "Tottenham"
        team5 = "Wolves"
        team6 = "Manchester City"
        team7 = "Leicester"
        team8 = "Arsenal"
        teamRel = "Everton"

        manager1 = "Jurgen Klopp"
        manager2 = "Ole Gunnar Solskjaer"
        manager3 = "Thomas Tuchel"
        manager4 = "Antonio Conte"
        manager5 = "Bruno Lage"
        manager6 = "Pep Guardiola"
        manager7 = "Brendon Rodgers"
        manager8 = "Mikel Arteta"
        managerRel = "Rafeal Benitez"

        # we'll use the books and the patrons in the tests, so make them class variables
        cls.team_1 = team.Team(team1, 100000000, 2, manager1)
        cls.team_2 = team.Team(team2, 100000000, 5, manager2)
        cls.team_3 = team.Team(team3, 100000000, 1, manager3)
        cls.team_4 = team.Team(team4, 100000000, 4, manager4)
        cls.team_5 = team.Team(team5, 100000000, 6, manager5)
        cls.team_6 = team.Team(team6, 100000000, 3, manager6)
        cls.team_7 = team.Team(team7, 100000000, 7, manager7)
        cls.team_8 = team.Team(team8, 100000000, 8, manager8)
        cls.team_Rel = team.Team(teamRel, 100000000, 18, managerRel)


        cls.Salah = player.Player('Mohamed Salah', 29, 100000000, cls.team_1)
        cls.Ronaldo = player.Player('Cristiano Ronaldo', 36, 100000000, cls.team_2)
        cls.Kante = player.Player("N'Golo Kante", 30, 100000000, cls.team_3)
        cls.Kane = player.Player("Harry Kane", 28, 100000000, cls.team_4)
        cls.Traore = player.Player("Adama Traore", 25, 100000000, cls.team_5)
        cls.Grealish = player.Player("Jack Grealish", 24, 100000000, cls.team_6)
        cls.Vardy = player.Player("Jamie Vardy", 34, 100000000, cls.team_7)
        cls.Xhaka = player.Player("Granit Xhaka", 29, 100000000, cls.team_8)

        cls.league.add_player(cls.Salah)
        cls.league.add_player(cls.Ronaldo)
        cls.league.add_player(cls.Kante)
        cls.league.add_player(cls.Kane)
        cls.league.add_player(cls.Traore)
        cls.league.add_player(cls.Grealish)
        cls.league.add_player(cls.Vardy)
        cls.league.add_player(cls.Xhaka)

        cls.league.add_teams(cls.team_1)
        cls.league.add_teams(cls.team_2)
        cls.league.add_teams(cls.team_3)
        cls.league.add_teams(cls.team_4)
        cls.league.add_teams(cls.team_5)
        cls.league.add_teams(cls.team_6)
        cls.league.add_teams(cls.team_7)
        cls.league.add_teams(cls.team_8)

    @classmethod
    def tearDownClass(cls):
        # called one time, at the very end--if you need to do any final cleanup, do it here
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')

    def tearDown(self):
        # called after every test
        print('tearDown()')

    # --------------------------------------------------------------------------------------

    def test_incorrect_do_transfer(self):
        # this tests the incorrect version of do_transfer to library: this test will fail
        # transfer kante from chelsea to liverpool
        c = self.league.do_transfer(self.Ronaldo, self.team_8)
        self.assertIsNone(c)

        # try to transfer kante to man u
        # this should fail (man u has no money to buy kante)
        c = self.league.do_transfer(self.Traore, self.team_8)
        self.assertIsNotNone(c) 
        
 # --------------------------------------------------------------------------------------

    def test_transfer_players(self):
        # transfer kante from chelsea to liverpool
        c = self.league.do_transfer(self.Kante, self.team_1)
        self.assertIsNone(c)

        # try to transfer kante to man u
        # this should fail (man u has no money to buy kante)
        c = self.league.do_transfer(self.Kane, self.team_1)
        self.assertIsNone(c) 

    # --------------------------------------------------------------------------------------
    
    def test_find_team_by_name(self):
        # create name of team
        name = "Manchester City"
        # find team in set of teams
        p = self.league.find_team_by_name(name)
        # assert true if team is found
        self.assertTrue(p)

    # --------------------------------------------------------------------------------------

    def test_find_player_by_name(self):
        # create name of player
        name = "Adama Traore"
        # find player in set of player
        p = self.league.find_player_by_name(name)
        # assert true if player is found
        self.assertTrue(p)

    # --------------------------------------------------------------------------------------

    def test_find_team_by_rank(self):
        # create test rank
        rank = 6
        # get team ranked at rank 6
        t = self.league.find_team_by_rank(rank)
        # compare t to team at rank 6
        self.assertEqual(t.get_name(), "Wolves")

    # --------------------------------------------------------------------------------------

    def test_relegate(self):
        # add team to team set
        self.league.add_teams(self.team_Rel)
        # relegate team
        self.league.relegate()
        # check to see if team is in team set
        name = "Evertone"    
        r = self.league.find_team_by_name(name)

        self.assertFalse(r)


if __name__ == '__main__':
    unittest.main()       
        


