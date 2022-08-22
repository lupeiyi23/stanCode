"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program builds the world for Breakout,
setting the required objects & elements.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
MAX_SPEED_STAGE1 = 8   # Maximum speed of the ball for stage 1
MAX_SPEED_STAGE2 = 11  # Maximum speed of the ball for stage 2
MAX_SPEED_STAGE3 = 15  # Maximum speed of the ball for stage 3
ACCELERATION = 0.1     # Acceleration speed for each move of the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'slategray'
        self.paddle.fill_color = 'slategray'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=self.window.height-paddle_offset-self.paddle.height)
        self.paddle_offset = paddle_offset

        # Prepare a scoreboard
        self.scoreboard = GLabel('')

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'darkslateblue'
        self.ball.fill_color = 'darkslateblue'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Prepare an additional ball for the ending animations
        self.another_ball = GOval(ball_radius*2, ball_radius*2)
        self.another_ball.filled = True
        self.another_ball.color = 'snow'
        self.another_ball.fill_color = 'snow'

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # The switch to indicate the ball is on move or not
        self.ball_on_move = False

        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.bricks_count = brick_rows * brick_cols
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                # colorize the bricks
                brick_color_control = i / self.brick_rows
                if brick_color_control < 0.1:
                    brick.color = 'rosybrown'
                    brick.fill_color = 'rosybrown'
                elif brick_color_control < 0.2:
                    brick.color = 'indianred'
                    brick.fill_color = 'indianred'
                elif brick_color_control < 0.3:
                    brick.color = 'brown'
                    brick.fill_color = 'brown'
                elif brick_color_control < 0.4:
                    brick.color = 'firebrick'
                    brick.fill_color = 'firebrick'
                elif brick_color_control < 0.5:
                    brick.color = 'sienna'
                    brick.fill_color = 'sienna'
                elif brick_color_control < 0.6:
                    brick.color = 'peru'
                    brick.fill_color = 'peru'
                elif brick_color_control < 0.7:
                    brick.color = 'goldenrod'
                    brick.fill_color = 'goldenrod'
                elif brick_color_control < 0.8:
                    brick.color = 'darkkhaki'
                    brick.fill_color = 'darkkhaki'
                elif brick_color_control < 0.9:
                    brick.color = 'lightsteelblue'
                    brick.fill_color = 'lightsteelblue'
                else:
                    brick.color = 'thistle'
                    brick.fill_color = 'thistle'
                self.window.add(brick, x=(brick.width+brick_spacing)*j, y=brick_offset+(brick_height+brick_spacing)*i)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def get_ball_on_move(self):
        return self.ball_on_move

    def set_ball_on_move(self):
        if self.ball_on_move:
            self.ball_on_move = False
        else:
            self.ball_on_move = True

    # reset ball to the starting point
    def set_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0

    def paddle_move(self, event):
        if event.x - self.paddle.width/2 <= 0:
            self.window.add(self.paddle, x=0,
                            y=self.window.height - self.paddle_offset - self.paddle.height)
        elif event.x + self.paddle.width/2 >= self.window.width:
            self.window.add(self.paddle, x=self.window.width - self.paddle.width,
                            y=self.window.height - self.paddle_offset - self.paddle.height)
        else:
            self.window.add(self.paddle, x=event.x - self.paddle.width / 2,
                            y=self.window.height-self.paddle_offset-self.paddle.height)

    def ball_move(self, event):
        # only trigger the function when ball is not on move
        if not self.ball_on_move:
            self.ball_on_move = True
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def accelerate(self):
        # stage 1
        if self.bricks_count > BRICK_ROWS*BRICK_COLS/2:
            if -MAX_SPEED_STAGE1 < self.__dx < MAX_SPEED_STAGE1:
                if self.__dx > 0:
                    self.__dx += ACCELERATION
                else:
                    self.__dx -= ACCELERATION
            if -MAX_SPEED_STAGE1 < self.__dy < MAX_SPEED_STAGE1:
                if self.__dy > 0:
                    self.__dy += ACCELERATION
                else:
                    self.__dy -= ACCELERATION
        # stage 2
        elif self.bricks_count > BRICK_ROWS*BRICK_COLS/4:
            if -MAX_SPEED_STAGE2 < self.__dx < MAX_SPEED_STAGE2:
                if self.__dx > 0:
                    self.__dx += ACCELERATION
                else:
                    self.__dx -= ACCELERATION
            if -MAX_SPEED_STAGE2 < self.__dy < MAX_SPEED_STAGE2:
                if self.__dy > 0:
                    self.__dy += ACCELERATION
                else:
                    self.__dy -= ACCELERATION
        # stage 3
        else:
            if -MAX_SPEED_STAGE3 < self.__dx < MAX_SPEED_STAGE3:
                if self.__dx > 0:
                    self.__dx += ACCELERATION
                else:
                    self.__dx -= ACCELERATION
            if -MAX_SPEED_STAGE3 < self.__dy < MAX_SPEED_STAGE3:
                if self.__dy > 0:
                    self.__dy += ACCELERATION
                else:
                    self.__dy -= ACCELERATION

    def get_bricks_count(self):
        return self.bricks_count

    def bad_ending(self):
        bg = GRect(self.window.width, self.window.height)
        bg.filled = True
        bg.color = 'darkred'
        bg.fill_color = 'darkred'
        self.window.add(bg)
        ment = GLabel('GAME OVER')
        ment.font = 'Courier-81-bold-italic'
        ment.color = 'snow'
        self.window.add(ment, x=0, y=self.window.height/2)
        self.paddle.color = 'snow'
        self.paddle.fill_color = 'snow'
        self.ball.color = 'snow'
        self.ball.fill_color = 'snow'
        self.window.add(self.ball)
        self.window.add(self.another_ball)
        self.__dx = MAX_SPEED_STAGE1 ** 2
        self.__dy = MAX_SPEED_STAGE1 ** 2

    def happy_ending(self):
        bg = GRect(self.window.width, self.window.height)
        bg.filled = True
        bg.color = 'thistle'
        bg.fill_color = 'thistle'
        self.window.add(bg)
        ment = GLabel('YOU ROCK!')
        ment.font = 'Courier-81-bold-italic'
        ment.color = 'snow'
        self.window.add(ment, x=0, y=self.window.height/2)
        self.paddle.color = 'snow'
        self.paddle.fill_color = 'snow'
        self.ball.color = 'snow'
        self.ball.fill_color = 'snow'
        self.window.add(self.ball)
        self.window.add(self.another_ball)
        self.__dx = MAX_SPEED_STAGE1 ** 2
        self.__dy = MAX_SPEED_STAGE1 ** 2

    def set_scoreboard(self, num_lives):
        s = ''
        for i in range(num_lives):
            s += chr(10084)

        if self.window.get_object_at(BRICK_SPACING, BRICK_OFFSET-BRICK_SPACING) is not None:
            self.window.remove(self.window.get_object_at(BRICK_SPACING, BRICK_OFFSET-BRICK_SPACING))
        self.scoreboard = GLabel(s)
        self.scoreboard.font = '-40'
        self.scoreboard.color = 'darkred'
        self.window.add(self.scoreboard, x=BRICK_SPACING, y=BRICK_OFFSET-BRICK_SPACING)

    # process all bouncing and removing bricks when the ball hits
    def game_in_progress(self):
        # 4 detecting points of the ball
        ball_top_left = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_top_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        ball_bottom_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        ball_bottom_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # prevent from removing scoreboard
        if self.ball.y > self.scoreboard.y:

            if ball_top_left is not None:
                self.set_dy()
                # prevent ball fails to bounce back
                if self.ball.y >= self.paddle.y - self.ball.height and self.__dy > 0:
                    self.set_dy()
                # remove bricks only and count the bricks left
                if self.scoreboard.y < ball_top_left.y < self.paddle.y:
                    self.window.remove(ball_top_left)
                    self.bricks_count -= 1
            elif ball_top_right is not None:
                self.set_dy()
                # prevent ball fails to bounce back
                if self.ball.y >= self.paddle.y - self.ball.height and self.__dy > 0:
                    self.set_dy()
                # remove bricks only and count the bricks left
                if self.scoreboard.y < ball_top_right.y < self.paddle.y:
                    self.window.remove(ball_top_right)
                    self.bricks_count -= 1
            elif ball_bottom_left is not None:
                self.set_dy()
                # prevent ball fails to bounce back
                if self.ball.y >= self.paddle.y - self.ball.height and self.__dy > 0:
                    self.set_dy()
                # remove bricks only and count the bricks left
                if self.scoreboard.y < ball_bottom_left.y < self.paddle.y:
                    self.window.remove(ball_bottom_left)
                    self.bricks_count -= 1
            elif ball_bottom_right is not None:
                self.set_dy()
                # prevent ball fails to bounce back
                if self.ball.y >= self.paddle.y - self.ball.height and self.__dy > 0:
                    self.set_dy()
                # remove bricks only and count the bricks left
                if self.scoreboard.y < ball_bottom_right.y < self.paddle.y:
                    self.window.remove(ball_bottom_right)
                    self.bricks_count -= 1
