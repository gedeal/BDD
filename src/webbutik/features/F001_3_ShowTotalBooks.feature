#- F001_3 ) Varukorgen visar alltid aktuell summa och antal böcker


Feature: Remove book
    ******  User can always see the books list and total   ******

    Scenario: User can see the book list and total in the basket
        Given User has books in basket list
        When  User asks to see the basket
        Then  Book basket list and total is show

