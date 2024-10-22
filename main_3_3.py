values_list = [True, 42, 'Urban']
values_dict = {'a': 7, 'b': 'string', 'c': False}
values_list_2 =[40, 41]

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42) #баг с тем, что подсвечивается параметр "a", вместо "c" пока не исправили