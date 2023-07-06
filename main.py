
from data import Work


def run():
    while True:
        choice_method = input('Виберіть метод: append for dict, append for tuple, popitem, pop, clear, items, values, keys, index, count:   ')
        w = Work()

        if choice_method == 'append for dict':
            w.append_dict()

        if choice_method == 'append for tuple':
            w.append_tuple()

        if choice_method == 'popitem':
            w.popitem()

        if choice_method == 'pop':
            w.pop()

        if choice_method == 'clear':
            w.clear()

        if choice_method == 'items':
            w.items()

        if choice_method == 'values':
            w.values()

        if choice_method == 'keys':
            w.keys()

        if choice_method == 'index':
            w.index()

        if choice_method == 'count':
            w.count()



run()