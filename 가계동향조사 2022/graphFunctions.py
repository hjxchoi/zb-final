import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 


df = pd.read_csv('./2022_연간자료(지출, 2019~) - 전체가구_1인이상_20240120_32176.csv', encoding='euc-kr', low_memory=False)

# 연령대 그룹 컬럼 추가
bins = [0, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109]
labels = ['10s', '20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s', '100s']
df['Age_Group'] = pd.cut(df['가구주_연령'], bins=bins, labels=labels, right=False)

# 1인가구
one = df[df['가구원수']==1]

# windows 한글깨짐
from matplotlib import rc
rc('font', family='Malgun Gothic')


remove_col = [ '가구원2_가구주관계코드',
 '가구원2_성별코드',
 '가구원2_연령',
 '가구원2_학력코드',
 '가구원2_수학구분코드',
 '가구원2_취업여부',
 '가구원2_10차산업분류코드',
 '가구원2_7차직업분류코드',
 '가구원2_종사상지위코드',
 '가구원3_가구주관계코드',
 '가구원3_성별코드',
 '가구원3_연령',
 '가구원3_학력코드',
 '가구원3_수학구분코드',
 '가구원3_취업여부',
 '가구원3_10차산업분류코드',
 '가구원3_7차직업분류코드',
 '가구원3_종사상지위코드',
 '가구원4_가구주관계코드',
 '가구원4_성별코드',
 '가구원4_연령',
 '가구원4_학력코드',
 '가구원4_수학구분코드',
 '가구원4_취업여부',
 '가구원4_10차산업분류코드',
 '가구원4_7차직업분류코드',
 '가구원4_종사상지위코드',
 '가구원5_가구주관계코드',
 '가구원5_성별코드',
 '가구원5_연령',
 '가구원5_학력코드',
 '가구원5_수학구분코드',
 '가구원5_취업여부',
 '가구원5_10차산업분류코드',
 '가구원5_7차직업분류코드',
 '가구원5_종사상지위코드',
 '가구원6_가구주관계코드',
 '가구원6_성별코드',
 '가구원6_연령',
 '가구원6_학력코드',
 '가구원6_수학구분코드',
 '가구원6_취업여부',
 '가구원6_10차산업분류코드',
 '가구원6_7차직업분류코드',
 '가구원6_종사상지위코드',
 '가구원7_가구주관계코드',
 '가구원7_성별코드',
 '가구원7_연령',
 '가구원7_학력코드',
 '가구원7_수학구분코드',
 '가구원7_취업여부',
 '가구원7_10차산업분류코드',
 '가구원7_7차직업분류코드',
 '가구원7_종사상지위코드',
 '가구원8_가구주관계코드',
 '가구원8_성별코드',
 '가구원8_연령',
 '가구원8_학력코드',
 '가구원8_수학구분코드',
 '가구원8_취업여부',
 '가구원8_10차산업분류코드',
 '가구원8_7차직업분류코드',
 '가구원8_종사상지위코드',
 '가구원9_가구주관계코드',
 '가구원9_성별코드',
 '가구원9_연령',
 '가구원9_학력코드',
 '가구원9_수학구분코드',
 '가구원9_취업여부',
 '가구원9_10차산업분류코드',
 '가구원9_7차직업분류코드',
 '가구원9_종사상지위코드',
 '비동거취업배우자유무',
 '비동거학업배우자유무',
 '비동거기타배우자유무',
 '비동거취업미혼자녀수',
 '비동거학업미혼자녀수',
 '비동거기타미혼자녀수',
 '가구원수',
 '취업인원수',
 '노인가구여부',
 '모자가구여부',
 '맞벌이가구여부']

one = one.drop(remove_col, axis=1)



# 소비지출 컬럼
col_cat = [
 '가계지출_소비지출_식료품비주류음료구입비',
 '가계지출_소비지출_의류신발구입비','가계지출_소비지출_주거수도광열비',
 '가계지출_소비지출_가정용품가사서비스이용금액',
 '가계지출_소비지출_보건제품구입비',
 '가계지출_소비지출_교통비',
 '가계지출_소비지출_통신비',
 '가계지출_소비지출_오락문화비',
 '가계지출_소비지출_교육비',
 '가계지출_소비지출_음식숙박비',
 '가계지출_소비지출_기타상품서비스이용금액',
 '가계지출_비소비지출금액']


