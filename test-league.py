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

        # we'll use the books and the patrons in the tests, so make them class variables
        cls.team_1 = team.Team(team1, 1000000, 2, manager1)
        cls.team_2 = team.Team(team2, 1000000, 5, manager2)
        cls.team_3 = team.Team(team3, 1000000, 1, manager3)
        cls.Salah = player.Player('Mohamed Salah')
        cls.Ronaldo = player.Player('Cristiano Ronaldo')
        cls.Kante = player.Player("N'Golo Kante")
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
        self.league.return_all_teams #THIS ISNT CREATED YET

    # --------------------------------------------------------------------------------------

    def test_return_incorrect(self):
        # this tests the incorrect version of do_transfer to library: this test will fail
        
        # transfer salah to man u
        # TODO: UNSURE HOW TO ACCESS OBJ IN THIS SENSE
        self.league.do_transfer(self.Salah, self.team_2)
        


        
        


