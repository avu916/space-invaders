# Andrew Vu
# CPSC 386-01
# avu916@csu.fullerton.edu
# MW 11:30-12:45pm

from pygame.sprite import Sprite
from spritesheet import Spritesheet


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        ss = Spritesheet('images/space_invaders_spritesheet.png')
        #
        # # Load the ship image, and get its rect.
        # self.image = ss.image_at((0, 192, 64, 64))

        # Load the alien image, and set its rect attribute.
        self.images = []
        self.images.append(ss.image_at((65, 512, 64, 64)))
        self.images.append(ss.image_at((0, 576, 64, 64)))
        # self.images.append(load_image('images/alien1_down.bmp'))
        self.index = 0
        self.image = self.images[self.index]
        # self.image2 = pygame.image.load('images/alien2_up.bmp')
        # self.rect = self.image2.get_rect()
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)

        # timer = pygame.time.get_ticks() / 1000

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
        # self.screen.blit(self.image2, self.rect)
