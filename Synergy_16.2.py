class Cheburashka:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Вверх: ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.s
        print(f"Вниз: ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.s
        print(f"Влево: ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.s
        print(f"Вправо: ({self.x}, {self.y})")

    def evolve(self):
        self.s += 1
        print(f"Эволюция! Шаг увеличен до {self.s}")

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Ошибка: шаг не может стать меньше или равным 0")
        self.s -= 1
        print(f"Деградация! Шаг уменьшен до {self.s}")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        moves = 0
        moves += dx // self.s
        if dx % self.s != 0:
            moves += 1

        moves += dy // self.s
        if dy % self.s != 0:
            moves += 1

        print(f"Минимальное количество ходов до ({x2}, {y2}): {moves}")
        return moves


cheb = Cheburashka(0, 0, 3)
cheb.go_right()
cheb.go_up()
cheb.count_moves(10, 10)
