import csv
import random


def searchfilm():
    data = []
    with open('cinema.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    print(data)

    lookup = input("Please enter a film name: ")
    lookup = lookup.lower()
    col4 = [x[3] for x in data]

    if lookup in col4:
        for k in range(0, len(col4)):
            if col4[k] == lookup:
                print(data[k])
    else:
        print('No film with that name found')


def searchref():
    data = []
    with open('cinema.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    print(data)

    check = input("Please enter a boooking reference number: ")
    refcol = [x[0] for x in data]

    if check in refcol:
        for k in range(0, len(refcol)):
            if refcol[k] == check:
                print(data[k])
    else:
        print('No entry with that referal number found')


def addbooking():
    bookings = []
    data = []
    with open('cinema.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    bookingref = random.randint(20, 40)
    bookingref = str(bookingref)
    col1 = [x[0] for x in data]
    if bookingref in col1:
        bookingref = int(bookingref)
        bookingref2 = random.randint(1, 10000)
        newbookingref = bookingref*bookingref2
        newbookingref = str(newbookingref)
        bookings.append(newbookingref)

        print('The booking reference is:', newbookingref)
        surname = input('Please enter your surname: ')
        forename = input('Please enter your forename: ')
        film = input('Please enter the film you want to see: ')
        film = film.lower()
        day = input('Which day of the week do you want to see the film?: ')
        bookings.append(surname)
        bookings.append(forename)
        bookings.append(film)
        bookings.append(day)
        with open('cinema.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(bookings)
    else:
        print('The booking reference is:', bookingref)
        surname = input('Please enter your surname: ')
        forename = input('Please enter your forename: ')
        film = input('Please enter the film you want to see: ')
        film = film.lower()
        day = input('Which day of the week do you want to see the film?: ')
        bookings.append(surname)
        bookings.append(forename)
        bookings.append(film)
        bookings.append(day)
        with open('cinema.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(bookings)


# Menu system
print('Welcome to the cinema booking system: ')
print('Select an option below to continue: ')

print('Press 1 to book a film: ')
print('Press 2 to search by film name: ')
print('Press 3 to search by booking referal number: ')

choice = input('Please select an option from above: ')

if choice == '1':
    addbooking()
elif choice == '2':
    searchfilm()
elif choice == '3':
    searchref()
else:
    print('invalid entry')
