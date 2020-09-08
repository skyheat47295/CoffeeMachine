class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9

    def remaining(self):
        print()
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.coffee_beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')
        print()

    @staticmethod
    def get_action(prompt):
        print(prompt)
        return input()

    def buy(self):

        coffee_type = dict(espresso={'water': 250, 'milk': 0, 'coffee_beans': 16, 'cost': 4},
                           latte={'water': 350, 'milk': 75, 'coffee_beans': 20, 'cost': 7},
                           cappuccino={'water': 200, 'milk': 100, 'coffee_beans': 12, 'cost': 6})
        print()
        action = self.get_action(
            'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if action == 'back':
            return
        for flavor in ['espresso', 'latte', 'cappuccino']:
            if self.water < coffee_type[flavor]['water']:
                print('Sorry, not enough water!')
                print()
                return
            elif self.milk < coffee_type[flavor]['milk']:
                print('Sorry, not enough milk!')
                print()
                return
            elif self.coffee_beans < coffee_type[flavor]['coffee_beans']:
                print('Sorry, not enough coffee beans!')
                print()
                return
        if self.cups < 1:
            print('Sorry, not enough cups!')
            print()
            return
        if action == '1':
            self.money += coffee_type['espresso']['cost']
            self.water -= coffee_type['espresso']['water']
            self.milk -= coffee_type['espresso']['milk']
            self.coffee_beans -= coffee_type['espresso']['coffee_beans']
            self.cups -= 1
        if action == '2':
            self.money += coffee_type['latte']['cost']
            self.water -= coffee_type['latte']['water']
            self.milk -= coffee_type['latte']['milk']
            self.coffee_beans -= coffee_type['latte']['coffee_beans']
            self.cups -= 1
        if action == '3':
            self.money += coffee_type['cappuccino']['cost']
            self.water -= coffee_type['cappuccino']['water']
            self.milk -= coffee_type['cappuccino']['milk']
            self.coffee_beans -= coffee_type['cappuccino']['coffee_beans']
            self.cups -= 1
        print('I have enough resources, making you a coffee!')
        print()

    def fill(self):

        print()
        action = self.get_action('Write how many ml of water do you want to add:')
        self.water += int(action)
        action = self.get_action('Write how many ml of milk do you want to add:')
        self.milk += int(action)
        action = self.get_action('Write how many grams of coffee beans do you want to add:')
        self.coffee_beans += int(action)
        action = self.get_action('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(action)
        print()

    def take(self):
        print()
        print('I gave you $' + str(self.money))
        print()
        self.money = 0

    def main(self):
        action = ''
        while not action == 'exit':
            action = self.get_action('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()


my_coffee_machine = CoffeeMachine()

my_coffee_machine.main()
