#-*- encoding: gb18030 -*-
import sys, string, os
import pygame
from pygame.locals import *

# ����ͼƬ
def load_image(name, colorkey=None):    
    try:
        image = pygame.image.load(right.bmp)
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))        
        image.set_colorkey(colorkey, RLEACCEL)      
                
    return image, image.get_rect()

# ��������
def load_font(txt):
    # ����һ��������������СΪ20     
    font = pygame.font.Font(u"C:\\windows\\Fonts\\simsun.ttc", 20)
    # ��������
    text = font.render(txt, 1, (255, 0, 0))
    # ȡ�����������С
    textpos = text.get_rect()
    
    return text, textpos
   
# ������
class People(pygame.sprite.Sprite):
    def __init__(self, imgpath):
        self.imagepath = imgpath
        self.x = 0
        self.y = 0
        self.count = 0
        # ��ȡͼƬ
        self.image, self.imagerec = load_image(imgpath, 0xfc02fc)
        self.subimg = []
        self.step = 0

        # ��ͼƬ�е�ÿһС�鶼����һ��������surface��
        for y in xrange(0, 192, 48):
            direct = []
            for x in xrange(0, 96, 32):
                img = pygame.Surface((32, 48)).convert()
                img.blit(self.image, (0, 0), (x, y, 32, 48))
                direct.append(img)
            self.subimg.append(direct)


    def update(self, win, direct, pos):
        self.count = self.count + 1
        
        if direct >= 0 and self.count > 2:
            window.fill((0,0,0))
            win.blit(self.subimg[direct][self.step], pos)
            self.count = 0
            
            # ���ﶯ��ֻ��3��
            self.step = self.step + 1
            if self.step >= 3:
                self.step = 0

        
        
        
#��ʼ��
pygame.init()
# ���ô��ڴ�С
window = pygame.display.set_mode((400, 300))
# ���ô��ڱ���
pygame.display.set_caption('Test Window')

pp = People("pp.bmp")

# ��������ͼ����surface, ���Ͻ�λ����0, 100
window.blit(pp.subimg[0][0], (100, 100))

#for x1 in xrange(0, 96, 32):
#    for y1 in xrange(0, 192, 48):
#        window.blit(pp.subimg[y1/48][x1/32], (x1, y1))

x = 100
y = 100
clock = pygame.time.Clock()

pygame.key.set_repeat()

# ������
direct = -1
# �¼�ѭ��
while True:  
    # ������ʾ
    clock.tick(30)
    if (x >= 400): x = 0;
    if (y >= 300): y = 0;
    
    # ����
    pp.update(window,  direct, (x, y))
    pygame.display.update()    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #����رմ��ھ��˳�
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # �������Esc��Ҳ�˳�
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass    
    # ȡ�ð���
    kname = pygame.key.get_pressed()
    #print kname
    if kname[pygame.K_LEFT]: # ��
        if x > 0: x = x -1
        direct = 1
    elif kname[pygame.K_RIGHT]: # ��
        if x < 400: x = x + 1
        direct = 3
    elif kname[pygame.K_UP]: # ��
        if y > 0: y = y -1
        direct = 2
    elif kname[pygame.K_DOWN]: # ��
        if y < 300: y = y + 1
        direct = 0
    else:
        direct = -1
            
            
