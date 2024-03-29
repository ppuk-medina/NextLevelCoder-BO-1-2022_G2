import pygame
from dino_runner.components.sound_manager import SoundUtils
from dino_runner.components.text_utils import TextUtils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,COLORS, RUNNING, MESSAGE_GAMEOVER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.powerup_manager import PowerUpManager
class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player=Dinosaur()
        self.obstacle_manager=ObstacleManager()
        self.points=0
        self.text_utils=TextUtils()
        self.game_running=True
        self.powerup_manager=PowerUpManager()
        self.sound_game=SoundUtils()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacle()        
        self.points=0
        self.powerup_manager.reset_power_ups(self.points)
        self.sound_game.sound_game_play()
        while self.playing:
            self.events()
            self.update()
            self.draw()
       

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input=pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points,self.game_speed,self.player,self.screen)
        

    def draw(self):
        
        self.clock.tick(FPS)
        self.screen.fill(COLORS["white"])
        self.draw_background()
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.score()
        self.player.check_invincibility(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points+=1
        text, text_rect= self.text_utils.get_score(self.points)
        
        self.screen.blit(text, text_rect)

    def show_menu(self, death_count=0):
        self.game_running=True
        self.screen.fill(COLORS['white'])
        self.prin_menu_elements(death_count) 
        pygame.display.update()
        self.handle_key_events()
    
    def prin_menu_elements(self, death_count=0):
        text, text_rect= self.text_utils.get_centered_message("Press and key to Start")
        self.screen.blit(text,text_rect)
        if death_count>0:
            score, score_rect= self.text_utils.get_centered_message("Your Score:"+str(self.points),height=SCREEN_HEIGHT//2+50)   
            self.screen.blit(score,score_rect) 
        self.screen.blit(RUNNING[0],(SCREEN_WIDTH//2-20,SCREEN_HEIGHT//2-140))

    def handle_key_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running=False
                self.playing=False
                pygame.display.quit()
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                self.run()
    
    def get_game_over_img(self,width=SCREEN_WIDTH//2):
        self.image=MESSAGE_GAMEOVER
        self.rect=self.image.get_rect()
        self.rect.center=(width,180)
        self.screen.blit(self.image,self.rect)