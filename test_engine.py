import unittest
from unittest.mock import patch
from engine import RockPaperScissors

class TestRockPaperScissorsAI(unittest.TestCase):

    def setUp(self):
        """Sets up a fresh instance before every single test."""
        self.game = RockPaperScissors(rounds=3)

    @patch('builtins.input', side_effect=['difficult'])
    def test_select_difficulty_valid(self, mock_input):
        """Verifies that difficulty is correctly updated on valid user input."""
        self.game.select_difficulty()
        self.assertEqual(self.game.difficulty, 'difficult')

    def test_ai_fallback_on_first_round(self):
        """Verifies AI defaults to random choice on round 1, even in difficult mode."""
        self.game.difficulty = 'difficult'
        self.game.rounds_played = 0
        
        # Should return a valid move choice without crashing
        choice = self.game.get_choice()
        self.assertIn(choice, self.game.choices)

    def test_ai_counters_highest_frequency(self):
        """Verifies AI predicts user habits and plays the absolute winning counter."""
        self.game.difficulty = 'difficult'
        self.game.rounds_played = 2
        
        # Simulate history: User has heavily spammed 'rock'
        self.game.history = {'rock': 5, 'paper': 1, 'scissors': 0}
        
        # AI should predict 'rock' and strictly choose 'paper' to counter it
        ai_choice = self.game.get_choice()
        self.assertEqual(ai_choice, 'paper')

    # Placed patches in correct stack alignment to match arguments
    @patch('random.choice', return_value='scissors')
    @patch('builtins.input', side_effect=['easy', 'rock', 'quit'])
    def test_history_dictionary_increments(self, mock_input, mock_random):
        """Verifies that user selections successfully update the history dict counters."""
        self.game.play_game()
        
        # The user history must explicitly register the 'rock' selection
        self.assertEqual(self.game.history['rock'], 1)
        self.assertEqual(self.game.history['paper'], 0)
        self.assertEqual(self.game.history['scissors'], 0)

if __name__ == '__main__':
    unittest.main()
