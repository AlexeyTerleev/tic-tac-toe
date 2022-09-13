

class Game:
    def __init__(self):

        self.curr_state = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        self.player_turn = 'X'

    def draw_bord(self):
        for i in range(3):
            for j in range(3):
                print('{}|'.format(self.curr_state[i][j]), end=' ')
            print()
        print()

    def is_end(self):
        for i in range(3):
            if (self.curr_state[0][i] != '.' and
                    self.curr_state[0][i] == self.curr_state[1][i] and
                    self.curr_state[0][i] == self.curr_state[2][i]):
                return self.curr_state[0][i]
        for i in range(3):
            if self.curr_state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.curr_state[i] == ['O', 'O', 'O']:
                return 'O'
        if (self.curr_state[0][0] != '.' and
                self.curr_state[0][0] == self.curr_state[1][1] and
                self.curr_state[0][0] == self.curr_state[2][2]):
            return self.curr_state[0][0]

        if (self.curr_state[0][2] != '.' and
                self.curr_state[0][2] == self.curr_state[1][1] and
                self.curr_state[0][2] == self.curr_state[2][0]):
            return self.curr_state[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if self.curr_state[i][j] == '.':
                    return None

        return '.'

    def max(self):

        max_v = -2

        pos_x, pos_y = None, None

        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(3):
            for j in range(3):
                if self.curr_state[i][j] == '.':
                    self.curr_state[i][j] = 'O'

                    (m, min_i, min_j) = self.min()

                    if m > max_v:
                        max_v, pos_x, pos_y = m, i, j

                    self.curr_state[i][j] = '.'

        return max_v, pos_x, pos_y

    def min(self):

        min_v = 2

        pos_x, pos_y = None, None

        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(3):
            for j in range(3):
                if self.curr_state[i][j] == '.':
                    self.curr_state[i][j] = 'X'

                    (m, max_i, max_j) = self.max()

                    if m < min_v:
                        min_v, pos_x, pos_y = m, i, j

                    self.curr_state[i][j] = '.'

        return min_v, pos_x, pos_y

    def play(self):
        result = self.is_end()

        if result is not None:
            if result == 'X':
                print('The winner is X')
            elif result == 'O':
                print('The winner is O')
            else:
                print('draw!')
            return

        if self.player_turn == 'X':

            (m, px, py) = self.max()
            self.curr_state[px][py] = 'O'
            self.player_turn = 'X'
            self.draw_bord()