col_food = [
 '가계지출_소비지출_식료품비주류음료_곡물구입비',
 '가계지출_소비지출_식료품비주류음료_곡물가공품구입비',
 '가계지출_소비지출_식료품비주류음료_빵떡류구입비',
 '가계지출_소비지출_식료품비주류음료_육류구입비',
 '가계지출_소비지출_식료품비주류음료_육류가공품구입비',
 '가계지출_소비지출_식료품비주류음료_신선수산동물구입비',
 '가계지출_소비지출_식료품비주류음료_염건수산동물구입비',
 '가계지출_소비지출_식료품비주류음료_기타수산동물가공구입비',
 '가계지출_소비지출_식료품비주류음료_유제품및알구입비',
 '가계지출_소비지출_식료품비주류음료_유지류구입비',
 '가계지출_소비지출_식료품비주류음료_과일가공품구입비',
 '가계지출_소비지출_식료품비주류음료_채소가공품구입비',
 '가계지출_소비지출_식료품비주류음료_해조가공품구입비',
 '가계지출_소비지출_식료품비주류음료_당류과자류구입비',
 '가계지출_소비지출_식료품비주류음료_조미식품구입비',
 '가계지출_소비지출_식료품비주류음료_기타식품구입비',
 '가계지출_소비지출_식료품비주류음료_커피차구입비',
 '가계지출_소비지출_식료품비주류음료_쥬스기타음료구입비',
]

col_alc = [
 '가계지출_소비지출_주류담배_주류구입비',
 '가계지출_소비지출_주류담배_담배구입비']


col_cloth = [
 '가계지출_소비지출_의류신발_직물및외의구입비',
 '가계지출_소비지출_의류신발_내의구입비',
 '가계지출_소비지출_의류신발_기타의복구입비',
 '가계지출_소비지출_의류신발_의복관련서비스구입비',
 '가계지출_소비지출_의류신발_신발구입비',
 '가계지출_소비지출_의류신발_신발서비스구입비',
]

col_house = [
 '가계지출_소비지출_주거수도광열_실제주거비구입비',
 '가계지출_소비지출_주거수도광열_주택유지수선구입비',
 '가계지출_소비지출_주거수도광열_상하수도폐기물처리비',
 '가계지출_소비지출_주거수도광열_기타주거관련서비스구입비',
 '가계지출_소비지출_주거수도광열_연료비구입비']

col_service = [
 '가계지출_소비지출_가정용품가사서비스_가구조명구입비',
 '가계지출_소비지출_가정용품가사서비스_실내장식구입비',
 '가계지출_소비지출_가정용품가사서비스_가구조명장식서비스이용금액',
 '가계지출_소비지출_가정용품가사서비스_가정용섬유구입비',
 '가계지출_소비지출_가정용품가사서비스_가전가정용기기구입비',
 '가계지출_소비지출_가정용품가사서비스_가전관련서비스이용금액',
 '가계지출_소비지출_가정용품가사서비스_가사용품구입비',
 '가계지출_소비지출_가정용품가사서비스_가정용공구기타구입비',
 '가계지출_소비지출_가정용품가사서비스_가사소모품구입비',
 '가계지출_소비지출_가정용품가사서비스_가사서비스금액']

col_med = [
 '가계지출_소비지출_보건_의약품구입비',
 '가계지출_소비지출_보건_의료용소모품구입비',
 '가계지출_소비지출_보건_보건의료용품기구구입비',
 '가계지출_소비지출_보건_외래의료서비스이용금액',
 '가계지출_소비지출_보건_치과서비스이용금액',
 '가계지출_소비지출_보건_기타의료서비스이용금액',
 '가계지출_소비지출_보건_입원서비스이용금액',
]

