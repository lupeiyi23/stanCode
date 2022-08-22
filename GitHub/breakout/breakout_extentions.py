"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This programme runs the Breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extentions import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    num_lives = NUM_LIVES
    # add scoreboard with full lives
    graphics.set_scoreboard(num_lives)
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        ball_on_move = graphics.get_ball_on_move()
        bricks_count = graphics.get_bricks_count()
        graphics.ball.move(dx, dy)
        # only accelerate when ball is already on move
        if ball_on_move:
            graphics.accelerate()
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        # when paddle fails to rebound the ball before it dropping out of the bottom of window
        # player loses 1 life and the ball and scoreboard are reset
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.set_ball()
            num_lives -= 1
            # Switch off
            graphics.set_ball_on_move()
            graphics.set_scoreboard(num_lives)
        # game over - lose
        if num_lives == 0:
            # Switch on to prevent the mouse event affect ending animation of the balls
            graphics.set_ball_on_move()
            break
        # game over - win
        if bricks_count == 0:
            break

        graphics.game_in_progress()

        pause(FRAME_RATE)

    graphics.window.clear()
    # animation for loser: balls moving fast
    if num_lives == 0:
        graphics.bad_ending()
        while True:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            graphics.another_ball.move(-dx, -dy)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx()
            if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.set_dy()
            pause(FRAME_RATE)
    # animation for winner: balls moving flash
    if bricks_count == 0:
        graphics.happy_ending()
        while True:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            graphics.another_ball.move(-dx, -dy)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx()
            if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.set_dy()
            pause(FRAME_RATE ** 2)


if __name__ == '__main__':
    main()
