"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

NUM_LIVES = 3  # Initial number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.brick_offset = brick_offset
        self.brick_rows = brick_rows
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.ball_radius = ball_radius
        self.__click_switch = 0
        self.brick_nums = brick_rows * brick_cols
        self.brick_clear = 0
        self.brick_score = 0
        self.num_lives = NUM_LIVES

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'navy'
        self.paddle.color = 'magenta'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=self.window.height-self.paddle.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'gray'
        self.ball.color = 'gray'
        self.window.add(self.ball, x=(window_width-2*ball_radius)/2, y=(window_height-2*ball_radius)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.starter)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                if i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                if i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                if i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                if i == 8 or i == 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=0+j*(brick_width+brick_spacing),
                                y=brick_offset+i*(brick_height+brick_spacing))

        # Scoreboard
        self.scoreboard = GLabel(f'Your Score: {self.brick_score}')
        self.scoreboard.font = 'Times new roman-20-Italic'
        self.scoreboard.color = 'navy'
        self.window.add(self.scoreboard, 5, 20)

        # Board of mum_lives
        self.lives_board = GLabel(f'Live(s) Remaining: {self.num_lives}')
        self.lives_board.font = 'Times new roman-20-Italic'
        self.lives_board.color = 'navy'
        self.window.add(self.lives_board, 5, 40)

        # Bonus 嘗試寫 ext 中可以忽略
        # self.bonus = None
        # self.bonus_width = 10
        # self.bonus_height = 10
        # self.bonus_x = 0
        # self.bonus_y = 0

    # Paddle control
    def move_paddle(self, mouse):
        self.paddle.y = self.window.height-self.paddle.height-self.brick_offset
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif self.paddle.width/2 < mouse.x < self.window.width-self.paddle.width/2:
            self.paddle.x = mouse.x-self.paddle.width/2
        else:
            self.paddle.x = self.window.width-self.paddle.width

    # In order to control mouse click
    def starter(self, mouse):
        if self.__click_switch == 0:
            self.__click_switch = 1
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.__dy = INITIAL_Y_SPEED

    # Control ball bouncing when hitting the window
    def window_probe(self):
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    # Control ball bouncing, brick elimination during the game
    def obj_probe(self):
        for i in range(0, 3, 2):
            for j in range(0, 3, 2):
                obj = self.window.get_object_at(self.ball.x + i * self.ball_radius, self.ball.y + j * self.ball_radius)
                if obj is not None and obj is not self.scoreboard and obj is not self.lives_board:
                    if obj == self.paddle:
                        self.__dy = -abs(self.__dy)
                    else:
                        # if random.random() > 0.1: 嘗試寫 ext 中可以忽略
                        #     bonus = GRect(10, 10)
                        #     bonus.filled = True
                        #     bonus.fill_color = 'magenta'
                        #     bonus.color = 'red'
                        #     self.bonus = bonus
                        #     self.bonus_x = obj.x + obj.width / 2 - self.bonus_width / 2
                        #     self.bonus_y = obj.y
                        if self.ball.x < obj.x or self.ball.x + self.ball_radius > obj.x + self.brick.width:
                            self.__dx = -self.__dx
                        if self.ball.y < obj.y or self.ball.y + self.ball_radius > obj.y + self.brick.height:
                            self.__dy = -self.__dy
                        self.window.remove(obj)
                        self.brick_clear += 1
                        for k in range(2, self.brick_rows + 2, 2):  # add different scores according to brick position
                            if self.brick_offset <= obj.y < self.brick_offset + k * \
                                    (self.brick_height + self.brick_spacing):
                                self.brick_score += (self.brick_rows - k + 2) * 10
                        self.scoreboard.text = f'Your Score: {self.brick_score}'

        # below is my previous code for obj_probe, which is shorten by for loop!!!!!!
        # (以下是原始內容，已被上方 code 精簡，只是留作紀錄)
        # obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        # obj_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        # obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        # obj_4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius)
        # if obj_1 is not None and obj_1 is not self.scoreboard:
        #     if obj_1 == self.paddle:
        #         self.__dy = -abs(self.__dy)
        #     else:
        #         self.__dy = -self.__dy
        #         self.window.remove(obj_1)
        #         self.brick_clear += 1
        #         self.scoreboard.text = f'Your Score: {self.brick_clear}'
        # elif obj_2 is not None and obj_2 is not self.scoreboard:
        #     if obj_2 == self.paddle:
        #         self.__dy = -abs(self.__dy)
        #     else:
        #         self.__dy = -self.__dy
        #         self.window.remove(obj_2)
        #         self.brick_clear += 1
        #         self.scoreboard.text = f'Your Score: {self.brick_clear}'
        # elif obj_3 is not None and obj_3 is not self.scoreboard:
        #     if obj_3 == self.paddle:
        #         self.__dy = -self.__dy
        #     else:
        #         self.__dy = -self.__dy
        #         self.window.remove(obj_3)
        #         self.brick_clear += 1
        #         self.scoreboard.text = f'Your Score: {self.brick_clear}'
        # elif obj_4 is not None and obj_4 is not self.scoreboard:
        #     if obj_4 == self.paddle:
        #         self.__dy = -abs(self.__dy)
        #     else:
        #         self.__dy = -self.__dy
        #         self.window.remove(obj_4)
        #         self.brick_clear += 1
        #         self.scoreboard.text = f'Your Score: {self.brick_clear}'

    # Getter for ball velocity_x
    def get_vel_x(self):
        return self.__dx

    # Getter for ball velocity_y
    def get_vel_y(self):
        return self.__dy

    # Setter to reset mouse detection into sensitive mode; also reset ball position
    def switch_setter(self, on):
        self.__click_switch = on
        self.ball.x = (self.window.width - 2 * self.ball_radius)/2
        self.ball.y = (self.window.height - 2 * self.ball_radius)/2

    # Setter for ball velocity_x (reset to zero)
    def reset_vel_x(self):
        self.__dx = 0

    # Setter for ball velocity_y (reset to zero)
    def reset_vel_y(self):
        self.__dy = 0

    # Check whether the player has won the game
    def win_check(self):
        if self.brick_clear == self.brick_nums:
            self.__dx = 0
            self.__dy = 0
            win = GLabel('You Win!!!')
            win.font = 'Courier-60-Bold'
            win.color = 'gold'
            self.window.add(win, x=(self.window.width - win.width)/2, y=(self.window.height + win.height)/2)
            return True

    # Loser label
    def you_lose(self):
        lose = GLabel('You Lose!!!')
        lose.font = 'Courier-60-Bold'
        lose.color = 'purple'
        self.window.add(lose, x=(self.window.width - lose.width) / 2, y=(self.window.height + lose.height) / 2)

    def ball_accelerator(self, times):
        self.__dy = times * self.__dy
        self.__dx = times * self.__dx

    # Setter for number of lives
    def num_lives_setter(self, lives):
        self.num_lives = lives
        self.lives_board.text = f'Live(s) Remaining: {self.num_lives}'
