import random
from datetime import datetime, timedelta
class Book:
    def __init__(self, name, checkout_date, return_date):
        self.name = name
        self.checkout_date = checkout_date
        self.return_date = return_date
class Member:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
def generate_random_date():
    start_date = datetime(2024, 1, 1)
    random_days = random.randint(1, 28)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def main():
    members = []
    for i in range(1, 11):
        member = Member("Member" + str(i))
        num_books = random.randint(10, 30)
        for j in range(1, num_books + 1):
            book_name = "Book" + str(j)
            checkout_date = generate_random_date()
            return_date = generate_random_date()
            book = Book(book_name, checkout_date, return_date)
            member.add_book(book)
        members.append(member)
    total_days = 0
    total_books = 0

    for member in members:
        for book in member.books:
            checkout_day = int(book.checkout_date.split("-")[2])
            return_day = int(book.return_date.split("-")[2])
            days_kept = return_day - checkout_day
            total_days += days_kept
            total_books += 1

    average_days = total_days / total_books if total_books > 0 else 0
    print(f"Average number of days each member keeps the book: {average_days:.2f}")
    print("\nList of Members:")
    for member in members:
        print(f"{member.name} - Number of Books: {len(member.books)}")

if __name__ == "__main__":
    main()
