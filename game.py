import pyxel
import random

class Game:
    def __init__(self):
        # ゲームの初期設定
        pyxel.init(256, 256)
        pyxel.load("my_resource.pyxres")  # リソースファイルの読み込み

        self.player_x = 128  # 主人公の初期位置
        self.obstacles = []  # 障害物のリスト
        self.lives = 3       # ライフ
        self.score = 0       # スコア

        pyxel.run(self.update, self.draw)

    def update(self):
        # ゲームのロジック更新
        self.update_player()
        self.update_obstacles()
        self.check_collisions()

    def update_player(self):
        # 主人公の移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)

    def update_obstacles(self):
        # 障害物の更新
        if random.random() < 0.05:  # 約0.5秒に一回の確率で障害物を追加
            obstacle_type = random.choice(['flame', 'thunder', 'virus'])
            x = random.randint(0, pyxel.width - 16)
            self.obstacles.append((x, 0, obstacle_type))

        # 障害物の移動
        self.obstacles = [(x, y + 2, type) for x, y, type in self.obstacles if y < pyxel.height]


    def check_collisions(self):
        # 衝突の確認
        player_rect = (self.player_x, 200, 80, 80)  # 主人公の矩形（x, y, 幅, 高さ）
        for x, y, type in self.obstacles:
            if type == 'flame':
                obstacle_rect = (x, y, 48, 48)  # 炎の矩形
            elif type == 'thunder':
                obstacle_rect = (x, y, 48, 56)  # 雷の矩形
            elif type == 'virus':
                obstacle_rect = (x, y, 56, 48)  # ウイルスの矩形
    
            if self.rects_overlap(player_rect, obstacle_rect):
                self.lives -= 1
                self.obstacles.remove((x, y, type))
                if self.lives <= 0:
                    pyxel.quit()
    
    def rects_overlap(self, rect1, rect2):
        x1, y1, w1, h1 = rect1
        x2, y2, w2, h2 = rect2
        return (x1 < x2 + w2 and x2 < x1 + w1 and
                y1 < y2 + h2 and y2 < y1 + h1)
    
    def draw(self):
        # ゲームの描画
        # ゲームの描画
        pyxel.cls(0)
        # pyxel.rect(1, 0, pyxel.width, pyxel.height, 1)  # 背景色


        # 主人公の描画
        pyxel.blt(self.player_x, 200, 0, 88, 168, 80, 80, 0) 



        # 障害物の描画
        for x, y, type in self.obstacles:
            if type == 'flame':
                pyxel.blt(x, y, 0, 72, 8, 48, 48, 0)  # 炎のサイズを更新
            elif type == 'thunder':
                pyxel.blt(x, y, 0, 16, 64, 48, 56, 0)  # 雷のサイズを更新
            elif type == 'virus':
                pyxel.blt(x, y, 0, 112, 72, 56, 48, 0)  # ウイルスのサイズを更新

        # ライフの表示（テキストと数字で）
        pyxel.text(50, 5, f"Lives: {self.lives}", 7)

Game()
