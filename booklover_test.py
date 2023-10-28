import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        b = BookLover('hithesh','email1','none')
        
        b.add_book('book1', 5)
        
        self.assertTrue(b.has_read('book1'))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        b = BookLover('hithesh','email1','none')

        b.add_book('book1', 5)
        b.add_book('book1', 5)
        
        self.assertEqual(b.num_books_read(),1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        b = BookLover('hithesh','email1','none')

        b.add_book('book1',5)
        
        self.assertEqual(b.has_read('book1'), True)        
    
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        b = BookLover('hithesh','email1','none')

        b.add_book('book1',5)
        
        self.assertFalse(b.has_read('book2'))
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        b = BookLover('hithesh','email1','none')

        b.add_book('book1',5)
        b.add_book('book2',1)
        b.add_book('book3',4)
        b.add_book('book4',3)
        b.add_book('book5',1)
        
        self.assertEqual(b.num_books_read(),5)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        b = BookLover('hithesh','email1','none')

        b.add_book('book1',5)
        b.add_book('book2',1)
        b.add_book('book3',4)
        b.add_book('book4',3)
        b.add_book('book5',1)

        self.assertTrue(all(b.fav_books()['book_rating'].values>3))

if __name__ == '__main__':
    
    unittest.main(verbosity=3)