import random 
import math
import pygame

pygame.init()

#СРАЗУ ГОВОРЮ КНОПКА "CONTINUE" В ИГРЕ ЕЩЕ НЕ РАБОТАЕТ - Я ЕЩЕ КОД НЕ НАПИСАЛ :)
#все остальное вроде как работает

#параметры окна
size = [800,600]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("My 2048")

#основные цвета
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (169,169,169)

gameOver = False
fps = 60

def menu_1():
    #собственно менью игры

    darkMode = False

    #возможные доски и индекс
    cellSizes = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    ind = 1    
    #выбранная копка (когда поносиш мышку текст белым становиться)
    selected = 0

    
    #какие то булеаны
    inGame = True
    isPerehodP = False
    isPerehodA = False
    isPerehod = False
    onMenuP = False
    onMenuA = False
    onMenu = True
    justBool = True

    perehod = 0
    clock = pygame.time.Clock()
    while inGame == True:  
        clock.tick(fps)
        if justBool == True:
               
            hw = cellSizes[ind]       
        #заливка экрана
            if darkMode == False:
                screen.fill(white)
                colorD = black
            else:
                screen.fill(black)
                colorD = white
        #получние координат мыши
            x,y = pygame.mouse.get_pos()
        #переменная движения для анимации перехода
            if isPerehodP == True:
                perehod += 50
                if isPerehod:
                    if perehod >=0:
                        isPerehodP = False
                        isPerehod= False
                        onMenu = True
                        onMenuA = False
                else:
                    if perehod >=800:
                        isPerehodP = False
            elif isPerehodA == True:
                perehod -= 50
                if isPerehod:
                    if perehod <= 0:
                        isPerehodA = False
                        isPerehod = False
                        onMenu = True
                        onMenuP = False
                else:
                    if perehod <= -800:
                        isPerehodA = False
                    
        #кнопки play,about,quit           
            #draw_button(rx,ry,rh,rw,clx,cly,crx,cry,rad,text,tx,ty,colort,colorb,font)           
            
            #выделение надписи
            if 200<x<600:
                if 175<y<275:
                    selected = 1 
                elif 325<y<425:
                    selected = 2
                elif 475<y<575:                 
                    selected = 3
                else:
                    selected = 0
            else:
                selected = 0
            #нарисовать кнопки (6.9px*4px per 10 unit)
            font = pygame.font.SysFont(None,70)
            if selected == 1:                
                draw_button(250-perehod,175,300,100,250-perehod,225,550-perehod,225,50,"Play",355-perehod,200,white,red,font)
                draw_button(250-perehod,325,300,100,250-perehod,375,550-perehod,375,50,"About",335-perehod,350,black,red,font)
                draw_button(250-perehod,475,300,100,250-perehod,525,550-perehod,525,50,"Quit",355-perehod,500,black,red,font)
                if onMenuP:
                    draw_button(250-perehod+800,175,300,100,250-perehod+800,225,550-perehod+800,225,50,"Continue",300-perehod+800,200,white,red,font)
                    draw_button(250-perehod+800,325,300,100,250-perehod+800,375,550-perehod+800,375,50,"New",360-perehod+800,350,black,red,font)
                    draw_button(250-perehod+800,475,300,100,250-perehod+800,525,550-perehod+800,525,50,"Back",350-perehod+800,500,black,red,font)
            elif selected == 2:                
                draw_button(250-perehod,175,300,100,250-perehod,225,550-perehod,225,50,"Play",355-perehod,200,black,red,font)
                draw_button(250-perehod,325,300,100,250-perehod,375,550-perehod,375,50,"About",335-perehod,350,white,red,font)
                draw_button(250-perehod,475,300,100,250-perehod,525,550-perehod,525,50,"Quit",355-perehod,500,black,red,font)
                if onMenuP:
                    draw_button(250-perehod+800,175,300,100,250-perehod+800,225,550-perehod+800,225,50,"Continue",300-perehod+800,200,black,red,font)
                    draw_button(250-perehod+800,325,300,100,250-perehod+800,375,550-perehod+800,375,50,"New",360-perehod+800,350,white,red,font)
                    draw_button(250-perehod+800,475,300,100,250-perehod+800,525,550-perehod+800,525,50,"Back",350-perehod+800,500,black,red,font)
            elif selected == 3:
                draw_button(250-perehod,175,300,100,250-perehod,225,550-perehod,225,50,"Play",355-perehod,200,black,red,font)
                draw_button(250-perehod,325,300,100,250-perehod,375,550-perehod,375,50,"About",335-perehod,350,black,red,font)
                draw_button(250-perehod,475,300,100,250-perehod,525,550-perehod,525,50,"Quit",355-perehod,500,white,red,font)
                if onMenuP:
                    draw_button(250-perehod+800,175,300,100,250-perehod+800,225,550-perehod+800,225,50,"Continue",300-perehod+800,200,black,red,font)
                    draw_button(250-perehod+800,325,300,100,250-perehod+800,375,550-perehod+800,375,50,"New",360-perehod+800,350,black,red,font)
                    draw_button(250-perehod+800,475,300,100,250-perehod+800,525,550-perehod+800,525,50,"Back",350-perehod+800,500,white,red,font)
            else:
                draw_button(250-perehod,175,300,100,250-perehod,225,550-perehod,225,50,"Play",355-perehod,200,black,red,font)
                draw_button(250-perehod,325,300,100,250-perehod,375,550-perehod,375,50,"About",335-perehod,350,black,red,font)
                draw_button(250-perehod,475,300,100,250-perehod,525,550-perehod,525,50,"Quit",355-perehod,500,black,red,font)
                if onMenuP:
                    draw_button(250-perehod+800,175,300,100,250-perehod+800,225,550-perehod+800,225,50,"Continue",300-perehod+800,200,black,red,font)
                    draw_button(250-perehod+800,325,300,100,250-perehod+800,375,550-perehod+800,375,50,"New",360-perehod+800,350,black,red,font)
                    draw_button(250-perehod+800,475,300,100,250-perehod+800,525,550-perehod+800,525,50,"Back",350-perehod+800,500,black,red,font)
            #строка выбора доски        
            img = font.render(str(hw)+' x '+str(hw),True,colorD)       
            if hw<10:
                screen.blit(img,(355-perehod,50))
                screen.blit(img,(355+800-perehod,50))
            else:
                screen.blit(img,(325-perehod,50))
                screen.blit(img,(325+800-perehod,50))
            
            if onMenuA == True:
                img = font.render('Игру сделал Атан!',True,colorD)
                imgg = font.render('Это кнопка назад',True,colorD)
                screen.blit(img,(250-850-perehod,250))
                screen.blit(imgg,(250-850-perehod,350))
            #стрелки выбора доски      
                #правые   
            pygame.draw.lines(screen,colorD,False,[[550-perehod+50,50],[575-perehod+50,75],[550-perehod+50,100]],3)
            pygame.draw.lines(screen,colorD,False,[[550-perehod+70,50],[575-perehod+70,75],[550-perehod+70,100]],3)
                #левые
            pygame.draw.lines(screen,colorD,False,[[250-perehod-50,50],[225-perehod-50,75],[250-perehod-50,100]],3)
            pygame.draw.lines(screen,colorD,False,[[250-perehod-70,50],[225-perehod-70,75],[250-perehod-70,100]],3)
            
            #кнопка даркмода
            #darkModeButton = (75,525)        
            #pygame.draw.circle(screen,colorD,darkModeButton,25)    
            tile_draw(75,525,25,25,5,colorD)      
            #все нажатия обрабатываються тут
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    inGame=False
                    pygame.quit()
                elif i.type == pygame.KEYUP:
                    if onMenu:
                        if i.key == pygame.K_RIGHT:
                            if ind<13:
                                ind+=1
                            else:
                                ind = 0 
                        elif i.key == pygame.K_LEFT:
                            if ind>0:
                                ind-=1
                            else:
                                ind = 13
                elif i.type == pygame.MOUSEBUTTONUP:
                    if 200<x<600:
                        if onMenu:
                            if 175<y<275:
                                isPerehodP = True
                                onMenuP = True       
                                onMenu = False                 
                            elif 325<y<425:
                                isPerehodA = True
                                onMenuA = True
                                onMenu = False
                            elif 475<y<575:                 
                                inGame = False
                                pygame.quit()
                        elif onMenuA:
                            if 300<y<400:
                                isPerehodP = True
                                isPerehod = True
                        elif onMenuP:
                            if 475<y<575:
                                isPerehodA = True
                                isPerehod = True
                            elif 325<y<425:
                                main(hw,darkMode)
                    elif 50<x<100:
                        if 500<y<550:
                            if darkMode == False:
                                darkMode = True
                            else:
                                darkMode = False
                    elif 50<y<100:
                        if onMenu:
                            if 155<x<200:
                                if ind > 0:
                                    ind-=1
                                else:
                                    if ind == 0:
                                        ind = 13                
                            elif 600<x<645:
                                if ind < 13:
                                    ind+=1
                                else:
                                    if ind == 13:
                                        ind = 0
                        
            #обновить дисплей
            pygame.display.flip()
        
        else:
            #кнопка выхода (крестик в правом верхнем углу окна)
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    inGame=False
                    pygame.quit()  

