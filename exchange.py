
# given transactions whose decimal amounts are sampled 
# from a distribution, attempt to pay for the exchange up to the exact 
# amount.
#
# Conventions:
# 0. WLOG the amount%100 is considered.
# 1. If there is less change than the transaction requires, 
#    then a round amount exceeding the cost is used to pay 
#    (i.e., 100 - amount%100 is paid)
# 2. If there is more change than the amount%100, 
#    and exact change is possible, it is done using *as many* coins 
#    as posible;
# 3. If exact change is not possible, then as many coins as possible 
#    are used to minimally exceed the amount.

coin_values = (25,10,5,1)

class Wallet:
    def __init__(self, currency=coin_values):
        self.w = {c:0 for c in currency}
        self.currency = currency
        return
    def sum_coins(self):
        self.s = sum([k*v for k,v in self.w.items()])
        return self.s
    def count_coins(self):
        return sum(list(self.w.values))
    def make_change(self,v):
        '''
        express integer v in terms of coins; in a largest-to-smallest 
        system.
        '''
        con = {c:0 for c in self.currency}
        for c in self.currency:
            i, r = v//c, v%c # number of coins, remainder of division.
            con[c] = i 
            v = r
        return con
    def match(self, v):
        '''
        Attempt to match amount v.
        
        Inputs:
            v : expected integer in [0,100).
        Outputs: None.
        '''
        v = v%100
        
        
        v = (100-v)%100
        new_coins = self.make_change(v)
        
        print(v)
        print(new_coins)
        for key,value in new_coins.items():
            self.w[key] += value
        print(self.w)
        self.sum_coins()
        return None
        
if __name__=="__main__":
    import numpy as np
    wa = Wallet()
    
    wa.match(np.random.randint(100))
    
