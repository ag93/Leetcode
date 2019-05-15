class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y_axis = 0
        x_axis = 0

        for move in moves:
            if move == 'U':
                y_axis = y_axis+1
            elif move == 'D':
                y_axis = y_axis-1
            elif move == 'L':
                x_axis = x_axis-1
            else:
                x_axis = x_axis+1

        if(x_axis == 0 and y_axis == 0):
            return(True)
        else:
            return(False)