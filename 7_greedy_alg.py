def greedy(start, duration):

    print(start)
    print(duration)

    merged = []

    #[ [start, duration, n(i)] ]
    for i in range(len(start)):
        merged.append([start[i], duration[i], i])
    # print(merged)

    #sort by duration asc, then start asc
    merged.sort(key = lambda element: (element[1], element[0]))
    # print(merged, '\n')

    #seen for already busy time
    seen=[]
    #solurtion is for number of event
    solution = []

    for i in merged:
        x = [x for x in range(i[0], i[1]+i[0])]
        flag = False
        for j in x:
            if j in seen:
                flag = True
                break
        if flag:
            break
        else:
            seen += x
            solution.append(i[2])

    return solution


if __name__ == '__main__':
    print(greedy([1, 0, 3, 0], [4, 1, 2, 4]))