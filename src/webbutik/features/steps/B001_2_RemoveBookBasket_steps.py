from behave import given, when, then

booklist=['Moby Dick', 'No mans land', 'Oz', '123 Olive']


B_list =[]

def Add_basket (books, item_nr):
    correct_book = booklist
    correct_item_nr = 1
    return books == correct_book and  item_nr == correct_item_nr

def get_book():
    correct_book = booklist[1]
    return correct_book

def remove_book(new_books, item):
    new_books.pop(item)
    return new_books


# --------------------------------------------------------------------

@given(u'User control books in list')
def step_choose_book(context):
    context_book= booklist
    context_chosen_book= get_book()

    print(f"User has these books:  {context_book}")
    print(f"User has chosen book:  {context_chosen_book}")


@when(u'User removes book from list')
def step_remove_book(context):
    context_book= booklist
    item = 1
    context_list = remove_book(context_book,item)
    print(f"\nUser has NOW the following books 1:  {context_list}")


@then(u'Book is removed from in list')
def step_book_removed(context):
    print(f"\nUser has NOW the following books 2:  {booklist}\n")
    assert 'No mans land' not in booklist


#------------------------------------------------------------------------
print ('\n***** F001_2 ) Användaren kan ta bort böcker från varukorgen')
step_choose_book('1')
step_remove_book('c')