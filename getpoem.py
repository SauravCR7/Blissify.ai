import pandas as pd

df = pd.read_csv("data/corpus/poemcorpus.csv",usecols= [1,2,3])

def getpoem(x):
	if x==0:
		return(df.loc[df['emotion'] == 0])
	else:
		return(df.loc[df['emotion'] == 1])		
print(getpoem(1))