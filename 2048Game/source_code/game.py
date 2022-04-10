import sys
import random
import datetime

import pygame

import constants as const

# 存储开始时间
startTime = datetime.datetime.now()
# 存储分数
score = 0
# 存储最高分数
highScore = 0


# 获取最高分数
def get_highest_score():
    file = open("score")
    scores = file.readlines()
    maxScore = int(scores[0].rstrip("\n"))
    # 遍历寻找最大值
    for i in range(len(scores)):
        score = int(scores[i].rstrip("\n"))
        if maxScore < score:
            maxScore = score
    return maxScore


class Logic:
    def __init__(self, matrix_shape=(4, 4)):
        self.matrix = [[0 for i in range(matrix_shape[0])]
                       for i in range(matrix_shape[1])]
        self.generate_new_num()
        self.generate_new_num()
        # 获取最高分
        global highScore
        highScore = get_highest_score()

    # 让左边为0的清空，使之非0数移动到左边
    def clear_zero(self, row):
        # 倒着遍历
        for i in range(len(row) - 1, -1, -1):
            if row[i] == 0:
                row.pop(i)
                row.append(0)

    # 往左移动并合并
    def merge(self, row):
        self.clear_zero(row)
        for i in range(len(row) - 1):
            if row[i] == 0:
                break
            if row[i] == row[i + 1]:
                row[i] *= 2  # 合并
                global score
                score += row[i]  # 分数统计
                row.pop(i + 1)
                row.append(0)

    def matrix_transpose(self):
        # 矩阵转置
        for col_index in range(1, len(self.matrix)):
            for row_index in range(col_index, len(self.matrix)):
                self.matrix[row_index][col_index - 1], self.matrix[col_index - 1][row_index] = \
                    self.matrix[col_index - 1][row_index], self.matrix[row_index][col_index - 1]

    def left(self):
        for row in self.matrix:
            self.merge(row)

    def right(self):
        for row in self.matrix:
            row.reverse()
            self.merge(row)
            row.reverse()

    def up(self):
        self.matrix_transpose()
        self.left()
        self.matrix_transpose()

    def down(self):
        self.matrix_transpose()
        self.right()
        self.matrix_transpose()

    def move(self, direction):
        dir_dict = {
            'left': self.left,
            'right': self.right,
            'up': self.up,
            'down': self.down
        }
        func = dir_dict.get(direction)
        if func:
            func()

    # 获取所有空的位置
    def get_empty_position(self):
        empty_position = []
        for row_index in range(len(self.matrix)):
            for col_index in range(len(self.matrix[row_index])):
                if self.matrix[row_index][col_index] == 0:
                    empty_position.append((row_index, col_index))
        return empty_position

    # 生成新数字
    def generate_new_num(self):
        self.empty_position = self.get_empty_position()
        if not self.empty_position:
            return False
        row_index, col_index = random.choice(self.empty_position)
        self.matrix[row_index][col_index] = 4 if random.randint(1,
                                                                10) == 1 else 2
        self.empty_position.remove((row_index, col_index))
        return True

    # 判断是否胜利
    def is_game_win(self):
        for r in self.matrix:
            if 2048 in r:
                return True
        return False

    # 判断是否结束
    def is_game_over(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r]) - 1):
                # 判断是否还可以走
                if self.empty_position:
                    return False
                # 判断是否还可以相加
                if self.matrix[r][c] == self.matrix[r][
                        c + 1] or self.matrix[c][r] == self.matrix[c + 1][r]:
                    return False
        return True


# 初始化标题，刷新时间
def init_title():
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pygame.display.set_caption("2048 (温馨提示：当前时间:{})".format(time))


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    init_title()# 刷新标题
    return screen


KEY_DOWN_DICT = {
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down',
    pygame.K_LEFT: 'left',
    pygame.K_RIGHT: 'right'
}


# 存储分数
def store_score(score):
    file = open("score", "a")
    file.write("{}\n".format(score))
    file.close()


# 退出事件
def quit_event(screen):
    # 保存分数
    global score
    store_score(score)
    pygame.quit()
    sys.exit()


