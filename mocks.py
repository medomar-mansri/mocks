import pygame, sys, random
import unittest
from unittest.mock import patch, Mock

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y  
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():  
    player.y += player_speed
    if player.top <= 0:
        player.top = 0 
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0 
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

class TestGame(unittest.TestCase):
    @patch('random.choice', return_value=1)
    def test_ball_restart(self, mock_choice):
        global ball_speed_x, ball_speed_y
        ball_speed_x = 5
        ball_speed_y = -5
        ball_restart()
        self.assertEqual(ball_speed_x, 5)
        self.assertEqual(ball_speed_y, 5)

    @patch('pygame.Rect.colliderect', return_value=True)
    def test_ball_animation_collision(self, mock_colliderect):
        global ball_speed_x
        ball_speed_x = 5
        ball_animation()
        self.assertEqual(ball_speed_x, -5)

    @patch('pygame.Rect.colliderect', return_value=False)
    def test_ball_animation_no_collision(self, mock_colliderect):
        global ball_speed_x
        ball_speed_x = 5
        ball_animation()
        self.assertEqual(ball_speed_x, 5)

if __name__ == '__main__':
    pygame.init()
    screen_width = 1200
    screen_height = 750
    screen = pygame.display.set_mode((screen_width, screen_height))
    ball = pygame.Rect(screen_width/2 - 14, screen_height/2 - 14, 28, 28)
    player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
    opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
    ball_speed_x = 7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))
    player_speed = 0
    opponent_speed = 7 

    unittest.main(exit=False)
