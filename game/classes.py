class SnakeBlock:  # Класс, описывающий строящиеся блоки на доске(В том числе и яблочкко)
    def __init__(self, x, y):  # объявляем координаты
        self.x = x
        self.y = y

    def is_inside(self, blocks_count):  # Проверяемя, выбранная нами клетка является клеткой, которой сейячас
        # находиьться змея или нет
        return 0 <= self.x < blocks_count and 0 <= self.y < blocks_count

    def __eq__(self, other):  # Метод сравнения двух  объектов этого класса(Равны если координаты равны)
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


class Bad_block:  # Класс барьеров
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Bad_block) and self.x == other.x and self.y == other.y
