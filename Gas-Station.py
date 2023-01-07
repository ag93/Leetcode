def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    totalGas = sum(gas)
    totalCost = sum(cost)
    
    if totalCost > totalGas:
        return -1

    n = len(gas)
    total_gas = 0
    start = 0
    remaining = 0
    for i in range(n):
        total_gas += gas[i] - cost[i]
        remaining += gas[i] - cost[i]
        print(i, total_gas, remaining)
        if remaining < 0:
            start = i + 1
            remaining = 0
    return start if total_gas >= 0 else -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(canCompleteCircuit(gas, cost))