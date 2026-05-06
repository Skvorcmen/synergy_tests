class Kassa:
    def __init__(self, money=0):
        self.money = money

    def top_up(self, x):
        self.money += x
        print(f"Касса пополнена на {x}. Теперь в кассе {self.money}")

    def count_1000(self):
        thousands = self.money // 1000
        print(f"В кассе {thousands} целых тысяч")
        return thousands

    def take_away(self, x):
        if x > self.money:
            print(
                f"Ошибка: Недостаточно денег в кассе! В кассе {self.money}, а вы пытаетесь забрать {x}"
            )
            raise ValueError(f"Недостаточно денег. В кассе {self.money}, запрошено {x}")
        else:
            self.money -= x
            print(f"Из кассы забрали {x}. Осталось {self.money}")


kassa = Kassa(5000)
kassa.top_up(3000)
kassa.count_1000()
kassa.take_away(2000)
kassa.take_away(10000)
