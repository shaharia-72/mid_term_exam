from datetime import datetime, timedelta


class star_cinema:
    hall_list = []  # !class attributes

    def entry_hall(self, hall):  # ! method
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        #! 5 instance
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        # ! star_cinema.entry_hall(self)
        star_cinema().entry_hall(self)

    def entry_show(self, movie_id, movie_name, date, time):  # !method
        show_info = (movie_id, movie_name, date, time)
        self.show_list.append(show_info)

        #! 2d list

        seats = [['available' for _ in range(self.cols)]
                 for _ in range(self.rows)]  # ! 2d array create
        self.seats[movie_id] = seats  # ! assigns in show id

    def book_seats(self, movie_id, book_the_seats):
        if movie_id not in self.seats:
            print("Invalid show ID. Try again.😒")
            return False

        for row, col in book_the_seats:
            if not (0 <= row <= self.rows) or not (0 <= col < self.cols):
                print("Invalid number.😎")
                return False

            if self.seats[movie_id][row][col] == 'booked':
                print("seat already booked.😁")
                return False

            self.seats[movie_id][row][col] = 'booked'

        #! print("Booked successfully. ✌️")
        return True

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Movie: {
                  show[1]}, Date:{show[2]}, Time: {show[3]}")

    def view_available_seats(self, movie_id):
        # print(f"Available seats for {movie_id}: {self.seats}")
        if movie_id not in self.seats:
            print(f"no show found with this ID -> 🥲. {movie_id}")
            return False

        #! break

        # !else:
        print(f"Available seats for this ID -> 👌 {movie_id}")
        seats_info = self.seats[movie_id]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[movie_id][row][col] == 'available':
                    print(f"O", end=' ')  # ! show in matrix
                else:
                    print(f"X", end=' ')

            print()  # ! next line


# hall_1 = Hall(rows=10, cols=10, hall_no=1)
# !hall_2 = Hall(rows=10, cols=10, hall_no=2)
hall_1 = Hall(rows=5, cols=5, hall_no=1)
# !hall_2 = Hall(rows=5, cols=5, hall_no=2)

# hall_1.entry_show("1", "Avangers", "12:00")
#! hall_2.entry_show("2", "Avangers_2", "12:00")

hall_1.entry_show("1", "Avangers", "2023-11-23", "12:00")
# !hall_2.entry_show("1", "Avangers_2", "2023-11-23", "12:00")
#! hall_2.entry_show("2", "Avangers_2", "2023-11-23", "12:00")


def main():
    while True:
        print("------------Welcome to Star Cinema!----------------")
        print("1-> View All Shows....")
        # print("2-> Available seats....")
        print("2-> View Available seats....")
        print("3-> Books tricks Now....")
        print("4-> Exits....")

        print("\n")

        ch = int(input("Enter you option \n"))

        if ch == 1:
            hall_1.view_show_list()
            #! hall_2.view_show_list()

        elif ch == 2:
            movie_id = input("Enter the movie ID: ")
            hall_1.view_available_seats(movie_id)
            # !hall_2.view_available_seats(movie_id)

        # ? elif ch == 3:
        # ?    movie_id = input("Enter the movie ID: ")
        # ?    try:
        # ?        book_the_seats = [(int(input("Enter the row, where you want to seat: "))-1, int(
        # ?            input("Enter column, where you want to seat: "))-1) for _ in range(3)]
        # ?    except ValueError:
        # ?        print("Enter valid information")
        # ?    finally:
        # ?        if hall_1.book_seats(movie_id, book_the_seats) or hall_2.book_seats(movie_id, book_the_seats):
        #  ?           print("Booking successful!")

        elif ch == 3:
            movie_id = input("Enter the movie ID: ")
            try:
                number_of_tricks = int(input("Enter the number of tickets: "))
                book_the_seats = []

                for i in range(number_of_tricks):
                    row = int(
                        input("Enter the row number there you want to sit (row->5): "))-1
                    col = int(
                        input("Enter the column number there you want to sit (row->5): "))-1

                book_the_seats.append((row, col))

            except ValueError:
                print("Booking failed. provide correct seats number.")
                # !continue

            # ?finally:
            #  ?   if hall_1.book_seats(movie_id, book_the_seats) or hall_2.book_seats(movie_id,book_the_seats):
            #   ?      print("Booking successfully:")

            # !if hall_1.book_seats(movie_id, book_the_seats) or hall_2.book_seats(movie_id, book_the_seats):
            if hall_1.book_seats(movie_id, book_the_seats):
                print("Booking successfully:")

            else:
                print("Booking failed, try again....")

        elif ch == 4:
            print("exiting.........")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