def draw_button(rx,ry,rh,rw,clx,cly,crx,cry,rad,text,tx,ty,colort,colorb,font):
    #рисует те красные кнопки в менью
    ButtonRect = pygame.Rect(rx,ry,rh,rw)
    ButtonCircleL = (clx,cly)
    ButtonCircleR = (crx,cry)
    pygame.draw.rect(screen,colorb,ButtonRect)
    pygame.draw.circle(screen,colorb,ButtonCircleL,rad)
    pygame.draw.circle(screen,colorb,ButtonCircleR,rad)
    img = font.render(text,True,colort)
    screen.blit(img,(tx,ty))

def spawn(cell,empty,hw):
    #спаун новых плиток иногда 2 иногда 4
    l = len(empty)
    if l != 0:
        rand = random.randint(0,l-1)
        tile = empty.pop(rand)
        x,y = de_indexer(tile,hw)
        rand = random.random()
        if rand > 0.9:
            cell[x][y] = 4
        else:
            cell[x][y] = 2

def over(empty,cell,hw):
    #"супер сложный искуственный интеллект" определяющий проиграл ты или еще нет
    empty_updater(cell,empty,hw)
    if len(empty)==0:
        for i in range(hw):
            for j in range(hw):
                if i==0:
                    if j==0:
                        if cell[i][j]==cell[i+1][j] or cell[i][j]==cell[i][j+1]:
                            return False
                    else:
                        if j!=hw-1:
                            if cell[i][j]==cell[i+1][j] or cell[i][j]==cell[i][j+1] or cell[i][j]==cell[i][j-1]:
                                return False
                        else:
                            if cell[i][j]==cell[i+1][j] or cell[i][j]==cell[i][j-1]:
                                return False
                else:
                    if i!=hw-1:
                        if j==0:
                            if cell[i][j]==cell[i+1][j] or cell[i][j]==cell[i-1][j] or cell[i][j]==cell[i][j+1]:
                                return False
                        else:
                            if j!=hw-1:
                                if cell[i][j]==cell[i+1][j] or cell[i][j]==cell[i-1][j] or cell[i][j]==cell[i][j+1] or cell[i][j]==cell[i][j-1]:
                                    return False
                            else:
                                if cell[i][j]==cell[i+1][j] or cell[i][j]==cell[i-1][j] or cell[i][j]==cell[i][j-1]:
                                    return False
                    else:
                        if j==0:
                            if cell[i][j]==cell[i-1][j] or cell[i][j]==cell[i][j+1]:
                                    return False
                        else:
                            if j!=hw-1:
                                if cell[i][j]==cell[i-1][j] or cell[i][j]==cell[i][j+1] or cell[i][j]==cell[i][j-1]:
                                    return False
                            else:
                                if cell[i][j]==cell[i-1][j] or cell[i][j]==cell[i][j-1]:
                                    return False
        else:
            return True
    else:
        return False

