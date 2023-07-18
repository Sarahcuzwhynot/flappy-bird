import random
from pgzhelper import *



WIDTH =640
HEIGHT = 480
TITLE =  'flappy bird '



ground = Actor('ground')
ground.x = 320
ground.y = 465


bird = Actor('bird0')
bird.x = 75
bird.y = 100
bird.images = ['bird0', 'bird1', 'bird2']
bird.fps = 10



gameover = Actor('gameover')
gameover.x = 320
gameover.y = 200
gameover.scale = 3

top_pipe = Actor('top')
bottom_pipe = Actor('bottom')
top_pipe.x = 640
top_pipe.y = -100
gap = 150
bottom_pipe.x = 640
bottom_pipe.y = top_pipe.height + gap




gravity = 0.3
bird.speed = 1
bird.alive = True
scroll_speed = -4
score = 0


def on_mouse_down():
    global score
    if bird.alive:
        bird.speed = -6.5
        sounds.wing.play()
    else:
        bird.alive  = True
        score = 0

def update():
    global score

    bird.animate()
    bird.y = bird.y + bird.speed
    bird.speed = bird.speed + gravity


    if bird.y > HEIGHT - 40 or bird.y < 0:
        bird.alive = False
        sounds.die.play()
    top_pipe.x = top_pipe.x + scroll_speed
    bottom_pipe.x = bottom_pipe.x + scroll_speed


    if top_pipe.x < -50:
        offset = random.uniform(-100, -200)
        top_pipe.midleft = (640, offset)
        bottom_pipe.midleft = (640, offset + top_pipe.height +gap)
        score = score + 1
        sounds.point.play()



    if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
        bird.alive = False
        sounds.hit.play()





def draw():
    screen.blit('background' , (0, 0))

    if bird.alive:
        top_pipe.draw()
        bottom_pipe.draw()
        bird.draw()
        ground.draw()

    else:
        gameover.draw()
        bird.x = 75
        bird.y = 100
        gravity = 0
        bird.speed = 0
        screen.draw.text("click to play this game like how did you die bruh", color ='white', center=(320, 300), shadow=(0.5, 0.5), scolor='black', fontsize=30)
        top_pipe.x = 640
        bottom_pipe.x = 640



    screen.draw.text('Score: ' + str(score), color='white' , midtop=(50, 10), shadow=(0.5, 0.5), scolor='black', fontsize=30)


