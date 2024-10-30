calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        if i.lower() == string:
            return True
    return False
    return string.lower() in [item.lower() for item in list_to_search]

print(string_info("Capibara"))
print(string_info("Armagedon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))
print(is_contains("cycle", ["recycling", "cyclic"]))

print(calls)