def empty_updater(cell,empty,hw):
    #функция обновляет значения пустых ячеек после каждого хода
    empty.clear()
    for i in range(hw):
        for j in range(hw):
            if cell[i][j] == 0:
                emptyTile = indexer(i,j,hw)
                empty.append(emptyTile)
            else:
                if cell[i][j]%2 == 1:
                    cell[i][j] -= 1

def move(cell,empty,vec,hw,score):
    #функция движения плиток
    #коментировать не буду я заебался
    # 2 up 8 down 4 left 6 right
    isMove = False
    moves = []
    notNull = False
    if vec == 2:
        for i in range(hw):
            if cell[0][i]!=0:
                moves.append(0)
                moves.append(i)
                s = cell[0][i]
                moves.append(s)
                moves.append(0)
        for i in range(hw):
            for j in range(1,hw):
                n=1
                k=1
                if cell[j][i]!=0:
                        moves.append(j)
                        moves.append(i)
                        s = cell[j][i]
                        moves.append(s)
                        notNull = True
                while n==1 and j-k>=0:                    
                    if cell[j-k][i]==0:
                        cell[j-k][i],cell[j-k+1][i]=cell[j-k+1][i],cell[j-k][i]
                        k+=1
                        if cell[j-k+1][i]!=0:
                            isMove = True
                    elif cell[j-k][i]==cell[j-k+1][i]:
                        if cell[j-k][i]%2!=1:
                            cell[j-k][i]+=(cell[j-k+1][i])
                            score+=cell[j-k][i]
                            cell[j-k][i]+=1
                            cell[j-k+1][i]=0                        
                            k+=1
                            isMove = True
                        else:
                            n=-1
                    else:
                        n=-1
                if notNull:
                    moves.append(k-1)
                    notNull = False

    elif vec == 8:
        for i in range(hw):
            if cell[hw-1][i]!=0:
                moves.append(hw-1)
                moves.append(i)
                s = cell[hw-1][i]
                moves.append(s)
                moves.append(0)
        for i in range(hw):
            for j in range(hw-2,-1,-1):
                n=1
                k=1
                if cell[j][i]!=0:
                        moves.append(j)
                        moves.append(i)
                        s = cell[j][i]
                        moves.append(s)
                        notNull = True
                while n==1 and j+k<=hw-1:
                    if cell[j+k][i]==0:
                        cell[j+k][i],cell[j+k-1][i]=cell[j+k-1][i],cell[j+k][i]
                        k+=1
                        if cell[j+k-1][i]!=0:
                            isMove = True
                    elif cell[j+k][i]==cell[j+k-1][i]:
                        if cell[j+k][i]%2!=1:
                            cell[j+k][i]+=(cell[j+k-1][i])
                            score+=cell[j+k][i]
                            cell[j+k][i]+=1
                            cell[j+k-1][i]=0
                            k+=1   
                            isMove = True                     
                        else:
                            n=-1
                    else:
                        n=-1
                if notNull:
                    moves.append(k-1)
                    notNull = False
    elif vec == 4:
        for i in range(hw):
            if cell[i][0]!=0:
                moves.append(i)
                moves.append(0)
                s = cell[i][0]
                moves.append(s)
                moves.append(0)
        for i in range(hw):
            for j in range(1,hw):
                n=1
                k=1
                if cell[i][j]!=0:
                        moves.append(i)
                        moves.append(j-k+1)
                        s = cell[i][j]
                        moves.append(s)
                        notNull = True
                while n==1 and j-k>=0:
                    if cell[i][j-k]==0:
                        cell[i][j-k],cell[i][j-k+1]=cell[i][j-k+1],cell[i][j-k]
                        k+=1
                        if cell[i][j-k+1]!=0:
                            isMove = True
                    elif cell[i][j-k]==cell[i][j-k+1]:
                        if cell[i][j-k]%2!=1:
                            cell[i][j-k]+=(cell[i][j-k+1])
                            score+=cell[i][j-k]
                            cell[i][j-k]+=1
                            cell[i][j-k+1]=0
                            k+=1     
                            isMove = True                   
                        else:
                            n=-1
                    else:
                        n=-1
                if notNull:
                    moves.append(k-1)
                    notNull = False
    elif vec == 6:
        for i in range(hw):
            if cell[i][hw-1]!=0:
                moves.append(i)
                moves.append(hw-1)
                s = cell[i][hw-1]
                moves.append(s)
                moves.append(0)
        for i in range(hw):
            for j in range(hw-2,-1,-1):
                n=1
                k=1
                if cell[i][j]!=0:
                        moves.append(i)
                        moves.append(j-k+1)
                        s = cell[i][j]
                        moves.append(s)
                        notNull = True
                while n==1 and j+k<=hw-1:
                    if cell[i][j+k]==0:
                        cell[i][j+k],cell[i][j+k-1]=cell[i][j+k-1],cell[i][j+k]
                        k+=1
                        if cell[i][j+k-1]!=0:
                            isMove = True
                    elif cell[i][j+k]==cell[i][j+k-1]:
                        if cell[i][j+k]%2!=1:
                            cell[i][j+k]+=(cell[i][j+k-1])
                            score+=cell[i][j+k]
                            cell[i][j+k]+=1
                            cell[i][j+k-1]=0
                            k+=1     
                            isMove = True                   
                        else:
                            n=-1
                    else:
                        n=-1
                if notNull:
                    moves.append(k-1)
                    notNull = False

    if isMove != False:
        empty_updater(cell,empty,hw)
        spawn(cell,empty,hw)

    return moves,score

