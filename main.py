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
                    #print(sprite.x)
                    #print(sprite.y)
                    #print(type(sprite))
                    return sprite
                else:
                    print('not your turn')

def select_second_piece(x,y):
    for sprite in all_sprites_list:
        if x >= sprite.rect.x and x <= (sprite.rect.x + sprite.rect.width):
            if y >= sprite.rect.y and y <= (sprite.rect.y + sprite.rect.height):
                """ print('hit')
                print(sprite.x)
                print(sprite.y) """
                #print(type(sprite))
                return sprite

def move_piece(sprite1, sprite2):
    #board.print_display()
    board.change_pieces(sprite1, sprite2)
    #board.print_display()
    # changing logical position
    sprite1.x, sprite2.x = sprite2.x, sprite1.x
    sprite1.y, sprite2.y = sprite2.y, sprite1.y
    # changing drawing position
    sprite1.rect.x, sprite2.rect.x = sprite2.rect.x, sprite1.rect.x
    sprite1.rect.y, sprite2.rect.y = sprite2.rect.y, sprite1.rect.y
    print('changed')

def capture(sprite1, sprite2, sprites_list):
    board.create_new_empty(sprite1.x, sprite1.y, sprite1.rect.x, sprite1.rect.y, sprites_list)
    sprite1.rect.x = sprite2.rect.x
    sprite1.rect.y = sprite2.rect.y
    sprite1.x = sprite2.x
    sprite1.y = sprite2.y
    sprite2.kill()

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
            selected_second_sprite = select_second_piece(x,y)
            if selected_sprite == selected_second_sprite: # player wants to select another piece to move/capture with
                selected = False
            elif selected_second_sprite is not None: # if not clicked 'outside' board
                if selected_sprite.move_allowed(selected_second_sprite.x, selected_second_sprite.y): # move allowed (need to check more conditions)
                    if selected_second_sprite.white == None: # moving to an empty space
                        move_piece(selected_sprite, selected_second_sprite) 
                    elif selected_second_sprite.white == (not whites_turn): # capturing
                        capture(selected_sprite, selected_second_sprite, all_sprites_list)
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




