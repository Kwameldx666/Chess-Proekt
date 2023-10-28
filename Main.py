from Board import DisplayBoard
from MiniMax import minimax
from Evaluation import Evalualtion
import chess
import pygame as py
from Random import complex_random_move
from greedy import  greedy_algorithm
import MCTS
from PionPioneer import get_best_move
# from Random import random_bot_move
# Общие переменные
MAX, MIN = 100000, -100000
depth = 4

board = chess.Board()
display = DisplayBoard(board)

# Эту функцию можно запустить в любое время и она полностью перезагрузит игру.
def Menu():

    display.opponent_menu()


def setup_game():
    board.reset_board()
    display.game_mode_menu()
    # display.main_menuAI()
    display.update(board)
    run()

def move():

    player_possible_move = display.square_select(py.mouse.get_pos())
    if player_possible_move != None:
        try:
            eval = Evalualtion(board, display.player_color)
            is_late_game = eval.is_late_game()

            if display.opponent_choice == "Bot 1":
                if display.player_color == "W":
                    makeMoveWhite(player_possible_move, is_late_game)
                    makeMoveBlack(player_possible_move, is_late_game)
                else:
                    makeMoveBlack(player_possible_move, is_late_game)
                    makeMoveWhite(player_possible_move, is_late_game)
            if display.opponent_choice == "Bot 2":
                if display.player_color == "W":
                    makeMoveWhiteNegamax(player_possible_move,)
                    makeMoveBlack_n(player_possible_move)
                else:
                    makeMoveBlack_n(player_possible_move)
                    makeMoveWhiteNegamax(player_possible_move)
            if display.opponent_choice == "Bot 3":
                if display.player_color == "W":
                    makeMoveWhiterandom(player_possible_move)
                    makeMoveBlackRandom(player_possible_move)
                else:
                    makeMoveBlackRandom(player_possible_move)
                    makeMoveWhiterandom(player_possible_move)
            if display.opponent_choice == "Bot 4":
                if display.player_color == "W":
                    makeMoveWhiteMCS(player_possible_move)
                    makeMoveBlackMCS(player_possible_move)
                else:
                    makeMoveBlackMCS(player_possible_move)
                    makeMoveWhiteMCS(player_possible_move)
            if display.opponent_choice == "Bot 5":
                if display.player_color == "W":
                    makeMoveWhiteRANDOM(player_possible_move)
                    makeMoveBlackRANDOM(player_possible_move)
                else:
                    makeMoveBlackRANDOM(player_possible_move)
                    makeMoveWhiteRANDOM(player_possible_move)
            if display.opponent_choice == "Bot 6":
                if display.player_color == "W":
                    makeMoveWhiterandom(player_possible_move)
                    display.player_color = "W"
                    makeMoveWhiterandom(player_possible_move)
                else:
                    makeMoveBlackMCS(player_possible_move)
                    display.player_color = "B"
                    makeMoveBlackMCS(player_possible_move)



        except: pass



def Pvp(move) :
    board.push_uci(move)
    display.update(board)



def makeMoveBlack(move, is_late_game):#minimax
    if display.player_color == "B":
        board.push_uci(move)
        print("BOT 1")
    else:
        # The depth attribute has to be odd
        if is_late_game:
            white = minimax(depth + 1, True, MIN, MAX, board, True)
        else:
            white = minimax(depth + 1, True, MIN, MAX, board, True)

        board.push(white)

    display.update(board)
def makeMoveWhite(move, is_late_game):#minimax
    if display.player_color == "W":
        board.push_uci(move)
        print("BOT 1")
    else:
        # The depth attribute has to be odd
        if is_late_game:
            white = minimax(depth + 1, True, MIN, MAX, board, True)
        else:
            white = minimax(depth + 1, True, MIN, MAX, board, True)

        board.push(white)

    display.update(board)
def   makeMoveWhiteNegamax(move):
    global board
    legal_moves_list = list(board.legal_moves)
    if display.player_color == "B" and len(legal_moves_list) == 0:
        white_move = greedy_algorithm(board, "W")
        print("Ход бота  :", white_move)
        if white_move:
            board.push(white_move)
    elif display.player_color == "W":  # If the player is white
        board.push_uci(move)  # Apply the player's move
        print("Ход игрока:", move)
    else:  # If the player is black and it's not the first move
        white_move = greedy_algorithm(board, "W")
        print("Ход бота  :", white_move)
        if white_move:
            board.push(white_move)

    display.update(board)  # Update the board




# If the board is in its initial state and the player chose black, let the bot make the first move.


def makeMoveBlack_n(move):  # Adding a new parameter for the first move

    global board

    # If the board is in its initial state and the player chose white, let the bot make the first move.
    legal_moves=list(board.legal_moves)
    if display.player_color == "W" and len(legal_moves) == 0:
        black_move = greedy_algorithm(board, "B")
        print("Ход бота  :", black_move)
        if black_move:
            board.push(black_move)
    elif display.player_color == "B":  # If the player is black
        board.push_uci(move)  # Apply the player's move
        print("Ход игрока:", move)
    else:  # If the player is white and it's not the first move
        black_move = greedy_algorithm(board, "B")
        print("Ход бота  :", black_move)
        if black_move:
            board.push(black_move)

    display.update(board)  # Update the board


