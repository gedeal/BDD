# - F001_5 ) Det skall gå att tömma varukorgen helt


Feature: erase basket
    ******  User clear the basked    ******

    Scenario: User can clear the basket
        Given User has books in basket
        When  User clears the basket
        Then  Basket is empty