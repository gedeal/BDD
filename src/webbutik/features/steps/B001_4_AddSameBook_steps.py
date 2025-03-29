from behave import given, when, then
from playwright.sync_api import expect

booklist=[['Moby Dick',1],['No mans land',1],['Oz',1],['123 Olive',1]]
quantity = len (booklist)
total_init=0


def books_in_basket(basket):
    print(f'User has {quantity} books in basket')
    if quantity > 0:
        return True
    else:
        return False

def add_basket(basket, book):
    context_basket= basket
    context_book= book
    found = False
    total = 0
    global total_init
    # print('Initial: ', context_basket)
    for row in context_basket:
        if row[0] == context_book:
            # print( 'FOUND BOOK: ', row[0] )
            total_init = row[1]
            row[1] += 1
            # print('Total: ',row[0],' = ', row[1])
            found = True
            total = row[1]
    # print(context_basket)
    return found, total

def check_basket_change(basket, qtd):
    if len(basket) == qtd:
        return True
    else:
        return False

def check_book_change(basket,book,qtd):
    context_basket= basket
    context_book=book
    # print(basket,book,qtd)
    for row in context_basket:
        if row[0] == book:
            print('FOUND BOOK: ', row[0])
            if row[1] != qtd:
                print(' ',row[1],' != ', qtd)
                return True
    return False

# ------------------------------------------------------------------------


@given(u'User has already books in basket list')
def step_basket_has_books(context):
    context_basket= booklist
    context_qt = len(booklist)
    # print(f'GIVEN: User has books in basket')
    context_check_basket = books_in_basket(context_basket)
    assert context_check_basket == True , "Books and nr are wrong :-("


@when(u'User adds the same book in basket')
def step_add_same_book(context):
    context_basket= booklist
    context_new_book='Oz'
    context_add_basket, total = add_basket(context_basket,context_new_book)
    # print('TO: ', total)
    # print('Res: ', context_add_basket)
    assert context_add_basket == True , "Books does not exist :-("


@then(u'Basket list does not change')
def step_basket_does_not_change(context):
    context_basket= booklist
    # context_basket_change = check_basket_change(context_basket, quantity+1)
    context_basket_change = check_basket_change(context_basket, quantity)
    assert context_basket_change == True , "Basket List changed :-("


@then(u'The book total changes')
def step_total_has_changed(context):
    # print('INITIAL VALUE: ', total_init)
    context_basket= booklist
    context_new_book = 'Oz'
    context_total_change = check_book_change(context_basket,context_new_book, total_init)
    assert context_total_change == True , "Total has not changed :-("


#------------------------------------------------------------------------
print ('\n***** F001_4 ) Om användaren försöker lägga en bok som redan finns i varukorgen ska antalet')
step_basket_has_books(booklist)
step_add_same_book(booklist)
step_basket_does_not_change(booklist)
step_total_has_changed(booklist)