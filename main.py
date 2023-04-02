# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    #y = input('\n').split()
    n = int(input())
    
    while not (n > 0 and n <= 1000000):
      print('\n'"Invalid COUNT input, try again COUNT input:")
      n = int(input())
    
    y = []
    y2 = []
    for i in range(n):
        y = input().split()
        
        if (y[0] == 'add'):
          while not (len(y) == 3):
            print('\n'"Invalid ADD COMMAND input, try again ADD COMMAND input:")
            y = input().split()
        else:
          while not (len(y) == 2):
            print('\n'"Invalid FIND or DEL COMMAND input, try again FIND or DEL COMMAND input:")
            y = input().split()
          
        c1=y[1]
        while not (y[1].isdigit() and (len(y[1]) <= 7) and (len(y[1]) >= 1) and (c1[0:1] != '0')):
          print('\n'"Invalid NUMBER input, try again NUMBER input:")
          y[1] = input('\n')
          c1=y[1]
          
        if y[0] == 'add':
          while not (len(y[2]) <= 15 and y[2].isalpha()):
            print('\n'"Invalid NAME input, try again NAME input:")
            y[2] = input('\n')
  
        y2.append(Query(y))
      
    return y2
    #return [Query(input().split()) for i in range(n)]
   
def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = [] # ko drukā uz ekrāna
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [] # add pieprasījumi tiek krāti šajā sarakstā
    for cur_query in queries:
        if cur_query.type == 'add': # cur_query ir tekošais pieprasījums
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
                # eksperimentam:
                #print(cur_query.type)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))