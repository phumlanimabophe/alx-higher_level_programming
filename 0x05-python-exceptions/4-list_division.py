#!/usr/bin/python3
    new_list = []
    for i in range(list_length):
        try:
            result = 0  # Default division result
            if i < len(my_list_1) and i < len(my_list_2):
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                    if divisor != 0:
                        result = dividend / divisor
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            else:
                print("out of range")
        except Exception:
            result = 0  # Default division result
        finally:
            new_list.append(result)
    return new_list
