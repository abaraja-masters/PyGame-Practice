import pygame

class Button:
    def __init__(self, x, y, width, height, text) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        font = pygame.font.Font(None, 28)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)