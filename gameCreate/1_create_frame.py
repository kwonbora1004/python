import pygame

pygame.init() #초기화(반드시 필요)

#화면크기설정
screen_width =480 # 가로
screen_heigth=640 #세로
pygame.display.set_mode((screen_width,screen_heigth))

#화면타이틀
pygame.display.set_caption("Bora Game")# 게임이름

#이벤트루프
running = True #게임진행중?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생?
        if event.type==pygame.QUIT: #창이 닫히는 이벤트
            running = False # 게임이 진행중이아님

#pygame 종료
pygame.quit()