def count_substring(string, sub_string):
    count=0
    #print(len(string),len(sub_string))
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count

#ahorter code
def count_substring(string, sub_string):
    return(sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))

    if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)