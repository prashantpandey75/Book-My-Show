class Theater:
    num_of_row = 0
    num_of_col = 0
    details = []
    current_income = 0

    # seat = [['s' for i in range(num_of_col)] for j in range(num_of_row)]

    def __init__(self, num_of_row, num_of_col):
        self.num_of_row = num_of_row
        self.num_of_col = num_of_col
        self.matrix = []
        for i in range(self.num_of_row):
            a = []
            for j in range(self.num_of_col):
                a.append('S')
            self.matrix.append(a)

    def display(self):
        print('\nCinema:')
        print(end='  ')
        for j in range(1, self.num_of_col + 1):
            print(j, end=" ")

        print()
        a = 0
        for i in self.matrix:
            a += 1
            print(a, end=' ')
            print(' '.join(i), sep=",")

    def seat_booking(self, user_row_no, user_col_no, price):
        name = str(input('Enter name: '))
        gender = str(input('Enter gender: '))
        age = int(input('Enter age: '))
        ph_no = int(input('Enter phone no: '))
        self.matrix[user_row_no - 1][user_col_no - 1] = 'B'
        self.details.append([user_row_no, user_col_no, name, gender, age, ph_no, price])
        self.current_income = self.current_income + price
        print('Booking Successful')

    def stat(self):
        purchased_tickets = len(self.details)
        percentage_of_booked_tickets = round((purchased_tickets / (self.num_of_row * self.num_of_col)) * 100,2)
        income = self.current_income
        # Total_income = rows*cols*10
        if self.num_of_row * self.num_of_col > 60:
            Total_income = (4 * self.num_of_col * 10) + ((self.num_of_row - 4) * self.num_of_col * 8)
        else:
            Total_income = self.num_of_row * self.num_of_col * 10

        print('Purchased tickets: {}'.format(purchased_tickets))
        print('Percentage of booked tickets: {}%'.format(percentage_of_booked_tickets))
        print('Current income: {}'.format(income))
        print('Total income: {}'.format(Total_income))

    def show_detail(self, user_row_no, user_col_no):
        for i in self.details:
            if user_row_no == i[0] and user_col_no == i[1]:
                print('Name: ', (i[2]))
                print('Age: ', (i[4]))
                print('Gender: ', (i[3]))
                print('Ticket Price: ', (i[6]))
                print('Phone no: ', (i[5]))
                return
            else:
                pass
        print('Booking not done for this seat')

    def price(self, user_row_no, user_col_no):
        if self.num_of_row * self.num_of_col < 60:
            price = 10
        elif self.num_of_row * self.num_of_col >= 60 and user_row_no > 4:
            price = 8
        else:
            price = 10
        return price


num_of_row = int(input('Enter number of rows: '))
num_of_col = int(input('Enter number of columns: '))
Theater = Theater(num_of_row, num_of_col)
print('1. Show the seat')
print('2. Buy a ticket')
print('3. Statistics')
print('4. Show booked tickets user info')
print('0. EXIT')
user_input = int(input('What you want to see?: '))
while user_input != 0:
    if user_input == 1:
        Theater.display()
    elif user_input == 2:
        user_row_no = int(input('Enter row number: '))
        user_col_no = int(input('Enter column number: '))
        if user_row_no > num_of_row and user_col_no > num_of_col:
            print('Beyond theater limit')
        elif Theater.matrix[user_row_no - 1][user_col_no - 1] == "B":
            print("This seat is already booked")
        else:
            price = Theater.price(user_row_no, user_col_no)
            print('Price of ticket is $', price)
            print('Type yes for booking ')
            print('Type no to cancel ')
            next = str(input('yes/no '))
            if next == 'yes' or next == 'YES':
                Theater.seat_booking(user_row_no, user_col_no, price)
            else:
                pass
    elif user_input == 3:
        Theater.stat()
    elif user_input == 4:
        booked_row_no = int(input('Enter row number: '))
        booked_col_no = int(input('Enter column number: '))
        Theater.show_detail(booked_row_no, booked_col_no)
    else:
        pass
    print('****************************')
    print('1. Show the seat')
    print('2. Buy a ticket')
    print('3. Statistics')
    print('4. Show booked tickets user info')
    print('0. EXIT')
    user_input = int(input('What you want to see?: '))
print('OK BYE')
print('Thank You')





