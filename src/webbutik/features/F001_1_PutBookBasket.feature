# - F001_1 ) Användaren kan lägga böcker i en varukorg

Feature: Add book
    *****  User can put a book in the basket  ******

    Scenario: User put a book in the basket
        Given User chooses a book
        When  User puts the book in the basket
        Then  Basket shows the book in the list
