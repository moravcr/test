import time


def passengers(passengers_list, a, b):
    driver = [a, b]
    # координаты вектора водителя
    ab = ((b[0] - a[0], b[1] - a[1]))
    # проверяем направление векоторов пассажиров, 
    # если совпадает с направлением водителя, 
    # то оставляем в списке, если нет то удаляем
    updated_list = []
    for passenger in passengers_list:
        vector = ((passenger[1][0] - passenger[0][0], passenger[1][1] - passenger[0][1]))
        scalar = ab[0] * vector[0] + ab[1] * vector[1]
        if scalar >= 0:
            updated_list.append(passenger)
    # если нет подходящего пассажира
    if not updated_list:
        print("никто не подходит")
        return


    # Функция для вычисления расстояния между двумя точками
    def distance(point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


    # Функция для вычисления расстояния от начальной точки прямой до точки a
    def distance_to_driver(line):
        return distance(line[0], driver[0])
    
    # сортировать список по расстоянию от точки А
    lines = sorted(updated_list, key=distance_to_driver)
    print(lines)
    # добавляем координаты точек А и Б в список как линии 
    lines.insert(0, [a, a])
    lines.append([b, b])


    def l2(x, y):
        return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

    graph = {}
    choice = 2
    for i in range(len(lines) + 1):
        if i < len(lines) - choice + 1:
            graph[i] = set([_ for _ in range(i + 1, i + choice + 1 )])
        else:
            graph[i] = set([_ for _ in range(i + 1, len(lines)+1)])

    visited = [None]*(len(lines))
    distances = [1e7]*(len(lines))

    q = set(v for v in range(len(lines)))
    distances[0] = 0


    # свободный клиент до которого минимальное расстояние
    def mindist(distances):
        minimum = 1e7
        min_index = None
        for v in q:
            if distances[v] < minimum:
                minimum = distances[v]
                min_index = v
        return min_index


    while q:
    #     выбрать клиента с минимальным известным расстоянием
        u = mindist(distances)
        q.remove(u)
        
    #     по каждому свободному клиенту
        for v in graph[u]:
            if v in q:
    #             посчитать расстояние уже пройденное + расстояние до клиента + расстояние поездки
                tmp = distances[u] + l2(lines[u][1], lines[v][0]) + l2(lines[v][0], lines[v][1])
    #             обновить если расстояние меньше чем уже известное
                if tmp < distances[v]:
                    distances[v] = tmp
                    visited[v] = u


    # вывести список клиентов и расстояние
    order = []
    last = len(visited) - 1
    while last is not None:
        order.append(last)
        last = visited[last]
    print('clients visited', list(reversed(order))[1:len(list(reversed(order)))-1])
    print('min Distance : ', distances[-1])
    # print('graph', graph)


if __name__ == "__main__":
    # входные данные - массив координат пассажиров, начальные и конечные координаты A B водителя
    lines = [[(-4, -3), (-2, -1)], [(-3, 0), (0, 1)], [(0, 2), (3, 3)], [(5, 4), (6, 5)], [(5, -7), (-9, 3)], [(-5, -6), (-2, -3)], [(0, 2), (10, 10)]]
    a = (-10, -10)
    b = (10, 10)
    results = passengers(lines, a, b)