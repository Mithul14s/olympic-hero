# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))


better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data.loc[:,['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(top_countries,parameters):
    country_list = []
    country_list=list(top_countries.nlargest(10,parameters)['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

common = list(set(top_10_summer).intersection(set(top_10_winter)).intersection(set(top_10)))
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig,(ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
summer_df.plot.bar('Country_Name','Total_Summer',ax=ax1)
ax1.set(Title='Summer',xlabel='Country Name',ylabel='Summer Medals')


winter_df.plot.bar('Country_Name','Total_Winter',ax=ax2)
ax2.set(Title='Winter',xlabel='Country Name',ylabel='Winter Medals')


top_df.plot.bar('Country_Name','Total_Medals',ax=ax3)
ax3.set(Title='Total',xlabel='Country Name',ylabel='Total Medals')

fig.tight_layout()
plt.legend()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()#value_counts().idxmax()
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()].Country_Name.item()
print(summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()#value_counts().idxmax()
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max()].Country_Name.item()
print(winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()#value_counts().idxmax()
top_country_gold=top_df[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max()].Country_Name.item()
print(top_country_gold)




# --------------
#Code starts here
data.drop(data.tail(1).index,inplace=True)
data_1 = data
data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total'])
best_country = data_1[data_1['Total_Points']==data_1['Total_Points'].max()].Country_Name.item()
most_points = data_1['Total_Points'].max()
print(best_country)
print(most_points)
#total = data_1.isnull.sum(axis=0)
#print(total)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel(best_country)
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


