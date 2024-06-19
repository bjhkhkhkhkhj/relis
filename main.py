from pygame import*
from random import*
import sys
import os

def resource_path(relative):
    if hasattr(sys,"_MEIPASS"):
        return os.path.join(sys._MEIPASS,relative)
    return os.path.join(relative)
font.init()
font.SysFont("arial",30)
lost=0
score=0
win_width =700
win_height = 500
coordinates = [90, 170, 250, 320]
clock=time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption("Чарівна корзина")

background = transform.scale(image.load(resource_path("backfon.jpg")), (win_width, win_height))#Дописати

class GamSprite(sprite.Sprite):
    def __init__ (self,player_image, player_x, player_y,size_x,size_y,player)#Дописати
        sprite.Sprite.__init__(self)
        self.image =
    