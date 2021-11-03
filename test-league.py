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
        manager1 = "Jurgen Klopp"
        manager2 = "Ole Gunnar Solskjaer"
        manager3 = "Thomas Tuchel"

        #team_1 = team.Team(team1, 100000000, 2, manager1)
        #team_2 = team.Team(team2, 100000000, 5, manager2)
        #team_3 = team.Team(team3, 100000000, 1, manager3)

        # we'll use the books and the patrons in the tests, so make them class variables
        cls.team_1 = team.Team(team1, 100000000, 2, manager1)
        cls.team_2 = team.Team(team2, 100000000, 5, manager2)
        cls.team_3 = team.Team(team3, 100000000, 1, manager3)
        cls.Salah = player.Player('Mohamed Salah', 29, 100000000, cls.team_1)
        cls.Ronaldo = player.Player('Cristiano Ronaldo', 36, 100000000, cls.team_2)
        cls.Kante = player.Player("N'Golo Kante", 30, 100000000, cls.team_3)
        cls.league.add_player(cls.Salah)
        cls.league.add_player(cls.Ronaldo)
        cls.league.add_player(cls.Kante)
        cls.league.add_teams(cls.team_1)
        cls.league.add_teams(cls.team_2)
        cls.league.add_teams(cls.team_3)

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
        #self.league.return_all_teams() #THIS ISNT CREATED YET

    # --------------------------------------------------------------------------------------

    # def test_return_incorrect(self):
    #     # this tests the incorrect version of do_transfer to library: this test will fail
        
    #     # transfer salah to man u
    #     # TODO: UNSURE HOW TO ACCESS OBJ IN THIS SENSE
    #     self.league.do_transfer(self.Salah, self.team_2)
        


    # --------------------------------------------------------------------------------------

    #TODO: FINISH
    # def test_transfer_correct(self):
    #     print("test transfer correct")
    #     # this test the correct implementation of transferring a player: it will succeed
        
    #     # transfer salah to man u
    #     self.league.do_transfer(self.Salah, self.team_2)
    #     # show transfer
    #     rc = self.league.show_transfers()
    #     self.assertTrue(rc)

    # --------------------------------------------------------------------------------------
    # DONE
    def test_transfer_one(self):
        # transfer salah from liverpool to man u
        c = self.league.do_transfer(self.Salah, self.team_2)
        self.assertIsNone(c)

        # transfer kante from chelsea to liverpool
        c = self.league.do_transfer(self.Kante, self.team_1)
        self.assertIsNone(c)

        # try to transfer kante to man u
        # this should fail (man u has no money to buy kante)
        c = self.league.do_transfer(self.Kante, self.team_2)
        self.assertIsNone(c) 

    # --------------------------------------------------------------------------------------

        
if __name__ == '__main__':
    unittest.main()


