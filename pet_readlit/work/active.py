def f():

    class Book:
        title = None
        author = None
        count = 0
        categories = None
        def __init__(self,count,categories):
            self.count = count
            self.categories = categories
        def __init__(self,title,author,count):
            self.title = title
            self.author = author
            self.count = count
            
        
    bal = 0

    #Data
    there_is = open('there_is.txt','r',encoding='utf-8')
    ts_list = there_is.readlines()
    there_is.close()

    offered = open('offered.txt','r',encoding='utf-8')
    of_list = offered.readlines()
    offered.close()

    best_100 = open('best100.txt','r',encoding='utf-8')
    b_list = best_100.readlines()
    best_100.close()

    cats = ['there_is','offered','best100']
    super_list = ts_list + of_list + b_list

   
    i = 0
    for x in super_list:
        super_list[i] = super_list[i].strip('\n')
        i += 1
        
    #print(super_list)

    dicty = {}
    books = []
    #books = set(books)
    for x in super_list:
        ind = super_list.count(x)
        title = x[:x.index(' -')]
        author = x[x.index('- '):].strip('- ')
        book = Book(title,author,ind)
        books.append(book)
        dicty[x] = ind

    #books = set(books)
    #for x in books:
    #    print(x.title + ' - ' + x.author + ' - ' + str(x.count))

    #print(type(books))

    rates = []
    _books = []
    _nums = []
    
    for x,y in dicty.items():
        _books.append(x)
        _nums.append(y)
        print(x + ' - ' + str(y))
        rates.append(y)

    max_rate = max(_nums)

    i = 0 # it can be improved
    for x in _nums:
        if max_rate == _nums[i]: break
        i += 1

    print('You you read the next book: {0}\
\nBecause it has max rate: {1}\
\nIt\'s categories: '.format(_books[i],max_rate))

    
    

    
        

    
