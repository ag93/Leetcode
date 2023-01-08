def minimumHealth(damage, armor):
    """
    :type damage: List[int]
    :type armor: int
    :rtype: int
    """

    minimumHealthNeeded = sum(damage) + 1
    if(armor == 0):
        return minimumHealthNeeded

    max_damage = max(damage)
    if armor > max_damage:
        minimumHealthNeeded -= max_damage
    else:
        minimumHealthNeeded -= armor 

    return minimumHealthNeeded


if __name__ == "__main__":
    damage = [2,5,3,4]
    armor = 7

    print(minimumHealth(damage, armor))