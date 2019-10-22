# list of name
list_of_names = ['Anna', 'Tim', 'Paul', 'Tim', 'Heinz', 'Tim', 'Clara', 'Peter', 'Tim']

# 2. use the filter function of python
def filter_by_filter(data):
    data = list(filter(lambda x:x!="Tim", data))	
    return data
 
# 3. Filter it using the map function
    
def filterData(x):
    if(x!="Tim"):
        return x
    else:
       return    

def filter_by_map(data):
    data = set(map(filterData, data))
    return data


#4. Filter by my style
def my_style(data):
    return [name for name in list_of_names if name !="Tim"]



#5. Filter using a counter
def filter_by_using_a_counter(data):
    i = 0
    list_len = len(data)
    ret = []
    
    while i < list_len:
        
        if data[i] != 'Tim' :
            ret.append(data[i])
        i = i + 1       
    
    return ret


def test_result(data):    
    for name in data:
        if name == 'Tim':
            return False
    return True


assert test_result(filter_by_using_a_counter(list_of_names.copy()))
assert test_result(filter_by_filter(list_of_names.copy()))
assert test_result(filter_by_map(list_of_names.copy()))
assert test_result(my_style(list_of_names.copy()))