col_traf = [
 '가계지출_소비지출_교통_자동차구입비',
 '가계지출_소비지출_교통_기타운송기구구입비',
 '가계지출_소비지출_교통_운송기구유지수리비',
 '가계지출_소비지출_교통_운송기구연료비',
 '가계지출_소비지출_교통_기타개인교통서비스이용금액',
 '가계지출_소비지출_교통_철도운송금액',
 '가계지출_소비지출_교통_육상운송금액',
 '가계지출_소비지출_교통_기타운송금액',
 '가계지출_소비지출_교통_기타교통관련서비스이용금액'
]

col_tel = [
 '가계지출_소비지출_통신_우편서비스이용금액',
 '가계지출_소비지출_통신_통신장비구입비',
 '가계지출_소비지출_통신_통신서비스이용금액']

col_fun = [
 '가계지출_소비지출_오락문화_영상음향기기구입비',
 '가계지출_소비지출_오락문화_사진광학장비구입비',
 '가계지출_소비지출_오락문화_정보처리장치구입비',
 '가계지출_소비지출_오락문화_기록매체구입비',
 '가계지출_소비지출_오락문화_영상음향정보기기수리비',
 '가계지출_소비지출_오락문화_내구재구입비',
 '가계지출_소비지출_오락문화_악기기구구입비',
 '가계지출_소비지출_오락문화_오락문화내구재유지수리비',
 '가계지출_소비지출_오락문화_장난감취미용품구입비',
 '가계지출_소비지출_오락문화_캠핑운동관련용품구입비',
 '가계지출_소비지출_오락문화_화훼관련용품구입비',
 '가계지출_소비지출_오락문화_애완동물관련물품구입비',
 '가계지출_소비지출_오락문화_화훼애완동물서비스이용금액',
 '가계지출_소비지출_오락문화_운동오락서비스이용금액',
 '가계지출_소비지출_오락문화_문화서비스이용금액',
 '가계지출_소비지출_오락문화_복권구입비',
 '가계지출_소비지출_오락문화_서적구입비',
 '가계지출_소비지출_오락문화_기타인쇄물구입비',
 '가계지출_소비지출_오락문화_문구구입비',
 '가계지출_소비지출_오락문화_단체여행경비'
]

col_edu = [
 '가계지출_소비지출_교육_정규교육비',
 '가계지출_소비지출_교육_초등교육비',
 '가계지출_소비지출_교육_중등교육비',
 '가계지출_소비지출_교육_고등교육비',
 '가계지출_소비지출_교육_학원보습교육비',
 '가계지출_소비지출_교육_학생학원교육비',
 '가계지출_소비지출_교육_성인학원비',
 '가계지출_소비지출_교육_기타교육비']

col_acc = [
 '가계지출_소비지출_음식숙박_식대',
 '가계지출_소비지출_음식숙박_숙박비'
]

col_etc = [
 '가계지출_소비지출_기타상품서비스_이미용서비스이용금액',
 '가계지출_소비지출_기타상품서비스_이미용기기구입비',
 '가계지출_소비지출_기타상품서비스_위생이미용용품구입비',
 '가계지출_소비지출_기타상품서비스_시계장신구구입비',
 '가계지출_소비지출_기타상품서비스_기타개인용품구입비',
 '가계지출_소비지출_기타상품서비스_복지시설비용금액',
 '가계지출_소비지출_기타상품서비스_보험료',
 '가계지출_소비지출_기타상품서비스_기타금융구입비',
 '가계지출_소비지출_기타상품서비스_기타서비스금액구입비'
]

col_neg = [
 '가계지출_비소비지출_경상조세',
 '가계지출_비소비지출_비경상조세',
 '가계지출_비소비지출_연금기여금',
 '가계지출_비소비지출_사회보장구입비',
 '가계지출_비소비지출_이자비용',
 '가계지출_비소비지출_가구간이전지출금액',
 '가계지출_비소비지출_비영리단체이전지출금액']


# 남성 1인가구, 여성 1인가구
one_m = one[one['가구주_성별코드']==1]
one_f = one[one['가구주_성별코드']==2]


