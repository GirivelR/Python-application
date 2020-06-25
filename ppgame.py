from kivy.app import App
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PingpongPaddle(Widget):
    s=NumericProperty(0)
    def bounce_ball(self,ball):
        if self.collide_widget(ball):
            ball.vel_x *= -1.1
class PingpongBall(Widget):
    vel_x=NumericProperty(0)
    vel_y=NumericProperty(0)
    vel=ReferenceListProperty(vel_x,vel_y)
    def move(self): #latest position = current velocity + current position
        self.pos=Vector(*self.vel) + self.pos

class PingpongGame(Widget):
    ball=ObjectProperty(None)
    p1=ObjectProperty(None)
    p2=ObjectProperty(None)
    def serve_ball(self):
        self.ball.vel=Vector(4,0).rotate(randint(0,360))
    def update(self,a):
        self.ball.move()
        if self.ball.x<0:
            self.ball.vel_x*=-1
            self.p2.s+=1
        if self.ball.x>self.width -50:
            self.ball.vel_x *= -1
            self.p1.s += 1
        if self.ball.y<0 or self.ball.y>self.height -50:
            self.ball.vel_y*=-1
        self.p1.bounce_ball(self.ball)
        self.p2.bounce_ball(self.ball)
    def on_touch_move(self, touch):
        if touch.x<self.width/ 1/4:
            self.p1.center_y = touch.y
        if touch.x>self.width* 3/4:
            self.p2.center_y = touch.y

class PingpongApp(App):
    def build(self):
        pgame=PingpongGame()
        pgame.serve_ball()
        Clock.schedule_interval(pgame.update,1.0/60.0)
        return pgame
PingpongApp().run()
