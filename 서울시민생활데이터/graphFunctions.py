# 시각화

#import os
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

import geopandas as gpd 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib as mpl 

# mac
mpl.rc('font', family='Arial Unicode MS')

plt.rcParams['figure.figsize'] = (20, 10)
mpl.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기(1인가구)
data = pd.read_csv('./(첨부5)서울 시민생활 데이터_예제코드/1인가구_관심집단.csv', encoding='cp949')

n = data.shape[0]
adm_cd = []
for i in range(n):
    adm_cd.append(str(data['행정동코드'][i]))
data['adm_cd'] = adm_cd

geo = gpd.read_file('./(첨부5)서울 시민생활 데이터_예제코드/서울_행정동.shp')
df_geo = geo.iloc[:, [2, 9]]
rdata = pd.merge(data, df_geo, on = 'adm_cd')
data_merge = gpd.GeoDataFrame(rdata, crs='EPSG:4326', geometry='geometry')


#####################
# 1인가구 시각화
# 연령대 병합
#####################

data_merge['연령대1'] = data_merge['연령대']

idx = (data_merge['연령대'] == 25)
data_merge['연령대1'][idx] = 20

idx = (data_merge['연령대'] == 35)
data_merge['연령대1'][idx] = 30

idx = (data_merge['연령대'] == 45)
data_merge['연령대1'][idx] = 40

# 50 - 60: 50대
idx = (data_merge['연령대'] == 55)
data_merge['연령대1'][idx] = 50

# 60세 이상
idx = (data_merge['연령대'] >= 60)
data_merge['연령대1'][idx] = 65

colname_ = list(data_merge.columns[5:17])
data_groupby = data_merge.groupby(['adm_cd', '연령대1'])[colname_].sum()
data_groupby = data_groupby.reset_index()
data_groupby = pd.merge(data_groupby, df_geo, on='adm_cd')
data_groupby = gpd.GeoDataFrame(data_groupby, crs='EPSG:4326',
                                geometry='geometry')



#######################
#######################

## 그래프 그리는 함수
# age_group: 연령대[20, 30, ...]
# col: column 이름
# sex: 1(남), 2(여)

#######################
#######################

def draw_one(age_group, col, sex='', cmap='BuGn'):
    data_tmp = data_groupby[data_groupby['연령대1']==age_group]

    # 성별 포함 분석시
    if sex:
        if sex==1:
            sex_w = '남성'
        elif sex==2:
            sex_w = '여성'
            
        data_tmp = data_merge[data_merge['연령대']==age_group][data_merge['성별']==sex]

    # 그래프
    plt.figure(figsize=(5,5))
    data_tmp.plot(column=col,
                legend=True,
                cmap=cmap,
                edgecolor='k',
                legend_kwds={'label': '명'})
    plt.axis('off')
    plt.tight_layout()

    # 제목에 오타 있음
    if col == '샹활서비스 이용이 많은 집단':
        col = '생활서비스 이용이 많은 집단'

    # 제목
    if sex:
        plt.title(f'{str(age_group)}대 {sex_w} 중 {col}', fontsize=20)
    else:
        plt.title(f'{str(age_group)}대 중 {col}', fontsize=20)
        
    plt.show()