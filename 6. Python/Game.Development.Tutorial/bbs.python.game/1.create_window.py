#-*- encoding: gb18030 -*-
import sys, string, os
import pygame

#��ʼ��
pygame.init()
# ���ô��ڴ�С
window = pygame.display.set_mode((800, 600))
# ���ô��ڱ���
pygame.display.set_caption('Test Window')

# �¼�ѭ��
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #����رմ��ھ��˳�
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # �������Esc��Ҳ�˳�
            sys.exit()
