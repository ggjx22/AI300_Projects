from b_write_your_own_class import CreditCard

class RewardsCards(CreditCard): # inherits from CreditCard
    
    # create constructor
    def __init__(self, account_number, credit_limit, rewards_rate):
        # call the superclass's initializer
        super().__init__(account_number, credit_limit)
        # add additional instance attributes
        self.rewards_rate = rewards_rate
        self._rewards_points = 0
    
    # method that inherits make_purchase method of class CreditCard and calculates rewards points base on purchase amount and rewards_rate
    def make_purchase(self, purchase_amount):
        super().make_purchase(purchase_amount)
        self._rewards_points += self.rewards_rate * purchase_amount
    
    # method that gets the rewards point
    def get_rewards_points(self):
        return self._rewards_points
    
    # method that calculates remaining rewards_points after redeeming some points
    def redeem_rewards_points(self, points_redeem):
        self._rewards_points -= points_redeem


# # test development for class RewardsCard
# my_rewards_card = RewardsCards(987654321, 2000, 0.02)

# assert my_rewards_card.account_number == 987654321
# assert my_rewards_card._credit_limit == 2000 
# assert my_rewards_card.rewards_rate == 0.02

# my_rewards_card.make_purchase(100)
# assert my_rewards_card.get_rewards_points() == 2

# my_rewards_card.redeem_rewards_points(1)
# assert my_rewards_card.get_rewards_points() == 1

# print('All tests passed!')