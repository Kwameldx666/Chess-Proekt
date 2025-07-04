import pygame as py
import chess


def second_bot_menu(self):
    # Similar to opponent_menuAI but with adjustments for black bot choice
    self.AI = "AI"

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        else:
            self.black_ai = "B"
            self.win.fill((0, 128, 128))
            largeText = py.font.SysFont("comicsansms", 90)
            mediumText = py.font.SysFont("comicsansms", 50)
            self.background_image = py.image.load('Image/ChessBlack1.png')
            self.win.blit(self.background_image, (0, 0))
            TextSurfMian, TextRectMain = self.text_objects("Черные", largeText)
            TextRectMain.center = ((self.dim / 2), (self.dim / 2 - 200))
            self.win.blit(TextSurfMian, TextRectMain)
            # Здесь вы можете добавить свой код для заднего фона меню, если он у вас есть,

            self.button("Минимакс с альфа-бета отсечением", 50 - 10, 120, 430, 60, (250, 235, 215), (50, 205, 50),
                        10)
            self.button("Greedy", 200 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 11)
            self.button("MiniMax", 350 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 12)
            self.button("MCR", 50 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 13)
            self.button("Рандом", 200 - 10, 280, 130, 60, (250, 235, 215), (50, 205, 50), 14)

            py.display.update()
            self.clock.tick(15)
            pass



