def backpack(weight: tuple, price: tuple, capacity) -> None:
    v_table = [[0 for _ in range(capacity + 1)]]
    tf_table = [[tuple([False]) for _ in range(capacity + 1)]]
    link_table = [[tuple([[0, 0]]) for _ in range(capacity + 1)]]
    # Row
    for i in range(len(weight)):
        # Column
        for j in range(capacity + 1):
            # If (capacity[r] - weight[i]) >= 0
            if j - weight[i] >= 0:
                print(f'weight {weight[i]} price {price[i]} {v_table[i]}')
                # If row exists add upper cell or curr price + price[capacity[r]-weight[i]]
                if price[i] + v_table[i][j - weight[i]] > v_table[i][j]:
                    v_table[i + 1].append(price[i] + v_table[i][j - weight[i]])
                    tf_table[i + 1].append(tuple([True]))
                    link_table[i + 1].append(tuple([[i, j - weight[i]]]))
                elif price[i] + v_table[i][j - weight[i]] < v_table[i][j]:
                    v_table[i + 1].append(v_table[i][j])
                    tf_table[i + 1].append(tuple([False]))
                    link_table[i + 1].append(tuple([[i, j]]))
                else:
                    v_table[i + 1].append(v_table[i][j])
                    tf_table[i + 1].append((True, False))
                    link_table[i + 1].append((tuple([[i, j - weight[i]], [i, j]])))
                print_table(v_table)
                print_table(tf_table)
                print_table(link_table)
            else:
                print(f'weight {weight[i]} price {price[i]} {v_table[i]}')
                # If row exists add upper cell
                if i + 1 < len(v_table):
                    v_table[i + 1].append(v_table[i][j])
                    tf_table[i + 1].append(tuple([False]))
                    link_table[i + 1].append(tuple([[i, j]]))
                else:
                    v_table.append([0])
                    tf_table.append([tuple([False])])
                    link_table.append([tuple([[0, 0]])])
                print_table(v_table)
                print_table(tf_table)
                print_table(link_table)

    print_table(v_table)
    solutions = []

    def rec(j=len(weight), i=capacity, solution=[]):
        for inter, x in enumerate(link_table[j][i]):

            print(tf_table[j][i][inter], end=' ')
            print('| j:', j, 'i:', i, '| value:',
                  v_table[j][i], 'link:', link_table[j][i],
                  '\n', 'x:', x, 'inter:', inter)
            print(solution)
            # print([i for i in range(1, 7)])
            # print(weight)
            print('\n')

            if i == 0 and j == 0:
                solutions.append(solution)
                return None

            if tf_table[j][i][inter]:
                solution.append(j)

            if inter > 0:
                rec(x[0], x[1], [solution])
            else:
                rec(x[0], x[1], solution)

        return None

    rec()
    for i, item in enumerate(solutions):
        for j, jtem in enumerate(item):
            if isinstance(jtem, list):
                # print(jtem[0:len(jtem)-(len(item)-1)])
                solutions[i][j] = jtem[0:len(jtem) - (len(item) - 1)]
    print(solutions)


def print_table(v_table):
    for i in v_table:
        for j in i:
            print(j, ' ', end='')
        print(' ')
    print('')


def main():
    # backpack((1, 3, 3, 3, 1, 2), (2, 1, 4, 4, 5, 2), 7)
    # backpack((2, 1, 3, 4), (3, 2, 4, 5), 5)
    backpack((1, 15, 15, 15, 1), (5, 50, 50, 50, 5), 16)
    # backpack((4, 3, 1, 3, 2), (5, 2, 2, 4, 3), 7)
    # backpack((2, 3, 4, 5), (3, 4, 5, 6), 7)


if __name__ == '__main__':
    main()
