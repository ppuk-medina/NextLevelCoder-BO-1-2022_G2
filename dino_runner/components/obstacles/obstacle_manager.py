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
            var=random.randint(0,2)   
            if var==0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif var==1:
               large=Cactus(LARGE_CACTUS)
               large.rect.y= self.POS_Y_LARGE_CACTUS
               self.obstacles.append(large)
            else: 
                pos_y_bird=random.randint(200,280)
                self.obstacles.append(Bird(BIRD,pos_y_bird))
                print("bird",var,pos_y_bird)           
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing=False
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles=[]
######
#   Agregar el bird
#   Agregar LOS 2 CACTUS