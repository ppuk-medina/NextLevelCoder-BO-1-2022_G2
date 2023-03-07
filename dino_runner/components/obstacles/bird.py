
from dino_runner.components.obstacles.obstacle import Obstacle 
import random
class Bird(Obstacle):
    POS_Y_BIRD=280
    def __init__(self,image_list):
        self.type= random.randint(0,2)
        super().__init__(image_list,self.type)
        self.rect.y=self.POS_Y_BIRD
        self.step_index=0
    

    def update(self, game_speed, obstacle):
        self.fly()
        if self.step_index>=10:
            self.step_index=0
        return super().update(game_speed, obstacle)
        

    def fly(self):
        self.image =self.image_list[0] if self.step_index < 5 else self.image_list[1]
        self.rect=self.image.get_rect()
        self.step_index+=1