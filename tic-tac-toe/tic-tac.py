class Game:
    def __init__(self):
        self.board=[" " for _ in range(9)]

    def show(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row) + ' |')
        
