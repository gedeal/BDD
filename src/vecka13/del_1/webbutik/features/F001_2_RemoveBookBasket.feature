#- F002 - Användaren kan ta bort böcker från varukorgen

Feature: Remove book
    ******  User can remove book from list   ******

    Scenario: User removes book from list
        Given user has books in list
        When user removes book from list
        Then book is removed from in list