def indexer(a,b,hw):
    #переводит индекс в основном списке на номер плитки на игровой доске
    return(a*hw+b+1)

def de_indexer(a,hw):
    #получает номер плитки и возвращает индекс плитки в основном списке
    a-=1
    return(a//hw,a%hw)

def color_randomizer():
    #придумывание цветов для плиток гениальным дизайнером
    colr=[]
    colg=[]
    colb=[]
    colors = []
    for i in range(24):
        r=random.randint(20,230)
        g=random.randint(20,230)
        b=random.randint(20,230)
        colr.append(r)
        colg.append(g)
        colb.append(b)
    colors.append(colr)
    colors.append(colg)
    colors.append(colb)
    return (colors)

def printer(cell):
    #вывод основного списка в консоль
    print('-'*50)
    for i in cell:
        print(*i)
    print('-'*50)

def coordinate(i,j,sizes,hw):
    #берет индекс плитки в основном списке и возвращает его координаты в пикселях
    x = j*(sizes[hw-3][3]+sizes[hw-3][4])+(sizes[hw-3][0]+sizes[hw-3][4])
    y = i*(sizes[hw-3][3]+sizes[hw-3][4])+(sizes[hw-3][1]+sizes[hw-3][4]) 
    return(x,y)

def draw(cell,colors,sizes,hw,moves,vec,score,thisGameIsOver,darkMode):
    #функция для вывода изображения на экран
    #переменная показывает должна ли быть анимация движения
    animT = False
    #узнаем сколько плиток сдвинулось с места
    if len(moves) != 0:
        animT = True
    #нормализатор итераций
    clock=pygame.time.Clock()
    #счетчик анимации
    animR = 0
    if darkMode:            
        colorD = white
    else:
        colorD = black
    while animT:
        #заливка экрана
        if darkMode:   
            screen.fill(black)         
            tile_draw(sizes[hw-3][0]-2,sizes[hw-3][1]-2,sizes[hw-3][2]+4,sizes[hw-3][2]+4,sizes[hw-3][3]//4+2,white)
        else:
            screen.fill(white)
        
        #рисуем фоновую плитку
        tile_draw(sizes[hw-3][0],sizes[hw-3][1],sizes[hw-3][2],sizes[hw-3][2],sizes[hw-3][3]//4,black)
        #кадры в секунду fps
        clock.tick(60)
        #пробегаемся по каждой плитке в списке
        for i in range(0,len(moves)-1,4):
            #переводим индексы в координаты
            x,y = coordinate(moves[i],moves[i+1],sizes,hw)
            #на сколько должна сдвинуться плитка за один кадр
            move = moves[i+3]*sizes[hw-3][3]//10
            #даем плитке цвет
            ind = int(math.log2(moves[i+2]))
            color = (colors[0][ind],colors[1][ind],colors[2][ind])
            #выполняем операции в зависимости вектора движения плиток (2 вверх, 8 вниз, 4 влево, 6 вправо) 
            if vec == 2:
                y-=move*animR
                tile_draw(x,y,sizes[hw-3][3],sizes[hw-3][3],sizes[hw-3][3]//4,color)
            elif vec == 8:
                y+=move*animR
                tile_draw(x,y,sizes[hw-3][3],sizes[hw-3][3],sizes[hw-3][3]//4,color)
            elif vec == 4:
                x-=move*animR
                tile_draw(x,y,sizes[hw-3][3],sizes[hw-3][3],sizes[hw-3][3]//4,color)
            else:
                x+=move*animR
                tile_draw(x,y,sizes[hw-3][3],sizes[hw-3][3],sizes[hw-3][3]//4,color)

            #рисуем значения каждой плитки 2.4.8.16.32 и т.д.
            text = str(moves[i+2])
            #в зависимости от длинны текста выбираем шрифт
            leng = len(text)
            if leng == 1:
                leng = 2
                m = True
            else:
                m=False
            #длинна и ширина плитки
            tilePx = sizes[hw-3][3]
            #общая длинна текста в пикселях
            textSize = tilePx - (tilePx//3)
            #длинна каждой буквы в пикселях
            fontSizePx = textSize//leng
            #размер шрифта
            fontSize = int(fontSizePx/4*10)
            font = pygame.font.SysFont(None,fontSize)
            #центрирование текста
            if m:
                xs = (tilePx - textSize)//2 + fontSizePx//2 + 1
            else:
                xs = (tilePx - textSize)//2
            ys = (tilePx - fontSize*6/10)//2
            #рендер текста как картинки и вывод на экран
            img = font.render(text,True, black)             
            screen.blit(img, (x+xs,y+ys))
        #кнопка back
        font = pygame.font.SysFont(None,30)
        img = font.render('Back',True, colorD)
        screen.blit(img,(50,50))
        pygame.draw.lines(screen,colorD,False,[[47,51],[33,58],[47,65]],3)
        #score
        img = font.render('Score: '+str(score),True,colorD)
        screen.blit(img,(50,550))
        #если ходов больше нет высвечивается надпись Game Over
        if thisGameIsOver:
            font = pygame.font.SysFont(None,70)
            img = font.render('Game Over!',True, colorD)
            screen.blit(img, (254,36))
        #счетчик анимации
        if animR>=6:
            animT = False
        animR+=1
        #обновление экрана
        pygame.display.flip()
    

    #тут почти то же самое только уже конечный результат без анимации движения
    
    #белая рамка для дарк мода
    if darkMode:
        screen.fill(black)
        tile_draw(sizes[hw-3][0]-2,sizes[hw-3][1]-2,sizes[hw-3][2]+4,sizes[hw-3][2]+4,sizes[hw-3][3]//4+2,white)
    else:
        screen.fill(white)
    tile_draw(sizes[hw-3][0],sizes[hw-3][1],sizes[hw-3][2],sizes[hw-3][2],sizes[hw-3][3]//4,black)
    
    #tile draw
    for i in range(hw):
        for j in range(hw):
            san = cell[i][j]
            if san != 0:
                ind = int(math.log2(san))
                color = (colors[0][ind],colors[1][ind],colors[2][ind])
                x,y = coordinate(i,j,sizes,hw)
                tile_draw(x,y,sizes[hw-3][3],sizes[hw-3][3],sizes[hw-3][3]//4,color)
                #text draw
                #6.9px*4px per 10size
                text = str(san)
                leng = len(text)
                if leng == 1:
                    leng = 2
                    m = True
                else:
                    m=False
                tilePx = sizes[hw-3][3]
                textSize = tilePx - (tilePx//3)
                fontSizePx = textSize//leng
                fontSize = int(fontSizePx/4*10)
                font = pygame.font.SysFont(None,fontSize)
                if m:
                    xs = (tilePx - textSize)//2 + fontSizePx//2 + 1
                else:
                    xs = (tilePx - textSize)//2
                ys = (tilePx - fontSize*6/10)//2
                img = font.render(text,True, black)
                screen.blit(img, (x+xs,y+ys))
    #back
    font = pygame.font.SysFont(None,30)
    img = font.render('Back',True, colorD)
    screen.blit(img,(50,50))
    pygame.draw.lines(screen,colorD,False,[[47,51],[33,58],[47,65]],3)

    #score
    img = font.render('Score: '+str(score),True,colorD)
    screen.blit(img,(50,550))

    if thisGameIsOver:
        font = pygame.font.SysFont(None,70)
        img = font.render('Game Over!',True, colorD)
        screen.blit(img, (254,36))
        
    pygame.display.flip()

def main(hw,darkMode):
    #список с размерами плиток и т.д.
    #x,y,bg,tile,border
    sizes = [[240,140,320,100,5],
            [188,88,425,100,5],
            [188,88,424,80,4],
            [185,85,430,67,4],
            [185,85,430,58,3],
            [186,86,427,50,3],
            [187,87,426,44,3],
            [189,89,422,40,2],
            [185,85,431,37,2],
            [183,83,434,34,2],
            [185,85,430,32,1],
            [182,82,435,30,1],
            [182,82,436,28,1],
            [183,83,433,26,1]]
    #основной список
    cell = []
    #счет игрока
    score = 0
    #создание игрового поля
    for i in range(hw):
        cell.append([0]*hw)
    #список пустых ячеек
    empty = []
    #заполнение списка с пустыми ячейками
    for i in range(hw*hw):
        empty.append(i+1)
    #спаун двух начальных плиток
    spawn(cell,empty,hw)
    spawn(cell,empty,hw)
    #каждую игру создается список с рандомными цветами для плиток (чтобы изменить цвет нажми Enter)
    colors = color_randomizer()
    #указатель окончания игры
    thisGameIsOver = False
    #указатель окончания сеанса
    gameOver = False
    #пустой список и переменная заглушки
    l=[]
    v=0
    #функция вывода на экран
    draw(cell,colors,sizes,hw,l,v,score,thisGameIsOver,darkMode)
    #счетчик итераций
    clock=pygame.time.Clock()
    
    while gameOver == False:  
        #кол-во итераций в секунду
        clock.tick(60)
        #получние координат мыши
        x,y = pygame.mouse.get_pos()
        #обработка нажатий на кнопки
        for i in pygame.event.get():  
            #крестик в углу окна              
            if i.type==pygame.QUIT:
                gameOver=True
                pygame.quit()
            elif i.type == pygame.KEYUP:
                #стрелки вверх, вниз, вправо, влево
                if i.key==pygame.K_UP:
                    #функции просчета движения плиток и вывода на экран
                    moves,score = move(cell,empty,2,hw,score)                        
                    draw(cell,colors,sizes,hw,moves,2,score,thisGameIsOver,darkMode)
                elif i.key==pygame.K_DOWN:
                    moves,score = move(cell,empty,8,hw,score)                        
                    draw(cell,colors,sizes,hw,moves,8,score,thisGameIsOver,darkMode)
                elif i.key==pygame.K_RIGHT:
                    moves,score = move(cell,empty,6,hw,score)                        
                    draw(cell,colors,sizes,hw,moves,6,score,thisGameIsOver,darkMode)
                elif i.key==pygame.K_LEFT:
                    moves,score = move(cell,empty,4,hw,score)                        
                    draw(cell,colors,sizes,hw,moves,4,score,thisGameIsOver,darkMode)
                #нажатие на Enter меняет цвет плиток
                elif i.key==pygame.K_RETURN:
                    #очищаем список и заполняем заново
                    colors.clear()
                    colors = color_randomizer()
                    #рисуем плитки уже с новыми цветами
                    draw(cell,colors,sizes,hw,l,v,score,thisGameIsOver,darkMode)
                #нажатие на Esc выход из игры
                elif i.key==pygame.K_ESCAPE:
                    gameOver=True
            #проверка на нажатие кнопки Back мышью
            elif i.type == pygame.MOUSEBUTTONUP:
                if 30<x<95:
                    if 40<y<75:                            
                        gameOver = True
        #функция проверка остались ли еще ходы
        thisGameIsOver = over(empty,cell,hw)

def tile_draw(x,y,width,height,radius,color):
    #эта функция рисует скругленные квадраты или прямоугольники

    #radius это радиус скругления квадратов
    diameter = radius*2
    #два прямоуголника наложенные друг на друга получается что то типа плюсика
    rect1 = pygame.Rect(x+radius,y,width-diameter,height)
    rect2 = pygame.Rect(x,y+radius,width,height-diameter)
    #четыре круга наложенные на пустоты в плюсике и собственно скругления нашей фигуры
    circle1 = (x+radius,y+radius)
    circle2 = (x-radius+width,y+radius)
    circle3 = (x+radius,y-radius+height)
    circle4 = (x-radius+width,y-radius+height)
    #рисуем это все на экране
    pygame.draw.rect(screen,color,rect1)
    pygame.draw.rect(screen,color,rect2)
    pygame.draw.circle(screen,color,circle1,radius)
    pygame.draw.circle(screen,color,circle2,radius)
    pygame.draw.circle(screen,color,circle3,radius)
    pygame.draw.circle(screen,color,circle4,radius)

menu_1()