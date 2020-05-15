list_for_handling = ['best100books','best100books2','litres','offered',
                     'philosophy','unfinished']
ready_lists = ['Mirzhan','mob_app','offered_from_study','storybook',
               'study']

path1 = 'D:\\pet_readlit\\pet_readlit\\work\\raw_lists\\'
path2 = 'D:\\pet_readlit\\pet_readlit\\work\\'
expa = '.txt'

def b100b():
    '''b100b'''
    # 1

    file_list = retrieve_data_from_file(list_for_handling[0])
    
    new_list = []
    for x in file_list:
        new_list.append(x[x.index(' - ')+3:].strip('\n'))

    create_new_file(new_list,list_for_handling[0])

def b100b2():
    '''b100b2'''
    # 2
    file_list = retrieve_data_from_file(list_for_handling[1])

    file_list.pop(len(file_list)-1)

    i = 0
    for x in file_list:
        try:
            file_list[i] = x[x.index('.')+2:x.index(',')]
        except ValueError:
            file_list[i] = x[x.index('.')+2:x.rindex('.')]
        i += 1
            
    show_list(file_list)

    create_new_file(file_list,list_for_handling[1])

def litres():
    '''litres'''
    # 3
    file_list = retrieve_data_from_file(list_for_handling[2])

    i = 0
    for x in file_list:
        file_list[i] = x[x.index('.')+2:x.index('(')]
        i += 1

    show_list(file_list)
    
    create_new_file(file_list,list_for_handling[2])
def unfinished():
    # 4
    file_list = retrieve_data_from_file(list_for_handling[5])

    file_list.pop(0)
    file_list.pop(0)
    file_list.pop(len(file_list)-1)
    
    i = 0
    for x in file_list:
        try:
            file_list[i] = x[x.index('"')+1:x.rindex('"')]
            
        except ValueError:
            file_list[i] = x[x.index('.')+2:].strip('\n')
        i += 1

    show_list(file_list)

    create_new_file(file_list,list_for_handling[5])
    

def philosophy():
    # 5
   
    file_list = retrieve_data_from_file(list_for_handling[4])

    file_list.pop(0)
    file_list.pop(len(file_list)-1)
    file_list.pop(len(file_list)-1)
    i = 0
    for x in file_list:
        try:
            file_list[i] = x[x.index('«'):x.rindex('»')+1]
        except ValueError:
            continue
        i += 1

    i = 0
    for x in file_list:
        file_list[i] = x.replace('«','"')
        i += 1

    i = 0
    for x in file_list:
        file_list[i] = x.replace('»','"')
        i += 1

    file_list[4] = 'Боэций Аниций "Комментарий к «Категориям» Аристотеля"'
  
    txt = []
    fili = []
    for x in file_list:
        txt = to_handle_string(x)
        for y in txt:
           fili.append(y)
           
    create_new_file(fili,list_for_handling[4])
 
def retrieve_data_from_file(path_from_list):
    
    file = open(path1+path_from_list+expa,'r',encoding='utf-8')
    some_list = file.readlines()
    file.close()
    return some_list

def create_new_file(some_list,name):
    new_file = open(path2+name+expa,'w',encoding='utf-8')
    fill_file(some_list,new_file)
    new_file.close()

def show_list(some_list):
    for x in some_list:
        print(x)
        
def fill_file(some_list, some_file):
    for x in some_list: some_file.write(x+'\n')

def to_handle_string(string):
    
    quotes_pos = []
    txts = []
    k = 0
    for z in string:
        if z == '"':
            quotes_pos.append(k)            
        k += 1
   
    odd = []
    even = []
    
    j = 0
    for z in quotes_pos:
        if j % 2 == 0:
            odd.append(quotes_pos[j])
        else:
            even.append(quotes_pos[j])
        j += 1
        
    i = 0
    for z in range(0,len(odd)):
        txts.append(string[odd[i]+1:even[i]])
        i += 1

    return txts
        

    
