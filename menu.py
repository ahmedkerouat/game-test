import pygame as py


class Interface():

    def __init__(self, font):
        self.font = font
        self.mx = 0
        self.my = 0
        self.clicked1 = False
        self.clicked2 = False
        self.color1 = (20, 0, 46)
        self.color2 = (20, 0, 46)
        logo_unscaled = py.image.load("ressources\sprites\\gamelogo.png")
        self.logo = py.transform.scale(logo_unscaled, (int(
            logo_unscaled.get_width() * 3), int(logo_unscaled.get_height() * 3)))

    def display(self, surface):
        self.mx, self.my = py.mouse.get_pos()
        py.mouse.set_visible(True)
        surface.fill((11, 0, 19))
        surface.blit(self.logo, (200, 0))
        button = Button(367, 300, "play", self.font,
                        self.color1,  self.mx, self.my)
        button.display(surface)
        if button.button1_rect.collidepoint(self.mx, self.my):
            self.color1 = (200, 100, 0)
            if py.mouse.get_pressed()[0]:
                self.clicked1 = True
        else:
            self.color1 = (20, 0, 46)

        button2 = Button(367, 400, "quit", self.font,
                         self.color2,  self.mx, self.my)
        button2.display(surface)
        if button2.button1_rect.collidepoint(self.mx, self.my):
            self.color2 = (200, 100, 0)
            if py.mouse.get_pressed()[0]:
                self.clicked2 = True
        else:
            self.color2 = (20, 0, 46)


class Button():

    def __init__(self, x, y, text, font, color, mx, my):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.color = color
        self.mx = mx
        self.my = my

    def display(self, surface):
        self.button1 = self.font.render(self.text, 1, self.color)
        self.button1_rect = self.button1.get_rect()
        self.button1_rect.center = (self.x + 30, self.y + 12)
        surface.blit(self.button1, (self.x, self.y))
