class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        from collections import defaultdict
        
        num_bulls = 0
        num_cows = 0
        
        s_dic = defaultdict(int)
        g_dic = defaultdict(int)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_bulls+=1
            else:
                s_dic[secret[i]] +=1
                g_dic[guess[i]] +=1

        for g in g_dic:
            if g in s_dic:
                num_cows += min(g_dic[g],s_dic[g])
        return str(num_bulls)+'A'+str(num_cows)+'B'
            