import collect_and_handle_data as chd

def f():
    print(chd.list_for_handling)
    

def p():

    questions = {'1 + 1':2,'1 - 1':0,'1 * 1':1,'1 / 1':1}
    user_dict = {}
    for x in questions:#.items():
        user_answer = input(x+' = \n')
        user_dict[x] = user_answer
        
        
    count = 0
    for x,y in user_dict.items():
        print(x,y)

    print(count)
    
    

    
