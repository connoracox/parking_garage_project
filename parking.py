class Parking():
    def __init__(self):
        self.current_ticket = {
            'quantity': 100,
            'parking': 1000,
            'price': 5.99,
            'paid': True 
        }

        self.list = []


    def take_ticket(self):
        quantity = self.current_ticket['quantity']
        parking = self.current_ticket['parking']
        ticket_count = 1
        new_amount = quantity - ticket_count
        available_parking = parking - ticket_count
        new_ticket = Ticket(new_amount, available_parking)
        self.list.append(new_ticket)
        print('Please take your ticket')
        # print(f'There are now {new_amount} tickets available and {available_parking} parking spaces open.')
        return
        
    def payForParking(self):
        price = self.current_ticket['price']
        cost = input('Please enter the amount owed: ($5.99) ')
        if cost.isdigit():
            cost = float(cost)
            if cost == price:
                print('Thank you, the ticket expires in 15 minutes. Please exit soon.')
            elif cost > price:
                refund = cost - price
                print(f'Thank you, please wait for your change ${refund}. The ticket expires in 15 minutes. Please exit soon.')
            else:
                amount_owed = price - cost
                print(f'Please pay the remaining amount ${amount_owed}')
                return
        else:
            print("Invalid input, please enter a number in digits.")

    def show_list(self):
        for items in self.list:
            print(f'Currently there are {items.new_amount} tickets and  {items.available_parking} parking spaces available.')

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
                    return
            else:
                print('Please value in digits ')


class Tickets():
    def __init__(self, ticket, parking):
        self.ticket = ticket
        self.parking = parking
    pass


garage = Parking()
garage.main()

