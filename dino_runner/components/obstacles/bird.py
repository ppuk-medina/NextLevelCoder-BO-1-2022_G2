
from dino_runner.components.obstacles.obstacle import Obstacle 
import random
class Bird(Obstacle):
    
    def __init__(self,image_list,pos_y_bird):
        super().__init__(image_list,0)
        self.rect.y=pos_y_bird
        self.step_index=0
     
    def update(self, game_speed, obstacles):
        self.fly()
        if self.step_index >= 10:
            self.step_index = 0
        return super().update(game_speed, obstacles)
    
    def fly(self):
        if self.step_index < 5:
            self.image = self.image_list[0]
        else:
            self.image = self.image_list[1]
        
        self.step_index += 1