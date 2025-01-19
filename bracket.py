def bracket_check(test_string):
    if test_string.startswith('(') and test_string.endswith(')') or test_string == "":
        print('YES')
    else:
        print('NO')


