from modes import one_point_two
import sqlite3

class Game: # Пока не знаю, нужно ли это делать в виде синглтон класса
    def __init__(self, balance, mode):
        self.balance = balance
        self.set_mode(mode)
        self.current_bet = 0

    def set_balance(self, balance):
        pass

    def set_mode(self, mode):
        self.__mode = one_point_two

    #   if mode == 1.2:
    #       pass
    #   elif mode == manual:
    #       pass


    def get_mode(self) -> ():
        return self.__mode

    def set_current_bet(self, bet):
        pass


    def menu(self):
        pass

    # 0 - если, пользователь вышел сам 
    # 1 - если баланс меньше или равен 0
    # 2 - если произошла ошибка
    def run(self) -> int: 
        print("Чтобы выйти из игры введите -1.\n")
        while True:
            if self.balance <= 0:
                print("Сожалеем, что Вы проиграли. Попробуйте в следующий раз.")
                exit(1)
            else:
                if self.play() == -1:
                    print("\n\nДо свидания! Ваш баланс %d$\n" % self.balance)
                    exit(0)
        

    def play(self) -> int:
        print("Текущий баланс: %f$" % self.balance)

        self.current_bet = float(input("Введите сумму ставки в $: "))
        if self.current_bet == -1:
            return -1
        while self.current_bet <= 0 or self.current_bet > self.balance:
            print("Сумма ставки должна быть больше нуля и не превышать текущий баланс. Попробуйте ещё раз.")
            self.current_bet = float(input("Введите сумму ставки в $: "))


        self.prize = self.get_mode()(self.current_bet)
        print("Потенциальный выигрыш: %f$ ".ljust(25) % self.prize)
        win = input("Ставка зашла? y/n: ")
        while win != "y" and win != "n":
            print("Вводить можно только y или n. Попробуй ещё раз.")
            win = input("Ставка зашла? y/n: ")

        self.balance -= self.current_bet
        if win == "y":
            self.balance += self.prize
            print("Поздравляю!\n")
        else:
            print("Сожалею, что вы проиграли\n")
        
def welcome():
    print("Привет!")

def usage():
    pass

def main():
    welcome()
    balance = float(input("Введите баланс, с которым хотите играть: "))
    mode = input("Введите коэффицент, на котором хотите играть. Пример: 1.2.\nВы можете выставлять коэффицент вручную каждую ставку, для этого введите manually.\n")
    game = Game(balance=balance, mode=mode)
    game.run()

if __name__ == '__main__':
    main()


# Сделать так, чтобы выход из игры происходил при вводе баланса