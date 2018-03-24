import pandas as pd

df = pd.read_csv("data/corpus/filmcorpus.csv",usecols= [0,1,2])

def getfilm(x):
	if x==0:
		return(df.loc[df['emotion'] == 0])
	else:
		return(df.loc[df['emotion'] == 1])		
print(getfilm(1))