from behave import given, when, then
from playwright.sync_api import expect

booklist=['Moby Dick', 'No mans land', 'Oz', '123 Olive']


def book_list (booklist, booksnr):
    correct_book = booklist
    correct_nrbooks = 4
    # print(f'correct nr books:  {correct_nrbooks}')
    return booklist == correct_book and correct_nrbooks == booksnr

def read_basket():

    return True

def remove_book(booklist, booksnr):
    correct_book = booklist
    correct_book.pop(1)
    correct_nrbooks = len(correct_book)
    print('Remove book --------------')
    return correct_nrbooks == booksnr-1


# ------------------------------------------------------------------------

# @given(u'User control books in list')
# def step_choose_book_list(context):
#     context_book= booklist
#     context_qt = len(context_book)
#     print('GIVEN: User control books in list')
#     print(f"User has  {context_qt}  books")
#     print(f"User has these books:  {context_book} ")
#     context_check_book_list = book_list(context_book, context_qt)
#     assert context_check_book_list == True , "Books and nr are wrong :-("
#
#
# @when(u'User asks for the book list')
# def step_remove_book(context):
#     context_book= booklist
#     context_qt = len(context_book)
#     print('WHEN: User control books in list')
#     print(f"User has chosen book {context_book}")
#     context_check_book_list = remove_book(context_book, context_qt)
#
#     assert context_check_book_list == True , "Books and nr are wrong :-("


# @when(u'User asks for the total nr of books in list')
# def step_remove_book(context):
#     context_book= booklist
#     context_qt = len(context_book)
#     print(f"User has chosen book {context_book}")


#
# @then(u'Book list and total shows')
# def step_book_removed(context):
#     context_book= booklist
#     context_qt = len(context_book)
#     print(f"User has chosen book {context_book}")


# step_choose_book_list(booklist)
# step_remove_book(booklist)