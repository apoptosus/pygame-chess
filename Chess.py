import pygame
from math import ceil


# Define the colors we will use in RGB format
black = (0, 0, 0)
white = (255, 255, 255)
gray = (150, 150, 150)
offwhite = (200, 190, 140)
green = (100,200,92)
blue = (0,0,255)
red = (255,0,0)

turn_count = 0


white_pieces = ('12Pawn','22Pawn','32Pawn','42Pawn','52Pawn','62Pawn','72Pawn','82Pawn','11Rook','21knight','31Bishop','41Queen','51King','61Bishop','71knight','81Rook')
black_pieces = ('17Pawn','27Pawn','37Pawn','47Pawn','57Pawn','67Pawn','77Pawn','87Pawn','18Rook','28knight','38Bishop','48Queen','58King','68Bishop','78knight','88Rook')

pieces = list()


class Piece():
    def __init__(self, name, color, position, symbol):
        self.name = name # 31bishop
        self.color = color # white
        self.position = position # 31
        self.symbol = symbol # b

    def __str__(self):
        return str(self.name) + ',' + str(self.color) + ',' + str(self.position) + ',' + str(self.symbol)



class Board():
    def __init__(self,pieces):
        self.pieces = pieces

    def draw_squares(self):
        color_shift = 0
        square_size = 50
        for i in range(8):
            for z in range(8):
                if color_shift % 2 == 0:
                    pygame.draw.rect(board_screen, green, pygame.Rect(square_size*z, square_size*i, square_size, square_size))
                else:
                    pygame.draw.rect(board_screen, offwhite, pygame.Rect(square_size*z, square_size*i, square_size, square_size))
                color_shift += 1
            color_shift -= 1


    def draw_pieces(self,pieces):
        gamegrid = [[0 for x in range(1, 9)] for y in range(1, 9)]

        for i in pieces:
            if i.position == 0:
                continue
            x = int(i.position[0])-1
            y = int(i.position[1])-1
            gamegrid[x][y] = i.symbol
            piece_screen = myfont.render(i.symbol, False, i.color)
            screen.blit(piece_screen, ((x * 50) + 10, (y * 50) + 10))

