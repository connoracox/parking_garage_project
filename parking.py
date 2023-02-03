class Parking():
    def __init__(self):
        self.current_ticket = {
            'quantity': 100,
            'parking': 1000,
            'price': 5.99,
            'paid': False
        }

    def take_ticket(self):
        while True:
            self.current_ticket['quantity'] -= 1
            self.current_ticket['parking'] -= 1
            print('Please take your parking ticket')
            print(
                f"Currently there are {self.current_ticket['quantity']} tickets and {self.current_ticket['parking']} parking spaces available.")
            return

    def payForParking(self):
        price = self.current_ticket['price']
        amount_owed = price
        while amount_owed != 0:
            cost = input(f'Please enter the amount owed ${amount_owed}: ')
            if cost.isdigit():
                cost = float(cost)
                if cost == amount_owed:
                    print(
                        'Thank you, the ticket expires in 15 minutes. Please exit soon.')
                    self.current_ticket['paid'] = True
                    break
                elif cost > amount_owed:
                    refund = cost - price
                    print(
                        f'Thank you, please wait for your change ${refund}. The ticket expires in 15 minutes. Please exit soon.')
                    self.current_ticket['paid'] = True
                    break
                elif cost < amount_owed:
                    amount_owed -= cost
                    print(f'Please pay the remaining amount ${amount_owed}: ')
            else:
                print("Invalid input, please enter a number in digits.")

    def leave_garage(self):
        for ticket in self.current_ticket:
            if self.current_ticket['paid'] == True:
                print('Thank you! Have a nice day!')

            else:
                print('Please pay for the ticket')
                self.payForParking()
                print("Thank you have a nice day!")

            self.current_ticket['parking'] += 1
            print(f"Current number of spots: {self.current_ticket['parking']}")

            self.current_ticket['quantity'] += 1
            print(
                f"Current number of tickets: {self.current_ticket['quantity']}")
            return

    def main(self):
        while True:
            user_selection = input(
                'What would you like to do? Take a ticket (#1), Pay for parking (#2), Leave garage (#3). Please enter digit value: ')
            if user_selection.isdigit():
                if user_selection == '1':
                    garage.take_ticket()
                elif user_selection == '2':
                    garage.payForParking()
                elif user_selection == '3':
                    garage.leave_garage()
                    return
            else:
                print('Please enter value in digits. ')


class Tickets():
    def __init__(self, new_amount, available_parking):
        self.new_amount = new_amount
        self.available_parking = available_parking


garage = Parking()
garage.main()
