"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This programme runs the Breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    num_lives = NUM_LIVES
    bricks_count = graphics.get_bricks_count()
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        # when paddle fails to rebound the ball before it dropping out of the bottom of window
        # player loses 1 life and the ball is reset
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.set_ball()
            num_lives -= 1
        # game over - lose
        if num_lives == 0:
            break
        # game over - win
        if bricks_count == 0:
            graphics.set_ball()
            break

        # 4 detecting points of the ball
        ball_top_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        ball_top_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        ball_bottom_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        ball_bottom_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                          graphics.ball.y + graphics.ball.height)

        if ball_top_left is not None:
            # reset location of ball to prevent ball fails to bounce back
            if graphics.ball.y >= graphics.paddle.y - graphics.ball.height:
                graphics.set_ball_y()
            graphics.set_dy()
            # remove bricks only and count the bricks left
            if ball_top_left.y < graphics.paddle.y:
                graphics.window.remove(ball_top_left)
                bricks_count -= 1
        elif ball_top_right is not None:
            # reset location of ball to prevent ball fails to bounce back
            if graphics.ball.y >= graphics.paddle.y - graphics.ball.height:
                graphics.set_ball_y()
            graphics.set_dy()
            # remove bricks only and count the bricks left
            if ball_top_right.y < graphics.paddle.y:
                graphics.window.remove(ball_top_right)
                bricks_count -= 1
        elif ball_bottom_left is not None:
            # reset location of ball to prevent ball fails to bounce back
            if graphics.ball.y >= graphics.paddle.y - graphics.ball.height:
                graphics.set_ball_y()
            graphics.set_dy()
            # remove bricks only and count the bricks left
            if ball_bottom_left.y < graphics.paddle.y:
                graphics.window.remove(ball_bottom_left)
                bricks_count -= 1
        elif ball_bottom_right is not None:
            # reset location of ball to prevent ball fails to bounce back
            if graphics.ball.y >= graphics.paddle.y - graphics.ball.height:
                graphics.set_ball_y()
            graphics.set_dy()
            # remove bricks only and count the bricks left
            if ball_bottom_right.y < graphics.paddle.y:
                graphics.window.remove(ball_bottom_right)
                bricks_count -= 1

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
