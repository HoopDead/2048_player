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
    list_of_operation = {"merged": 0, "moved": 0}
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
                list_of_operation["moved"] = 1
              
            else: 
                w.append(v[j])
            j += 1
  
        for j in range(n): 
            list_of_tile_informations[j][i] = 0
  
        j = 0
  
        for it in w: 
            list_of_tile_informations[j][i] = it 
            j += 1
    print("UP MOVES", list_of_tile_informations)
    return list_of_operation
    
def check_move_left(list_of_tile_informations):
    n = len(list_of_tile_informations)
    list_of_operation = {"merged": 0, "moved": 0}
    # For each row 
    for i in range(n): 
        v = [] 
        w = [] 

        # For each element of the 
        # row from left to right 
        for j in range(n): 
              
            # If not 0 
            if (list_of_tile_informations[i][j]): 
                v.append(list_of_tile_informations[i][j]) 

        # For each temporary array 
        j = 0
        while(j < len(v)): 
              
            # If two element have same 
            # value at consecutive position. 
            if (j < len(v) - 1 and 
               v[j] == v[j + 1]): 
                  
                # Insert only one element 
                # as sum of two same element. 
                w.append(2 * v[j]) 
                j += 1
              
            else: 
                w.append(v[j]) 
                  
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

def check_move_down(list_of_tile_informations):
    n = len(list_of_tile_informations)
    list_of_operation = {"merged": 0, "moved": 0}
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
                list_of_operation["moved"] = 1
            else: 
                w.append(v[j])
            j += 1
                  
        for j in range(n): 
            list_of_tile_informations[j][i] = 0  
        j = n - 1
  
        for it in w: 
            list_of_tile_informations[j][i] = it
            j -= 1
    print("DOWN MOVES", list_of_tile_informations)
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

if __name__ == "__main__":
    print("Im working!")
    while Game:
        list_of_tiles = get_values_from_tiles()
        list_of_tile_informations = modify_list_of_tiles(list_of_tiles)
        list_of_tile_informations = np.transpose(list_of_tile_informations)
        print(list_of_tile_informations)
        up_moves = check_move_up(list_of_tile_informations)
        down_moves = check_move_down(list_of_tile_informations)
        left_moves = check_move_left(list_of_tile_informations)
        main_window = driver.find_element_by_tag_name("body")
        move_score = {"up": up_moves["moved"], "down": down_moves["moved"], "left": left_moves["moved"]}
        print(move_score)
        # if(move_score["up"] > move_score["down"] and move_score["up"] > move_score["left"]):
            # main_window.send_keys(Keys.ARROW_UP)
            # print("Algorithm move up")
        # elif(move_score["down"] > move_score["up"] and move_score["down"] > move_score["left"]):
            # main_window.send_keys(Keys.ARROW_DOWN)
            # print("Algorithm move down")
        # elif(move_score["left"] > move_score["down"] and move_score["left"] > move_score["up"]):
            # main_window.send_keys(Keys.ARROW_LEFT)
            # print("Algorithm move left")
        # else:
        #     random_move(main_window)
        time.sleep(0.5)
        Game = False
        