import pandas as pd

df = pd.read_excel(
    r'D:\Montan University\2021 Summer semester\Monitoring Techniques, Data Handling\Case study\Case study 1.xlsx')

loading_bag_1 = df.loc[df['loader_numberplate'] == 'Bagger 1']
av_baggger_1 = loading_bag_1['duration_loading'].mean()
# print(av_baggger_1)

loading_bag_2 = df.loc[df['loader_numberplate'] == 'Bagger 2']
av_baggger_2 = loading_bag_2['duration_loading'].mean()

loading_bag_3 = df.loc[df['loader_numberplate'] == 'Bagger 3']
av_baggger_3 = loading_bag_3['duration_loading'].mean()

loading_bag_4 = df.loc[df['loader_numberplate'] == 'CAT_Loader']
av_baggger_4 = loading_bag_4['duration_loading'].mean()

loading_bag_5 = df.loc[df['loader_numberplate'] == 'Doosan']
av_baggger_5 = loading_bag_5['duration_loading'].mean()

loading_bag_6 = df.loc[df['loader_numberplate'] == 'Liebherr']
av_baggger_6 = loading_bag_6['duration_loading'].mean()

loading_bag_7 = df.loc[df['loader_numberplate'] == 'Silo']
av_baggger_7 = loading_bag_7['duration_loading'].mean()

loading_bag_8 = df.loc[df['loader_numberplate'] == 'Volvo_Loader']
av_baggger_8 = loading_bag_8['duration_loading'].mean()

data = {'Loaders': ['Bagger 1', 'Bagger 2', 'Bagger 3', 'CAT', 'Doosan', 'Liebherr', 'Silo', 'Volvo'],
        'Average loading time': [av_baggger_1, av_baggger_2, av_baggger_3, av_baggger_4, av_baggger_5, av_baggger_6,
                                 av_baggger_7, av_baggger_8]}

df4 = pd.DataFrame(data, columns=['Loaders', 'Average loading time'])

#df4.to_excel('Average loading time.xlsx', index=False)

print('oh yeah')

