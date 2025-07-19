import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE,WHITE
from checkers.game import Game
from checkers.ai import minimax 

# Set up the display
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# The main game loop function
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

  

    while run:
        clock.tick(FPS)

        # --- AI's Turn ---
       
        if game.turn == WHITE:
        
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
           
            game.ai_move(new_board)

        
      
     
        # After every turn, check if someone has won.
        if game.winner() is not None:
            
          
            
          
            if game.winner() == WHITE:
                winner_text = "WHITE WINS!"
            else:
                winner_text = "RED WINS!"
            
        
            font = pygame.font.SysFont("comicsans", 80)
            
           
            text_surface = font.render(winner_text, 1, (255, 255, 255)) 
            
         
            WIN.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, HEIGHT/2 - text_surface.get_height()/2))
            
          
            pygame.display.update()
            
            
            pygame.time.delay(5000)
            
            
            break

       
      
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

          
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

      
        game.update()
   
    
    pygame.quit()


if __name__ == '__main__':
    main()