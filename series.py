list = [1,2,3,4,5,['a','b',['c']],[3.5,4.0]]
list2 = []
def flatten(input_1, output_1):
    for item in input_1:
        if type(item) is list:
            flatten(item, output_1)
        else:
            output_1.append(item)
flatten(list, list2) 
print(list2)   