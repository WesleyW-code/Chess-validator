# Chess-validator

## INTRODUCTION ##

The following url is the coding practise i had to do which has its own test cases: https://www.codingame.com/ide/puzzle/is-the-king-in-check-part-1 To see my code run correctly use it to solve the problem and run the test cases

## CODING TASK ##

8 x 8 space-separated character rows of a chessboard with only two pieces on the board. Your King and some enemy piece. This code will Print "Check" or "No Check" depending on whether the enemy piece is able to attack your king on the next turn.

The King will be a K character. The enemy piece will be Bishop (B), Knight (N), Rook (R) or Queen (Q). The empty positions will be _ in the input. The only two non-_ characters will be K and one of either B/N/R/Q.

Bishops (B): Attack diagonally in all four directions.
Rooks (R): Attack horizontally/verically in all four directions (can attack along same row or column)
Queens (Q): Attack in all eight of the above directions.

Knights (N): Attack in L-shapes - squares that are two rows and one column away (L), or one row and two columns away (∟). (These happen to be the only eight squares in a 5x5 sub-grid that a Queen can't attack from the same spot).

Diagram for the squares a Knight can attack (NB: x is used here to indicate these squares, will never be in the game input):

_ _ _ _ _ _ _ _
_ _ x _ x _ _ _
_ x _ _ _ x _ _
_ _ _ N _ _ _ _
_ x _ _ _ x _ _
_ _ x _ x _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _

If a King is in any of those x positions relative to the Knight on the input diagram, then the answer is "Check", otherwise "No Check".

