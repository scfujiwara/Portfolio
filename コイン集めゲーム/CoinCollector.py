import pygame
import random
import tkinter as tk
import tkinter.messagebox as messagebox

#初期化
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("Coin Collector Game")

# 背景画像
screen_image = pygame.image.load("Data/sea.jpg") # 画像を読み込む
screen_image = pygame.transform.scale(screen_image,[800,600]) # 画像のサイズを指定する
screen_rect = screen_image.get_rect()


# プレイヤー関連
player_image = pygame.image.load("Data/player.png") # 画像を読み込む
player_image = pygame.transform.scale(player_image,[40,40]) # 画像のサイズを指定する
player_rect = player_image.get_rect() # Rect（四角）オブジェクトも生成しておく

# コイン関連
coin_image = pygame.image.load("Data/kaigara_nimaigai.png") # 画像を読み込む
coin_image = pygame.transform.scale(coin_image,[40,40]) # 画像のサイズを指定する
coins_rect = []
for i in range(20): # コインの数
    x = random.randint(0,700)
    y = random.randint(200,500)
    coins_rect.append(pygame.Rect(x, y, coin_image.get_width(), coin_image.get_height()))

# エネミー関連
enemy_image = pygame.image.load("Data/barakuda.png") # 画像を読み込む
enemy_image = pygame.transform.scale(enemy_image,[80,40]) # 画像のサイズを指定する
enemys_rect = [] # Rect（四角）オブジェクトも生成しておく
for i in range(300): #エネミーの数
    x = random.randint(600,40000)
    y = random.randint(200,600)
    enemys_rect.append(pygame.Rect(x, y, enemy_image.get_width(), enemy_image.get_height()))

# 開始効果音関連
def start(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
start("Data/男衆「始めいッ！」.mp3")

# アイテム取得効果音関連
def get(getfilename):
    pygame.mixer.init()
    pygame.mixer.music.load(getfilename)
    pygame.mixer.music.play()

# ゲームオーバー効果音関連
def over(overfilename):
     pygame.mixer.init()
     pygame.mixer.music.load(overfilename)
     pygame.mixer.music.play()

# ゲームクリア効果音関連
def clear(clearfilename):
     pygame.mixer.init()
     pygame.mixer.music.load(clearfilename)
     pygame.mixer.music.play()

# スコア用
collected_coins = 0

# ゲームループ
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # キー操作を受け付けてプレイヤーを動かす
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] == True:
        player_rect.x -= 1
    if keys[pygame.K_RIGHT] == True:
        player_rect.x += 1
    if keys[pygame.K_UP] == True:
        player_rect.y -= 1
    if keys[pygame.K_DOWN] == True:
        player_rect.y += 1
    
    # プレイヤーがコインに触れた時の処理
    for coin_rect in coins_rect:
        if player_rect.colliderect(coin_rect) == True:
            coins_rect.remove(coin_rect)
            get("Data/アイテムを入手1.mp3") #アイテム取得効果音を追加
            collected_coins += 1

    # 背景色を塗りつぶす
    screen.blit(screen_image, screen_rect)

    # コイン、プレイヤー、エネミーを描画
    for coin_rect in coins_rect:
        screen.blit(coin_image, coin_rect)
    for enemy_rect in enemys_rect:
        screen.blit(enemy_image, enemy_rect)
        enemy_rect.x -= 1 # エネミー移動
    screen.blit(player_image, player_rect)
    
    pygame.display.update()

    #クリア時の処理
    if collected_coins == 20:
        clear("Data/歓声と拍手.mp3") # ゲームクリア効果音を流す
        tk.Tk().withdraw() # ダイアログ追加
        messagebox.showinfo('ゲームクリア！', 'おめでとうございます！ゲームクリアです！') # ゲームクリアメッセージ
        running = False

    #　ゲームオーバーの処理
    for enemy_rect in enemys_rect:
        if player_rect.colliderect(enemy_rect) == True:
            over("Data/男性の悲鳴.mp3") # ゲームオーバー効果音を流す
            tk.Tk().withdraw() # ダイアログ追加
            messagebox.showinfo('ゲームオーバー', 'バラクーダ（オニカマス）に嚙まれました！') # ゲームオーバーメッセージ
            running = False
    
# ゲーム終了
pygame.quit()
