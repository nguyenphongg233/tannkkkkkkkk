import pygame
import time
import random
import math 

pygame.init()
pygame.mixer.init()

screensize = []
screensize = pygame.display.get_desktop_sizes()
pygame.display.set_caption("honganhcute")
tanker = []
tanker.append(pygame.image.load("tanker.png"))
tanker.append(pygame.image.load("tanker2.png"))
wx = []
wx.append(pygame.image.load("awin.png"))
wx.append(pygame.image.load("Bwin.png"))

gunsound = pygame.mixer.Sound("fd.mp3")
xc = []
xc.append(pygame.mixer.Sound("loser.mp3"))
xc.append(pygame.mixer.Sound("loser.mp3"))

background = pygame.image.load("Root.png")

font = pygame.font.Font('freesansbold.ttf', 32)

n = 700
m = 900
x = [100,500]
y = [200,600]
typee = [0,0]
c = 10 
score1 = 0
score2 = 0
s = ""
dx = [0,-1,0,1]
dy = [-1,0,1,0]
xx = []
xxx = []

inside = [74,107,462,792]

screen = pygame.display.set_mode([n,m])

running = True

def cross (x,y,u,v,rx,ry,ru,rv) : 
    xr = max(x,rx)
    ur = min(u,ru)
    vr = min(v,rv)
    yr = max(y,ry)

    if xr <= ur and yr <= vr : 
        return True
    else : 
        return False


def update () :

    screen.blit(background,(0,0))

    for i in range (0,2) : 
        x[i] = (x[i] + dx[typee[i]] * c + inside[2] - inside[0] * 2 + 1) % (inside[2] - inside[0] + 1) + inside[0]
        y[i] = (y[i] + dy[typee[i]] * c + inside[3] - inside[1] * 2 + 1) % (inside[3] - inside[1] + 1) + inside[1]
        screen.blit(pygame.transform.rotate(tanker[i],90 * typee[i]),(x[i] - 15,y[i] - 15))
        print(x[i],y[i],i)
    
    ok = 1 

    for i in range (0,len(xx)) : 

        rx = xx[i]

        xx[i][0] += c * 2 * dx[xx[i][2]]
        xx[i][1] += c * 2 * dy[xx[i][2]]

        if xx[i][0] > inside[2] or xx[i][0] < inside[0] or xx[i][1] > inside[3] or xx[i][1] < inside[1] : 
            continue 
        else : 
            xt = xx[i][0] 
            yt = xx[i][1] 
            ut = xx[i][0] + c * dx[xx[i][2]]
            vt = xx[i][1] + c * dy[xx[i][2]]

            if ut > inside[2] or ut < inside[0] or vt > inside[3] or vt < inside[1] :
                continue
            if xt > ut : 
                xt,ut = ut,xt
            
            if yt > vt : 
                yt,vt = vt,yt

            costx = 1
            costy = 1

            if dx[xx[i][2]] != 0 : 
                costx = 2
            else :
                costy = 2

            pygame.draw.rect(screen,xx[i][3],[xt - 5,yt - 5,costx * 9,costy * 9])
            print(xt,yt,ut,vt,xx[i][3])

            vc = 0

            if xx[i][3] == 'Black' :
                vc = 1

            
            if cross(xt,yt,xt + costx * 9 - 1,yt + costy * 9 - 1,x[vc]-15,y[vc]-15,x[vc] + 14,y[vc] + 14) : 
                screen.blit(wx[vc],(0,0))
                xc[vc].play()
                pygame.display.update()
                time.sleep(5)

                x[0] = 100
                x[1] = 500
                y[0] = 200
                y[1] = 600
                typee[0] = 0
                typee[1] = 0

                xx.clear()
                xxx.clear()
                
                return vc

            
            xxx.append(xx[i])

    
    xx.clear()

    for i in range (0,len(xxx)) :        
        xx.append(xxx[i])
    
    xxx.clear()

    pygame.draw.rect(screen,'Black',(67,100,470 - 67 + 1,106 - 100 + 1))
    pygame.draw.rect(screen,'Black',(463,100,470 - 463 + 1,799 - 100 + 1))
    pygame.draw.rect(screen,'Black',(67,793,470 - 67 + 1,799 - 793 + 1))
    pygame.draw.rect(screen,'Black',(67,100,73 - 67 + 1,799 - 100 + 1))

    text = font.render(s, True, "white", "Black")
    screen.blit(text, (574,244))
    pygame.display.update()
    time.sleep(0.1)

    return 2

while running: 

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT :
            running = 0
        # if event.type == pygame.K_ESCAPE : 
        #     running = False
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_ESCAPE :
                running = 0
            if event.key == pygame.K_LEFT: 
                typee[0] = 1
            elif event.key == pygame.K_RIGHT : 
                typee[0] = 3
            elif event.key == pygame.K_UP :
                typee[0] = 0
            elif event.key == pygame.K_DOWN :
                typee[0] = 2
            elif event.key == pygame.K_p :
                xx.append([x[0],y[0],typee[0],'Black'])
                gunsound.play()
            elif event.key == pygame.K_w : 
                typee[1] = 0
            elif event.key == pygame.K_a : 
                typee[1] = 1
            elif event.key == pygame.K_s : 
                typee[1] = 2
            elif event.key == pygame.K_d : 
                typee[1] = 3
            elif event.key == pygame.K_t : 
                xx.append([x[1],y[1],typee[1],'Red'])
                gunsound.play()
    
    s = str(score1) + "-" + str(score2)
    xtt = update()

    if xtt == 0 : 
        score1 += 1
    elif xtt == 1 :
        score2 += 1

    print(xtt,s,score1,score2)
    

pygame.quit()
