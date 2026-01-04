import random
import math

ERROR_MESSAGE_1 = 'Несовпадение размера матрицы расстояний'
ERROR_MESSAGE_2 = 'Несовпадение строки матрицы'


def ant(n: int, distances: list, a, b, q: int, p: float, generations: int) -> None:
    # ПроверОчка
    assert len(distances) == n, ERROR_MESSAGE_1
    for i, item in enumerate(distances):
        assert len(item) == n - 1, ERROR_MESSAGE_2
        pass
    pheromones = [[0.2 for i in range(n - 1)] for j in range(n)]
    print(f'\nИсходная матрица феромонов: {pheromones}')
    print(f'Матрица расстояний: {distances}\n')

    # Массив с решениями
    all_routes = []

    def passage(start: int) -> tuple[int, list[int]]:
        nonlocal delta_pheromones
        # Матрица дельт для изменения
        local_distances = distances.copy()
        # Массив с номерами городов
        route = [start]
        # Массив с координатами феромонов в матрице
        routes = []
        # Длина маршрута
        route_len = 0
        # print(local_distances, '\n')
        # Номер актуального города
        j = start
        while len(route) < n:
            # Сумма вероятностей для перехода
            prob_sum = 0
            # Массив с вероятностями перехода
            prob = [0]
            # Массив с возможными городами для перехода
            possible = [i for i in range(n) if i not in route]
            # print(f'Массив с возможными городами для перехода из {j}:\n{possible}')

            # Подсчет prob_sum
            for i in possible:
                # Нужная ячейка в таблице
                in_table = [j, i - 1] if j < i else [j, i]
                # print(in_table)
                # Актуальные дистанция и феромон для возможной ячейки
                actual_closeness = 1 / distances[in_table[0]][in_table[1]]
                actual_pheromone = pheromones[in_table[0]][in_table[1]]
                # print(
                #     f'Для {i}:\nБлизость:{actual_closeness}\nФеромон:{actual_pheromone}\n')
                prob_sum += actual_closeness ** a + actual_pheromone ** b
            # Подсчет prob
            for i in possible:
                in_table = [j, i - 1] if j < i else [j, i]
                # print(in_table)
                actual_closeness = 1 / distances[in_table[0]][in_table[1]]
                actual_pheromone = pheromones[in_table[0]][in_table[1]]
                prob.append(((actual_closeness ** a + actual_pheromone ** b) / prob_sum) + prob[-1])
            #     print(f'Вероятность перехода для {i}: {(actual_closeness ** a + actual_pheromone ** b) / prob_sum}')
            # print(prob)

            # Выбор случайного числа на последовательности
            rng = random.uniform(0, 1)
            i = 1
            while i < len(prob):
                if prob[i - 1] < rng < prob[i]:
                    pick = possible[i - 1]
                    break
                i += 1

            # pick = random.choice(possible)
            # print('pick:', pick)
            # print(j, pick)

            # Нужная ячейка в таблице (также как сверху, только для выбранного)
            in_table = [j, pick - 1] if j < pick else [j, pick]
            # print(in_table)
            # print('В таблице:', distances[in_table[0]][in_table[1]])
            # print('Феромон:', pheromones[in_table[0]][in_table[1]], '\n')

            # Добавка нового города в общий массив
            route.append(pick)
            # Увеличение длины маршрута
            route_len += distances[in_table[0]][in_table[1]]
            # Добавление координат перехода
            routes.append([in_table[0], in_table[1]])
            # Переход к следующему  городу
            j = pick

        # Добавление последнего перехода
        route.append(start)
        in_table = [route[-2], route[-1] - 1] if route[-2] < route[-1] else [route[-2], route[-1]]
        route_len += distances[in_table[0]][in_table[1]]
        routes.append([in_table[0], in_table[1]])

        # print(f'Координаты переходов маршрута: {routes}')
        # print(f'Длина маршрута: {route_len}')
        # print(f'Маршрут: {route}\n')

        # Обновление матрицы изменения феромонов
        for i in routes:
            delta_pheromones[i[0]][i[1]] += q / route_len
        # print(f'Матрица изменения феромонов: {delta_pheromones}')

        return route_len, route

    for i in range(generations):
        delta_pheromones = [[0 for i in range(n - 1)] for j in range(n)]
        for i in range(n):
            all_routes.append(passage(i))
        for i, item in enumerate(delta_pheromones):
            for j, jtem in enumerate(item):
                pheromones[i][j] = pheromones[i][j] * p + jtem

    all_routes.sort(key=lambda element: element[0])
    print(f'Конечная матрица феромонов: {pheromones}\n')
    print('Лучшие решения:')
    for i in range(10):
        print(all_routes[i])


if __name__ == '__main__':
    # ant(5, [[4, 5, 7, 5], [8, 5, 6, 6], [3, 5, 9, 6], [3, 5, 6, 2], [6, 2, 3, 8]], 1, 1, 4, 0.9, 150)
    # ant(5, [[38, 74, 59, 45], [38, 46, 61, 72], [74, 46, 49, 85], [59, 61, 49, 42], [45, 72, 85, 42]], 1, 1, 4, 0.9, 150)
    ant(4, [[23, 25, 19], [19, 16, 18], [25, 10, 10], [9, 4, 13]], 1, 1, 4, 0.9, 10)
