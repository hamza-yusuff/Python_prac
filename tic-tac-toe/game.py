from player import player
class Game:
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.winnner=None
        self.board=['_' for i in range(9)]

    def display_board(self):
        print('\n')
        for row in range(0,9,3):
            numbers='|'+str(row)+'|'+str(row+1)+'|'+str(row+2)+'|'
            print(' |   |   |   | ')
            print(' | '+self.board[row]+' | '+self.board[row+1]+' | '+self.board[row+2]+' | '+"  "+numbers)
        print('\n')
    def play(self):
        self.display_board()
        current_player=self.player1
        while True:
            self.board=current_player.validate_move(self.board)
            self.display_board()
            winner=self.check_winner()
            if winner:
                print("Congrats the winner is: ", self.winner)
                break                
            if '_' not in self.board:
                print("All filled Up It's a tie")
                break
                
            if current_player==self.player2:
                current_player=self.player1
            elif current_player==self.player1:
                current_player=self.player2

            

    @staticmethod # dont need to create an instance to access this method
    def which_player(symbol,player1,player2):
        if symbol==player1.symbol:
            return player1
        else:
            return player2
        
    def check_winner(self):

        
        #check rows
        for row in range(0,9,3):
            if self.board[row]==self.board[row+1]==self.board[row+2]!='_':
                self.winner=self.which_player(self.board[row],self.player1,self.player2)
                return True

        for col in range(3):
            if self.board[col]==self.board[col+3]==self.board[col+6]!='_':
                self.winner=self.which_player(self.board[col],self.player1,self.player2)
                return True

        #diagonal check
        if self.board[0]==self.board[4]==self.board[8]!='_':
            self.winner=self.which_player(self.board[0],self.player1,self.player2)
            return True
        
        if self.board[2]==self.board[4]==self.board[6]!='_':
            self.winner=self.which_player(self.board[2],self.player1,self.player2)
            return True

    
        
        return False
    

    
            

if __name__=="__main__":
    print("Player one: ")
    name, symbol =input("enter firstname and symbol : ").split()
    player_one=player(name,symbol)
    print("Player Two: ")
    name, symbol =input("enter firstname and symbol : ").split()
    while symbol == player_one.symbol:
        print("player one has the symbol already")
        print("Player Two: ")
        name, symbol =input("enter firstname and symbol").split()
    player_two=player(name,symbol)
    tic_tac_toe=Game(player_one,player_two)
    tic_tac_toe.play()