class Turn():
    def begin_turn(self):
        turns = myfont1.render('Turn: ' + str(turn_count + 1), False, blue)
        screen.blit(turns, (0, 480))
        if turn_count % 2 == 0:
            bottom_text = myfont.render("White's Turn", False, gray)
            screen.blit(bottom_text, (90, 450))
            return white
        else:
            bottom_text = myfont.render("Black's Turn", False, gray)
            screen.blit(bottom_text, (90, 450))
            return black

    def mouse_position_translator(self,og_square,destination_square):
        for i in range(2):
            og_square[i] = ceil(og_square[i]/50)
            destination_square[i] = ceil(destination_square[i]/50)

        return og_square,destination_square

    def piece_position_switch(self,og_square,destination_square):
        #Here is the position of the original square
        old_position = str(og_square[0]) + str(og_square[1])
        new_position = str(destination_square[0])+str(destination_square[1])

        #let's determine if the position has a piece in it
        for i in pieces:
            if old_position == i.position:
            #if it does, then lets take the piece from that position and put it to the new position
                legal = new_turn.check_moves(i, new_position) # lets check to see if that move is legal in the wonderful world of chess
                if legal == True:
                    for j in pieces:
                        if j.name != i.name and j.position == new_position:
                            j.position = '00'
                    i.position = new_position
                    return True



    def check_moves(self,piece,new_position):
        if new_turn.begin_turn() != piece.color:
            return False
        if piece.symbol == 'P':
            return new_turn.pawn_moves(piece, new_position)
        if piece.symbol == 'k':
            return new_turn.knight_moves(piece, new_position)
        if piece.symbol == 'B':
            return new_turn.bishop_moves(piece, new_position)
        if piece.symbol == 'R':
            return new_turn.rook_moves(piece, new_position)
        if piece.symbol == 'Q':
            if new_turn.rook_moves(piece, new_position) == False:
                return new_turn.bishop_moves(piece,new_position)
            else:
                return new_turn.rook_moves(piece, new_position)
        if piece.symbol == 'K':
            return new_turn.king_moves(piece,new_position)


    def pawn_moves(self,piece,new_position):
        x = int(piece.position[0])
        y = int(piece.position[1])
        newx = int(new_position[0])
        newy = int(new_position[1])


        if abs(newy-y) > 2:
            return False
        if abs(newy-y) == 2:
            if piece.name[0:2] == piece.position:
                pass
            else:
                return False
        if piece.color == white:
            for c in range(y+1, newy+1):
                for i in pieces:
                    print(i)
                    if int(i.position[1]) == c: #checks if any piece is in the line of pawn move
                        if int(i.position[0]) == x:
                            return False
                    for i in pieces:
                        print('i want to make it')
                        if int(i.position[1]) == c:
                            print(i)
                            print(c)
                            if int(i.position[0]) == (x+1) or int(i.position[0]) == (x-1):
                                if i.position == new_position:
                                    return True
                    if newx-x != 0: #if pawn moves left or right, bye
                        return False

            return True

        if piece.color == black:
            for c in range(newy, y):
                print (c)
                for i in pieces:
                    print(i)
                    if int(i.position[1]) == c:  # checks if any piece is in the line of pawn move
                        if int(i.position[0]) == x:
                            return False
                    for i in pieces:
                        print('i want to make it')
                        if int(i.position[1]) == c:
                            print(i)
                            print(c)
                            if int(i.position[0]) == (x + 1) or int(i.position[0]) == (x - 1):
                                if i.position == new_position:
                                    return True
                    if newx - x != 0:  # if pawn moves left or right, bye
                        return False

            return True

    def knight_moves(self,piece,new_position):

        if piece.color == white:
            for i in pieces:
                if i.position == new_position:
                    if i.color == white:
                        return False
        if piece.color == black:
            for i in pieces:
                if i.position == new_position:
                    if i.color == black:
                        return False
        if int(piece.position[0]) == int(new_position[0]) - 1 or int(piece.position[0]) == int(new_position[0]) + 1:
            if int(piece.position[1]) == int(new_position[1]) - 2 or int(piece.position[1]) == int(new_position[1]) + 2:
                print('what on earth')
                return True # add a take function
        if int(piece.position[0]) == int(new_position[0])-2 or int(piece.position[0]) == int(new_position[0]) + 2:
            if int(piece.position[1]) == int(new_position[1]) - 1 or int(piece.position[1]) == int(new_position[1]) + 1:
                return True # add a take function
        else:
            return False

    def bishop_moves(self,piece,new_position):
        x = int(piece.position[0])
        y = int(piece.position[1])
        newx = int(new_position[0])
        newy = int(new_position[1])
        count = 0

        if x == newx or y == newy:
            return False

        if (newx - x) != (newy - y) and (newx-x) != (y-newy):
            print('major tenent wrong')
            return False

        if x > newx and y > newy:
            #direction (-,-)
            xcount = newx
            for ycount in range(newy, y):
                print(xcount,ycount)

                for i in pieces:

                    if int(i.position[1]) == ycount:
                        if int(i.position[0]) == xcount:
                            if i.color == piece.color:
                                return False
                            else:
                                count += 1
                xcount += 1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False

        if x > newx and y < newy:
            #direction (-,+)
            xcount = newx
            for ycount in range(newy, y):

                for i in pieces:

                    if int(i.position[1]) == ycount:
                        if int(i.position[0]) == xcount:
                            if i.color == piece.color:
                                return False
                            else:
                                count += 1
                xcount -= 1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False

        if x < newx and y > newy:
            #direction (+, -)
            xcount = newx
            for ycount in range(newy, y):

                for i in pieces:

                    if int(i.position[1]) == ycount:
                        if int(i.position[0]) == xcount:
                            if i.color == piece.color:
                                return False
                            else:
                                count += 1
                xcount -= 1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False



        if x < newx and y < newy:
            #direction (+,+)
            xcount = x+1
            for ycount in range(y+1, newy+1):
                for i in pieces:
                    if int(i.position[1]) == ycount:
                        if int(i.position[0]) == xcount:
                            if i.color == piece.color:
                                return False
                            else:
                                count += 1
                xcount += 1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False


    def rook_moves(self,piece,new_position):
        x = int(piece.position[0])
        y = int(piece.position[1])
        newx = int(new_position[0])
        newy = int(new_position[1])
        count = 0

        if x != newx and y != newy:
            return False #rook cannot move in two directions

        if x == newx and newy > y:
            #direction = '+y'
            for b in range(y+1, newy+1):
                for i in pieces:
                    if x == int(i.position[0]):
                        if int(i.position[1]) == b:
                            if i.color == piece.color:
                                return False
                            else:
                                count += 1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False


        if x == newx and newy < y:
            #direction = '-y'
            for b in range(y, newy):
                for i in pieces:
                    if y == int(i.position[0]):
                        if int(i.position[0]) == b:
                            if i.color == piece.color:
                                return False
                            else:
                                count += 1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False

        if y == newy and newx > x:
            #direction = '+x'
            for b in range(x+1, newx+1):
                for i in pieces:
                    if y == int(i.position[1]):
                        if int(i.position[0]) == b:
                            if i.color == piece.color:
                                return False
                            else:
                                count+=1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False

        if y == newy and newx < x:
            #direction = '-x'
            for b in range(newx, x):
                for i in pieces:
                    if y == int(i.position[1]):

                        if int(i.position[0]) == b:
                            if i.color == piece.color:
                                return False
                            else:
                                count+=1
            if count == 0:
                return True
            if count == 1:
                for i in pieces:
                    if new_position == i.position:
                        return True
            if count <= 1:
                return False

    def king_moves(self,piece,new_position):
        x = int(piece.position[0])
        y = int(piece.position[1])
        newx = int(new_position[0])
        newy = int(new_position[1])


        for i in pieces:
            if new_position == i.position:
                if i.color == piece.color:
                    return False
        print('Praise be the oligarchy, until the damnest day I die')

        if x-1 <= newx <= x+1 and y-1 <= newy <= y+1:
            return True