def press(is_game_over, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击关闭按钮退出
            quit_event(screen)
        elif event.type == pygame.KEYDOWN:
            if not is_game_over:
                direction = KEY_DOWN_DICT.get(event.key)
                return direction
            elif event.key == 13:
                return True


# 画分数
def draw_score(score, screen):
    # 画方块
    color = "#eee4da"
    pygame.draw.rect(screen, color, (370, 10, 190, 80))
    # 画内容
    content = "Score:{}".format(score)
    font = pygame.font.SysFont('arialblod', 45)
    screen.blit(font.render(content, True, "#9e948a"), (380, 40))


# 画最高分
def draw_highest_score(maxScore, screen):
    # 画方块
    color = "#f67c5f"
    pygame.draw.rect(screen, color, (370, 190, 190, 80))
    # 画内容
    content = "HighestScore:{}".format(maxScore)
    font = pygame.font.SysFont('arialblod', 30)
    screen.blit(font.render(content, True, "#776e65"), (380, 220))


# 画游戏时间
def draw_game_time(screen):
    # 画方块
    color = "#f2b179"
    pygame.draw.rect(screen, color, (370, 280, 190, 80))
    # 画内容
    time = datetime.datetime.now()
    res = (time - startTime).seconds
    content = "GameTime:{}".format(res)
    font = pygame.font.SysFont('arialblod', 35)
    screen.blit(font.render(content, True, "#776e65"), (380, 310))


# 画上次分数
def draw_last_score(screen):
    # 画方块
    color = "#edcc61"
    pygame.draw.rect(screen, color, (370, 100, 190, 80))
    # 读取上次分数
    file = open("score")
    line = file.readline()
    lastLine = ""
    while line:
        lastLine = line
        line = file.readline()
    lastLine = lastLine.rstrip("\n")
    # 画内容
    content = "LastScore:{}".format(lastLine)
    font = pygame.font.SysFont('arialblod', 35)
    screen.blit(font.render(content, True, "#776e65"), (380, 130))
    file.close()


def draw_num(logic, screen):
    for r in range(len(logic.matrix)):
        for c in range(len(logic.matrix[r])):
            num = logic.matrix[r][c]
            color = pygame.Color(
                const.BACKGROUND_COLOR_DICT.get(
                    num, const.BACKGROUND_COLOR_CELL_EMPTY))
            x = const.MARGIN * (c + 1) + c * const.CELL_SIZE
            y = const.MARGIN * (r + 1) + r * const.CELL_SIZE
            width = const.CELL_SIZE
            height = const.CELL_SIZE
            pygame.draw.rect(screen, color, (x, y, width, height))
            if num != 0:
                font_color = pygame.Color(const.CELL_COLOR_DICT.get(num))
                font_size = const.CELL_SIZE - const.PADDING * len(str(num))
                font = pygame.font.SysFont('arialblod', font_size)
                font_width, font_height = font.size(str(num))
                screen.blit(font.render(str(num), True, font_color),
                            (x + (const.CELL_SIZE - font_width) / 2, y +
                             (const.CELL_SIZE - font_height) / 2 + 5))


def game_over_or_win(screen, clock, text='Game Over!'):
    font = pygame.font.SysFont('Blod', const.FONT_SIZE)
    font_width, font_height = font.size(str(text))
    while True:
        if press(True, screen):
            break
        screen.blit(font.render(str(text), True, (0, 0, 0)),
                    ((const.SCREEN_WIDTH - font_width) / 2,
                     (const.SCREEN_HEIGHT - font_height) / 2))
        pygame.display.update()
        clock.tick(const.FPS)


def main():
    screen = init_game()
    clock = pygame.time.Clock()
    logic = Logic()
    is_wined = False
    while True:
        if not is_wined and logic.is_game_win():
            is_wined = True
            game_over_or_win(screen, clock, text='You Win!')
        if logic.is_game_over():
            break
        direction = press(False, screen)
        if direction:
            logic.move(direction)
            logic.generate_new_num()
        screen.fill(pygame.Color(const.BACKGROUND_COLOR))
        draw_num(logic, screen)
        draw_score(score, screen)
        draw_highest_score(highScore, screen)
        draw_last_score(screen)
        draw_game_time(screen)
        pygame.display.update()
        clock.tick(const.FPS)
        init_title()
    game_over_or_win(screen, clock)


if __name__ == '__main__':
    while True:
        main()
