"""



"""
class Solution:
    def isValid(self, transaction, transactionsDict):
        name, time, amount, city = transaction.split(",")

        # excess amount
        if int(amount) > 1000:
            return False

        # fraudulent transaction
        for prevTime, prevAmount, prevCity in transactionsDict[name]:
            if abs(prevTime - int(time)) <= 60 and city != prevCity:
                return False
        return True

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # build transaction history
        transactionsDict = defaultdict(list)

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            transactionsDict[name].append((int(time), int(amount), city))

        # validate transactions
        invalidTransactions = []
        for transaction in transactions:
            if not self.isValid(transaction, transactionsDict):
                invalidTransactions.append(transaction)
        return invalidTransactions



