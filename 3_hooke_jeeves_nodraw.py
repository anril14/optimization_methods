def f(x1, x2):
    return x1 ** 2 + 3 * x2 ** 2 + 3 * x1 * x2 - x1 - 2 * x2 - 1


x1, x2 = 3, 3


def hooke_jeeves(i=-1, x1=2.0, x2=3.0, dx1=1.0, dx2=1.0,
                 is_next_i=True, delta=2.0, acc_ratio=2.2, eps=0.01):
    old_point = dict({'x1': x1, 'x2': x2})
    fx0 = f(x1, x2)

    def check_x1():
        nonlocal x1, x2
        print(f'\nИтерация: {i}\nПроверка нового X1: X1 {x1} X2 {x2}'
              f' dX1 {dx1} dX2 {dx2}')
        if f(x1 + dx1, x2) < fx0:
            x1 = x1 + dx1
            print('X1 увеличен до:', x1)
            check_x2()
        elif f(x1 - dx1, x2) < fx0:
            x1 = x1 - dx1
            print('X1 уменьшен до:', x1)
            check_x2()
        else:
            check_x2()

    def check_x2():
        nonlocal dx1, dx2, x1, x2, is_next_i
        print(f'Проверка нового X2: X1 {x1} X2 {x2} dX1 {dx1} dX2 {dx2}')
        if f(x1, x2 + dx2) < fx0:
            x2 = x2 + dx2
            print('X2 увеличен до:', x2)
        elif f(x1, x2 - dx2) < fx0:
            x2 = x2 - dx2
            print('X2 уменьшен до:', x2)
        else:
            if old_point['x1'] == x1 and dx1 >= dx2:
                print('Дельта X1 уменьшена')
                dx1 /= delta
                is_next_i = False
            dx2 /= delta
            print('Дельта X2 уменьшена')

        if old_point['x1'] != x1 and old_point['x2'] != x2:
            print('*Шаг ускорения применен')
            acc_step()

    def acc_step():
        # var acc_ratio is acceleration step ratio when multiplying
        nonlocal x1, x2
        print(f'*До шага ускорения: X1 {x1} X2 {x2}')
        if f(x1, x2) > f((x1 - old_point['x1']) * acc_ratio + old_point['x1'],
                         (x1 - old_point['x2']) * acc_ratio + old_point['x2']):
            x1 = (x1 - old_point['x1']) * acc_ratio + old_point['x1']
            x2 = (x2 - old_point['x2']) * acc_ratio + old_point['x2']
            print('Оба значения были изменены')
        elif f(x1, x2) > f((x1 - old_point['x1']) * acc_ratio + old_point['x1'], x2):
            x1 = (x1 - old_point['x1']) * acc_ratio + old_point['x1']
            print('X1 Был изменен')
        elif f(x1, x2) > f(x1, (x1 - old_point['x2']) * acc_ratio + old_point['x2']):
            x2 = (x2 - old_point['x2']) * acc_ratio + old_point['x2']
            print('X2 Был изменен')
        print(f'*Значения после шага: X1 {x1} X2 {x2}')

    # Delta condition
    if dx1 > eps and dx1 > eps:
        # Checking for delta changes only
        if is_next_i:
            i += 1

        is_next_i = True
        check_x1()

        return hooke_jeeves(i, x1, x2, dx1, dx2, is_next_i)
    else:
        print(f'Финальные значения: X1 {x1} X2 {x2}')


hooke_jeeves(x1=x1, x2=x2)
