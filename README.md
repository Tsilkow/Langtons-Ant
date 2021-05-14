# Langton's Ant

Script that simulates movements of langton's ant for customized rules.
There are n digits in each rule and i-th digit describes ant's behaviour, when number of visits modulo n is equal to i. Digits range from 0 to 5, where 0 describes	not changing direction, 1 is turning left 60 degrees, 2 is turning 120 degrees left and so on.
So for example rule 123 would mean that on visits 0, 3, 6 and so on, ant will turn 60 degrees left, on visits 1, 4, 7 and so on, ant will turn 120 degrees left ...

langtonsant.py runs a single simulation of a single rule.

langtonrunner.py runs all specified rules through langtonsant.py 

Arguments of langtonsant.py:
1. if 0, only the final (after 100000 steps or hitting the border) image will be saved; if 1, all frames will be saved to a folder with rules number
2. the rule ant will follow
3. tile size (width in case of hexagons)
4. width of area
5. height of area
6. tile verticies; currently supported: 4 and 6

Arguments of langtonrunner.py:
1. Length up to which rules will be explored
2. starting rule, from which possibilities will be explored recursively