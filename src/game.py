import pygame
import random #import 隨機的模組
import os
FPS = 60
#遊戲初始化 and 創建視窗
pygame.init()   #把pygame裡的東西做初始化的動作
screen=pygame.display.set_mode((500,600))  
#創建視窗:可以傳入一個tuple模組像是寬度500高度600
pygame.display.set_caption("SPACE SHIP FIGHTING BABY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
clock = pygame.time.Clock() 
# 創建一個物件 對時間做出管理跟操控
BLACK=(0,0,0)
#載入圖片
background_img=pygame.image.load(os.path.join("./images/black.png")).convert()        
# os.path代表python檔案的位置  convert 是可以將圖片轉換成python轉換得懂的
player_img=pygame.image.load(os.path.join("./images/fluffy devil.png")).convert()
rock_img=pygame.image.load(os.path.join("./images/fatty boy.png")).convert()
bullet_img=pygame.image.load(os.path.join("./images/bullet.png")).convert()
class Player (pygame.sprite.Sprite):   
    #Sprite可以用來創建東西，像是石頭、飛行船、子彈等等，用Player來繼承內建sprite的類別
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale( player_img,(50,38 ) )    
        #scale可以幫我們自動調整圖片的大小     
        #image代表要顯示的圖片   pygame.Surface((50,40))先用pygame平面標示用而已
                                # (0,255,0)就只有深綠色
        self.rect=self.image.get_rect()    #rect定位我們要的圖片，
        self.rect.centerx = 500/2            
        #self.rect.center=(500/2,600/2)    綠色框框放在中間 
        self.rect.bottom = 600-10
        #self.rect.x=200 self.rect.y=200 目前我們可以設定總共有9個 xy軸、left or right、top right or left、bottom right or left 以及center X軸往右 Y軸往下 ，做標(500,600)，我們現在的圖片標示為(200,200)=top left的座標
        self.speedx =8 #增加移動的速度
    def update(self):       #建立一個更新的函式
            key_pressed = pygame.key.get_pressed() # 函式pygame.key.get_pressed()會回傳一堆布林值代表的是我們鍵盤上的按鍵是否有被按到 true =有按 fasle =沒按
            if key_pressed [pygame.K_d]:    #判斷鍵盤上的右鍵(也可以設成pygame.K_RIGHT如果被按到，則按d往右移動)是否有被按到
                self.rect.x+=self.speedx        #按到就往右邊移動    
            if key_pressed [pygame.K_a]:     #判斷鍵盤上的左鍵(也可以設成pygame.K_LEFT如果被按到，則按d往左移動)是否有被按到
                self.rect.x-=self.speedx        #按到就往左邊移動                #self.rect.x +=2  # 綠色框框會一直往右邊移動
                                                                                # if self.rect.left >500:#判斷綠色方塊左邊的座標大於畫面的寬度時，同時讓右邊的座標為0
                                                                                # self.rect.right=0#畫面就會變成綠色框框會往右邊移動，超出了畫面又會從左邊從頭開始移動
            if self.rect.right > 500:           
                #判斷綠色框框的右邊座標是否超出視窗的寬度(500)
                self.rect.right = 500           
                #如果超出則待在視窗的角落，不讓它超出視窗
            if self.rect.left < 0:             
                #判斷綠色框框的左邊座標是否超出視窗的寬度(0)
                self.rect.left = 0              
                #如果超出則待在視窗的角落，不讓它超出視窗
    def shoot (self) :
        bullet = Bullet(self.rect.centerx , self.rect.top)   
        #飛船的centerx 跟頂部的座標存在子彈
        all_sprites.add(bullet)  #把bullet加進sprites裡面
        bullets.add(bullet)     #把子彈加進子彈的群組
class Rock(pygame.sprite.Sprite):   
    #Sprite可以用來創建東西，像是石頭、飛行船、子彈等等，用Rock來繼承內建sprite的類別
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = rock_img
        self.image = self.image_ori.copy()
        self.image_ori.set_colorkey(BLACK)
        self.image= rock_img   
        #image代表要顯示的圖片   pygame.Surface((30,40))先用pygame平面標示用而已
        #(255,0,0)就只有深紅色
        self.rect=self.image.get_rect()    #rect定位我們要的圖片，
        self.rect.x = random.randrange(0,500-self.rect.width)             
        # 要讓石頭掉下來的函式庫 random.randrange()隨機傳入兩個數字進入函式裡面，函式再回傳兩個數字之間的隨機數字  (0,500-seld.rect.width) 視窗寬度減掉石頭的寬度，就是石頭的x軸
        self.rect.y = random.randrange(-100,-40)    
        # 讓石頭掉下來從視窗看不到的地方掉下來
        self.speedy = random.randrange(2,10)    
        #講解一下: self.rect.x=200 self.rect.y=200 目前我們可以設定總共有9個 xy軸、left or right、top right or left、bottom right or left 以及center X軸往右 Y軸往下 ，做標(500,600)，我們現在的圖片標示為(200,200)=top left的座標
        self.speedx = random.randrange(-3,3)    #石頭的水平速度
                                                #self.speedx =8 #增加移動的速度
        self.total_degree = 0
        self.rot_degree = 3                                        
    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360 
        #石頭不會轉超過360度 對360度取餘數
        
        self.image = pygame.transform.rotate(self.image_ori,self.total_degree)
        #傳入兩個參數 1.轉動的圖片 2.轉動幾度?假設我們寫轉動5度，但是會讓圖片一點點失針 
        #所以我們創建self.image_ori(不會轉動的圖片)對它一直轉動3度，self.total_degree(整個總角度)持續做轉動，所以每3度就累加轉動次數 ex:第1次轉3度 第2次轉6度 第3次轉9度 and so on
    
    
    
    
    
    def update(self):       #建立一個更新的函式
        self.rotate()       #石頭一秒鐘轉動60次
        self.rect.y += self.speedy        #讓石頭有垂直速度    
        self.rect.x+= self.speedx         #讓石頭有水平速度 
        if self.rect.top > 600 or self.rect.left > 500 or self.rect.right < 0  :     
            #只有石頭頂部高於我們視窗的高度、或左邊的大於我們視窗、或右邊的小於0就重設
            self.rect.x = random.randrange(0,500-self.rect.width)             # 要讓石頭掉下來的函式庫 random.randrange()隨機傳入兩個數字進入函式裡面，函式再回傳兩個數字之間的隨機數字  (0,500-seld.rect.width) 視窗寬度減掉石頭的寬度，就是石頭的x軸
            self.rect.y = random.randrange(-100,-40)    
            # 讓石頭掉下來從視窗看不到的地方掉下來
            self.speedy = random.randrange(2,10)    
            #講解一下: self.rect.x=200 self.rect.y=200 目前我們可以設定總共有9個 xy軸、left or right、top right or left、bottom right or left 以及center X軸往右 Y軸往下 ，做標(500,600)，我們現在的圖片標示為(200,200)=top left的座標
            self.speedx = random.randrange(-3,3)    #石頭的水平速度

class Bullet(pygame.sprite.Sprite):   
    #Sprite可以用來創建東西，像是石頭、飛行船、子彈等等，用Rock來繼承內建sprite的類別
    def __init__(self,x,y):     #傳入飛船的xy的資訊
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))  
        #image代表要顯示的圖片   pygame.Surface((10,20))先用pygame平面標示用而已
        self.image.fill((255,255,0))    # (255,255,0)就只有深黃色
        self.rect=self.image.get_rect()    #rect定位我們要的圖片，
        self.rect.centerx = x             # 子彈的x把它設成傳進來的x
        self.rect.bottom =y   #子彈的底部設成傳進來的y
        self.speedy = -10   #子彈又有速度，子彈往上射，速度就是負的
                            #self.speedx =8 #增加移動的速度
    def update(self):       #建立一個更新的函式
        self.rect.y += self.speedy
        if self.rect.bottom < 0 : #子彈往上射超出了視窗就把他給刪了
            self.kill()     #sprite裡的群組中把子彈給移除掉
            
 
            
