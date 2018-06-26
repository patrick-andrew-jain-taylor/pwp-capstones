class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = dict()

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email has been updated to {email}".format(email=self.email))

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books}".format(user=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        return (self.name == other_user.name and self.email == other_user.email)
    
    def read_book(self, book, rating=None):
        self.books[book] = rating
        
    def get_average_rating(self):
        rating = [rating for rating in self.books.values() if rating]
        return (sum(rating)/len(rating))
    
    def __hash__(self):
        return hash((self.name, self.email))
    
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = list()
        
    def __repr__(self):
        return "Title: {title}, ISBN: {isbn}, Rating: {ratings}".format(title=self.title, isbn=self.isbn, ratings=self.ratings)
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn_new):
        self.isbn = isbn_new
        print("ISBN on {title} has been updated to {isbn}".format(title=self.title,isbn=self.isbn))
        
    def add_rating(self, rating):
        if rating:
            if 0 <= rating <= 4: self.ratings.append(rating)
            else: print("Invalid Rating")
        
    def __eq__(self, other_book):
        return (self.title == other_book.title and self.isbn == other_book.isbn)

    def get_average_rating(self):
        return (sum(self.ratings)/len(self.ratings))
    
    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
    
class TomeRater:
    def __init__(self):
        self.users = dict()
        self.books = dict()
        
    def __repr__(self):
        return "{users} {books}".format(users=self.users,books=self.books)
    
    def __eq__(self, other_tomeraters):
        return (self.users == other_tomeraters.users and self.books == other_tomeraters.books)
        
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=None):
        try:
            self.users[email].read_book(book, rating)
        except KeyError:
            print("No user with email {email}!".format(email=email))
        book.add_rating(rating)
        try:
            self.books[book] += 1
        except KeyError:
            self.books[book] = 1
            
    def add_user(self, name, email, user_books=None):
        if self.users[email]: print("This user already exists.")
        else:
            self.users[email] = User(name, email)
            if user_books:
                for book in user_books:
                    TomeRater.add_book_to_user(self, book, email)
                
    def print_catalog(self):
        for book in self.books.keys(): print(book)
        
    def print_users(self):
        for user in self.users.values(): print(user)
        
    def most_read_book(self):
        for book in self.books.keys():
            if self.books[book] == max(self.books.values()): return book
            
    def highest_rated_book(self):
        average_rating = {book:book.get_average_rating() for book in self.books.keys()}
        for book in self.books.keys():
            if average_rating[book] == max(average_rating.values()): return book
            
    def most_positive_user(self):
        average_rating = {user:user.get_average_rating() for user in self.users.values()}
        for user in self.users.values():
            if average_rating[user] == max(average_rating.values()): return user