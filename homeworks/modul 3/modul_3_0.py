calls = 0
def count_calls ():
   global calls
   calls += 1
def string_info(string):
    list = [len(string),string.upper(),string.lower()]
    count_calls()
    return list
def is_contains(string,list_to_search):
    for i in list_to_search:
        if i.upper() == string.upper():
            return True
    count_calls()
    return False
print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