all_sprites = pygame.sprite.Group() #sprite的群組可以放許多sprite的物件
rocks = pygame.sprite.Group()       #創建一個放石頭的群組
bullets = pygame.sprite.Group()     #創建一個放子彈的群組




player = Player()
all_sprites.add(player) #把player加進sprite的群組

for i in range (8):
    r=Rock()            #r= Rock()#創建石頭
    all_sprites.add(r)      #把石頭加進sprites的群組 ，會隨機掉下石頭一共有八顆
    rocks.add(r)            #把石頭加進石頭的群組
      

running=True    
#用變數判斷迴圈是該進行下去

#遊戲迴圈
while running :
    clock.tick(FPS)  
    # 這個函示是1秒鐘最多只能被執行60次
#取得玩家的輸入，ex:玩家點右上方的叉叉就要關掉
    for event in pygame.event.get():         
        #回傳所有發生的事件像是滑鼠滑到哪裡，鍵盤按了什麼，回傳列表，同時也會發生很多事件，像是按了許多次鍵盤，要一一做檢查     
        if event.type== pygame.QUIT:         #如果按了叉叉就要離開遊戲視窗
            running =False                   #離開遊戲
        elif event.type == pygame.KEYDOWN:   
            #KEYDOWN 就是按下鍵盤鍵的意思
            if event.key == pygame.K_SPACE:   
                #判斷按的是什麼鍵  如果是空白鍵的話就發射子彈
                player.shoot()         


#更新遊戲 不同電腦 速度會不一樣 體驗就會不一樣 所以要解決這個問題
    all_sprites.update()    
    #執行sprites群組裡每一個物件的更新函式 會把子彈跟石頭的位置做更新
    hits = pygame.sprite.groupcollide(rocks,bullets,True,True)   
    #判斷石頭跟子彈碰撞 要寫入兩個布林值去做判斷 石頭是不是要刪掉，要的話寫True，那子彈要不要刪除?要的話要寫True
    for hit in hits : #每消滅一個石頭，就創建一個新的石頭
        r = Rock ()            #創建石頭
        all_sprites.add(r)      #all sprite加進石頭的群組
        rocks.add(r)            #石頭加進石頭的群組
    hits=pygame.sprite.spritecollide(player, rocks,False)            
    #判斷石頭跟飛船碰撞 石頭不能馬上被消滅，所以要寫false
    if hits:                                                    
        #但是如果飛船被石頭砸到 則game over 
        running = False

#畫面顯示
    screen.fill((0,0,0))    
    #screen.fill((R,G,B))  視窗塗滿顏色    R,G,B,共可被寫成0~255的數字，數字愈大顏色就愈重 white =(255,255,255) black=(0,0,0)
    screen.blit(background_img, (0,0))                          
    #blit的意思就是畫背景話在畫面上，要畫的圖片畫在第1個參數、第2個畫在哪一個位置
    
    all_sprites.draw(screen) #把all sprite群組裡的所有物件全部畫在我們的sceen上
    pygame.display.update() #畫面做更新，畫面都是紅色的
pygame.quit()                        