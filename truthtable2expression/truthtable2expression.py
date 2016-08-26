def base102n(input_int, base, length):
    '''
    parameters: 
        input_int: should be the integer
        base:      should be integer
    return val:
        A list with each digit in the converted number as an element
    '''
    import math
    result = []
    for _ in range(length):
        result = [input_int % base] + result
        input_int = math.floor(input_int / base)
    return result

def basen210(input_list, base):
    '''
    parameters:
        input_list: should be a list, in which each element is a single digit,
                    representing each digit in the integer of base n
        base:       the base. Should be an integer
    return val:
        an integer based in 10
    '''
    if (max(input_list) >= base):
        return -1
    import math
    result = 0
    for i in range(len(input_list)):
        result = result + math.pow(base, i) * input_list[i]
    return math.floor(result)

def testoutput(boolvals, config):
    '''
    parameters:
        boolvals:   a row in truth table. It's a list
        config:     current tested expression configuration. Also a list. 
                    Each element in the list should be [0, 1, 2]. 
                    0: the value
                    1: the not value
                    2: no that symbol
    return val:
        [0, 1]
    '''
    if (len(boolvals) != len(config)):
        return 2
    result = 1
    for i in range (len(boolvals)):
        if (config[i] == 2):
            continue
        if (config[i] == 1):
            result = result * (not boolvals[i])
        if (config[i] == 0):
            result = result * boolvals[i]
    return result

def solver(trtable_result, symbols):
    '''
    parameters:
        trtable_result: Usually the last column of the truth table. The output of the 
                        expression. A list
        symbols:        The symbols will be used to display. It should be a list
    return val:
        A list, in which each element should be connected by or(+)
    '''
    import math
    import itertools
    result = []
    num_res = len(trtable_result)
    if (not(num_res != 0 and ((num_res & (num_res - 1)) == 0))):              # Check if the num_res is power of 2
        return []
    num_var = math.floor(math.log2(num_res))
    if (num_var > len(symbols)):
        return []
    truth_tab = []
    for i in range (num_res):
        truth_tab.append(base102n(i, 2, num_var))
    #print (truth_tab)
    for i in range (basen210(list(itertools.repeat(2, num_var)), 3)):
        cur_conf = base102n(i, 3, num_var)
        for j in range (num_res):
            if (testoutput(truth_tab[j], cur_conf) > trtable_result[j]):
                break;
        else:
            str = ""
            for k in range(num_var):
                if (cur_conf[k] == 0):
                    str = str + symbols[k]
                if (cur_conf[k] == 1):
                    str = str + symbols[k] + '\''
            result.append(str)
    return result

def main():
    #print ('test')
    #print (base102n(18, 3, 5))
    #print (basen210([2, 2, 2], 3)) 
    result = solver([0, 0, 0, 1, 1, 0, 1, 0], ['x', 'y', 'z'])
    result_str = ''
    for str in result:
        result_str += str + '+'
    print (result_str[:-1])

main()
