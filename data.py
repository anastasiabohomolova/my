class Work:

    def __init__(self):
        self.dict_t = {'name': 'Mary', 'food': 'junk food', 'dog': 'Tao', 'age': 21}
        self.tuple_e = (1, 1, 1, 'salary', 'salary', 'name', 32323, 'home')

    def append_dict(self):
        el = input('choice: item, key, value : ')
        if el == 'key':
            k = input('print element for key: ')
            for key in self.dict_t.keys():
                if k == key:
                    etap = input('e takuy key, miniemo yogo znachina? yes or no: ')
                    if etap == 'yes':
                        value = input('print new value: ')
                        self.dict_t[k] = value
                        #print(self.dict_t)
                        break
        elif el == 'value':
            v = input('print el: ')
            for value in self.dict_t.values():
                if v == value:
                    etap = input('takuy value e, minaemo na new value: yes or no: ')
                    if etap == 'yes':
                        new_value = input('print new value')
                        new_key = input('print new key: ')
                        self.dict_t[new_key] = new_value
                        print(self.dict_t)
                        break
            new_key = input('print new key: ')
            self.dict_t[new_key] = v
            print(self.dict_t)

        elif el == 'item':
            new_k = input('print key: ')
            new_v = input('print value: ')
            #item = self.dict_t.setdefault('new_k', 'new_v')
            #print(item)
            for items in self.dict_t.items():
                if new_k and new_v != items:
                    item = self.dict_t.setdefault(new_k, new_v)
                    print(self.dict_t)
                elif new_k == items and new_v == items:
                    print('taki elementu e')
                break

    def append_tuple(self):
        add_el = input('choice type str or int: ')
        if add_el == 'int':
            n_int = int(input('print int: '))
            new_t = self.tuple_e + (n_int, )
            print(new_t)
        elif add_el == 'str':
            n_str = input('print str:' )
            new_t = self.tuple_e + (n_str, )
            print(new_t)


    def popitem(self):
        p_it = self.dict_t.popitem()
        print(p_it)

    def pop(self):
        k = input('Print key: ')
        p_op = self.dict_t.pop(k)
        print(p_op)

    def clear(self):
        clr = self.dict_t.clear()
        print(clr)

    def items(self):
        i_tms = self.dict_t.items()
        print(i_tms)

    def values(self):
        v_es = self.dict_t.values()
        print(v_es)

    def keys(self):
        k_ys = self.dict_t.keys()
        print(k_ys)

    def index(self):
        el = input('ch int or str: ')
        if el == 'int':
            vubir = int(input('print int: '))
            ind = self.tuple_e.index(vubir)
            print(ind)
        elif el == 'str':
            vubir_2 = str(input('print str: '))
            ix = self.tuple_e.index(vubir_2)
            print(ix)

    def count(self):
        ch = input('choise int or str: ')
        if ch == 'int':
            number = int(input('print numder: '))
            c_nt = self.tuple_e.count(number)
            print(c_nt)
        elif ch == 'str':
            element = input('print el: ')
            c_nt = self.tuple_e.count(element)
            print(c_nt)








