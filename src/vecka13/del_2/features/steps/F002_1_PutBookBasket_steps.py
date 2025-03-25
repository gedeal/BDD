from behave import given, when, then

bookname="Moby Dick"
bookqt = 'UNO'

def Add_Basket (book, item_nr):
    correct_book = bookname
    correct_item_nr = bookqt
    return book == correct_book and  item_nr == correct_item_nr


@given(u'user has chosen a book')
def step_chosen_book(context):
    context_book= bookname
    context_qt = bookqt
    print(f"User has chosen book {context_book}")


@when(u'use puts the book in the basket')
def step_puts_book_basket(context):
    context_book= bookname
    context_qt = bookqt
    context_puts_book = Add_Basket(context_book, context_qt )
    with open('basket.csv', 'a') as file:
        file.write(context_book +' ; ' + str(context_qt)+'\n')

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

@then(u'the basket shows the book in the list')
def step_show_basket(context):
    # with open('string_data.json', 'w') as file:
    #     file.write(json_string)
    print("User has chosen book")
