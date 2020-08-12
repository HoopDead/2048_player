import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np



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
        for r in (("tile", ""), ("new", ""), ("merged", ""), ("-", ""), ("position", ""), (" ", "")):
            element = element.replace(*r)
        list_of_tile_informations[int(element[1])-1][int(element[2])-1] = int(element[0])
    return list_of_tile_informations


def check_best_move(list_of_tile_informations):
    np_list_of_tile_informations = np.array(list_of_tile_informations)

def check_move_up(list_of_tile_informations):
    for i in range(len(list_of_tile_informations)):
        n = len(list_of_tile_informations)
        v = []
        w = []
        for j in range(n - 1, -1, -1):
            if(list_of_tile_informations[i][j]):
                v.append(list_of_tile_informations[i][j])

        j = 0
        while (j < len(v)): 
                if (j < len(v) - 1 and v[j] == v[j + 1]): 
                    w.append(2 * v[j]) 
                    j += 1
                else: 
                    w.append(v[j])

                j += 1
                for j in range(n): 
                    list_of_tile_informations[i][j] = 0
  
                j = n - 1
                for it in w: 
                    list_of_tile_informations[i][j] = it 
                    j -= 1
    print(list_of_tile_informations)
    
Game = True

if __name__ == "__main__":
    print("Im working!")
    while Game:
        list_of_tiles = get_values_from_tiles()
        list_of_tile_informations = modify_list_of_tiles(list_of_tiles)
        main_window = driver.find_element_by_tag_name("body")
        check_best_move(list_of_tile_informations)
        check_move_up(list_of_tile_informations)