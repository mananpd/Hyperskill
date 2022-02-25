class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.menu = {"espresso": {"water": 250,
                                  "milk": 0,
                                  "beans": 16,
                                  "cost": 4},
                     "latte": {"water": 350,
                               "milk": 75,
                               "beans": 20,
                               "cost": 7},
                     "cappuccino": {"water": 200,
                                    "milk": 100,
                                    "beans": 12,
                                    "cost": 6}}
        self.action_input = None
        self.buy_input = None

    def __str__(self):
        return f"The coffee machine has:\n" \
               f"{self.water} ml of water\n" \
               f"{self.milk} ml of milk\n" \
               f"{self.beans} g of coffee beans\n" \
               f"{self.cups} disposable cups\n" \
               f"${self.money} of money"

    def action(self):
        print("Write action (buy, fill, take, remaining, exit): ")
        self.action_input = input()

    def enough_resources(self, item):
        if self.water < item.get("water"):
            print("Sorry, not enough water!")
            return False
        elif self.milk < item.get("milk"):
            print("Sorry, not enough milk!")
            return False
        elif self.beans < item.get("beans"):
            print("Sorry, not enough coffee beans!")
            return False
        elif self.cups < 1:
            print("Sorry, not enough cups!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.buy_input = input()
        if self.buy_input.isdigit():
            self.buy_input = int(self.buy_input)
        if self.buy_input == 1:
            item = "espresso"
        elif self.buy_input == 2:
            item = "latte"
        elif self.buy_input == 3:
            item = "cappuccino"
        elif self.buy_input == 'back':
            self.main()
        item = self.menu.get(item)
        if self.enough_resources(item):
            self.water -= item.get("water")
            self.milk -= item.get("milk")
            self.beans -= item.get("beans")
            self.cups -= 1
            self.money += item.get("cost")

    def fill_machine(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee you want to add:"))

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def main(self):
        while True:
            self.action()
            if self.action_input == "buy":
                self.buy()
            elif self.action_input == "fill":
                self.fill_machine()
            elif self.action_input == "take":
                self.take_money()
            elif self.action_input == "remaining":
                print(self.__str__())
            elif self.action_input == "exit":
                exit()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.main()
