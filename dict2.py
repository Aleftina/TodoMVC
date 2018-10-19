#"{},{}".format(index, task)
#'1,Task#1'
def f_a():print('A')
def f_b():print('B')
def f_c():print('C')

actions = {'a': f_a, 'b': f_b, 'c': f_c }
action = 'a'
actions[action]()