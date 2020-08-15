arr = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 1, 1]
]

print(arr)

def check_move_left(list_of_tile_informations):
    n = len(list_of_tile_informations)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    # For each row 
    for i in range(n): 
        v = [] 
        w = [] 

        for j in range(n): 
              
            # If not 0 
            if (list_of_tile_informations[i][j]): 
                v.append(list_of_tile_informations[i][j]) 
        print(v)
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
            list_of_tile_informations[i][j] = 0

        j = 0

        for it in w: 
            list_of_tile_informations[i][j] = it 
            j += 1
    print("LEFT MOVES", list_of_tile_informations)
    return list_of_operation

check_move_left(arr)