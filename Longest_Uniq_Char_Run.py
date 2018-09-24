
def longest_run_uniq_chars():
    char_string = input()
    num_uniq_chars = int(input())
    
    if len(char_string) < num_uniq_chars:
        return (-1, "char string too short")
    elif num_uniq_chars == 1:
        return (1)
    
    dict_chars = {}
    dict_current = {}
    current_index = 0
    best_total = 0
    
    #add the first number of unique chars to the dictionary
    while len(dict_chars) < num_uniq_chars and current_index < len(char_string):
        if current_index >= len(char_string):
            return (-1)
        if char_string[current_index] not in dict_chars:
            dict_chars[char_string[current_index]] = current_index
            dict_current[char_string[current_index]] = current_index
        else:
            dict_current[char_string[current_index]] = current_index
        current_index += 1

    if len(dict_chars) < num_uniq_chars:
        return (-1, "len dict < num")
        
    while current_index < len(char_string):
        #print (char_string[current_index], "start", start_index, "end", end_index)
        if char_string[current_index] in dict_chars:
            dict_current[char_string[current_index]] = current_index
        else:
            #checks for best total
            sub_total = max(dict_current.values()) - min(dict_chars.values())
            if best_total < sub_total:
                best_total = sub_total

            #remove the lowest index char
            key_to_del = min(dict_current, key=dict_current.get)
            del dict_chars[key_to_del]
            del dict_current[key_to_del]
            dict_chars[char_string[current_index]] = current_index
            dict_current[char_string[current_index]] = current_index
            for k,v in dict_current.items():
                dict_chars[k] = v
        current_index += 1
    
    sub_total = (max(dict_current.values()) - min(dict_chars.values()))
    if best_total < sub_total:
        best_total = sub_total
        
    if len(dict_chars) >= num_uniq_chars:
        return (best_total + 1)
        
test_cases = int(input())

for test in range(test_cases):
    print (longest_run_uniq_chars())