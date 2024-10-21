calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    count = len(string)
    up_case = string.upper()
    low_case = string.lower()
    return count, up_case, low_case

def is_contains(string, list_to_search):
    count_calls()
    is_true = False
    for x in list_to_search:
        if x == string:
            is_true = True
    return is_true





print(string_info('bla'))
print(is_contains('bla', ['blabla', 'bla']))
print(is_contains('bla', ['blabla', 'not bla']))
print(calls)