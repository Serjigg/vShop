import random


COLOR = ["з", "к", "с"]
class Obj:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

def sort_objects_points(objects: list[Obj], order: str) -> list:
    """
    :param objects: list[str] - список с цветами
    :param order:  string - отношение порядка цветов. пример("зcк")
    :return: sorted list - сортированный список состоящий из строк(цвет объекта)
    :return: None - если передали пустой список
    сортирует список с объектами по условию заданным вторым аргументом

    """
    if not objects:
        return None
    color_order = {}
    for ind, col in enumerate(order):
        color_order[col] = ind
    print(color_order)
    left = 0
    center = 0
    right = len(objects) - 1

    while center <= right:
        if color_order[objects[center].color] == 0:
            objects[left], objects[center] = objects[center], objects[left]
            left += 1
            center += 1
        elif color_order[objects[center].color] == 1:
            center += 1
        else:
            objects[center], objects[right] = objects[right], objects[center]
            right -= 1

    return [str(i) for i in objects]


objects = [Obj(random.choice(COLOR)) for i in range(15)]
order = "зск"

sort_objects = sort_objects_points(objects, order)
print(sort_objects)


class Test:

    def test_sorted(self):
        self.color_order = {}
        for ind, col in enumerate(order):
            self.color_order[col] = ind
        sorted_objects = sorted(objects, key=lambda obj: self.color_order[obj.color])
        res1 = [str(i) for i in sorted_objects]
        res2 = sort_objects_points(objects, order)
        assert res1 == res2, f"ожидаем {res1} получили {res2}"
        print('test_sorted success ')

a = Test()
a.test_sorted()



