from dino_runner.utils.constants import SCREEN_WIDTH
from pygame.sprite import Sprite 

class Obstacle(Sprite):
    def __init__(self, image_lista,type):
        self.image_list=image_lista
        self.type= type
        self.image= image_lista[type]
        self.rect= self.image.get_rect()
        self.rect.x=SCREEN_WIDTH

    def update(self, game_speed,obstacle):
        self.rect.x-= game_speed
        if self.rect.x<=0:
            obstacle.pop()

    def draw(self, screen):
        screen.blit(self.image,self.rect)