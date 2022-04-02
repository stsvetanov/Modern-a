try:

    amounts = {}
    with open("Task2/amounts.txt") as f:
        for line in f:
            (val, key) = line.split()
            amounts[float(val)] = key

    exchange = {}
    with open("Task2/exchange.txt") as f:
        for line in f:
            (key, val) = line.split()
            exchange[key] = float(val)

    for amnt in amounts:
        for exch in exchange:
            if amounts[amnt] == exch:
                print(round((amnt / exchange[exch]), 2))
except:
    print("INVALID INPUT")