from queue import PriorityQueue
from a_star_algo import *
import copy

def dfs(visited, board, pos_moves):

    pos_moves = possible_moves(board)
    if node not in visited:
        print (node)
        visited.append(board)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def check_victory(board):
    if board[2][2] == 9:
        return True
    else:
        return False

def print_board(board):
    print("***PRINTING BOARD***")
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                print(" _", end="")
            elif board[i][j] == 10:
                print(" x", end="")
            elif board[i][j] == 9:
                print(" R", end="")
            else:
                print(" " + str(board[i][j]), end="")
        print ("\n")
    print("***FINISHED PRINTING BOARD***\n")

def make_move(board,move):
    stone = move[0]
    #direction = move[1]
    new_board = copy.deepcopy(board)
    x,y = find_xy_of_stone(new_board, stone)
    x_new, y_new = move[2]
    new_board[y][x] = 0
    new_board[y_new][x_new] = stone
    return new_board

def find_xy_of_stone(board,stone):
    y = 5 #Not valid numbers
    x = 5 #Not valid numbers
    for i in range(5):
        if stone in board[i]:
            y = i
            x = board[i].index(stone)
    return (x,y)

# def check_closest_stone_in_direction(board,x,y,direction):
#     if direction =="R":
#         for 
#     elif direction == "L":
#     elif direction == "U":
#     elif direction == "D":
        
def possible_moves(board):
    possible_moves = []

    for y in range(5):
        for x in range(5):
            if board[y][x] < 10 and board[y][x] > 0 :
                stone = board[y][x]

                #CHECK IF IT CAN MOVE RIGHT
                if x != 4 and (board[y][x+1] == 0 or board[y][x+1] == 10):
                    for i in range(4-x):
                        checkx = x+i+1
                        if ((board[y][checkx] > 0 and board[y][checkx] < 10)):
                            possible_moves.append([stone,"R",(checkx-1,y)])
                            break
                
                #CHECK IF IT CAN MOVE LEFT
                if x != 0 and (board[y][x-1] == 0 or board[y][x-1] == 10):
                    for i in range(x-1,-1,-1):
                        checkx = i
                        if ((board[y][checkx] > 0 and board[y][checkx] < 10)):
                            possible_moves.append([stone,"L",(checkx+1,y)])
                            break
                
                #CHECK IF IT CAN MOVE UP
                if y != 0 and (board[y-1][x] == 0 or board[y-1][x] == 10):
                    for i in range(y-1,-1,-1):
                        checky = i
                        if ((board[checky][x] > 0 and board[checky][x] < 10)):
                            possible_moves.append([stone,"U",(x,checky+1)])
                            break
                
                #CHECK IF IT CAN MOVE DOWN
                if y != 4 and (board[y+1][x] == 0 or board[y+1][x] == 10):
                    for i in range(4-y):
                        checky = i+y+1
                        if ((board[checky][x] > 0 and board[checky][x] < 10)):
                            possible_moves.append([stone,"D",(x,checky-1)])
                            break
    return possible_moves

def construct_board(board,moves):
    """
    Constructs the board based on given moves
    """
    for move in moves:
        board = copy.deepcopy(make_move(board,move))
    return board

solution = []
visited_boards = []
solved_board = []

def similar_possible_moves(new_board,pos_moves):
    new_moves = possible_moves(new_board)
    old_moves = copy.deepcopy(pos_moves)
    count = 0
    for move in old_moves:
        if move in new_moves:
            count +=1

    #We minus 1 because one of the old moves is the move used from the newboard
    if (count-1)/len(old_moves) > 0.75:
        return True
    
    #Return false if moves are not that similar
    return False

def dfs(board, move):
        """
        visited is global list of visited boards
        move is the move used to make the board
        graph is the board
        node is also the board
        solution is global list used to hold the winning moves
        """
        #Check if we've seen this board before
        if board not in visited_boards:

            #Add board to previously seen boards
            visited_boards.append(board)
            
            #Check if it's the winner?
                #record move
                #return true (note solution is global)
            if check_victory(board):
                solution.append(move)
                solved_board.append(board)
                return True

            #Check if board doesn't have possible moves:
                #return false
            pos_moves = possible_moves(board)
            if len(pos_moves) == 0:
                return False

            #record move
            if move[0] != 0:
                solution.append(move)
            #print("Solution so far is ", solution)

            #Arrange order of moves:
            arranged_moves = copy.deepcopy(pos_moves)
            for next_move in pos_moves:
                
                #Check similar moves
                if similar_possible_moves(new_board, board):
                    arranged_moves.pop(0)
                    arranged_moves.append(next_move)

            #For all possible moves from current board,
            # neighbour = possible boards made from current board
            for next_move in pos_moves:
                #make new board
                #print (next_move)
                new_board = make_move(board,next_move)
                #print_board(new_board)
                #if dfs returns true, 
                    #automatically return true
                if dfs(new_board,next_move):
                    return True
                #if dfs returns false, continue
                else:
                    continue
            
            #we are at the end and we still don't have a solution so we need to remove the last move:
            #solution remove last index
            solution.pop()

BOARDS = [[ [1,0,0,0,9],
            [0,0,2,0,0],
            [0,0,10,0,0],
            [0,0,0,3,0],
            [0,4,0,0,0]],

        [   [0,0,1,0,0],
            [0,2,0,0,0],
            [0,0,3,4,0],
            [0,9,0,0,0],
            [0,0,0,0,0]],

        [   [0,0,0,0,0],
            [1,0,0,0,0],
            [0,0,10,0,2],
            [3,0,0,0,0],
            [9,0,0,0,0]],

         [  [1,0,2,0,0],
            [0,0,0,0,3],
            [0,0,10,4,5],
            [0,0,0,0,0],
            [0,9,0,0,6]]]

if __name__ == '__main__':

    print("*************************STARTING NEW GAME**********************")
    print("****************************************************************")

    #NOTE: 9 IS THE RED ONE
    start_board =  [[1,0,0,0,9],
                    [0,0,2,0,0],
                    [0,0,10,0,0],
                    [0,0,0,3,0],
                    [0,4,0,0,0]]

    board = copy.deepcopy(BOARDS[3])
    print_board(board)

    dfs(board,[0])
    print("\n****************SOLUTION***************")
    print (solution)
    print("*******************************************\n")
    
    print_board(solved_board[0])
    #source = 0
    #target = 2
    #best_first_search(source, target, vertices)