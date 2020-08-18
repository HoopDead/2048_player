import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from random import randint

Game = True


driver = webdriver.Chrome('/mnt/d/Programs/Projekty/2048_player/chromedriver.exe')
driver.get('https://play2048.co/')

if __name__ == "__main__":
    print("Im working!")
    while Game:
        main_window = driver.find_element_by_tag_name("body")
        main_window.send_keys(Keys.ARROW_UP)
        main_window.send_keys(Keys.ARROW_LEFT)
        main_window.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.25)