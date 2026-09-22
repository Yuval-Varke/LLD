"""

Create a class Movie with the following:

Attributes:
movie_name -> name of the movie
total_seats -> total seats available in the theatre
ticket_price -> price per ticket
booked_seats -> starts at 0

Methods :
book_ticket(num_tickets) - books the given number of tickets. If enough seats are available,
confirm the booking and show the total amount to pay. If not,
show "Sorry, not enough seats available"

show_status() - displays movie name, seats available, and seats booked so far

"""



class Movie:
    def __init__(self, movie_name:str, total_seats:int, ticket_price:int, booked_seats:int) -> None:
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = booked_seats

    def book_ticket(self, num:int):
        if num > (self.total_seats - self.booked_seats):
            print("Sorry, not enough seats available !")
        else:
            self.booked_seats += num
            print(f"{num} tickets booked, amount to be paid is :- \n INR {num * self.ticket_price} /-")

    def show_status(self) -> None:
        print(f"Movie name is {self.movie_name}, seats available are {self.total_seats - self.booked_seats}, and seats booked so far are {self.booked_seats}")


m1 = Movie("Tarzen",100,10,0)
m1.show_status()

m1.book_ticket(50)
m1.show_status()

m1.book_ticket(49)
m1.show_status()