# Andrew Vu
# CPSC 386-01
# avu916@csu.fullerton.edu
# MW 11:30-12:45pm


class GameStats:
    """Track statistics for Space Invaders."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
