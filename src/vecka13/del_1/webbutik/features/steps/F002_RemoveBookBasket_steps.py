from behave import given, when, then

bookname="Moby Dick"
bookqt = 1

def Add_basket (book, item_nr):
    correct_book = bookname
    correct_item_nr = bookqt
    return book == correct_book and  item_nr == correct_item_nr

def read_basket():

    return True

def remove_book(book):

    return True


@given(u'user has books in list')
def step_choose_book(context):
    context_book= bookname
    context_qt = bookqt
    print(f"User has chosen book {context_book}")


@when(u'user removes book from list')
def step_remove_book(context):
    context_book= bookname
    context_qt = bookqt
    print(f"User has chosen book {context_book}")

@then(u'book is removed from in list')
def step_book_removed(context):
    context_book= bookname
    context_qt = bookqt
    print(f"User has chosen book {context_book}")
