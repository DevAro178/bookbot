def get_word_count(str):
    arr=str.split()
    return len(arr)

def get_char_frequency(str):
    count_dict={}
    for word in str.split():
        for char in word.lower():
            if char in count_dict:
                count_dict[char]+=1
            else:
                count_dict[char]=1
    return count_dict

def sort_on(items):
    return items["num"]

def sort_char_dict(data):
    arr=[]
    for key in data:
        arr.append({"char":key,"num":data[key]})
    arr.sort(reverse=True, key=sort_on)
    return arr