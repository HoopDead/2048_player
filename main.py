import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from random import randint
from moves import check_move_down, check_move_up, check_move_left, check_move_right
import json


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
def modify_list_of_tiles(list_of_tiles_in):
    rows, cols = (4, 4) 
    list_of_tile_informations = [[0 for i in range(cols)] for j in range(rows)] 
    for element in list_of_tiles_in:
        for r in (("tile ", ""), ("tile-", ""), ("position-", ""), (" new", ""), ("-", ""), (" ", ",")):
            element = element.replace(*r)
        value = element[0:element.index(",")]
        pos = element[element.index(",")+1:]
        list_of_tile_informations[int(pos[0])-1][int(pos[1])-1] = int(value)
    return list_of_tile_informations


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
    if(down_moves["tiles_after_move"] != number_of_tiles_on_board):
        possible_moves["down"] = True
        moves_score["down"] = down_moves["merged"]
    if(left_moves["tiles_after_move"] != number_of_tiles_on_board):
        possible_moves["left"] = True
        moves_score["left"] = left_moves["merged"]
    if(right_moves["tiles_after_move"] != number_of_tiles_on_board):
        possible_moves["right"] = True
        moves_score["right"] = right_moves["merged"]
    return moves_score

def make_best_move(move_score, window):
    best_move = max(move_score, key=move_score.get)
    is_equal = all(value == 0 for value in move_score.values())
    if(is_equal):
        best_move = None
    if(best_move == "up"):
        window.send_keys(Keys.ARROW_UP)
        print("Algorithm move up")
        moves["algo"] += 1
    elif(best_move == "down"):
        window.send_keys(Keys.ARROW_DOWN)
        print("Algorithm move down")
        moves["algo"] += 1
    elif(best_move == "left"):
        window.send_keys(Keys.ARROW_LEFT)
        print("Algorithm move left")
        moves["algo"] += 1
    elif(best_move == "right"):
        window.send_keys(Keys.ARROW_RIGHT)
        print("Algorithm move right")
        moves["algo"] += 1
    else:
        random_move(window)
        moves["random"] += 1
        print("Random move")
    moves["number_of_moves"] += 1

def check_if_game_over():
    element = driver.find_elements_by_xpath("//div[contains(@class, 'game-over')]")
    print(moves)
    if(element):
        driver.find_element_by_xpath('//a[contains(text(), "Try again")]').click()
        with open('results.json') as json_file: 
            data = json.load(json_file) 
            temp = data['algorithm_results']
            temp.append(moves)
            write_json(data)
        moves["random"] = 0
        moves["algo"] = 0
        moves["highest-tile"] = 2
        moves["number_of_moves"] = 0

def write_json(data, filename='results.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      


if __name__ == "__main__":
    atempt = 0
    print("Im working!")
    moves = {"random": 0, "algo": 0, "highest-tile": 2, "number_of_moves": 0}
    while Game:
        list_of_tiles = get_values_from_tiles()
        list_of_tile_informations = modify_list_of_tiles(list_of_tiles)
        list_of_tile_informations_transpose = np.transpose(list_of_tile_informations)
        moves["highest-tile"] = int(np.max(list_of_tile_informations_transpose))
        up_moves = check_move_up(list_of_tile_informations_transpose)
        list_of_tile_informations_transpose = np.transpose(list_of_tile_informations)
        down_moves = check_move_down(list_of_tile_informations_transpose)
        list_of_tile_informations_transpose = np.transpose(list_of_tile_informations)
        left_moves = check_move_left(list_of_tile_informations_transpose)
        list_of_tile_informations_transpose = np.transpose(list_of_tile_informations)
        right_moves = check_move_right(list_of_tile_informations_transpose)
        move_score = check_moves(up_moves, down_moves, left_moves, right_moves, np.count_nonzero(list_of_tile_informations))
        main_window = driver.find_element_by_tag_name("body")
        make_best_move(move_score, main_window)
        check_if_game_over()
        time.sleep(0.1)
        