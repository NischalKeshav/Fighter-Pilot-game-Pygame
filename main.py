import pygame
import time
import random

pygame.init()  #initialize pygame

background_colour = (0, 0, 0)

# Define the dimensions of
# screen object(width,height)

ScreenHeight = 600
ScreenWidth = 600
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

# Set the caption of the screen
pygame.display.set_caption('Fighter Pilot game')

# Fill the background colour to the screen
Screen.fill(background_colour)

# Update the display using flip
pygame.display.update()

# Variable to keep our game loop running
running = True

EnemyList = []


class Bomber:
    def __init__(self, x, y, width, height, list=EnemyList, pygame=pygame):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pygame.draw.rect(Screen, (0, 255, 255),
                         (self.x, self.y, self.width, self.height))

        angleList = [1, 2, 3]
        self.xMove = random.choice(angleList)
        self.yMove = random.choice(angleList)

        list.append(self)

    def move(self):
        global ScreenHeight
        global ScreenWidth
        self.x += self.xMove
        self.y += self.yMove
        pygame.draw.rect(Screen, (0, 255, 255),
                         (self.x, self.y, self.width, self.height))
        if (0 < self.x < ScreenWidth - self.width) == False:
            self.xMove = self.xMove * -1
        if (0 < self.y < ScreenHeight - self.height) == False:
            if self.y > ScreenHeight - self.height and self.yMove < 0:
                pass
            else:
                self.yMove = self.yMove * -1


class Player:
  def load(self):
      pygame.draw.rect(Screen, (255, 0, 255),(self.x, self.y, self.width, self.height))
  def __init__(self):
    self.x = 300
    self.y = 300
    self.width = 40
    self.height = 40
    self.load()
  def MouseClickResponse(self,event):
    if event.pos[0]-self.x in range(-30,30) and event.pos[1]-self.y in range(-30,30):
          if event.pos[0] - self.x in range(-30,30):
              self.x = event.pos[0]
          if event.pos[1] - self.y in range(-30,30):
              self.y = event.pos[1]





Bomber1 = Bomber(20, 20, 40, 40)
Bomber2 = Bomber(560, 20, 30, 70)
Bomber3 = Bomber(20, 560, 60, 35)
Bomber4 = Bomber(550, 540, 30, 50)
Player = Player()

count = 0
MouseDown = False
# game loop
while running:
    count += 1

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Player.MouseClickResponse(event)
            MouseDown = True
        elif event.type == pygame.MOUSEMOTION and MouseDown:
            Player.MouseClickResponse(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            MouseDown = False



    Screen.fill(background_colour)
    Player.load()
    for obj in EnemyList:
        obj.move()
        if count % 500 == 0 and obj.xMove < 10:
            obj.xMove *= 1.25
    pygame.display.update()
    time.sleep(0.01)
