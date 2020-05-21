import pygame


import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")
    play_button = Button(ai_settings, screen, "Gra")

    ship = Ship(ai_settings, screen)


    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
           ship.update()
           gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
           gf.update_aliens(ai_settings, screen, stats,  sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)



run_game()
