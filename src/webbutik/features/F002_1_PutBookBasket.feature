#- F002_1) Rabattfunktion. Om användaren köper fler än tre böcker skall hon få 10% rabatt
#          på hela kundkorgen. Testa flera olika fall, inklusive värden som är osannolika
#          som -1000 och 64000 böcker.

Feature: Give discount
    *****  User gets discount when buing many books  ******

    Scenario: user buys more then 3 books - get 10% discount
        Given user puts 3 books in basket
        When  user adds one more book
        And   the total nr of books is more then 3
        Then  user gets 10% discont on total price


#   Scenario: user buys more then 100 books - gets  fail message
#        Given user puts more them 100 books in basket
#        When  the total nr of books is more then 100
#        Then  user gets fail message (to big number)
#
#
#   Scenario: user buys less then 0 books - gets fail message
#        Given user has no books in basket
#        When  user removes 1 books fron basket
#        Then  user gets fail message (can not be negative)