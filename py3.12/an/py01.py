import pandas as pd
#data = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number']))
data = pd.DataFrame({'A':range(1,6),'B':range(10,60,10)})
print(data.query('A > 2 & B < 50'))
