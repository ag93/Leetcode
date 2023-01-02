def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """

    if word.upper() == word or word.capitalize() == word or word.lower() == word:
        return True
    return False

if __name__ == '__main__':
    word = "Cawffee"
    print(detectCapitalUse(word))