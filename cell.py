import pygame


class Cell:
    pygame.font.init()
    font = pygame.font.Font(None, 90)
    line_color = pygame.Color("light blue")
    original_text_color = pygame.Color("black")

    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.editable = False
        self.selected = False
        self.highlighted = False
        self.common = False
        self.wrong=False

    def set_cell_value(self, value):
        self.value = value
        self.set_sketched_value(value)

    def set_sketched_value(self, value):
        self.sketched_value = value

    def set_selected(self, selected):
        self.selected = selected

    def set_highlighted(self, highlighted):
        self.highlighted = highlighted

    def set_editable(self, editable):
        self.editable = editable
        if self.editable:
            self.original_text_color = pygame.Color("dark blue")
        else:
            self.original_text_color = pygame.Color("black")

    def set_common(self, common):
        self.common = common

    def set_wrong(self,wrong):
        self.wrong=wrong

    def draw(self, x, y, width, height):
        #Cell Color
        if self.wrong:
            fill_color=pygame.Color("lightcoral")
        elif self.selected:
            fill_color = pygame.Color("lightskyblue")
        elif self.common:
            fill_color = pygame.Color("lightskyblue")
        elif self.highlighted:
            fill_color = pygame.Color("lightsteelblue1")
        else:
            fill_color = pygame.Color("white")

        #Cell Borders
        pygame.draw.rect(self.screen, fill_color, pygame.Rect(x, y, width, height))
        pygame.draw.line(self.screen, self.line_color, (x, y),(x+width, y), 3)
        pygame.draw.line(self.screen, self.line_color, (x, y),(x, y+height), 3)
        pygame.draw.line(self.screen, self.line_color, (x+width, y),(x+width, y+height), 3)
        pygame.draw.line(self.screen, self.line_color, (x, y+height),(x+width, y+height), 3)

        #Cell Numbers
        if self.sketched_value != 0:
            if self.wrong:
                text_color=pygame.Color("red")
            elif self.selected and self.editable:
                text_color = pygame.Color("royal blue")
            else:
                text_color = self.original_text_color
            text_surface = self.font.render(str(self.sketched_value), True, text_color)
            self.screen.blit(text_surface, (x+width/3.5, y))