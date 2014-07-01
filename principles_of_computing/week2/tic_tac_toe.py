"""
Monte Carlo Tic-Tac-Toe Player
"""

__author__ = 'mamaray'

import random
import ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 1  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move. The function should play a game starting with the
    given player by making random moves, alternating between players. The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.

    :param board: run a trial on this board
    :param player: starting player
    :return: None, board is modified
    """

    curplayer = player
    winner = board.check_win()

    # Run game
    while winner is None:
        # calculate a random move and make it
        row, col = random.choice(board.get_empty_squares())
        # print "row,col", row, col
        # print "player: ", provided.STRMAP[curplayer]
        # Make the random move
        board.move(row, col, curplayer)

        # check if the game continues
        winner = board.check_win()

        # game continues, switch players
        curplayer = provided.switch_player(curplayer)

        # Display board
        # print board
        # print

    return


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, a board
    from a completed game, and which player the machine player is. The function should score the completed board and
    update the scores grid. As the function updates the scores grid directly, it does not return anything,

    :param scores: variable used to track scores between trials
    :param board: final board
    :param player: player whose turn it is
    :return: None, score is passed by reference
    """

    # who won?
    winner = board.check_win()

    # loop through the board and update the score
    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if winner == provided.DRAW:
                scores[row][col] += 0
            elif board.square(row, col) == provided.EMPTY:
                continue
            elif board.square(row, col) == winner:
                scores[row][col] += MCMATCH
            else:
                scores[row][col] -= MCOTHER

    return


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The  should find all of the empty squares with the maximum
    score and randomly return one of them as a (row, column) tuple. It is an error to call this function with a board
    that has no empty squares (there is no possible next move), so your function may do whatever it wants in that case.
    The case where the board is full will not be tested.

    :param board: current board in play
    :param scores: current scores grid
    :return: the next square to play
    """

    # initialize local variables
    max_score = float("-inf")
    move = None

    empty_squares = board.get_empty_squares()

    for row, col in empty_squares:
        print row, col
        if scores[row][col] > max_score:
            max_score = scores[row][col]
            move = (row, col)

    return move


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials to run. The
    function should use the Monte Carlo simulation to return a move for the machine player in the form of a
    (row, column) tuple.

    :param board:
    :param player:
    :param trials:
    :return:
    """

    return


# Lets start the game
board = provided.TTTBoard(3)

print get_best_move(provided.TTTBoard(3,
                                False,
                                [[provided.EMPTY, provided.EMPTY, provided.PLAYERO],
                                 [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                 [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]),
              [[3, 4.5, 0],
               [0, 0, .5],
               [5, 0, 0]])

# provided.play_game(mc_move, NTRIALS, False)
