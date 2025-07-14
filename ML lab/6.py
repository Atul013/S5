import numpy as np
import pandas as pd

ar = np.array( [[1, 6012], [2, 7079], [3, 6886], [4, 7230], [5, 4598], [6, 5564], [7, 6971], [8, 7763], [9, 8032], [10, 9569]] )

ar[:, 1] += 2000

df = pd.DataFrame(ar, columns=['Day Number', 'Steps Walked'])
print(df.to_string(index=False))

print("\nThe days where Lee walked more than 9000 steps :")
morethan9k = df[df['Steps Walked'] > 9000]
print (morethan9k.to_string(index=False))

print("\nSorted steps :")
sortedsteps = df.sort_values(by="Steps Walked")
print(sortedsteps.to_string(index=False))
