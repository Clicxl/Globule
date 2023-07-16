import pygame,random,sys
from SETTINGS import *
from pygame.locals import *
from os import listdir

class Country(pygame.sprite.Sprite):
  def __init__(self,display):
    super().__init__()
    self.Display = display
    # Random Country Selector ---------------------------------------------#
    self.Countries = {}
    self.con_dict()
    self.randCont()
    # New Sruface ---------------------------------------------------------#
    
    # Sprites -------------------------------------------------------------#
    self.image = pygame.image.load(self.Img_path,).convert_alpha()
    self.image = pygame.transform.scale(self.image,self.Display.get_size())
    self.rect = self.image.get_rect()
    self.rect.center = [self.Display.get_width()/2,self.Display.get_height()/2]
    
  def con_dict(self):
    for image in listdir('Assets/Countries'):
      self.Countries[image.replace(".png","")] = {"Name":image.replace(".png","").lower(),"Dir":"Assets/Countries/"+image}
    self.Countries_copy = self.Countries.copy()

  def randCont(self):
    self.Con_Keys = list(self.Countries_copy.keys())
    try:
      self.Rand_Cont = random.choice(self.Con_Keys)
    except:
      print('Game Options over')
      pygame.quit()
      sys.exit()
    self.Img_path = self.Countries_copy[self.Rand_Cont]["Dir"]

  def check(self,Input):
    self.Input = Input.lower()
    if self.Input == self.Countries_copy[self.Rand_Cont]["Name"]:
      self.Countries_copy.pop(self.Rand_Cont)
      self.redraw_display()
    else:
      print("Wrong")
    return ""

  def redraw_display(self):
      self.randCont()
      self.Display.fill('White')
      self.image = pygame.image.load(self.Img_path,).convert_alpha()
      self.image = pygame.transform.scale(self.image,self.Display.get_size())

class Input(pygame.sprite.Sprite):
  def __init__(self,display,rect):
    super().__init__()
    # Country Display Surf And Rect ---------------------------------------#
    self.display_surf = display
    self.display_rect = rect
    self.Font = pygame.font.SysFont("Arial",32)
    # Sprite --------------------------------------------------------------#
    self.image = pygame.Surface((self.display_surf.get_width(),50))
    self.image.fill('Red')
    self.rect = self.image.get_rect()
    self.rect.topleft = [self.display_rect.left,self.display_rect.bottom+100]

    self.Input_text = ""

  def text_input(self,event):
    if event.type == pygame.KEYDOWN:
      if event.key not in [K_RETURN,K_TAB,K_DELETE]:
        if event.key == K_BACKSPACE:
          self.Input_text = self.Input_text[:-1]
        else:
          self.Input_text += event.unicode

  def update(self,event):
    self.image.fill('Red')
    self.text_input(event)
    self.Font_surf = self.Font.render(self.Input_text,False,(0,0,0))
    self.image.blit(self.Font_surf,(10,7))

class Timer(pygame.sprite.Sprite):
  def __init__(self,start_time):
    super().__init__()
    self.image = pygame.Surface((300,25))
    self.image.fill("Blue")
    self.rect = self.image.get_rect()
    self.rect.midleft = [450,650]
    
    self.current_time = 0
    self.start_time = start_time
    
  def update(self):
    self.current_time = pygame.time.get_ticks() - self.start_time
    self.ratio = max(0,TIME-(self.current_time/1000))
    self.image = pygame.transform.scale(self.image,(self.ratio*30,60))
    if self.ratio == 0:
      pygame.quit()
      sys.exit()
