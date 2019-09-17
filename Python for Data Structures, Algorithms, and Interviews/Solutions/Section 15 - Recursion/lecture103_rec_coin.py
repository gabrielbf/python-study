'''
Section 15 - Lecture 103 - Coin Change Interview Problem

rec_coin_meu    Minha solução para o problema usando recursão
rec_coin        Solução do curso sem memoização
rec_coin_dynam  Solução do curso com memoização
'''


def rec_coin_meu(target, coins):
    # Base case
    if (target == 0) or (not coins):
        return 0
    else:
        if target // coins[len(coins) - 1] > 0:
            return 1 + rec_coin_meu(target - coins[len(coins) - 1], coins)
        else:
            return rec_coin_meu(target, coins[:-1])


def rec_coin(target, coins):
    # Base case
    min_coins = target

    if target in coins:
        return 1

    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            # Recursive Call (add a coint coin and subtract from target)
            num_coins = 1 + rec_coin(target - i, coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


def rec_coin_dynam(target, coins, known_results):

    # Default output to target
    min_coins = target

    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        # for every coin value that is <= than target
        num_coins = 1 + rec_coin_dynam(target, coins, known_results)

        # Reset Minimum if we have a new minimum
        if num_coins < min_coins:
            min_coins = num_coins

            # Reset the known_results
            known_results[target] = min_coins

    return min_coins
