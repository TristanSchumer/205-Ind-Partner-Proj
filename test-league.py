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

        manager1 = "Jurgen Klopp"
        manager2 = "Ole Gunnar Solskjaer"
        manager3 = "Thomas Tuchel"
        manager4 = "Antonio Conte"
        manager5 = "Bruno Lage"
        manager6 = "Pep Guardiola"
        manager7 = "Brendon Rodgers"

        # we'll use the books and the patrons in the tests, so make them class variables
        cls.team_1 = team.Team(team1, 100000000, 2, manager1)
        cls.team_2 = team.Team(team2, 100000000, 5, manager2)
        cls.team_3 = team.Team(team3, 100000000, 1, manager3)
        cls.team_4 = team.Team(team4, 100000000, 4, manager4)
        cls.team_5 = team.Team(team5, 100000000, 6, manager5)
        cls.team_6 = team.Team(team6, 100000000, 3, manager6)
        cls.team_7 = team.Team(team7, 100000000, 3, manager7)


        cls.Salah = player.Player('Mohamed Salah', 29, 100000000, cls.team_1)
        cls.Ronaldo = player.Player('Cristiano Ronaldo', 36, 100000000, cls.team_2)
        cls.Kante = player.Player("N'Golo Kante", 30, 100000000, cls.team_3)
        cls.Kane = player.Player("Harry Kane", 28, 100000000, cls.team_4)
        cls.Traore = player.Player("Adama Traore", 25, 100000000, cls.team_5)
        cls.Grealish = player.Player("Jack Grealish", 24, 100000000, cls.team_6)
        cls.Vardy = player.Player("Jamie Vardy", 34, 100000000, cls.team_7)

        cls.league.add_player(cls.Salah)
        cls.league.add_player(cls.Ronaldo)
        cls.league.add_player(cls.Kante)
        cls.league.add_player(cls.Kane)
        cls.league.add_player(cls.Traore)
        cls.league.add_player(cls.Grealish)
        cls.league.add_player(cls.Vardy)

        cls.league.add_teams(cls.team_1)
        cls.league.add_teams(cls.team_2)
        cls.league.add_teams(cls.team_3)
        cls.league.add_teams(cls.team_4)
        cls.league.add_teams(cls.team_5)
        cls.league.add_teams(cls.team_6)
        cls.league.add_teams(cls.team_7)

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
        # self.league.return_all_teams() #THIS ISNT CREATED YET

    # --------------------------------------------------------------------------------------

    # def test_return_incorrect(self):
    #     # this tests the incorrect version of do_transfer to library: this test will fail
        
    #     # transfer salah to man u
    #     # TODO: UNSURE HOW TO ACCESS OBJ IN THIS SENSE
    #     self.league.do_transfer(self.Salah, self.team_2)
        


    # --------------------------------------------------------------------------------------

   # TODO: FINISH
    # def test_transfer_correct(self):
    #     print("test transfer correct")
    #     # this test the correct implementation of transferring a player: it will succeed
        
    #     # transfer salah to man u
    #     self.league.do_transfer(self.Salah, self.team_2)
    #     # show transfer
    #     rc = self.league.show_transfers()
    #     self.assertTrue(rc)

    # --------------------------------------------------------------------------------------

    def test_transfer_players(self):
        # transfer kante from chelsea to liverpool
        c = self.league.do_transfer(self.Kante, self.team_1)
        self.assertIsNone(c)

        # try to transfer kane to liverpool
        # this should fail (liverpool has no money to buy kane)
        c = self.league.do_transfer(self.Kane, self.team_1)
        self.assertIsNone(c) 

    # --------------------------------------------------------------------------------------

    def test_transfer_budget(self):
        # transfers player to team 2
        self.league.do_transfer(self.Salah, self.team_2)
        # records new teams budget after transfer
        new_team_budget = self.team_2.get_transfer_budget()
        # compares new_team_budget to what it should be
        self.assertEqual(new_team_budget, 0)

    # --------------------------------------------------------------------------------------
    
    def test_team_players(self):
        # create new player and add to team
        Tristan = player.Player("Tristan Schumer", 20, 100000000, self.team_6)
        self.team_6.players.add(Tristan)

        # get name of player on team
        p = list(self.team_6.players)[0].get_name()

        # compare name of player to name
        self.assertEqual(p, "Tristan Schumer")

    # --------------------------------------------------------------------------------------

    def test_find_player_by_name(self):
        # create name of player
        name = "Adama Traore"
        
        # find player in set of player
        p = self.league.find_player_by_name(name)

        # assert true if player is found
        self.assertTrue(p)

    # def test_find_team_by_rank(self):
    #     rank = 6

        



if __name__ == '__main__':
    unittest.main()       
        


