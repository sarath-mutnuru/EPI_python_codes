def get_max_profit(prices):
    min_price_till_i = float("inf")
    buy_idx = -1
    sell_idx = -1
    max_profit = float("-inf")

    for idx, p in enumerate(prices):
        if min_price_till_i > p:
            min_price_till_i = p
            buy_idx = idx

        if (p - min_price_till_i) > max_profit:
            max_profit = p - min_price_till_i
            sell_idx = idx
    return buy_idx, sell_idx, max_profit


def main():
    prices = [5,3,4,8]
    res = get_max_profit(prices)
    print("buy at {} on {}th day, sell at {} on {}th day, maximum profit is {}".
          format(prices[res[0]], res[0], prices[res[1]], res[1], res[2]))


if __name__ == '__main__':
    main()
