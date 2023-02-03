class Parking():
    def __init__(self):
        self.current_ticket = {
            'quantity': 100,
            'parking': 1000,
            'price': 5.99,
            'paid': False 
        }

        self.list = []


    def take_ticket(self):
        quantity = self.current_ticket['quantity']
        parking = self.current_ticket['parking']
        ticket_count = 1
        new_amount = quantity - ticket_count
        available_parking = parking - ticket_count
        new_ticket = Tickets(new_amount, available_parking)
        self.list.append(new_ticket)
        # print('Please take your ticket')
        # print(f'There are now {new_amount} tickets available and {available_parking} parking spaces open.')
        return
        
    def payForParking(self):
        price = self.current_ticket['price']
        amount_owed = price
        while amount_owed != 0:
            cost = input(f'Please enter the amount owed ${amount_owed}: ')
            if cost.isdigit():
                cost = float(cost)
                if cost == amount_owed:
                    print('Thank you, the ticket expires in 15 minutes. Please exit soon.')
                    self.current_ticket['paid'] = True 
                    break
                elif cost > amount_owed:
                    refund = cost - price
                    print(f'Thank you, please wait for your change ${refund}. The ticket expires in 15 minutes. Please exit soon.')
                    self.current_ticket['paid'] = True 
                    break
                elif cost < amount_owed:
                    amount_owed -= cost
                    print(f'Please pay the remaining amount ${amount_owed}: ')
            else:
                print("Invalid input, please enter a number in digits.")

    def show_list(self):
        for items in self.list:
            print('Please take your ticket')
            print(f'Currently there are {items.new_amount} tickets and  {items.available_parking} parking spaces available.')

    def leave_garage(self):
        for ticket in self.current_ticket:
            if 'paid' == True:
                print('Thank you! Have a nice day!')
            else:
                input("Please pay your ticket amount:")
                print("Thank you have a nice day!")
            testing = self.list['new_amount'] + 1
            print(f'{testing}')

    def main(self):
        while True:
            user_selection = input('What would you like to do? Take a ticket (#1), Pay for parking (#2), Leave garage (#3). Please enter digit value: ')
            if user_selection.isdigit():
                if user_selection == '1':
                    garage.take_ticket()
                    garage.show_list()
                elif user_selection == '2':
                    garage.payForParking()
                # elif user_selection == 3:
                #     garage.
                    
            else:
                print('Please value in digits ')


class Tickets():
    def __init__(self, new_amount, available_parking):
        self.new_amount = new_amount
        self.available_parking = available_parking



garage = Parking()
garage.main()

