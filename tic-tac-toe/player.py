class player:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol

    def __str__(self):
        return f"{self.name} {self.symbol}"

    def validate_move(self,board):
        invalid=True
        while invalid:
            print('\n')
            print('Enter {} in a valid position from zero to eight'.format(self.symbol))
            move=int(input(self.symbol+' : '))
            if str(move) in '012345678':
                 if board[move]=='_':
                     board[move]=self.symbol
                     invalid=False
                     return board
                 else:
                     print("Position already occupied at {}".format(move))
            else:
                print("Number not in 012345678")
                
                     
        
