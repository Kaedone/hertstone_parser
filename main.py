import pandas as pd
from requests import *

main_data = pd.read_csv(r"...")

content = ["ID", "Card_Name", "Hero_Strength"]

temp = [0] * len(main_data["Card_Name"])

for i in range(len(main_data["Card_Name"])):
    main_data[content[0]][i] = i

main_data[content[2]] = temp

edit = winning()

for i in range(len(edit)):
    for j in range(len(main_data[content[1]])):
        if edit[i] == main_data[content[1]][j]:
            main_data[content[2]][j] += 1
