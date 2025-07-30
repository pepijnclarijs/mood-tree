from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongApp(App):
    score = NumericProperty(0)

    def build(self):
        game = PongGame()
        game.serve_ball(vel=(randint(-6, 6), 0))
        game.serve_square(vel=(randint(-6, 6), 0))
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

class PongGame(Widget):
    ball = ObjectProperty(None) # This is an instance of the ball class. It is defined in the .kv file
    square = ObjectProperty(None) # This is the square object
    player1 = ObjectProperty(None) # This is the PongPadle object
    player2 = ObjectProperty(None) # This is the PongPadle object

    def serve_ball(self, vel):
        self.ball.center = self.center
        self.ball.velocity = vel

    def serve_square(self, vel):
        self.square.center = self.center
        self.square.velocity = vel

    def bounce_off_walls(self, obj):
        if obj.y < 0 or obj.top > self.height:
            obj.velocity_y *= -1
        if obj.x < 0 or obj.right > self.width:
            obj.velocity_x *= -1

    def check_goal(self, obj, serve_function):
        if obj.x < self.x:
            self.player2.score += 1
            serve_function(vel=(4,0))
        if obj.right > self.width:
            self.player1.score += 1
            serve_function(vel=(-4,0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def update(self, dbt):
        # Handle movement
        self.ball.move()
        self.square.move()
        self.bounce_off_walls(self.ball)
        self.bounce_off_walls(self.square)
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        self.player1.bounce_square(self.square)
        self.player2.bounce_square(self.square)

        # Handle points
        self.check_goal(self.ball, self.serve_ball)
        self.check_goal(self.square, self.serve_square)

class PongPaddle(Widget):
    """This class is instantiated by referencing it in the kv file."""
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
    
    def bounce_square(self, square):
        if self.collide_widget(square):
            vx, vy = square.velocity
            offset = (square.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            square.velocity = vel.x, vel.y + offset

class PongBall(Widget):
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Square(Widget):
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


if __name__ == '__main__':
    PongApp().run()