class DisplayBoard:

    def __init__(self, board):
        self.bot = False
        self.second_bot_choice = None
        self.menu_activeAI = False
        self.menu_active = False  # Флаг, указывающий активно ли меню в данный момент
        self.opponent_choice = None  # Переменная для хранения выбора противника (бота)
        self.run = False  # Флаг, контролирующий основной цикл программы (True, если программа активна)
        self.intro = True  # Флаг, определяющий, следует ли показать вступление/начальный экран
        self.game_over = False  # Флаг, указывающий, окончена ли игра
        self.dim = 500  # Размеры (в пикселях) игровой доски (или окна?)
        self.boardPos = {}  # Словарь для хранения позиций на доске (?)
        self.boardLayout = {}  # Словарь для хранения расположения фигур на доске (?)
        self.show_moves_surf_list = []  # Список для хранения элементов интерфейса (?), связанных с отображением ходов
        self.selected_square = None  # Квадрат доски, выбранный пользователем для перемещения фигуры
        self.square_to_move_too = None  # Квадрат доски, на который пользователь хочет переместить фигуру
        self.player_color = None  # Цвет фигур, которыми управляет игрок ("W" или "B")
        self.white_ai = None
        self.black_ai = None
        self.AI = None
        self.clock = py.time.Clock()  # Экземпляр часов для контроля частоты кадров в игре
        self.board = board  # Доска, представляющая текущее состояние шахматной партии
        self.fen = board.fen()  # Строка FEN (Forsyth-Edwards Notation), представляющая текущее состояние доски

        # General pygame Init

        py.init()  # Инициализация модуля pygame

        # Создание окна игры с заданными размерами и установка заголовка окна
        self.win = py.display.set_mode((self.dim, self.dim))  # Создание окна для отображения с заданными размерами
        py.display.set_caption("Chess")  # Установка заголовка окна

        # Загрузка и масштабирование изображения шахматной доски
        self.chessBoard = py.image.load("Image/Board.jpg").convert_alpha()  # Загрузка изображения доски
        self.chessBoard = py.transform.scale(self.chessBoard, (
            self.dim, self.dim))  # Масштабирование изображения доски до нужных размеров

        # Создание поверхности для отображения возможных ходов и рисование на ней круга
        self.show_moves_surf = py.Surface((50, 50), py.SRCALPHA, 32)  # Создание прозрачной поверхности
        # Рисование зеленого полупрозрачного круга на созданной поверхности
        py.draw.circle(self.show_moves_surf, (0, 200, 0, 100), (25, 25), 20, 0)

        self.boardlayout_init()  # Вызов метода для инициализации расположения фигур на доске (метод определен в другом месте вашего кода)

    def boardlayout_init(self):

        # Инициализация словаря boardLayout
        for x in range(8):
            for y in range(8):
                # boardPos инициализируется один раз и только сохраняет данные о координатах,
                # где находятся реальные блоки (клетки шахматной доски)
                self.boardPos[str(chr(97 + x) + str(y + 1))] = [x * 51.5 + 46, 405 - y * 51]

                # Сохранение позиции в шахматной нотации, где располагаются разные фигуры.
                # Это будет динамически изменяться после каждого хода.
                # Здесь происходит только инициализация имен различных элементов в словаре
                self.boardLayout[str(chr(97 + x) + str(y + 1))] = None

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = py.mouse.get_pos()
        click = py.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            py.draw.rect(self.win, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                if action == 1:
                    self.intro = False
                    self.run = False
                    self.player_color = "W"
                    self.opponent_menu()  # Переход к меню выбора бота
                elif action == 2:
                    self.intro = False
                    self.run = False
                    self.player_color = "B"
                    self.opponent_menu()  # Переход к меню выбора бота
                elif action == 3:
                    py.quit()
                elif action == 4:
                    self.run = False
                    self.intro = True
                    self.game_over = False
                elif action == 10:
                    if self.AI == "AI":
                        self.opponent_choice = "Bot 1"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                    else:
                        self.opponent_choice = "Bot 1"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                elif action == 11:
                    if self.AI == "AI":
                        self.opponent_choice = "Bot 2"
                        self.menu_active = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                    else:
                        self.opponent_choice = "Bot 2"
                        self.menu_active = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                elif action == 12:
                    if self.AI == "AI":
                        self.opponent_choice = "Bot 3"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                    else:
                        self.opponent_choice = "Bot 3"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                elif action == 13:
                    if self.AI == "AI":
                        self.opponent_choice = "Bot 4"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                    else:
                        self.opponent_choice = "Bot 4"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                elif action == 14:
                    if self.AI == "AI":
                        self.opponent_choice = "Bot 5"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                    else:
                        self.opponent_choice = "Bot 5"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                elif action == 15:
                    if self.AI == "AI":
                        self.opponent_choice = "Bot 6"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                    else:
                        self.opponent_choice = "Bot 6"
                        self.menu_active = False
                        self.menu_activeAI = False
                        self.run = True  # Начать игру после выбора бота
                        self.game_over = False
                elif action == 16:
                    self.intro = False
                    self.run = True

                elif action == 17:
                    self.main_menu()




        else:
            py.draw.rect(self.win, ic, (x, y, w, h))

        smallText = py.font.SysFont("comicsansms", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.win.blit(textSurf, textRect)

    def update(self, board):
        # Очистить словарь boardLayout, чтобы можно было создать новый
        for x in range(8):
            for y in range(8):
                self.boardLayout[str(chr(97 + x) + str(y + 1))] = None

        self.board = board
        self.fen = board.fen()

        # Удаление ненужных данных в конце строки
        boardString = str(self.fen)[0:str(self.fen).find(' ')]
        boardString = boardString + '/'

        # Базовая обработка строк для определения, где каждая фигура на доске должна быть расположена
        for y in range(8, 0, -1):
            dash = boardString.find('/')
            rawCode = boardString[0:dash]
            boardString = boardString[dash + 1:len(boardString)]

            alphabetCounter = 97
            for char in rawCode:
                if char.isdigit():
                    alphabetCounter += int(char)
                else:
                    self.boardLayout[str(chr(alphabetCounter)) + str(y)] = self.pieceData(char)
                    alphabetCounter += 1
        self.update_screen()

    def update_screen(self):
        # This function updates the screen should be run every time a change is made to the board state
        self.win.blit(self.chessBoard, (0, 0))
        # Display all pieces in BoardLayout
        for num in self.boardLayout:
            if self.boardLayout[num] != None:
                self.win.blit(self.boardLayout[num].render(), (self.boardPos[num][0], self.boardPos[num][1]))
        # Displays circles that show possible moves
        if self.show_moves_surf_list != []:
            for num in self.show_moves_surf_list:
                self.win.blit(self.show_moves_surf, (num[0], num[1]))

        py.display.update()
        self.clock.tick(10)

    def game_mode_menu(self):
        self.win.fill((255, 255, 255, 100))
        self.menu_active = True
        while self.menu_active:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()
            self.background_image = py.image.load('Image/Botik.png')
            self.win.blit(self.background_image, (0, 0))

            self.button("AI vs AI ", 40, 400, 130, 50, (250, 235, 215), (50, 205, 50), 16)
            self.button("Player vs AI", 270, 400, 200, 50, (250, 235, 215), (50, 205, 50), 17)

            py.display.update()
            self.clock.tick(15)

    def update_possible_moves(self):
        """
           Обновление отображения возможных ходов.

           Данный метод обновляет позицию маленьких кружков, которые показывают игроку,
           куда выбранная фигура может двигаться.
           """

        # Проверяем, была ли выбрана какая-либо клетка
        if self.selected_square != None:
            # Очистка списка позиций для отображения возможных ходов
            self.show_moves_surf_list.clear()
            # Получение всех допустимых ходов для текущей позиции на доске
            lg = self.board.legal_moves

            # Итерация по всем допустимым ходам
            for pos in lg:
                # Если начальная позиция хода совпадает с выбранной клеткой...
                if str(pos)[0:2] == self.selected_square:
                    # ...добавляем позицию конечной клетки хода в список для отображения возможных ходов
                    self.show_moves_surf_list.append(
                        (self.boardPos[str(pos)[2:4]][0], self.boardPos[str(pos)[2:4]][1])
                    )

    def pieceData(self, piece):

        # This class gets referenced when initializing new Pieces using Pieces class
        if piece == 'p':
            return Piece("Pawn", "B")
        elif piece == 'r':
            return Piece("Rook", "B")
        elif piece == 'n':
            return Piece("Knight", "B")
        elif piece == 'b':
            return Piece("Bishop", "B")
        elif piece == 'k':
            return Piece("King", "B")
        elif piece == 'q':
            return Piece("Queen", "B")

        elif piece == 'P':
            return Piece("Pawn", "W")
        elif piece == 'R':
            return Piece("Rook", "W")
        elif piece == 'N':
            return Piece("Knight", "W")
        elif piece == 'B':
            return Piece("Bishop", "W")
        elif piece == 'K':
            return Piece("King", "W")
        elif piece == 'Q':
            return Piece("Queen", "W")

    """
       Метод выбора квадрата на шахматной доске. 
       Если игрок кликает левой кнопкой мыши по клетке, фигура на этой клетке должна быть выбрана для перемещения.
       Если фигура уже была выбрана, то второй клик будет интерпретироваться как клетка, на которую должна переместиться выбранная фигура.
       Однако, если второй клик сделан по фигуре того же цвета, что и первая, то эта фигура становится выбранной для перемещения.
       """

    def square_select(self, pos):
        # Конвертация позиции мыши в координаты доски
        x_board_pos = ((pos[0] - 45) // 50)
        y_board_pos = -((pos[1] - 405) // 50) + 1
        # Если фигура/клетка еще не выбрана...
        if self.selected_square == None:
            self.square_to_move_too = None
            # Запоминаем выбранный квадрат
            self.selected_square = str(chr(97 + x_board_pos) + str(y_board_pos))
            # Обновляем возможные ходы
            self.update_possible_moves()
            return None
        else:
            # Иначе, выбрана клетка для перемещения
            self.square_to_move_too = str(chr(97 + x_board_pos) + str(y_board_pos))
            result = str(self.selected_square + self.square_to_move_too)

            # Проверяем, является ли ход законным
            for move in self.board.legal_moves:
                # Проверяем, требуется ли замена пешки на королеву
                if str(move) == str(result + "q"):
                    self.remove_square_select()
                    return str(result + "q")
                # Проверяем, является ли ход допустимым
                elif str(move) == result:
                    self.remove_square_select()
                    return result

            # Если ход не допустим и была выбрана другая фигура того же цвета, переопределяем выбор
            if self.boardLayout[str(chr(97 + x_board_pos) + str(y_board_pos))] != None:
                self.square_to_move_too = None
                self.selected_square = str(chr(97 + x_board_pos) + str(y_board_pos))
                self.update_possible_moves()
                return None

    # If RightClick the current selected Piece is set to None.
    def remove_square_select(self):
        self.selected_square = None
        self.square_to_move_too = None
        self.show_moves_surf_list = []

    ############################################################################################################################
    # From here is only UI stuff to display menus and buttons ect.

    def main_menu(self):

        red = (200, 0, 0)
        green = (0, 200, 0)

        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)

        while self.intro:
            for event in py.event.get():
                # print(event)
                if event.type == py.QUIT:
                    py.quit()
            self.background_image = py.image.load('Image/Chess2.png')
            self.win.blit(self.background_image, (0, 0))
            largeText = py.font.SysFont("comicsansms", 115)
            # TextSurf, TextRect = self.text_objects("Chess", largeText)
            # TextRect.center = ((self.dim / 2), (self.dim / 2 - 200))
            # self.win.blit(TextSurf, TextRect)
            # self.button("AI vs AI ", 180, 350, 130, 50, (250, 235, 215), (50, 205, 50), 16)
            self.button("WHITE", 50, 350, 100, 50, (250, 235, 215), bright_green, 1)
            self.button("BLACK", 350, 350, 100, 50, (250, 235, 215), bright_green, 2)
            self.button("Quit", 210, 430, 80, 50, red, bright_red, 3)

            py.display.update()
            self.clock.tick(15)

    def opponent_menu(self):
        self.win.fill((255, 255, 255, 100))
        self.menu_active = True
        while self.menu_active:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
            if self.player_color == "W":
                self.win.fill((0, 128, 128))
                largeText = py.font.SysFont("comicsansms", 90)
                mediumText = py.font.SysFont("comicsansms", 50)
                self.background_image = py.image.load('Image/ChessWHITE.png')
                self.win.blit(self.background_image, (0, 0))
                TextSurfMian, TextRectMain = self.text_objects("Белые", largeText)
                TextRectMain.center = ((self.dim / 2), (self.dim / 2 - 200))
                self.win.blit(TextSurfMian, TextRectMain)

                # Здесь вы можете добавить свой код для заднего фона меню, если он у вас есть,

                self.button("Минимакс с альфа-бета отсечением", 50 - 10, 120, 430, 60, (250, 235, 215), (50, 205, 50),
                            10)
                self.button("Greedy", 200 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 11)
                self.button("MiniMax", 350 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 12)
                self.button("MCR", 50 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 13)
                self.button("Рандом", 200 - 10, 280, 130, 60, (250, 235, 215), (50, 205, 50), 14)
                self.button("1 VS 1 ", 350 - 10, 280, 130, 60, (250, 235, 215), (50, 205, 50), 15)
                self.button("AI vs AI ", 50 - 10, 280, 130, 60, (250, 235, 215), (50, 205, 50), 16)

                py.display.update()
                self.clock.tick(15)

            elif self.player_color == "B":
                self.win.fill((0, 128, 128))
                largeText = py.font.SysFont("comicsansms", 90)
                mediumText = py.font.SysFont("comicsansms", 50)
                self.background_image = py.image.load('Image/ChessBlack1.png')
                self.win.blit(self.background_image, (0, 0))
                TextSurfMian, TextRectMain = self.text_objects("Черные", largeText)
                TextRectMain.center = ((self.dim / 2), (self.dim / 2 - 200))
                self.win.blit(TextSurfMian, TextRectMain)
                # Здесь вы можете добавить свой код для заднего фона меню, если он у вас есть,

                self.button("Минимакс с альфа-бета отсечением", 50 - 10, 120, 430, 60, (250, 235, 215), (50, 205, 50),
                            10)
                self.button("Greedy", 200 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 11)
                self.button("MiniMax", 350 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 12)
                self.button("MCR", 50 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 13)
                self.button("Рандом", 200 - 10, 280, 130, 60, (250, 235, 215), (50, 205, 50), 14)
                self.button("1 VS 1 ", 350 - 10, 280, 130, 60, (250, 235, 215), (50, 205, 50), 15)
                self.button("AI vs AI ", 50 - 10, 280, 130, 60, (250, 235, 215), (50, 205, 50), 16)

                py.display.update()
                self.clock.tick(15)

    def opponent_menuAI(self):
        self.win.fill((255, 255, 255, 100))
        self.AI = "AI"
        self.menu_activeAI = True
        while self.menu_activeAI:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
            else:
                self.white_ai = "W"
                self.win.fill((0, 128, 128))
                largeText = py.font.SysFont("comicsansms", 90)
                mediumText = py.font.SysFont("comicsansms", 50)
                self.background_image = py.image.load('Image/ChessWHITE.png')
                self.win.blit(self.background_image, (0, 0))
                TextSurfMian, TextRectMain = self.text_objects("Белые", largeText)
                TextRectMain.center = ((self.dim / 2), (self.dim / 2 - 200))
                self.win.blit(TextSurfMian, TextRectMain)

                # Здесь вы можете добавить свой код для заднего фона меню, если он у вас есть,

                self.button("Минимакс с альфа-бета отсечением", 50 - 10, 120, 430, 60, (250, 235, 215), (50, 205, 50),
                            10)
                self.button("Greedy", 200 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 11)
                self.button("MiniMax", 350 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 12)
                self.button("MCR", 50 - 10, 200, 130, 60, (250, 235, 215), (50, 205, 50), 13)
                self.button("Рандом", 40, 280, 430, 60, (250, 235, 215), (50, 205, 50), 14)

                py.display.update()
                self.clock.tick(15)

    def game_over_menu(self):

        red = (200, 0, 0)
        green = (0, 200, 0)

        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)

        while self.game_over:
            for event in py.event.get():
                # print(event)
                if event.type == py.QUIT:
                    py.quit()

            self.win.fill((255, 255, 255, 100))
            largeText = py.font.SysFont("comicsansms", 90)
            mediumText = py.font.SysFont("comicsansms", 50)
            TextSurfMian, TextRectMain = self.text_objects("Game Over", largeText)
            TextRectMain.center = ((self.dim / 2), (self.dim / 2 - 120))
            self.win.blit(TextSurfMian, TextRectMain)

            if self.board.turn == chess.WHITE:
                TextSurf, TextRect = self.text_objects("Black Won", mediumText)
            else:
                TextSurf, TextRect = self.text_objects("White Won", mediumText)

            TextRect.center = ((self.dim / 2), (self.dim / 2) - 20)
            self.win.blit(TextSurf, TextRect)

            self.button("Play Again", 225, 300, 100, 50, green, bright_green, 4)
            self.button("Quit", 225, 400, 100, 50, red, bright_red, 3)

            py.display.update()
            self.clock.tick(15)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    # This class is used to create Pieces and assign a Surface and Image to them


class Piece():

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.dim = 45

        if (self.color == "W") or (self.color == "White"):
            if self.name != "Knight":
                self.pieceSurface = py.image.load("Image/Chess_" + self.name.lower()[0] + "lt60.png")
            else:
                self.pieceSurface = py.image.load("Image/Chess_nlt60.png")
        else:
            if self.name != "Knight":
                self.pieceSurface = py.image.load("Image/Chess_" + self.name.lower()[0] + "dt60.png")
            else:
                self.pieceSurface = py.image.load("Image/Chess_ndt60.png")

        self.pieceSurface = py.transform.scale(self.pieceSurface, (self.dim, self.dim))

    def render(self):

        return self.pieceSurface

