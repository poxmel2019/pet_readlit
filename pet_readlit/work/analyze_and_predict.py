import collect_and_handle_data as chd
sup_list = []
fullist = []
full_texts = []
repeated_texts = []
rep_text_dict = {}
counts = []
categories = ['Mirzhan','mob_app','offered_from_study','storybook',
          'study','best100books','best100books2','litres',
          'offered','philosophy','unfinished','meloman']
categories_dict = {}

def f():

    
    sup_list = chd.ready_list + chd.list_for_handling
    sup_list.append('meloman')

    i = 0
    for x in range(0,len(sup_list)):
        file = open(chd.path2+sup_list[i]+chd.expa,'r',encoding='utf-8')
        file_list = file.readlines()
        fullist.append(file_list)
        file.close()
        i += 1

    j = 0
    for x in fullist:
        categories_dict[categories[j]] = fullist[j]
        for y in x:
            full_texts.append(y)
        j += 1

    count = 0
    i = 0
    while i < len(full_texts):
        handled_text = full_texts[i]
        for x in full_texts:
            if handled_text == x:
                count += 1
        if count > 1:
            repeated_texts.append(handled_text)
            counts.append(count)
            rep_text_dict[handled_text] = count
        count = 0
        i += 1

    set_repeated_texts = set(repeated_texts)
    
    for x,y in rep_text_dict.items():
        print(x + ' - ' + str(y))

    print(len(rep_text_dict))

def create_lists(*args):

    all_list = []
    for x in range(0,*args):
        all_list.append([])

    print(all_list)
    

def p():

    questions = {'1 + 1':2,'1 - 1':0,'1 * 1':1,'1 / 1':1}
    user_dict = {}
    count = 0
    
    for x in questions:#.items():
        user_answer = input(x+' = \n')
        user_dict[x] = user_answer
        

    print(count)

    # 'Mirzhan' # 0
    # 'mob_app' # 1
    # 'offered_from_study' # 2
    # 'storybook' # 3
    # 'study' # 4
    # 'best100books' # 5
    # 'best100books2' # 6
    # 'litres' # 7
    # 'offered' # 8
    # 'philosophy' # 9
    # 'unfinished' # 10
    # 'meloman' # 11

    

    
