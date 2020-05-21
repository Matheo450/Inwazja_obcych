import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):

        ###inicjalizacja atrybutow przycisku ###
        self.screen = screen
        self.screen_rect = screen.get_rect()

        ### zdefiniowanie wymiarow i wlasciwosci przycisku###
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)


        ### stworzenie prostokata przycisku i wysrodkowanie go
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        ### komunikat wystwietlany przez przycisk trzedba przygowac tylko jednokrotnie###
        self.prep_msg(msg)


    def prep_msg(self, msg):
        ### umieszczenie komunikatu w wygenerowanym obrazie i wysrodkowanie tekstu na przycisku###
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)