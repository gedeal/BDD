from behave import given, when, then
from playwright.sync_api import expect

# ['book name',quantity,price]
books = [ ['Orange clock',1,500],
          ['Moby Dick',0,350],
          ['No mans land',0,100],
          ['Oz',0,890],
          ['123 Olive',1,330]
        ]


def Add_Basket (basket,book):
    correct_book = book
    correct_basket = basket
    # print('BASKET ',correct_basket)
    correct_basket.append(correct_book)

    return correct_basket

def clear_basket(basket):
    correct_basket = basket
    correct_basket.clear()
    return correct_basket


def get_discount(nrbooks):
    print('Nr.BOOKS: ', len(nrbooks))
    if len(nrbooks) < 3:
        return False
    else:
        return True


def get_price ():

    return True
# --------------------------------------------------------------------


@given(u'user puts 3 books in basket')
def step_add_tree_books(context):
    global basket
    basket = []
    for x in range(0, 3):
        basket.append(books[x])
    # print('BASKET 1: ', basket)
    # print('BASKET 1: ', len(basket))
    assert len(basket) == 3 , "There are not 3 books in basket :-("

@when(u'user adds one more book')
def step_add_one_more_book(context):
    context_add_basket = Add_Basket(basket, books[4])
    # print('BASKET 2: ', context_add_basket)
    assert len(context_add_basket) == 4 , "There are not 3 books in basket :-("

@when(u'the total nr of books is more then 3')
def step_more_them_tree_books(context):
    global discount
    context_basket = basket
    context_get_discount = get_discount(context_basket)
    assert context_get_discount == True , "There are less them 3 books in basket :-("
    discount = context_get_discount
    print('Discount : ', discount)

@then(u'user gets 10% discont on total price')
def step_gets_10pc_discount(context):
    if discount:
        print('The user gets 10% discount on total price')
    assert discount == True , "No discount :-("

# -----------------------------------------------

# @given(u'user puts more them 100 books in basket')
# def step_impl(context):
#     print('STEP: Given user puts more them 100 books in basket')
#
#
# @when(u'the total nr of books is more then 100')
# def step_impl(context):
#     print('STEP: When the total nr of books is more then 100')
#
#
# @then(u'user gets fail message (to big number)')
# def step_impl(context):
#     print ('STEP: Then user gets fail message (to big number)')

# -----------------------------------------------

# @given(u'user has no books in basket')
# def step_impl(context):
#     print ('STEP: Given user has no books in basket')
#
#
# @when(u'user removes 1 books fron basket')
# def step_impl(context):
#     print ('STEP: When user removes 1 books fron basket')
#
#
# @then(u'user gets fail message (can not be negative)')
# def step_impl(context):
#     print ('STEP: Then user gets fail message (can not be negative)')
#



step_add_tree_books('')
step_add_one_more_book('')
step_more_them_tree_books('')
step_gets_10pc_discount('')

