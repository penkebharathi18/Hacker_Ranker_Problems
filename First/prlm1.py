def merge_the_tools(string, k):
    for i in range(0, len(string), k):   # step by k
        substring = string[i:i+k]
        result = ""
        for ch in substring:
            if ch not in result:   # avoid duplicates but keep order
                result += ch
        print(result)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)