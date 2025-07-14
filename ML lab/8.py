import pandas as pd
import matplotlib as plt

with open ('rainfall.csv' , 'r') as file :
	data = [line.strip().split(',') for line in file]
	df = pd.DataFrame(data[1:], columns=data[0])
	print(df)
