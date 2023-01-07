from main import Ar_Fielts
import pandas as pd
import csv

with open('ruta/al/archivo.csv', 'r') as file:
    fake_data = csv.reader(file)

contract = Ar_Fielts(data=fake_data)
result = contract.average(column="tags").export()

assert result == 3.0
