def lorry_load(n, names, weights, prices):
    sorted_prices = sorted(prices, reverse=True)
    free_space = n
    value = 0
    items = []

    for price in sorted_prices:
        item_weight = weights[prices.index(price)]
        diff = free_space - item_weight
        if diff > 0:
            free_space -= item_weight
            value += item_weight * price
            items.append((item_weight, names[prices.index(price)]))
        else:
            value += free_space * price
            items.append((free_space, names[prices.index(price)]))
            # No more free space to put more items
            break

    print(f'Load composition value = {value}')
    print(' and '.join([f'{item[0]} kg of {item[1]}' for item in items]))

    # while True:
    #     items_name = input("Enter the item's name: ")
    #     items_weight = input("Enter the items name, weights, and price per kilo: ")
    #     items_ = input("Enter the items name, weights, and price per kilo: ")
    # items_list = items.split(",")


items_name = ["gold", "copper", "plastic"]
items_weight = [400, 700, 150]
items_price = [100, 65, 30]

weight_limit = 1000
lorry_load(weight_limit, items_name, items_weight, items_price)