def makeMoveWhiteMCS(move):
    global board
    mcts = MCTS.ChessMCTS()

    # Если игрок выбрал белые фигуры
    if display.player_color == "W":
        board.push_uci(move)  # Применяем ход игрока
        print("Ход игрока:", move)
    else:  # Если игрок выбрал черные фигуры, то белые делает ход бот
        best_move = mcts.MCTS_1(board)
        best_move_uci = board.uci(best_move)
        print("Ход бота  :", best_move_uci)
        if best_move:
            board.push(best_move)

    display.update(board)  # Обновляем доску


def makeMoveBlackMCS(move):
    global board
    mcts = MCTS.ChessMCTS()  #

    # Если игрок выбрал черные фигуры
    if display.player_color == "B":
        if move:  # Если игрок сделал ход
            board.push_uci(move)
            print("Ход игрока:", move)
        else:  # Если игрок не сделал ход (не уверен, может ли это случиться, но пусть будет проверка)
            print("Ошибка: Ход игрока отсутствует!")
    else:  # Если игрок выбрал белые фигуры, то черные делает ход бот
        best_move = mcts.MCTS_1(board)
        best_move_uci = board.uci(best_move)
        print("Ход бота  :", best_move_uci)

        if best_move in board.legal_moves:
            board.push(best_move)
        else:
            print("Ошибка: Ход не допустим!")

    display.update(board)  # Обновляем доску
def makeMoveWhiteRANDOM(move):
    global board
    legal_moves_list = list(board.legal_moves)
    if display.player_color == "B" and len(legal_moves_list) == 0:
        white_move = complex_random_move(board)
        print("Ход бота  :", white_move)
        if white_move:
            board.push(white_move)
    elif display.player_color == "W":  # If the player is white
        board.push_uci(move)  # Apply the player's move
        print("Ход игрока:", move)
    else:  # If the player is black and it's not the first move
        white_move = complex_random_move(board)
        print("Ход бота  :", white_move)
        if white_move:
            board.push(white_move)

    display.update(board)  # Update the board
def makeMoveBlackRANDOM(move):
        global board

        # If the board is in its initial state and the player chose white, let the bot make the first move.
        legal_moves = list(board.legal_moves)
        if display.player_color == "B" and len(legal_moves) == 0:
            black_move = complex_random_move(board)
            print("Ход бота  :", black_move)
            if black_move:
                board.push(black_move)
        elif display.player_color == "B":  # If the player is black
            board.push_uci(move)  # Apply the player's move
            print("Ход игрока:", move)
        else:  # If the player is white and it's not the first move
            black_move = complex_random_move(board)
            print("Ход бота  :", black_move)
            if black_move:
                board.push(black_move)

        display.update(board)  # Update the board

def makeMoveWhiterandom(move):
    global board
    legal_moves_list = list(board.legal_moves)
    if display.player_color == "B" and len(legal_moves_list) == 0:
        white_move = get_best_move(board)
        print("Ход бота  :", white_move)
        if white_move:
            board.push(white_move)
    elif display.player_color == "W":  # If the player is white
        board.push_uci(move)  # Apply the player's move
        print("Ход игрока:", move)
    else:  # If the player is black and it's not the first move
        white_move = get_best_move(board)
        print("Ход бота  :", white_move)
        if white_move:
            board.push(white_move)

    display.update(board)  # Update the board

def makeMoveBlackRandom(move):
    global board

    # If the board is in its initial state and the player chose white, let the bot make the first move.
    legal_moves = list(board.legal_moves)
    if display.player_color == "B" and len(legal_moves) == 0:
        black_move = get_best_move(board)
        print("Ход бота  :", black_move)
        if black_move:
            board.push(black_move)
    elif display.player_color == "B":  # If the player is black
        board.push_uci(move)  # Apply the player's move
        print("Ход игрока:", move)
    else:  # If the player is white and it's not the first move
        black_move = get_best_move(board)
        print("Ход бота  :", black_move)
        if black_move:
            board.push(black_move)

    display.update(board)  # Update the board

def is_game_over(board):#minimax
    if board.is_game_over():
        display.run = False
        display.game_over = True
        display.game_over_menu()

def is_game_over(board):#minimax
    if board.is_game_over():
        display.run = False
        display.game_over = True
        display.game_over_menu()

def run():#minimax
    if display.opponent_choice == "Bot 1":
        if display.player_color == "B":
            makeMoveWhite(None, False)
    if display.opponent_choice == "Bot 2":
        if display.player_color == "B":
            makeMoveWhiteNegamax(None)
    if display.opponent_choice == "Bot 3":
        if display.player_color == "B":
            makeMoveWhiterandom(None)
    if display.opponent_choice == "Bot 4":
        if display.player_color == "B":
            makeMoveWhiteMCS(None)
    if display.opponent_choice == "Bot 5":
        if display.player_color == "B":
            makeMoveWhiteRANDOM(None)



    while display.run:
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT:
                exit()
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1 :
            move()
        elif event.type == py.MOUSEBUTTONDOWN and event.button == 3 :
            display.remove_square_select()

        display.update_screen()
        is_game_over(board)

while run:
    setup_game()

py.quit()


