def check_move_up(list_of_tiles_local):
    n = len(list_of_tiles_local)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    for i in range(n): 
        v = [] 
        w = [] 
        for j in range(n): 
              
            # If not 0 
            if (list_of_tiles_local[j][i]): 
                v.append(list_of_tiles_local[j][i])
        j = 0
        while(j < len(v)): 
              
            if (j < len(v) - 1 and 
               v[j] == v[j + 1]): 
                  
                w.append(2 * v[j]) 
                j += 1
                list_of_operation["merged"] += 1
              
            else: 
                w.append(v[j])
                list_of_operation["tiles_after_move"] += 1
            j += 1
  
        for j in range(n): 
            list_of_tiles_local[j][i] = 0
  
        j = 0
  
        for it in w: 
            list_of_tiles_local[j][i] = it 
            j += 1
    return list_of_operation
    
def check_move_left(list_of_tiles_local):
    n = len(list_of_tiles_local)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    # For each row 
    for i in range(n): 
        v = [] 
        w = [] 

        for j in range(n): 
              
            # If not 0 
            if (list_of_tiles_local[i][j]): 
                v.append(list_of_tiles_local[i][j]) 
        # For each temporary array 
        j = 0
        while(j < len(v)): 
              
            if (j < len(v) - 1 and 
               v[j] == v[j + 1]): 
                  
                # Insert only one element 
                # as sum of two same element. 
                w.append(2 * v[j]) 
                j += 1
                list_of_operation["merged"] += 1
              
            else: 
                w.append(v[j]) 
                list_of_operation["tiles_after_move"] += 1
            j += 1

        # Filling the each row element to 0. 
        for j in range(n): 
            list_of_tiles_local[i][j] = 0

        j = 0

        for it in w: 
            list_of_tiles_local[i][j] = it 
            j += 1
    return list_of_operation

def check_move_right(list_of_tiles_local):
    n = len(list_of_tiles_local)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    for i in range(n):
        v = [] 
        w = [] 

        for j in range(n - 1, -1, -1): 
              
            # if not 0 
            if (list_of_tiles_local[i][j]): 
                v.append(list_of_tiles_local[i][j])
  
        j = 0
        while (j < len(v)): 
            if (j < len(v) - 1 and 
               v[j] == v[j + 1]): 
                  
                w.append(2 * v[j]) 
                j += 1
                list_of_operation["merged"] += 1
              
            else: 
                w.append(v[j]) 
                list_of_operation["tiles_after_move"] += 1
            j += 1
  
        for j in range(n): 
            list_of_tiles_local[i][j] = 0
  
        j = n - 1
   
        for it in w: 
            list_of_tiles_local[i][j] = it 
            j -= 1
    return list_of_operation

def check_move_down(list_of_tiles_local):
    n = len(list_of_tiles_local)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    for i in range(n): 
        v = [] 
        w = [] 
  
        for j in range(n - 1, -1, -1): 
            if (list_of_tiles_local[j][i]): 
                v.append(list_of_tiles_local[j][i]) 
        j = 0
        while(j < len(v)): 
            if (j <len( v) - 1 
                and v[j] == v[j + 1]): 
                w.append(2 * v[j]) 
                list_of_operation["merged"] += 1
                j += 1
            else: 
                w.append(v[j])
                list_of_operation["tiles_after_move"] += 1
            j += 1
                  
        for j in range(n): 
            list_of_tiles_local[j][i] = 0  
        j = n - 1
  
        for it in w: 
            list_of_tiles_local[j][i] = it
            j -= 1
    return list_of_operation