'''
{
    'johnsmith@mail.com': ['John', 'john_newyork@mail.com', 'john00@mail.com'], 
    'john_newyork@mail.com': ['John', 'johnsmith@mail.com'], 
    'john00@mail.com': ['John', 'johnsmith@mail.com'], 
    'mary@mail.com': ['Mary'], 
    'johnnybravo@mail.com': ['John']     
}    


johnsmith@mail.com
    john_newyork@mail.com john00@mail.com




v = [johnsmith@mail.com, john_newyork@mail.com]
    
a = johnsmith@mail.com, res=[], lis=[johnsmith@mail.com]
    a = john_newyork@mail.com, res=[], lis=[johnsmith@mail.com, john_newyork@mail.com]


    After creating the above dict to make connections between the accounts of the same person, perform bfs to combine the accounts of the same person together. 
'''
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        #perform DFS to connect all of the same person accounts together
        visitset = set()
        res = []
        def DFS(account, lis):
            #base case 
            if account in visitset:
                return None
            visitset.add(account) #visitset = ('johmsmith','john_newyork@mail.com' )
            lis.append(account) # lis = ['johnsmith','john_newyork@mail.com']
            for accounts in account_dict[account][1:]:
                DFS(accounts, lis) 

        account_dict = {}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in account_dict:
                    account_dict[account[i]] = [name] + account[1:i] + account[i+1:] 
                else:
                    account_dict[account[i]] += account[i+1:] + account[1:i]

        for account in account_dict:
            if account not in visitset:
                lis = []
                DFS(account, lis)
                lis = sorted(lis)
                res.append([account_dict[account][0]] + lis)

        return res
        
   
    