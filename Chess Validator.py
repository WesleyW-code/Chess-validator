import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

chessboard = []
for i in range(8):
    chess_row = input()
    chessboard.append(chess_row)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Getting positions of King:
position_K = []
position_E = []
for i in range(8):
    if "K" in chessboard[i]:
        position_K.append(i)
        row = chessboard[i].split(" ")
        for c in range(8):
            if "K" in row[c]:
                position_K.append(c)

# Getting position of Enemy and type:
enemies = ["B","N","R","Q"]
for i in range(8):
    row = chessboard[i].split(" ")
    for c in range(8):
        temp = row[c]
        if temp in enemies:
            position_E.append(i)
            position_E.append(c)
            position_E.append(temp)

       
# Making functions for each enemy piece:

def rook (position_K,position_E):
    if position_K[0] == position_E[0]:
        return "Check"
    elif position_K[1] == position_E[1]:
        return "Check"
    else:
        return "No Check"

def bishop(position_K,position_E):
    row_dif = abs(position_K[0] - position_E[0])
    col_dif = abs(position_K[1] - position_E[1])
    if position_K[1] == position_E[1] + row_dif:
        return "Check"
    elif position_K[1] == position_E[1] - row_dif:
        return "Check"
    elif position_K[0] == position_E[0] + col_dif:
        return "Check"
    elif position_K[0] == position_E[0] - col_dif:
        return "Check"
    else:
        return "No Check"

def queen(position_K,position_E):
    rook_move = rook(position_K,position_E)
    bishop_move = bishop(position_K,position_E)
    if rook_move == "Check" or bishop_move == "Check":
        return "Check"
    else:
        return "No Check"

def knight(position_K,position_E):
    if position_K[0] == position_E[0] + 2 and position_E[1] + 1 == position_K[1]:
        return "Check"
    elif position_K [0] == position_E[0] - 2 and position_E[1] - 1 == position_K[1]:
        return "Check"
    elif position_K[0] == position_E[0] + 1 and position_E[1] + 2 == position_K[1]:
        return "Check"
    elif position_K[0] == position_E[0] - 1 and position_E[1] - 2 == position_K[1]:
        return "Check"
    elif position_K[0] == position_E[0] + 2 and position_E[1] - 1 == position_K[1]:
        return "Check"
    elif position_K [0] == position_E[0] - 2 and position_E[1] + 1 == position_K[1]:
        return "Check"
    elif position_K[0] == position_E[0] - 1 and position_E[1] + 2 == position_K[1]:
        return "Check"
    elif position_K[0] == position_E[0] + 1 and position_E[1] - 2 == position_K[1]:
        return "Check"
    else:
        return "No Check"

# Checking to see which function to run and determining check or not:
if position_E[2] == "R":
    output = rook(position_K,position_E)

elif position_E[2] == "B":
    output = bishop(position_K,position_E)

elif position_E[2] == "Q":
    output = queen(position_K,position_E)

elif position_E[2] == "N":
    output = knight(position_K,position_E)


print(output)




