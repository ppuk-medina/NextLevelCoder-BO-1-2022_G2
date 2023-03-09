import pygame
from dino_runner.utils.constants import SOUNDTRACK_GAMEPLAY

class SoundUtils:
    
    def sound_game_play(self):
        SOUNDTRACK_GAMEPLAY[0].play(-1)
        

    def sound_game_stop(self):
        SOUNDTRACK_GAMEPLAY[0].stop()
        

    def sound_dead(self):
        
        SOUNDTRACK_GAMEPLAY[1].play()
        
    def sound_shieldp(self):

        SOUNDTRACK_GAMEPLAY[3].play()        

    def sound_jump(self):
        SOUNDTRACK_GAMEPLAY[2].play()