from board import Board
from player import Player

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

player1 = Player(board, True)
player2 = Player(board, False)


whites_turn = True
selected = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    player = player1 if whites_turn else player2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and selected == False:
            x, y = pygame.mouse.get_pos()
            selected_sprite = player.select_piece(all_sprites_list, x,y, whites_turn)  
            if selected_sprite is not None:
                selected = True
        elif event.type == pygame.MOUSEBUTTONDOWN and selected == True:
            x, y = pygame.mouse.get_pos()
            selected_second_sprite = player.select_second_piece(all_sprites_list, x,y)
            if selected_sprite == selected_second_sprite: # player wants to select another piece to move/capture with
                selected = False
            elif selected_second_sprite is not None: # if not clicked 'outside' board
                if selected_sprite.move_allowed(selected_second_sprite.x, selected_second_sprite.y): # move allowed (need to check more conditions)
                    if selected_second_sprite.white == None: # moving to an empty space
                        player.move_piece(board, selected_sprite, selected_second_sprite) 
                    elif selected_second_sprite.white == (not whites_turn): # capturing
                        player.capture(board, selected_sprite, selected_second_sprite, all_sprites_list)
                    elif selected_second_sprite.white == whites_turn:
                        continue
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




