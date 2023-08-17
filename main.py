from decimal import *
class Game: # Пока не знаю, нужно ли это делать в виде синглтон класса
    def __init__(self):
        self.balance = None
        self.current_bet = None
        self.gain = None
        self.handle_balance_input()
        self.handle_gain_input()
    # 
    # 
    # GETTERS AND SETTERS
    #
    #
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance) -> Decimal:

        if not isinstance(balance, Decimal):
            if isinstance(balance, int) or isinstance(balance, float):
                balance = Decimal(balance)
            else:
                self.__balance = None

        self.__balance = balance

    @property
    def current_bet(self):
        return self._current_bet

    @current_bet.setter
    def current_bet(self, bet):

        if not isinstance(bet, Decimal):
            if isinstance(bet, int) or isinstance(bet, float):
                bet = Decimal(bet)
            else:
                self._current_bet = None

        self._current_bet = bet

    @property
    def gain(self):
        return self._gain

    @gain.setter
    def gain(self, gain):
        if not isinstance(gain, Decimal):
            if isinstance(gain, int) or isinstance(gain, float):
                gain = Decimal(gain)
            else:
                self._gain = None

        self._gain = gain

    # 
    # 
    # INPUT HANDLERS
    #
    #
    # def handle_decimal_input(self, getter):
    #     while getter != None:
    #         try:
    #             balance_input = Decimal(input("Введите баланс, с которым хотите играть: "))
    #         except ValueError:
    #             print("Вы ввели неправильное значение!")
    #         while True:
    #             try:
    #                 balance_input = Decimal(input("Введите баланс, с которым хотите играть: "))
    #             except ValueError:
    #                 print("Вы ввели неправильное значение!")
    #             else:
    #                 break
    #         except KeyboardInterrupt:
    #             print("До свидания!")
    #             exit()
    #         except Exception as e:
    #             print(f"Непредвиденная ошибка {e}. До свидания!")
    #             exit()
    #         else:
    #             self.balance = balance_input

    def handle_balance_input(self):
        while True:
            try:
                balance_input = Decimal(input("Введите баланс, с которым хотите играть: "))
            except InvalidOperation:
                print("Вы ввели неправильное значение!")
            except KeyboardInterrupt:
                print("До свидания!")
                exit()
            except Exception as e:
                print(f"Непредвиденная ошибка {e}. До свидания!")
                exit()
            else:
                self.balance = balance_input
                break

    def handle_current_bet_input(self):
        while True:
            try:
                current_bet_input = Decimal(input("Введите сумму ставки в $: "))
            except InvalidOperation:
                print("Вы ввели неправильное значение!")
            except KeyboardInterrupt:
                print("До свидания!")
                exit()
            except Exception as e:
                print(f"Непредвиденная ошибка {e}. До свидания!")
                exit()
            else:
                self.current_bet = current_bet_input
                break

    def handle_gain_input(self):
        while True:
            try:
                gain_input = Decimal(input("Введите баланс, с которым хотите играть: "))
            except InvalidOperation:
                print("Вы ввели неправильное значение!")
            except KeyboardInterrupt:
                print("До свидания!")
                exit()
            except Exception as e:
                print(f"Непредвиденная ошибка {e}. До свидания!")
                exit()
            else:
                self.gain = gain_input
                break

    def handle_win_input(self):
        pass

    def potential_win(self):
        return self.current_bet * self.gain


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

        self.current_bet = Decimal(input("Введите сумму ставки в $: "))

        while self.current_bet <= 0 or self.current_bet > self.balance:
            if self.current_bet == -1:
                return -1

            print("Сумма ставки должна быть больше нуля и не превышать текущий баланс. Попробуйте ещё раз.")
            self.current_bet = Decimal(input("Введите сумму ставки в $: "))


        print( "Потенциальный выигрыш: %f$ ".ljust(25) % self.potential_win() )
        win = input("Ставка зашла? y/n: ")
        while win != "y" and win != "n":
            print("Вводить можно только y или n. Попробуй ещё раз.")
            win = input("Ставка зашла? y/n: ")

        self.balance -= self.current_bet

        if win == "y":
            self.balance += self.potential_win()
            self.balance = self.balance.quantize(Decimal('1.00'))
            print("\nПоздравляю!\n")
        else:
            print("Сожалею, что вы проиграли\n")
        
def welcome():
    print("Привет!")

def usage():
    pass

def main():
    welcome()


    #set start balance
    # try:
    #     balance = Decimal(input("Введите баланс, с которым хотите играть: "))
    # except ValueError:
    #     print("Вы ввели неправильное значение!")
    #     while True:
    #         try:
    #             balance = Decimal(input("Введите баланс, с которым хотите играть: "))
    #         except ValueError:
    #             print("Вы ввели неправильное значение!")
    #         else:
    #             break
    # except KeyboardInterrupt:
    #     print("До свидания!")
    #     exit()
    # except Exception as e:
    #     print(f"Непредвиденная ошибка {e}. До свидания!")
    #     exit()
    #handle_balance_input()
        

    #set start gain
    # try:
    #     gain = Decimal(input("Введите коэффицент, на который будет умножаться ставка: "))
    # except ValueError:
    #     print("Вы ввели неправильное значение!")
    #     while True:
    #         try:
    #             gain = Decimal(input("Введите коэффицент, на который будет умножаться ставка: "))
    #         except ValueError:
    #             print("Вы ввели неправильное значение!")
    #         else:
    #             break
    # except KeyboardInterrupt:
    #     print("До свидания!")
    #     exit()
    # except Exception as e:
    #     print(f"Непредвиденная ошибка {e}. До свидания!")
    #     exit()

    game = Game()
    game.run()

if __name__ == '__main__':
    main()


# Сделать так, чтобы выход из игры происходил при вводе баланса