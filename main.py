import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

d = webdriver.Chrome('/mnt/d/Programs/Projekty/2048_player/chromedriver.exe')
d.get('https://www.google.nl/')

if __name__ == "__main__":
    print("Im working!")