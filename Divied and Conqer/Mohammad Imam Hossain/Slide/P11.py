# Longest common prefix of n strings

#def compare_prefix(str1, str2):
#    common_prefix = ""
#    min_len = min(len(str1), len(str2))
#   for i in range(min_len):
#       if str1[i] == str2[i]:
#           common_prefix += str1[i]
#       else:
#           break
#    return common_prefix

    
    
def compare_prefix(str1, str2, index=0):
    if index >= min(len(str1), len(str2)): 
        return ""
    
    if str1[index] == str2[index]: 
        return str1[index] + compare_prefix(str1, str2, index + 1)
    else:  
        return ""

def common_prefix(str_list, start, end):
    if start == end:
        return str_list[start]
    else:
        mid = (start + end) // 2
        prefix1 = common_prefix(str_list, start, mid)
        prefix2 = common_prefix(str_list, mid + 1, end)
        return compare_prefix(prefix1, prefix2)

def main():
    strings = ["Algolab", "Algorithms", "Algeria"]
    if not strings:
        print("No strings provided.")
        return
    longest_common_prefix = common_prefix(strings, 0, len(strings) - 1)
    if not longest_common_prefix:
        print("No common prefix exists.")
    else:
        print("Longest common prefix:", longest_common_prefix)

main()

