from behave import given, when, then
from playwright.sync_api import expect

booklist=['Moby Dick', 'No mans land', 'Oz', '123 Olive']



def book_list (booklist):
    correct_book = booklist
    correct_nrbooks = len(booklist)
    return booklist == correct_book and correct_nrbooks >0

def books_in_basket(booklist):
    context_qt = len(booklist)
    print(f'User has {context_qt} books in basket')
    if context_qt > 0 :
        return True
    else:
        return False

def show_basket(booklist):
    correct_book = booklist
    return correct_book

# ------------------------------------------------------------------------
@given(u'User has books in basket list')
def step_basket_has_books(context):
    context_book= booklist
    context_qt = len(booklist)
    print(f'GIVEN: User has books in basket')
    context_check_basket = books_in_basket(context_book)
    assert context_check_basket == True , "Books and nr are wrong :-("

@when(u'User asks to see the basket')
def step_ask_to_see_basket(context):
    context_book= booklist
    print('\nWhen: User asks to see the basket\n')
    context_check_book_list = book_list(context_book)
    assert context_check_book_list == True , "Books and nr are wrong :-("

@then(u'Book basket list and total is show')
def show_books_in_basket(context):
    context_book = booklist
    print('When: Basket shows')
    context_check_basket = show_basket(context_book)
    # assert len(context_check_basket) == 0 , "No books in basket :-("
    assert len(context_check_basket) > 0 , "No books in basket :-("
    print(f"User has these books:  {context_check_basket} \n")

step_basket_has_books(booklist)
step_ask_to_see_basket(booklist)
show_books_in_basket(booklist)