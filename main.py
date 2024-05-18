from player import Player
from pieces.bishop import Bishop
from board import Board

# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((568,568)) # 25,25 -> 545,545
# cada quadrado tem 65 px, 
clock = pygame.time.Clock()
running = True

board_img = pygame.image.load('./assets/board_plain_05.png')
board = Board()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
all_sprites_list = pygame.sprite.Group() 

for row in range(8):
    for column in range(8):
        if board.display[row][column] != 0:
            board.display[row][column].rect.x = (column+1)*60
            board.display[row][column].rect.y = (row+1)*50
            all_sprites_list.add(board.display[row][column])

def detect_collision(x,y):
    for sprite in all_sprites_list:
        if x >= sprite.rect.x and x <= (sprite.rect.x + sprite.rect.width):
            if y >= sprite.rect.y and y <= (sprite.rect.y + sprite.rect.height):
                if sprite.white == False:
                    print('hit') 
                    return sprite
                else:
                    print('not black')

def change_positions(sprite1, sprite2):
    print('start change')
    tempx = sprite1.rect.x
    tempy = sprite1.rect.y
    sprite1.rect.x = sprite2.rect.x
    sprite1.rect.y = sprite2.rect.y
    sprite2.rect.x = tempx
    sprite2.rect.y = tempy
    print('changed')


player1_turn = True
selected = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and selected == False:
            x, y = pygame.mouse.get_pos()
            selected_sprite = detect_collision(x,y)  
            if selected_sprite is not None:
                selected = True
        elif event.type == pygame.MOUSEBUTTONDOWN and selected == True:
            x, y = pygame.mouse.get_pos()
            selected_second_sprite = detect_collision(x,y)
            if selected_second_sprite is not None:
                change_positions(selected_sprite, selected_second_sprite) 
                selected = False
        elif event.type == pygame.QUIT:
            running = False

    screen.blit(board_img, (0,0))

    all_sprites_list.update() 
    all_sprites_list.draw(screen) 


    x, y = pygame.mouse.get_pos()
    #print(x,y)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()


""" player1 = Player(white=True)
player2 = Player(white=False)

def game_over():
    if player1.king.is_mated():
        return True
    if player2.king.is_mated():
        return True
    return False

turn = 1
while not game_over():
    if turn % 2 != 0:
        player1.move_piece()
    else:
        player2.move_piece()
    turn += 1
 """


