class Game: # Пока не знаю, нужно ли это делать в виде синглтон класса
    def __init__(self, balance, gain):
        self.balance = balance
        self.current_bet = 0
        self.gain = gain

    def set_balance(self, balance):
        pass

    def set_current_bet(self, bet):
        pass

    def menu(self):
        pass

    def potential_win(self) -> float:
        return self.current_bet * self.gain

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


        print( "Потенциальный выигрыш: %f$ ".ljust(25) % self.potential_win() )
        win = input("Ставка зашла? y/n: ")
        while win != "y" and win != "n":
            print("Вводить можно только y или n. Попробуй ещё раз.")
            win = input("Ставка зашла? y/n: ")

        self.balance -= self.current_bet

        if win == "y":
            self.balance += self.potential_win()
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
    gain = float(input("Введите коэффицент, на которой будет умножаться ставка: "))
    game = Game(balance=balance, gain=gain)
    game.run()

if __name__ == '__main__':
    main()


# Сделать так, чтобы выход из игры происходил при вводе баланса