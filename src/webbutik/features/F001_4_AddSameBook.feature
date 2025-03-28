# - F001_4 ) Om användaren försöker lägga en bok som redan finns i varukorgen ska antalet
#            av just den boken öka istället för att skapa en ny rad

Feature: Add same book only add total, not a new book in list
    ******  User add a new book, not change the list only total    ******

    Scenario: User can add same book in list and only total changes
        Given User has already books in basket list
        When  User adds the same book in basket
        Then  Basket list does not change
        And   The book total changes
