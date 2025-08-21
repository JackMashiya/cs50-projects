def main():
    total_tendered = 0
    coke_price = 50
    coins = [25, 5, 10]

    while total_tendered < coke_price:
        try:
            coin = int(input('Insert coin: '))
        except ValueError:
            continue

        if coin in coins:
            total_tendered += coin
            if total_tendered < coke_price:
                print(f'Amount due: {coke_price - total_tendered}')
        else:
            print(f'Amount Due: {coke_price}')

    print(f'Change owed: {total_tendered - coke_price}')



print(main())
