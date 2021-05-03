"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The Breakout Project is a fun game.
Players need to control the paddle in order to bounce the ball.
When the ball hits a brick, the brick will be removed and the player scores.
The score will be given according to bricks' position (higher the bricks, higher the points)
To win the game, players need to remove all bricks. The player will have 3 attempts initially.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts
ACCELERATOR = 1.0001


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    num_lives = NUM_LIVES
    graphics.num_lives_setter(num_lives)
    while num_lives > 0:
        while True:
            dx = graphics.get_vel_x()
            dy = graphics.get_vel_y()
            graphics.ball.move(dx, dy)
            graphics.window_probe()
            graphics.obj_probe()
            # graphics.bonus.move(dy) 嘗試寫 ext 中可以忽略
            if graphics.win_check():
                num_lives = 0
                break
            if graphics.ball.y >= graphics.window.height:
                num_lives -= 1
                graphics.num_lives_setter(num_lives)
                graphics.reset_vel_x()
                graphics.reset_vel_y()
                graphics.switch_setter(0)
                break
            graphics.ball_accelerator(ACCELERATOR)
            pause(FRAME_RATE)
    # if not graphics.win_check():
    graphics.you_lose()


if __name__ == '__main__':
    main()
