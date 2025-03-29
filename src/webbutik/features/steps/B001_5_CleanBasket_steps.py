from behave import given, when, then
from playwright.sync_api import expect

booklist=[['Moby Dick',1],['No mans land',1],['Oz',1],['123 Olive',1]]
quantity = len (booklist)
total_init=0

def books_in_basket(basket):
    nrbooks = len(basket)
    print(basket)
    print(f'User has {nrbooks} books in basket')
    if nrbooks > 0 :
        return True


def no_books_in_basket(basket):
    nrbooks = len(basket)
    print(basket)
    print(f'User has {nrbooks} books in basket')
    if nrbooks == 0 :
        return True

def clear_basket(basket,qtd):
    correct_book = booklist
    print('Remove book --------------')
    correct_book.clear()
    correct_nrbooks = len(correct_book)
    # print(correct_nrbooks)
    return correct_nrbooks


# ------------------------------------------------------------------------

@given(u'User has books in basket')
def step_has_books_in_basket(context):
    context_basket= booklist
    print('START GIVEN : ', context_basket)
    context_qt = len(booklist)
    context_check_basket = books_in_basket(context_basket)
    print('GIVEN : ',context_check_basket)
    assert context_check_basket == True , "There are no books in basket :-("


@when(u'User clears the basket')
def step_clear_basket(context):
    context_basket= booklist
    context_qt = len(booklist)
    context_check_basket = clear_basket(context_basket, context_qt)
    print(f'RESULT {context_check_basket}')
    assert context_check_basket == 0 , "Books and not zero :-("

@then(u'Basket is empty')
def step_books_in_basket(context):
    context_basket = booklist
    context_check_basket = no_books_in_basket(context_basket)
    assert context_check_basket == True, "Still have books :-("



#------------------------------------------------------------------------
print ('\n***** F001_5 ) Det skall gå att tömma varukorgen helt')
# books_in_basket(booklist)
# clear_basket(booklist,quantity)
# no_books_in_basket(booklist)