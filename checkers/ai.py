from copy import deepcopy
import pygame


RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
   
    # Base case for the recursion: if depth is 0 or a winner is found
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position
    
    # If it's the maximizing player's (AI's) turn
    if max_player:
        maxEval = float('-inf')  # Start with the lowest possible score
        best_move = None
        # Iterate through all possible moves the AI can make
        for move in get_all_moves(position, WHITE, game):
            # Recursively call minimax for the opponent's turn (minimizing player)
            evaluation = minimax(move, depth - 1, False, game)[0]
            # If the new evaluation is better, update the max score and best move
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
        
        return maxEval, best_move
    
    # If it's the minimizing player's (human) turn
    else:
        minEval = float('inf')  # Start with the highest possible score
        best_move = None
        # Iterate through all possible moves the human player can make
        for move in get_all_moves(position, RED, game):
            # Recursively call minimax for the AI's turn (maximizing player)
            evaluation = minimax(move, depth - 1, True, game)[0]
            # If the new evaluation is worse for the AI, update the min score
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
        
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    """
    Simulates a move on a temporary board.
    - piece: The piece to move.
    - move: The (row, col) tuple where the piece is moving to.
    - board: The board object to perform the move on.
    - game: The main game object.
    - skip: A list of pieces that were captured during the move.
    """
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
   
    moves = []

  
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
    
        for move, skip in valid_moves.items():
            
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
           
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves