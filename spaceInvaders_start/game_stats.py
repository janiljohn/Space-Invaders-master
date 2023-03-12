class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.game_active = False
        self.ai_settings = ai_settings.settings
        self.reset_stats()
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        