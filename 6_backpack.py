def backpack(weight: tuple, price: tuple, capacity) -> None:
    table = [[0 for _ in range(capacity + 1)]]
    # Row
    for i in range(len(weight)):
        # Column
        for j in range(capacity + 1):
            # If (capacity[r] - weight[i]) >= 0
            if j - weight[i] >= 0:
                print(f'weight {weight[i]} price {price[i]} {table[i]}')
                # If row exists add upper cell or curr price + price[capacity[r]-weight[i]]
                table[i + 1].append(max(price[i] + table[i][j - weight[i]],
                                        table[i][j]))
                printtable(table)
            else:
                print(f'weight {weight[i]} price {price[i]} {table[i]}')
                # If row exists add upper cell
                if i + 1 < len(table):
                    table[i + 1].append(table[i][j])
                else:
                    table.append([0])
                printtable(table)


def printtable(table):
    for i in table:
        for j in i:
            print(j, ' ', end='')
        print(' ')
    print('')


def main():
    backpack((2, 1, 3, 4), (3, 2, 4, 5), 5)
    # backpack((4, 3, 1, 3, 2), (5, 2, 2, 4, 3), 7)


if __name__ == '__main__':
    main()
