from birdyboard import *
from prompt import *

class Menu:

    def __init__(self):
        self.bird = Birdyboard()

    def main(self):
        while True:
            self.clear_menu()
            title = 'Welcome to Birdyboard! Command Line Short Public and Private Message Posting System'

            heading = ''
            heading += '\033[34m'
            heading += '*' * 54 + '\n'
            heading += '*\033[36m' + title.center(52, ' ') + '\033[34m*\n'
            heading += '*' * 54 + '\n'
            heading += '\033[37;40m'

            menu = {
                '1. Create a user account': self.prompt_user,
                '2. Choose active user': self.prompt_choose_user,
                '3. Create a chirp': self.prompt_create_chirp,
                '5. Create a reply': self.prompt_create_reply,
                '6. See all chirps': self.print_all_chirps,
                '7. Exit Birdyboard!': exit
            }

            prompt_message = 'Choose an option'

            choice = show_menu(heading, menu, prompt_message)
            choice()

    def prompt_user(self):
        self.clear_menu()

        name = prompt('Enter user Name')
        screen_name = prompt('Enter screen_name')

        self.bang.create_new_user(name, screen_name)

        print('Your new user has been created')
        pause()

    def prompt_choose_user(self):
        self.clear_menu()

        user_menu = {
            '{}. {}'.format(c.id, c.name):c for c in self.bang.users.values()}
        chosen_user = show_menu('User List:', user_menu, '')
        self.bang.select_active_user(chosen_user.id)

        print('You are using Birdyboard as ' + chosen_user.name)
        pause()

    def prompt_create_payment(self):
        self.clear_menu()

        if self.bang.active_user_id == 0:
            pause('You must choose a user account first')
            return

        payment_type = prompt('Enter Payment Type (e.g. AmEx, Visa, Checking)')
        account_number = prompt('Enter Account Number')
        self.bang.create_new_payment(payment_type, account_number, self.bang.active_user_id)

        print('New Payment Option created as {} with account number {}'
            .format(payment_type, account_number))
        pause()

    def prompt_add_product(self):
        self.clear_menu()

        if self.bang.active_user_id == 0:
            pause('Please choose a user first.')
            return

        while True:
            self.clear_menu()
            print('Add Products')
            product_menu = {
                '{}. {}'.format(p.id, p.name):p for p in self.bang.products.values()}
            product_menu['7. Back to main menu'] = None
            chosen_product = show_menu('Products:', product_menu, '')

            if chosen_product is None: break

            self.bang.create_new_order(self.bang.active_user_id)
            self.bang.add_product_to_order(self.bang.active_order_id, chosen_product.id)

            order_total = sum([self.bang.products[item.product_id].price
                    for item in self.bang.order_line_items.values()
                    if item.order_id == self.bang.active_order_id])
            print('You have added ' + chosen_product.name + ' to your shopping cart')
            print('Your current total is ${:.2f}.'.format(order_total))
            pause('Press enter to continue adding to your cart')

    def prompt_complete_order(self):
        self.clear_menu()
        if self.bang.active_order_id == 0:
            pause('You must have an active order before you can checkout')
            return

        order_total = sum([self.bang.products[item.product_id].price
                for item in self.bang.order_line_items.values()
                if item.order_id == self.bang.active_order_id])
        should_continue = prompt('Your order total is ${:.2f}. Pay now? [\033[32mY\033[37m/n]'
                                    .format(order_total))

        if should_continue and should_continue.lower()[0] == 'n': return

        payment_menu = {
            '{}. {}'.format(p.id, p.payment_type):p for p in self.bang.payment_options.values()}
        chosen_payment = show_menu('Choose Your Payment Method', payment_menu, '')
        self.bang.pay_order(chosen_payment.id)

        print('Your order is complete! You paid ${:.2f} with your {}.'.format(
            order_total,
            chosen_payment.payment_type))
        pause()

    def print_popular_products(self):
        self.clear_menu()
        popular = self.bang.get_popular_products()
        products = popular['products']
        totals = popular['totals']

        # column widths
        products_col_width = 18
        orders_col_width = 11
        users_col_width = 11
        revenue_col_width = 15
        total_width = (products_col_width +
                       orders_col_width +
                       users_col_width +
                       revenue_col_width)

        # formating strings for table lines
        title_string = '{:<18}{:<11}{:<11}{:<15}'
        line_string = '{:<18}{:<11}{:<11}${:<14,.2f}'

        print('\033[36m' + title_string.format('Product', 'Orders', 'users', 'Revenue'))
        print('\033[34m*\033[37m' * total_width)
        for p in products:
            name = p['name']
            # limit name string length
            name = (name if len(name) <= 17 else name[:14] + '...') + ' '
            orders = p['order_count']
            users = p['user_count']
            revenue = p['revenue']
            print(line_string.format(name, orders, users, revenue))
        print('\033[34m*\033[37m' * total_width)
        print(line_string.format(
            '\033[36mTotals:\033[37m', totals['order_sum'], totals['user_sum'], totals['revenue_sum']))

        # wait to continue
        pause()

    def clear_menu(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

if __name__ == '__main__':
    Menu().main()