# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque
from collections import namedtuple
from operator import attrgetter

Foliage = namedtuple('Leaf', 'letters, cnt, code')
MyNode = namedtuple('Node', 'letters, cnt, n_left, n_right')


def my_try(node_list):

    list_node = deque()
    list_node.extend(node_list)

    while len(list_node) > 1:

        node_name = []
        node_left = list_node.popleft()
        node_right = list_node.popleft()
        node_name.extend(node_left.letters)
        node_name.extend(node_right.letters)
        list_node.appendleft(MyNode(node_name, node_left.cnt + node_right.cnt, node_left, node_right))
        list_node = deque(sorted(list_node, key=attrgetter('cnt')))

    return list_node[0]


def my_code(obj, list_letter):

    if hasattr(obj, 'n_left') and hasattr(obj, 'n_right'):

        n_left = obj.n_left
        n_right = obj.n_right

        for key in list_letter:

            if hasattr(n_right, 'letters') and key.letters in n_left.letters:
                key.code.append('0')

            elif hasattr(n_right, 'letters') and key.letters in n_right.letters:
                key.code.append('1')

        return my_code(n_left, list_letter), my_code(n_right, list_letter)
    return None


text = input('Ведите строку:')  # Корабли лавировали, лавировали, да не вылавировали!!!
string = Counter(text)
fol = []
print(string)
for char in string.keys():
    fol.append(Foliage(char, string[char], []))

fol = sorted(fol, key=attrgetter('cnt'))
tree = my_try(fol)
my_code(tree, fol)

print(f'{"*" * 10} Результат кодирования {"*" * 10}')
print(*[key.letters + ': ' + ''.join(key.code) for key in fol], sep='\n')

print(locals())