# 20대와 3-40대 소비지출비교
def compare2_34(target, col, title=''):
    
    one_2 = target[target['Age_Group'].isin(['20s'])]
    one_34 = target[target['Age_Group'].isin(['30s', '40s'])]

    # Reshape the DataFrame
    df_melted2 = one_2[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')
    df_melted34 = one_34[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')

    # Add a new column for labeling
    df_melted2['Group'] = '20s'
    df_melted34['Group'] = '30s-40s'

    # Combine the dataframes
    combined_df = pd.concat([df_melted2, df_melted34])

    # Plot using Seaborn
    plt.figure(figsize=(12, 5))  # Adjust the size as needed
    sns.barplot(data=combined_df, x='Expense_Type', y='Amount', hue='Group')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.legend(title='Age Group')
    plt.title(title)
    plt.show()



# 20대와 4-50대 소비지출비교
def compare2_45(target, col, title=''):
    
    one_2 = target[target['Age_Group'].isin(['20s'])]
    one_45 = target[target['Age_Group'].isin(['40s', '50s'])]

    # Reshape the DataFrame
    df_melted2 = one_2[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')
    df_melted45 = one_45[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')

    # Add a new column for labeling
    df_melted2['Group'] = '20s'
    df_melted45['Group'] = '40s-50s'

    # Combine the dataframes
    combined_df = pd.concat([df_melted2, df_melted45])

    # Plot using Seaborn
    plt.figure(figsize=(12, 5))  # Adjust the size as needed
    sns.barplot(data=combined_df, x='Expense_Type', y='Amount', hue='Group')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.legend(title='Age Group')
    plt.title(title)
    plt.show()


# 20, 30, 40, 50대 비교
def compare_2345(target, col, title=''):

    one_2 = target[target['Age_Group'].isin(['20s'])]
    one_3 = target[target['Age_Group'].isin(['30s'])]
    one_4 = target[target['Age_Group'].isin(['40s'])]
    one_5 = target[target['Age_Group'].isin(['50s'])]

    # Reshape the DataFrame
    df_melted2 = one_2[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')
    df_melted3 = one_3[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')
    df_melted4 = one_4[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')
    df_melted5 = one_5[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')

    # Add a new column for labeling
    df_melted2['Group'] = '20s'
    df_melted3['Group'] = '30s'
    df_melted4['Group'] = '40s'
    df_melted5['Group'] = '50s'

    # Combine the dataframes
    combined_df = pd.concat([df_melted2, df_melted3, df_melted4, df_melted5])

    # Plot using Seaborn
    plt.figure(figsize=(12, 4))  # Adjust the size as needed
    sns.barplot(data=combined_df, x='Expense_Type', y='Amount', hue='Group')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.legend(title='Age Group')
    plt.title(title)
    plt.show()


# 여성, 남성 비교
def comparemf(target, col, age_group, title=''):
    one_gen = target[target['Age_Group']==age_group]
    male = one_gen[one_gen['가구주_성별코드']==1]
    female = one_gen[one_gen['가구주_성별코드']==2]

    # Reshape the DataFrame
    df_melted_m = male[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')
    df_melted_f = female[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')

    df_melted_m['Sex'] = 'Male'
    df_melted_f['Sex'] = 'Female'

    combined_df = pd.concat([df_melted_m, df_melted_f])

    # Plot using Seaborn
    plt.figure(figsize=(12, 4))  # Adjust the size as needed
    sns.barplot(data=combined_df, x='Expense_Type', y='Amount', hue='Sex')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.title(f'{title}')
    plt.legend(title='')
    plt.show()


# 40대와 50대 소비지출비교
def compare4_5(target, col, title=''):
    
    one_4 = target[target['Age_Group'].isin(['40s'])]
    one_5 = target[target['Age_Group'].isin(['50s'])]

    # Reshape the DataFrame
    df_melted4 = one_4[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')
    df_melted5 = one_5[col].melt(value_vars=col, var_name='Expense_Type', value_name='Amount')

    # Add a new column for labeling
    df_melted4['Group'] = '40s'
    df_melted5['Group'] = '50s'

    # Combine the dataframes
    combined_df = pd.concat([df_melted4, df_melted5])

    # Plot using Seaborn
    plt.figure(figsize=(12, 5))  # Adjust the size as needed
    sns.barplot(data=combined_df, x='Expense_Type', y='Amount', hue='Group')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.legend(title='Age Group')
    plt.title(title)
    plt.show()
