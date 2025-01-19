import pygame
import random

class Meteor:
    def __init__(self, screen_width):
        meteor_image = pygame.image.load("meteor.png")
        self.image = pygame.transform.scale(meteor_image, (115, 145))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(random.randint(0, screen_width - 115), 0, 115, 145)

    def move(self):
        self.rect.y += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)