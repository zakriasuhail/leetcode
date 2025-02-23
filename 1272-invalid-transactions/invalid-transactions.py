"""
observations:
- use name as unique id
- we also need to check that all time - 60 transactions are in the same city


key takeaways:
- we can store latest transaction by each user and use that to validate time-city diff


approach - 1:
=============
- create a dict {name : [time, amount, city]}
- whenever there is an invalid transaction because of the city-time diff, pop transactions into a result array

"""
class Solution:

    def __init__(self):
        self.transMap = collections.defaultdict(list)
        self.invalid = []
        self.transactionLimit = 1000

    def isValid(self, transaction):
        name, time, amount, city = transaction.split(",")

        if int(amount) > self.transactionLimit:
            return False

        for prevTime, prevAmount, prevCity in self.transMap[name]:
            if city != prevCity and abs(int(time) - prevTime) <= 60:
                return False
        
        return True
            

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")

            # add to map
            self.transMap[name].append((int(time), int(amount), city))

        
        # validate transactions
        for transaction in transactions:
            if not self.isValid(transaction):
                self.invalid.append(transaction)

        return self.invalid
            

        












        