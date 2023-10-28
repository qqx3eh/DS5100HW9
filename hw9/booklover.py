import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name': pd.Series(dtype='str'),
                   'book_rating': pd.Series(dtype='int')})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        if rating <= 5:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            if book_name not in self.book_list['book_name'].values:
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            return self.book_list
        else:
            return None
    
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
        
    def num_books_read(self):
        return len(self.book_list['book_name'])
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
            
    

if __name__ == '__main__':
    b = BookLover('hithesh','email1','none')
    # Add Book Test
    print(b.add_book('book1', 5))
    print(b.add_book('book2', 2))
    # Has Read Test
    print(b.has_read('book3'))
    print(b.has_read('book3'))
    # Num Books Read
    print(b.num_books_read())
    # Fav Books
    print(b.fav_books())