#- F001_2 ) Användaren kan ta bort böcker från varukorgen

Feature: Remove book
    ******  User remove book from list   ******

    Scenario: User removes book from list
        Given User control books in list
        When  User removes book from list
        Then  Book is removed from in list
