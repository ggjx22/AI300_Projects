# In-Class Practice: Write your own class from scratchod

class CreditCard:
    
    # create constructor
    def __init__(self, account_number, credit_limit):
        # instance attributes
        self.account_number = account_number
        self._credit_limit = credit_limit
        self._current_bal = 0
    
    # method of the class to get account balance
    def get_balance(self):
        return self._current_bal
    
    # method of the class to get the credit limit
    def get_credit_limit(self):
        return self._credit_limit
    
    # method of the class to set the credit limit
    def set_credit_limit(self, new_credit_limit):
        if new_credit_limit < 0 or new_credit_limit > 100000:
            print('Credit limit must be above 0 and positive but also below 100000.')
        else:
            self._credit_limit = new_credit_limit
            
    # method of the class to make a purchase
    def make_purchase(self, purchase_amount):
        if purchase_amount < 0:
            print('Purchase amount less than 0 is invalid.')
        elif self._current_bal + purchase_amount > self._credit_limit:
            print('Credit limit exceeded. Purchase declined. '\
                  'Your current credit card balance is', self.get_balance(),\
                  'and your current purchase amount', purchase_amount,\
                  'will exceed current your credit limit of', self.get_credit_limit(),'.')
        else:
            self._current_bal += purchase_amount
            
    # method of the class to make a credit card payment
    def make_payment(self, payment_amount):
        if payment_amount > self._current_bal:
            over_paid = payment_amount - self._current_bal
            print('You have an outstanding balance of', self._current_bal,\
                  'and you have paid', payment_amount,'.'\
                  'The additional payment of', over_paid, 'will be returned to you and credit card balance will be $0.')
            self._current_bal = 0
        elif payment_amount < 0:
            print('Payment amount must be above 0. Please make a new payment.')
        else:
            self._current_bal -= payment_amount
    
## Uncomment all lines to test your class once completed

# my_credit_card = CreditCard(123456789, 5000)
# assert my_credit_card.account_number == 123456789
# assert my_credit_card.get_balance() == 0
# assert my_credit_card.get_credit_limit() == 5000

# my_credit_card.set_credit_limit(1000)
# my_credit_card.set_credit_limit(-1)       # print error
# my_credit_card.set_credit_limit(100001)   # print error
# print(my_credit_card.get_credit_limit())
# assert my_credit_card.get_credit_limit() == 1000

# my_credit_card.make_purchase(900)
# my_credit_card.make_purchase(-1)          # print error
# my_credit_card.make_purchase(200)         # print error
# assert my_credit_card.get_balance() == 900

# my_credit_card.make_payment(500)
# assert my_credit_card.get_balance() == 400

# my_credit_card.make_payment(5000)
# assert my_credit_card.get_balance() == 0

# print("All tests passed!")
