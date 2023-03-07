from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random
import pygame
class ObstacleManager:
    POS_Y_LARGE_CACTUS=300
    def __init__(self) :
        self.obstacles=[]

    def update(self, game):
        if len(self.obstacles)==0:
               
            if random.randint(0,2)==1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0,2)==2:
               large=Cactus(LARGE_CACTUS)
               large.rect.y= self.POS_Y_LARGE_CACTUS
               self.obstacles.append(large)
            else: 
                self.obstacles.append(Bird(BIRD))           
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing=False
                break

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
######
#   Agregar el bird
#   Agregar LOS 2 CACTUS