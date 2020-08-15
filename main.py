import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from random import randint



driver = webdriver.Chrome('/mnt/d/Programs/Projekty/2048_player/chromedriver.exe')
driver.get('https://play2048.co/')

"""
Desc: Get all values from container and return list of className of tiles  
In: -
out: WebElement list of tiles
"""
def get_values_from_tiles():
    list_of_tiles = list()
    element = driver.find_elements_by_xpath("//div[contains(@class, 'tile-position')]")
    for e in element:
        list_of_tiles.append(e.get_attribute("class"))
    return list_of_tiles


"""
Desc: Modify list_of_tiles to get tile value and its position, String with 3 values - the first value is tile value, the second is positon in x-axis and third is also position in y-axis
In: List of tiles
Out: 2D Array (Matrix) of actual situation in tile container
"""
def modify_list_of_tiles(list_of_tiles):
    rows, cols = (4, 4) 
    list_of_tile_informations = [[0 for i in range(cols)] for j in range(rows)] 
    for element in list_of_tiles:
        for r in (("tile ", ""), ("tile-", ""), ("position-", ""), (" new", ""), ("-", ""), (" ", ",")):
            element = element.replace(*r)
        value = element[0:element.index(",")]
        pos = element[element.index(",")+1:]
        list_of_tile_informations[int(pos[0])-1][int(pos[1])-1] = int(value)
    return list_of_tile_informations

def check_move_up(list_of_tile_informations):
    n = len(list_of_tile_informations)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    for i in range(n): 
        v = [] 
        w = [] 
        for j in range(n): 
              
            # If not 0 
            if (list_of_tile_informations[j][i]): 
                v.append(list_of_tile_informations[j][i])
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
            list_of_tile_informations[j][i] = 0
  
        j = 0
  
        for it in w: 
            list_of_tile_informations[j][i] = it 
            j += 1
    # print("UP MOVES", list_of_tile_informations)
    return list_of_operation
    
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

def check_move_right(list_of_tile_informations):
    n = len(list_of_tile_informations)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    for i in range(n):
        v = [] 
        w = [] 

        for j in range(n - 1, -1, -1): 
              
            # if not 0 
            if (list_of_tile_informations[i][j]): 
                v.append(list_of_tile_informations[i][j])
  
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
            list_of_tile_informations[i][j] = 0
  
        j = n - 1
   
        for it in w: 
            list_of_tile_informations[i][j] = it 
            j -= 1
    return list_of_operation

def check_move_down(list_of_tile_informations):
    n = len(list_of_tile_informations)
    list_of_operation = {"merged": 0, "tiles_after_move": 0}
    for i in range(n): 
        v = [] 
        w = [] 
  
        for j in range(n - 1, -1, -1): 
            if (list_of_tile_informations[j][i]): 
                v.append(list_of_tile_informations[j][i]) 
        j = 0
        while(j < len(v)): 
            if (j <len( v) - 1 
                and v[j] == v[j + 1]): 
                w.append(2 * v[j]) 
                j += 1
                list_of_operation["merged"] += 1
            else: 
                w.append(v[j])
                list_of_operation["tiles_after_move"] += 1
            j += 1
                  
        for j in range(n): 
            list_of_tile_informations[j][i] = 0  
        j = n - 1
  
        for it in w: 
            list_of_tile_informations[j][i] = it
            j -= 1
    # print("DOWN MOVES", list_of_tile_informations)
    return list_of_operation

def random_move(window):
    a = randint(1, 4)
    if (a == 1):
        window.send_keys(Keys.ARROW_LEFT)
        print("Random move left")
    if (a == 2):
        window.send_keys(Keys.ARROW_RIGHT)
        print("Random move right")
    if (a == 3):
        window.send_keys(Keys.ARROW_DOWN)
        print("Random move down")
    if (a == 4):
        window.send_keys(Keys.ARROW_UP)
        print("Random move up")
Game = True

def check_moves(up_moves, down_moves, left_moves, right_moves, number_of_tiles_on_board):
    possible_moves = {"up": False, "down": False, "left": False, "right": False}
    moves_score = {"up": 0, "down": 0, "left": 0, "right": 0}
    if(up_moves["tiles_after_move"] != number_of_tiles_on_board):
        possible_moves["up"] = True
        moves_score["up"] = up_moves["merged"]
    elif(down_moves["tiles_after_move"] != number_of_tiles_on_board):
        possible_moves["down"] = True
        moves_score["down"] = down_moves["merged"]
    elif(left_moves["tiles_after_move"] != number_of_tiles_on_board):
        possible_moves["left"] = True
        moves_score["left"] = left_moves["merged"]
    elif(right_moves["tiles_after_move"] != number_of_tiles_on_board):
        possible_moves["right"] = True
        moves_score["left"] = right_moves["merged"]
    print(possible_moves, moves_score)

if __name__ == "__main__":
    print("Im working!")
    moves = {"random": 0, "algo": 0}
    while Game:
        list_of_tiles = get_values_from_tiles()
        list_of_tile_informations = modify_list_of_tiles(list_of_tiles)
        list_of_tile_informations_transpose = np.transpose(list_of_tile_informations)
        print(list_of_tile_informations_transpose)
        up_moves = check_move_up(list_of_tile_informations_transpose)
        down_moves = check_move_down(list_of_tile_informations_transpose)
        left_moves = check_move_left(list_of_tile_informations_transpose)
        right_moves = check_move_right(list_of_tile_informations_transpose)
        check_moves(up_moves, down_moves, left_moves, right_moves, np.count_nonzero(list_of_tile_informations))
        # move_score = {"up": up_moves["moved"]+up_moves["merged"], "down": down_moves["moved"]+down_moves["merged"], "left": left_moves["moved"]+left_moves["merged"], "right": right_moves["moved"] + right_moves["merged"]}
        # print(move_score)
        # if(move_score["up"] > move_score["down"] and move_score["up"] > move_score["left"]):
        #     main_window.send_keys(Keys.ARROW_UP)
        #     print("Algorithm move up")
        #     moves["algo"] += 1
        # elif(move_score["down"] > move_score["up"] and move_score["down"] > move_score["left"]):
        #     main_window.send_keys(Keys.ARROW_DOWN)
        #     print("Algorithm move down")
        #     moves["algo"] += 1
        # elif(move_score["left"] > move_score["down"] and move_score["left"] > move_score["up"]):
        #     main_window.send_keys(Keys.ARROW_LEFT)
        #     print("Algorithm move left")
        #     moves["algo"] += 1
        # else:
        #     random_move(main_window)
        #     moves["random"] += 1
        time.sleep(0.25)
        