#Define Class-Objects
for i in white_pieces:
    i = Piece(i, white, i[0:2], i[2])
    pieces.append(i)
for i in black_pieces:
    i = Piece(i, black, i[0:2], i[2])
    pieces.append(i)

gameboard = Board(pieces)
new_turn = Turn()

#set up pygame
pygame.init()

myfont = pygame.font.SysFont('Comic Sans MS', 50)
myfont1 = pygame.font.SysFont('Comic Sans MS', 20)

##Sets up screens
screen = pygame.display.set_mode((400, 500))
board_screen = pygame.Surface((400, 400))
piece_screen = pygame.Surface((400, 400))

gameboard.draw_squares()
screen.blit(board_screen, (0, 0))

gameboard.draw_pieces(pieces)


"""GAME LOOP BEGINS HERE"""
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(board_screen, (0, 0))
    gameboard.draw_pieces(pieces)
    for i in pieces:
        if i.symbol == 'K' and i.position == '00':
            checkmate = pygame.font.SysFont('Comic Sans MS', 100)
            bottom_text = checkmate.render("CHECKMATE", False, red)
            screen.blit(bottom_text, (0, 150))
    new_turn.begin_turn()
    pygame.display.flip()
    '''RIGHT  HERE WE NEED A MORE ACCURATE CLICK RECEIVER AND PROMPT'''
    if turn_count %2 == 0:
        print("White to select a move")
    else:
        print("Black to select a move")


    while event.type!= pygame.MOUSEBUTTONDOWN:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = int(pygame.mouse.get_pos()[0])
            mousey = int(pygame.mouse.get_pos()[1])
            og_square = [mousex, mousey]

    while event.type!= pygame.MOUSEBUTTONUP:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONUP:
            mousex = int(pygame.mouse.get_pos()[0])
            mousey = int(pygame.mouse.get_pos()[1])
            destination_square = [mousex,mousey]

    new_turn.mouse_position_translator(og_square, destination_square)

    print("checking the legality of the move...")
    legality = new_turn.piece_position_switch(og_square, destination_square)

    while legality != True:
        #Check when a mouse is clicked
        while event.type != pygame.MOUSEBUTTONDOWN:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex = int(pygame.mouse.get_pos()[0])
                mousey = int(pygame.mouse.get_pos()[1])
                og_square = [mousex, mousey]
        # when mouse is released take its coordinates
        while event.type != pygame.MOUSEBUTTONUP:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONUP:
                mousex = int(pygame.mouse.get_pos()[0])
                mousey = int(pygame.mouse.get_pos()[1])
                destination_square = [mousex, mousey]
        #reformat them to match the board layout
        new_turn.mouse_position_translator(og_square, destination_square)

        print("waiting for a legal move...")
        legality = new_turn.piece_position_switch(og_square, destination_square)

    pygame.display.flip()
    clock.tick(60)
    turn_count += 1

    screen.fill(black)

# am i in check?