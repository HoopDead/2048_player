import json
import pandas as pd


with open('results.json') as json_file: 
    data = json.load(json_file) 

columns = ["algorithm_results", "random_results", "four_moves_results"] 
df_algorithm = pd.DataFrame(data["algorithm_results"])
df_random = pd.DataFrame(data["random_results"])
df_four_moves = pd.DataFrame(data["four_moves_results"])
print(df_algorithm.mean())
print(df_random.mean())
print(df_four_moves.mean())
print("==================")
print(df_algorithm.median())
print(df_random.median())
print(df_four_moves.median())