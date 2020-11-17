import pandas as pd
data = pd.read_csv('./APTdata.csv', encoding='CP949')

# 연령 범위 구하기 (이상 ~ 미만)
bins = [0, 10, 19, 28]
bins_labels = ['0~9', '10~18', '18~27']
data['연령2'] = pd.cut(data['연령'], bins, right=False, labels=bins_labels)

# 평당 범위 구하기 (이상 ~ 미만)
quote = data['시세'] / data['평수']
bins = [400, 850, 1300, 1876]
bins_labels = ['400~850', '850~1300', '1300~1875']
data['평당가격2'] = pd.cut(quote, bins, right=False, labels=bins_labels)

# 단지규모 범위 구하기 (초과 ~ 이하)
# 0~500, 501~800, 801~900, 901~1100, 1101~1200, 1201~1400, 1401~2100, 2101~2900, 2901~5000
bins = [0, 500, 800, 900, 1100, 1200, 1400, 2100, 2900, 5000]
bins_labels = ['범주1', '범주2', '범주3', '범주4', '범주5', '범주6', '범주7', '범주8', '범주9']
data['단지규모2'] = pd.cut(data['단지규모'], bins, labels=bins_labels,
                       include_lowest=True)

# 문제 a
print(data.groupby(['연령2', '평당가격2']).size().unstack())
# 문제 c
print(data.groupby(['연령2', '단지규모2']).size().unstack())
