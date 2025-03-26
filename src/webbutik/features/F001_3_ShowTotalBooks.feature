#- F003 - Varukorgen visar alltid aktuell summa och antal böcker


Feature: Remove book
    ******  User can see the books list and total   ******

    Scenario: User asks for the book list and total
        Given User has books in list
        When  User asks for the book list
        And   User asks for the total nr of books in list
        Then  Book list and total shows

