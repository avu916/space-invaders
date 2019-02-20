# Andrew Vu
# CPSC 386-01
# avu916@csu.fullerton.edu
# MW 11:30-12:45pm

import pygame
import pygame.font
from spritesheet import Spritesheet
from settings import Settings


class StartScreen:

    def __init__(self, settings, screen, button):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.theSettings = Settings
        self.button = button

        ss = Spritesheet('images/space_invaders_spritesheet.png')

        # Load in alien images
        self.image = ss.image_at((65, 512, 64, 64))
        self.image2 = ss.image_at((65, 704, 64, 64))
        self.image3 = ss.image_at((65, 896, 64, 64))
        self.image4 = ss.image_at((65, 0, 64, 64))
        self.rect = self.image.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        screen.fill(settings.bg_color)

    def make_screen(self, settings, screen):
        pygame.init()
        start_screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Space Invaders")

        background = pygame.Surface(start_screen.get_size())
        background = background.convert(background)
        background.fill(settings.bg_color)

        # Display Space text
        font = pygame.font.Font(None, 144)
        text1 = font.render("Space", 2, (255, 255, 255))
        text_pos1 = text1.get_rect()
        text_pos1.centerx = background.get_rect().centerx
        font = pygame.font.Font(None, 144)

        # Display Invaders text
        text2 = font.render("Invaders", 2, (0, 255, 0))
        text_pos2 = ((settings.screen_width / 2) - 200, settings.screen_height / 6)

        # Alien position and text
        font = pygame.font.Font(None, 44)
        text3 = font.render(" = 20 pts", 2, (250, 250, 250))
        text4 = font.render(" = 40 pts", 2, (250, 250, 250))
        text5 = font.render(" = 10 pts", 2, (250, 250, 250))
        text6 = font.render(" = 100 pts", 2, (250, 250, 250))
        text7 = font.render("Play Game", 2, (250, 250, 250))
        text8 = font.render("High Score", 2, (250, 250, 250))

        # top alien
        text_pos5 = ((settings.screen_width / 2) - 30, (settings.screen_height / 2) - 40)
        alien_pos1 = ((settings.screen_width / 2) - 100, (settings.screen_height / 2) - 60)

        # middle alien
        text_pos3 = ((settings.screen_width / 2) - 30, (settings.screen_height / 2) + 20)
        alien_pos3 = ((settings.screen_width / 2) - 100, settings.screen_height / 2)

        # bottom alien
        text_pos4 = ((settings.screen_width / 2) - 30, (settings.screen_height / 2) + 80)
        alien_pos2 = ((settings.screen_width / 2) - 100, (settings.screen_height / 2) + 60)

        # Mothership
        text_pos6 = ((settings.screen_width / 2) - 20, (settings.screen_height / 2) + 140)
        alien_pos4 = ((settings.screen_width / 2) - 100, (settings.screen_height / 2) + 120)

        # Play Game
        text_pos7 = ((settings.screen_width / 2) - 70, (settings.screen_height/2) + 250)

        # High Score
        text_pos8 = ((settings.screen_width / 2) - 70, (settings.screen_height / 2) + 300)

        # Draw onto screen
        background.blit(text1, text_pos1)
        background.blit(text2, text_pos2)
        background.blit(self.image, alien_pos1)
        background.blit(text3, text_pos3)
        background.blit(self.image2, alien_pos2)
        background.blit(text4, text_pos4)
        background.blit(self.image3, alien_pos3)
        background.blit(text5, text_pos5)
        background.blit(self.image4, alien_pos4)
        background.blit(text6, text_pos6)
        background.blit(text7, text_pos7)
        background.blit(text8, text_pos8)

        # Blit everything to screen
        screen.blit(self.image, (settings.screen_width / 2, settings.screen_height / 3))
        screen.blit(background, (200, 200))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return

            screen.blit(background, (0, 0))
            pygame.display.flip()
