for row in range(1,11):
    for column in range(1,11):
        product = row * column
        if product < 10:
            print('', product, '', end='')   #adds space if product is single digit
        else:
            print(product, '', end='')
    print()