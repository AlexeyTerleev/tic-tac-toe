import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QLCDNumber, QLineEdit

from logic import Game



class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.game = Game()
        self.initUI()

    def initUI(self):

        self.setGeometry(550, 400, 300, 300)
        self.setWindowTitle('Крестики-нолики')

        self.btn0 = QPushButton('', self)
        self.btn0.resize(self.btn0.sizeHint())
        self.btn0.move(0, 0)
        self.btn0.resize(100, 100)

        self.btn1 = QPushButton('', self)
        self.btn1.resize(self.btn0.sizeHint())
        self.btn1.move(100, 0)
        self.btn1.resize(100, 100)

        self.btn2 = QPushButton('', self)
        self.btn2.resize(self.btn0.sizeHint())
        self.btn2.move(200, 0)
        self.btn2.resize(100, 100)

        self.btn3 = QPushButton('', self)
        self.btn3.resize(self.btn0.sizeHint())
        self.btn3.move(0, 100)
        self.btn3.resize(100, 100)

        self.btn4 = QPushButton('', self)
        self.btn4.resize(self.btn0.sizeHint())
        self.btn4.move(100, 100)
        self.btn4.resize(100, 100)

        self.btn5 = QPushButton('', self)
        self.btn5.resize(self.btn0.sizeHint())
        self.btn5.move(200, 100)
        self.btn5.resize(100, 100)

        self.btn6 = QPushButton('', self)
        self.btn6.resize(self.btn0.sizeHint())
        self.btn6.move(0, 200)
        self.btn6.resize(100, 100)

        self.btn7 = QPushButton('', self)
        self.btn7.resize(self.btn0.sizeHint())
        self.btn7.move(100, 200)
        self.btn7.resize(100, 100)

        self.btn8 = QPushButton('', self)
        self.btn8.resize(self.btn0.sizeHint())
        self.btn8.move(200, 200)
        self.btn8.resize(100, 100)

        self.btn0.clicked.connect(self.b0)
        self.btn1.clicked.connect(self.b1)
        self.btn2.clicked.connect(self.b2)
        self.btn3.clicked.connect(self.b3)
        self.btn4.clicked.connect(self.b4)
        self.btn5.clicked.connect(self.b5)
        self.btn6.clicked.connect(self.b6)
        self.btn7.clicked.connect(self.b7)
        self.btn8.clicked.connect(self.b8)

    def update(self):
        if self.game.curr_state[0][0] == 'O':
            self.btn0.setText('O')
        if self.game.curr_state[0][1] == 'O':
            self.btn1.setText('O')
        if self.game.curr_state[0][2] == 'O':
            self.btn2.setText('O')
        if self.game.curr_state[1][0] == 'O':
            self.btn3.setText('O')
        if self.game.curr_state[1][1] == 'O':
            self.btn4.setText('O')
        if self.game.curr_state[1][2] == 'O':
            self.btn5.setText('O')
        if self.game.curr_state[2][0] == 'O':
            self.btn6.setText('O')
        if self.game.curr_state[2][1] == 'O':
            self.btn7.setText('O')
        if self.game.curr_state[2][2] == 'O':
            self.btn8.setText('O')

    def b0(self):
        if self.game.player_turn == 'X' and self.game.curr_state[0][0] == '.':

            self.game.curr_state[0][0] = 'X'
            self.btn0.setText('X')
            self.game.play()
            self.update()

    def b1(self):
        if self.game.player_turn == 'X' and self.game.curr_state[0][1] == '.':

            self.game.curr_state[0][1] = 'X'
            self.btn1.setText('X')
            self.game.play()
            self.update()

    def b2(self):
        if self.game.player_turn == 'X' and self.game.curr_state[0][2] == '.':

            self.game.curr_state[0][2] = 'X'
            self.btn2.setText('X')
            self.game.play()
            self.update()

    def b3(self):
        if self.game.player_turn == 'X' and self.game.curr_state[1][0] == '.':

            self.game.curr_state[1][0] = 'X'
            self.btn3.setText('X')
            self.game.play()
            self.update()

    def b4(self):
        if self.game.player_turn == 'X' and self.game.curr_state[1][1] == '.':

            self.game.curr_state[1][1] = 'X'
            self.btn4.setText('X')
            self.game.play()
            self.update()

    def b5(self):
        if self.game.player_turn == 'X' and self.game.curr_state[1][2] == '.':

            self.game.curr_state[1][2] = 'X'
            self.btn5.setText('X')
            self.game.play()
            self.update()


    def b6(self):
        if self.game.player_turn == 'X' and self.game.curr_state[2][0] == '.':

            self.game.curr_state[2][0] = 'X'
            self.btn6.setText('X')
            self.game.play()
            self.update()

    def b7(self):
        if self.game.player_turn == 'X' and self.game.curr_state[2][1] == '.':

            self.game.curr_state[2][1] = 'X'
            self.btn7.setText('X')
            self.game.play()
            self.update()

    def b8(self):
        if self.game.player_turn == 'X' and self.game.curr_state[2][2] == '.':

            self.game.curr_state[2][2] = 'X'
            self.btn8.setText('X')
            self.game.play()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    bord = UI()

    bord.show()

    sys.exit(app.exec())
