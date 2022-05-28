from numpy import tri
import pygame
pygame.init()

font = pygame.font.SysFont(None, 90)

class Board:
    def __init__(self, playersigns):
        '''
        playersigns: Sign for respective players
        e.g. {1: 'X', 0: 'O'}
        '''
        self.size = 3
        self.playersigns = playersigns
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def draw(self, screen):
        '''
        Draws cell seperators and player moves on pygame screen
        '''
        s_h = screen.get_height()
        s_w = screen.get_width()
        dx = s_w // self.size
        dy = s_h // self.size

        # Draw cell seperators
        for i in range(self.size+1):
            pygame.draw.line(screen, (255, 255, 255), (dx*i, 0), (dx*i, s_h), 3)
            pygame.draw.line(screen, (255, 255, 255), (0, dy*i), (s_w, dy*i), 3)

        # Draw player moves
        for i in range(self.size):
            for j in range(self.size):
                screen.blit(font.render(self.board[i][j], 1, (255, 255, 255)), (j*dx+26, i*dy+26))

    def update(self, i, j, player):
        '''
        Updates board[i][j] for player 1 or 2
        Returns True if successful
        '''
        # Already played in this cell
        if self.board[i][j] != ' ':
            return False

        self.board[i][j] = self.playersigns[player]
        return True
    
    @staticmethod
    def check_winner(board, playersigns):
        '''
        Returns winner player number, [Array of cells that made up wins]
        If no winner, retruns None, None
        '''
        for player, sign in playersigns.items():
            # Check each rows
            for i in range(len(board)):
                if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
                    return player, [(i, 0), (i, 1), (i, 2)]
            
            # Check each cols
            for i in range(len(board)):
                if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
                    return player, [(0, i), (1, i), (2, i)]

            # Check each diagonals
            if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
                    return player, [(0, 0), (1, 1), (2, 2)]
            if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
                    return player, [(0, 2), (1, 1), (2, 0)]
        return None, None

    @staticmethod
    def all_filled(board):
        '''
        Checks if all spots are filled
        '''
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    return False
        return True

    def clear(self):
        '''
        Initializes a clear new board
        '''
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def draw_line(self, screen, cell1, cell2):
        '''
        Draws a line from cell1 to cell2 on pygame screen
        '''
        s_h = screen.get_height()
        s_w = screen.get_width()
        dx = s_w // self.size
        dy = s_h // self.size

        point1 = dx * cell1[1] + dx//2, dy * cell1[0] + dy//2 
        point2 = dx * cell2[1] + dx//2, dy * cell2[0] + dy//2
        pygame.draw.line(screen, (255, 255, 255), point1, point2, 5)