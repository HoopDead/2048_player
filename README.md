# 2048_Player

It is a simple Python script, that literally plays 2048 game and comparision between four diffrent ways to deal with the game.

## Installation

You can just use git clone comand and run the scripts with virtualenv and python3 <name of script> command

```bash
git clone https://github.com/hoopdead/2048_player
```

```bash
virtualenv env
```

Head into the directory, that you have installed env
```bash
source bin/activate
```

```
python3 main.py
````

## Structure of the project

#### Handles probably the most complex algorithm made by me that checks what move is probably the best - if there is no "best" move, it heads up to use random move.
```
main.py
```

#### Does four moves - UP, LEFT, DOWN, RIGHT and repeat.
```
four_moves_algo.py
```

#### Does three moves - LEFT, RIGHT, DOWN and repeat.
```
three_moves_algo.py
```

#### Keep four functions in it, every function check how the board will look after each move.
```
moves.py
```

#### Does a random moves on the board.
```
random.py
```

#### Created only for tests, how each function work, because there were bug with matrix transpose
```
tests.py
```

#### Maths and stats about how each of scripts works and analyze the results for each of them.
```
analyze.py
```




## Analyze

Here's a statisticts and analyze of how each of approach works:

#### Average of Algorithm Approach

| Random moves | Algorithm Moves | Highest tile | Number of moves |
|--------------|-----------------|--------------|-----------------|
| 65           | 125             | 158          | 190             |

#### Average of Random moves Approach

| Number of moves | Highest tile |
|-----------------|--------------|
| 138             | 98           |

#### Average of Four moves Approach


| Number of moves | Highest tile |
|-----------------|--------------|
| 50              | 193          |


#### ======================= ####

#### Median of Algorithm Approach

| Random moves | Algorithm moves | Highest tile | Number of moves |
|--------------|-----------------|--------------|-----------------|
| 63           | 119             | 128          | 184             |

#### Median of Random moves Approach

| Number of moves | Highest tile |
|-----------------|--------------|
| 129             | 64           |

#### Median of Four moves Approach

| Number of moves | Highest tile |
|-----------------|--------------|
| 48              | 128          |

#### There's also an some results for three moves algorithm, it won't be added in median and average, but will be mentioned in conclusions

#### Conclusions

* Problably the best approach to reach the highest tile with the most risk is to use LEFT-DOWN, RIGHT-DOWN moves.
* The worst method to reach highest score is to use random algorithm
* You can reach the best result in the less moves using UP-LEFT-DOWN-RIGHT algorithm
* Mediana of highest tiles in best move algorithm and four moves is the same


## License
[MIT](https://choosealicense.com/licenses/mit/)