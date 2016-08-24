from birdyboard import *

from prompt import *

class Menu:
    chosen_user = None

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
                '4. See all chirps': self.print_all_chirps,
                '5. Exit Birdyboard!': exit
            }

            prompt_message = 'Choose an option'

            choice = show_menu(heading, menu, prompt_message)
            choice()

    def prompt_user(self):
        self.clear_menu()


        name = prompt('Enter user Name')
        screen_name = prompt('Enter screen_name')

        self.chosen_user = self.bird.create_new_user(name, screen_name)


        print('Your new user has been created')
        pause()

    def prompt_choose_user(self):
        self.clear_menu()

        user_menu = {
            '{}. {}'.format(c.id, c.name):c for c in self.bird.users.values()}
        self.chosen_user = show_menu('User List:', user_menu, '')

        print('You are using Birdyboard as ' + self.chosen_user.name)
        pause()

    def prompt_create_chirp(self):
        self.clear_menu()

        message = prompt('Write a chirp')
        user_id = self.chosen_user

        self.bird.create_new_chirp(message, user_id)

        print('Your new chrip says ' + message)
        pause()


    def print_all_chirps(self):
        self.clear_menu()
        all_chirps = self.bird.get_all_chirps()
        public_chirps = all_chirps['public_chirps']
        view_all_chirps = all_chirps['view_all_chirps']

        # column widths
        public_chirps_col_width = 18
        orders_col_width = 11
        users_col_width = 11
        revenue_col_width = 15
        total_width = (public_chirps_col_width +
                       orders_col_width +
                       users_col_width +
                       revenue_col_width)

        # formating strings for table lines
        title_string = '{:<18}{:<11}{:<11}{:<15}'
        line_string = '{:<18}{:<11}{:<11}${:<14,.2f}'

        print('\033[36m' + title_string.format('User', 'Title', 'message'))
        print('\033[34m*\033[37m' * total_width)
        for p in public_chirps:
            name = p['name']
            # limit name string length
            name = (name if len(name) <= 17 else name[:14] + '...') + ' '
            users = p['user_count']
            revenue = p['revenue']
            print(line_string.format(name, chirp_title, message))
        print('\033[34m*\033[37m' * total_width)
        print(line_string.format(
            '\033[36mTotals:\033[37m', view_all_chirps['order_sum'], view_all_chirps['user_sum'], view_all_chirps['revenue_sum']))

        # wait to continue
        pause()

    def clear_menu(self):
        ('clear')

if __name__ == '__main__':
    Menu().main()