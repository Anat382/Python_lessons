"""
2) Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.

"""
import collections as cl


class MyNode:
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value=}->{self.left=}+{self.right=}'


def my_search(node, path='', ):
    if node.letter is not None:
        node.value = 0
        return node.letter, path
    if node.right is not None and node.right.value != 0:
        rez = my_search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return rez
    if node.left is not None and node.left.value != 0:
        rez = my_search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return rez


def create_tree(_list_):
    node_list = cl.deque([MyNode(_list_[i], i) for i in _list_])
    # print(node_list)

    for i in range(len(_list_) - 1):
        node_list = cl.deque(sorted(node_list, key=lambda node: node.value))

        first_el = node_list.popleft()
        second_el = node_list.popleft()

        new_node = MyNode(first_el.value + second_el.value, left=first_el, right=second_el)

        node_list.appendleft(new_node)

    return node_list


text = str(input("Введите текст: "))  # 'beep boop beer!'

s_dict = dict(sorted(cl.Counter(text).items(), key=lambda x: x[1]))
# print(s_dict)

tree = create_tree(s_dict)[0]
# print(tree)

table = {}
for _ in range(len(s_dict)):
    k = my_search(tree)
    table[k[0]] = k[1]
del tree
# print(table)

print('Кодированная строка:')
[print(table[char], end=' ') for char in text]
