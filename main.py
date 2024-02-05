# Program: Movie Seat Finder
# Description: This program enables users to choose a seat in a theater by providing the number of seats they are searching for and the seat map from the movie theater. It returns a list of all available seat alternatives.

# imports
import theaterSeats as t

# Level 1: Find all available seats
def find_available_seats(theater_seats):
    available_seats = []  # Tracks available seats

    for row in theater_seats[1:]:  # Iterate through each row of theater_seats, excluding the first row with letters
        row_num = row[0]  # Row number
        for index, seat_status in enumerate(row[1:]):  # Iterate through each seat in the row
            if seat_status == 'o':  # Checks if seat is available 
                row_letter = theater_seats[0][index + 1]  # Get seat letter
                available_seats.append(f"{row_num}{row_letter}")  # Add available seats to the list
    return available_seats  # Output list of available seats

## Level 1 Test
test1 = find_available_seats(t.theater_seats2)
print(test1)

# Level 2: Find single pairs of empty seats
def find_single_pair(theater_seats):
    pairs_available = []  # Tracks available pairs of seats

    for row in theater_seats[1:]:  # Iterate through each row of theater_seats
        for index in range(len(row) - 1):  # Iterate through each seat in the row (-1 because we start at index 1)
            if row[index] == 'o' and row[index + 1] == 'o':  # Checks for a pair of available seats
                pairs = f"{row[0]}{theater_seats[0][index]}{theater_seats[0][index + 1]}"  # Add pairs of available seats
                pairs_available.append(pairs)
    return pairs_available  # Return list of available pairs

## Level 2 Test
test2 = find_single_pair(t.theater_seats2)
print(test2)

# Level 3: Find all pairs of empty seats
def find_pairs_available(theater_seats):
    pairs_available = []  # Tracks all available pairs

    for row in theater_seats[1:]:  # Iterate through each row of theater_seats
        for index in range(len(row) - 1):  # Iterate through each seat in the row (-1 because we start at index 1)
            if row[index] == 'o' and row[index + 1] == 'o':  # Checks for a pair of available seats
                pairs = f"{row[0]}{theater_seats[0][index]}{theater_seats[0][index + 1]}"  # Add pairs of available seats
                pairs_available.append(pairs) 
    return pairs_available  # Return list of available pairs

## Level 3 Test
test3 = find_pairs_available(t.theater_seats2)
print(test3)

# Level 4: Find all possible combinations of seats with a specified number of seats together
def find_combinations(theater_seats, num_seats):

    seat_combinations = []  # Tracks all possible combinations

    for row in theater_seats[1:]:  # Iterate through each row of theater_seats
        row_num = row[0]  # Row number
        for index in range(len(row) - num_seats + 1):  # Iterate through each seat in the row, considering the required number of seats
            if all(seat == 'o' for seat in row[index:index + num_seats]):  # Checks if consecutive seats are available
                combination = [(row_num, seat_num) for seat_num in range(index + 1, index + num_seats + 1)]  # Creates a combination of seat numbers
                seat_combinations.append(combination)

    return seat_combinations  # Return list of seat combinations

## Level 4 Test
test4 = find_combinations(t.theater_seats2, 3)
print(test4)

for row in t.theater_seats:
  print(row)

for row in t.theater_seats2:
 print(row)

