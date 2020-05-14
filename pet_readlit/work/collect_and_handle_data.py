list_for_handling = ['best100books','best100books2','litres','offered',
                     'philosophy','unfinished']
ready_lists = ['Mirzhan','mob_app','offered_from_study','storybook',
               'study']

path1 = 'D:\\pet_readlit\\pet_readlit\\work\\raw_lists\\'
path2 = 'D:\\pet_readlit\\pet_readlit\\work\\'
expa = '.txt'

def best100books():

    
    file = 'D:\\pet_readlit\\pet_readlit\\work\\raw_lists\\' + \
    list_for_handling[0]+'.txt'
    handling_file = open(file,encoding='utf-8')
    handling_file_list = handling_file.readlines()
    handling_file.close()

   
    new_list = []
    for x in handling_file_list:
        new_list.append(x[x.index(' - ')+3:].strip('\n'))

    new_file = open('D:\\pet_readlit\\pet_readlit\\work\\best100books.txt','w')
    fill_file(new_list,new_file)
    new_file.close()

def b100b2():

    file = open(path1+list_for_handling[1]+expa,'r',encoding='utf-8')
    file_list = file.readlines()
    file.close()

    file_list.pop(len(file_list)-1)

    i = 0
    for x in file_list:
        try:
            file_list[i] = x[x.index('.')+2:x.index(',')]
        except ValueError:
            file_list[i] = x[x.index('.')+2:x.rindex('.')]
        i += 1
            
        

    new_file = open(path2+'best100books2'+expa,'w',encoding='utf-8')
    fill_file(file_list,new_file)
    new_file.close()
        
    show_list(file_list)

def litres():

    file = open(path1+list_for_handling[2]+expa,'r',encoding='utf-8')
    file_list = file.readlines()
    file.close()

    i = 0
    for x in file_list:
        file_list[i] = x[x.index('.')+2:x.index('(')]
        i += 1

    new_file = open(path2+'litres'+expa,'w',encoding='utf-8')
    fill_file(file_list,new_file)
    new_file.close()
        
    show_list(file_list)

def unfinished():

    file = open(path1+list_for_handling[5]+expa,'r',encoding='utf-8')
    file_list = file.readlines()
    file.close()

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

    new_file = open(path2+'unfinished'+expa,'w',encoding='utf-8')
    fill_file(file_list,new_file)
    new_file.close()
        
    show_list(file_list)

def philosophy():

    file = open(path1+list_for_handling[4]+expa,'r',encoding='utf-8')
    file_list = file.readlines()
    file.close()


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
    #new_file = open(path2+'philosophy'+expa,'w',encoding='utf-8')
    #fill_file(file_list,new_file)
    #new_file.close()

    i = 0
    for x in file_list:
        if i == 4:
            continue
        file_list[i] = x.replace('«','"')
        i += 1

    i = 0
    for x in file_list:
        file_list[i] = x.replace('»','"')
        i += 1

    txt = []
    fili = []
    for x in file_list:
        txt = to_handle_string(x)
        for y in txt:
            fili.append(y)
    #show_list(file_list)
    show_list(fili)
    print(len(file_list))
    print(len(fili))
    


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
        

    
