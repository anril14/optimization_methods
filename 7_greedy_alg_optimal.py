def greedy(start, duration, t):

    print('start:    ', start)
    print('duration: ', duration)

    merged = []

    #[ [start, duration, n(i)] ]
    for i in range(len(start)):
        merged.append([start[i], start[i] + duration[i], i+1])
    # print(merged)

    #sort by duration asc, then start asc
    merged.sort(key = lambda element: (element[0], element[1]+element[0]))
    # print(merged, '\n')

    #seen for already busy time
    seen=[]
    #solution is for number of event
    solution = []

    for i in merged:
        flag = False
        for j in [x for x in range(i[0], i[1])]:
            # print(i, j)
            if j in seen or j == t:
                flag = True
                break
        if flag:
            continue
        else:
            # if len(seen + [x for x in range(i[0], i[1])]) > t:
            #     continue
            seen += [x for x in range(i[0], i[1])]
            solution.append(i[2])
    # print(seen)
    return solution


if __name__ == '__main__':
    # print(greedy([1, 0, 3, 0], [4, 1, 2, 4], 5))
    print('Номера мероприятий: ',greedy([1, 0, 3, 0], [4, 1, 1, 4], 4))
