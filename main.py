from player import Player
from pieces.bishop import Bishop
from board import Board

# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((564,592)) # 25,25 -> 545,545
# cada quadrado tem 65 px, 
clock = pygame.time.Clock()
running = True

board_img = pygame.image.load('assets\Board -  Named.png')
board = Board()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
all_sprites_list = pygame.sprite.Group() 

board.allocate_sprites(all_sprites_list)

def select_piece(x,y, white_moves):
    for sprite in all_sprites_list:
        if x >= sprite.rect.x and x <= (sprite.rect.x + sprite.rect.width):
            if y >= sprite.rect.y and y <= (sprite.rect.y + sprite.rect.height):
                if sprite.white == white_moves:
                    #print('hit')
                    print(sprite.x)
                    print(sprite.y)
                    return sprite
                else:
                    print('not your turn')

def select_second_piece(x,y, white_moves):
    for sprite in all_sprites_list:
        if x >= sprite.rect.x and x <= (sprite.rect.x + sprite.rect.width):
            if y >= sprite.rect.y and y <= (sprite.rect.y + sprite.rect.height):
                if sprite.white != (not white_moves):
                    """ print('hit')
                    print(sprite.x)
                    print(sprite.y) """
                    return sprite
                else:
                    print('not your turn')

def change_positions(sprite1, sprite2):
    # changing logical position
    sprite1.x, sprite2.x = sprite2.x, sprite1.x
    sprite1.y, sprite2.y = sprite2.y, sprite1.y
    # changing drawing position
    sprite1.rect.x, sprite2.rect.x = sprite2.rect.x, sprite1.rect.x
    sprite1.rect.y, sprite2.rect.y = sprite2.rect.y, sprite1.rect.y
    print('changed')


whites_turn = True
selected = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and selected == False:
            x, y = pygame.mouse.get_pos()
            selected_sprite = select_piece(x,y, whites_turn)  
            if selected_sprite is not None:
                selected = True
        elif event.type == pygame.MOUSEBUTTONDOWN and selected == True:
            x, y = pygame.mouse.get_pos()
            selected_second_sprite = select_second_piece(x,y, whites_turn)
            if selected_second_sprite is not None:
                move_allowed = selected_sprite.move_allowed(selected_second_sprite.x, selected_second_sprite.y)
                if move_allowed:
                    change_positions(selected_sprite, selected_second_sprite) 
                    selected = False
                    whites_turn = not whites_turn
        

    screen.blit(board_img, (0,0))

    all_sprites_list.update() 
    all_sprites_list.draw(screen) 


    #x, y = pygame.mouse.get_pos()
    #print(x,y)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()




