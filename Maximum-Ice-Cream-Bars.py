def maxIceCream(costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count = 0
        for cost in costs:
            if coins - cost >= 0:
                count += 1
                coins = coins - cost
            else:
                break
        
        return count
if __name__ == "__main__":
    costs = [1,6,3,1,2,5]
    coins = 20

    print(maxIceCream(costs, coins))