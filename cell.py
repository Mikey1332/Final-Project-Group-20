import pygame


class Cell:
    pygame.font.init()
    font = pygame.font.Font(None, 90)

    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def set_selected(self, selected):
        self.selected = selected

    def draw(self, x, y, width, height):
        if self.selected:
            fill_color = pygame.Color("gray")
        else:
            fill_color = pygame.Color("white")
        pygame.draw.rect(self.screen, fill_color, pygame.Rect(x, y, width, height))
        pygame.draw.line(self.screen, pygame.Color("purple"), (x, y),(x+width, y), 3)
        pygame.draw.line(self.screen, pygame.Color("purple"), (x, y),(x, y+height), 3)
        pygame.draw.line(self.screen, pygame.Color("purple"), (x+width, y),(x+width, y+height), 3)
        pygame.draw.line(self.screen, pygame.Color("purple"), (x, y+height),(x+width, y+height), 3)

        if self.sketched_value != 0:
            if self.selected and self.sketched_value!=self.value:
                text_color = pygame.Color("orange")
            else:
                text_color = pygame.Color("black")
            text_surface = self.font.render(str(self.sketched_value), True, text_color)
            self.screen.blit(text_surface, (x+width/3.5, y))