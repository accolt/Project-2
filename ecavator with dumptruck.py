import pandas as pd

df = pd.read_excel(
    r'D:\Montan University\2021 Summer semester\Monitoring Techniques, Data Handling\Case study\Case study 1.xlsx')

ex_1 = (df.loc[df['loader_numberplate'] == 'Bagger 1'])
# cool = ex_1['truck_numberplate'].isin(['Articulated_Lkw'])

truck_1 = (ex_1.loc[ex_1['truck_numberplate'] == 'Articulated_Lkw'])
truck_2 = (ex_1.loc[ex_1['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
truck_3 = (ex_1.loc[ex_1['truck_numberplate'] == 'Mulde 1'])
truck_4 = (ex_1.loc[ex_1['truck_numberplate'] == 'Mulde 10'])
truck_5 = (ex_1.loc[ex_1['truck_numberplate'] == 'Mulde 11'])
truck_6 = (ex_1.loc[ex_1['truck_numberplate'] == 'Mulde 2'])
truck_7 = (ex_1.loc[ex_1['truck_numberplate'] == 'Mulde 6'])

ex_2 = (df.loc[df['loader_numberplate'] == 'Bagger 2'])
ex_2_truck_1 = (ex_2.loc[ex_2['truck_numberplate'] == 'Articulated_Lkw'])
ex_2_truck_2 = (ex_2.loc[ex_2['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
ex_2_truck_3 = (ex_2.loc[ex_2['truck_numberplate'] == 'Mulde 1'])
ex_2_truck_4 = (ex_2.loc[ex_2['truck_numberplate'] == 'Mulde 10'])
ex_2_truck_5 = (ex_2.loc[ex_2['truck_numberplate'] == 'Mulde 11'])
ex_2_truck_6 = (ex_2.loc[ex_2['truck_numberplate'] == 'Mulde 2'])
ex_2_truck_7 = (ex_2.loc[ex_2['truck_numberplate'] == 'Mulde 6'])

ex_3 = (df.loc[df['loader_numberplate'] == 'Bagger 3'])
ex_3_truck_1 = (ex_3.loc[ex_3['truck_numberplate'] == 'Articulated_Lkw'])
ex_3_truck_2 = (ex_3.loc[ex_3['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
ex_3_truck_3 = (ex_3.loc[ex_3['truck_numberplate'] == 'Mulde 1'])
ex_3_truck_4 = (ex_3.loc[ex_3['truck_numberplate'] == 'Mulde 10'])
ex_3_truck_5 = (ex_3.loc[ex_3['truck_numberplate'] == 'Mulde 11'])
ex_3_truck_6 = (ex_3.loc[ex_3['truck_numberplate'] == 'Mulde 2'])
ex_3_truck_7 = (ex_3.loc[ex_3['truck_numberplate'] == 'Mulde 6'])

ex_4 = (df.loc[df['loader_numberplate'] == 'CAT_Loader'])
ex_4_truck_1 = (ex_4.loc[ex_4['truck_numberplate'] == 'Articulated_Lkw'])
ex_4_truck_2 = (ex_4.loc[ex_4['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
ex_4_truck_3 = (ex_4.loc[ex_4['truck_numberplate'] == 'Mulde 1'])
ex_4_truck_4 = (ex_4.loc[ex_4['truck_numberplate'] == 'Mulde 10'])
ex_4_truck_5 = (ex_4.loc[ex_4['truck_numberplate'] == 'Mulde 11'])
ex_4_truck_6 = (ex_4.loc[ex_4['truck_numberplate'] == 'Mulde 2'])
ex_4_truck_7 = (ex_4.loc[ex_4['truck_numberplate'] == 'Mulde 6'])

ex_5 = (df.loc[df['loader_numberplate'] == 'Doosan'])
ex_5_truck_1 = (ex_5.loc[ex_5['truck_numberplate'] == 'Articulated_Lkw'])
ex_5_truck_2 = (ex_5.loc[ex_5['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
ex_5_truck_3 = (ex_5.loc[ex_5['truck_numberplate'] == 'Mulde 1'])
ex_5_truck_4 = (ex_5.loc[ex_5['truck_numberplate'] == 'Mulde 10'])
ex_5_truck_5 = (ex_5.loc[ex_5['truck_numberplate'] == 'Mulde 11'])
ex_5_truck_6 = (ex_5.loc[ex_5['truck_numberplate'] == 'Mulde 2'])
ex_5_truck_7 = (ex_5.loc[ex_5['truck_numberplate'] == 'Mulde 6'])

ex_6 = (df.loc[df['loader_numberplate'] == 'Liebherr'])
ex_6_truck_1 = (ex_6.loc[ex_6['truck_numberplate'] == 'Articulated_Lkw'])
ex_6_truck_2 = (ex_6.loc[ex_6['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
ex_6_truck_3 = (ex_6.loc[ex_6['truck_numberplate'] == 'Mulde 1'])
ex_6_truck_4 = (ex_6.loc[ex_6['truck_numberplate'] == 'Mulde 10'])
ex_6_truck_5 = (ex_6.loc[ex_6['truck_numberplate'] == 'Mulde 11'])
ex_6_truck_6 = (ex_6.loc[ex_6['truck_numberplate'] == 'Mulde 2'])
ex_6_truck_7 = (ex_6.loc[ex_6['truck_numberplate'] == 'Mulde 6'])

ex_7 = (df.loc[df['loader_numberplate'] == 'Silo'])
ex_7_truck_1 = (ex_7.loc[ex_7['truck_numberplate'] == 'Articulated_Lkw'])
ex_7_truck_2 = (ex_7.loc[ex_7['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
ex_7_truck_3 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 1'])
ex_7_truck_4 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 10'])
ex_7_truck_5 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 11'])
ex_7_truck_6 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 2'])
ex_7_truck_7 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 6'])

ex_8 = (df.loc[df['loader_numberplate'] == 'Volvo_Loader'])
ex_8_truck_1 = (ex_8.loc[ex_8['truck_numberplate'] == 'Articulated_Lkw'])
ex_8_truck_2 = (ex_8.loc[ex_8['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
ex_8_truck_3 = (ex_8.loc[ex_8['truck_numberplate'] == 'Mulde 1'])
ex_8_truck_4 = (ex_8.loc[ex_8['truck_numberplate'] == 'Mulde 10'])
ex_8_truck_5 = (ex_8.loc[ex_8['truck_numberplate'] == 'Mulde 11'])
ex_8_truck_6 = (ex_8.loc[ex_8['truck_numberplate'] == 'Mulde 2'])
ex_8_truck_7 = (ex_8.loc[ex_8['truck_numberplate'] == 'Mulde 6'])

data = {'Dump truck': ['Articulated_Lkw', 'Knickgelenkte Mulde M4', 'Mulde 1', 'Mulde 10', 'Mulde 11', 'Mulde 2',
                       'Mulde 6'],
        'Bagger 1': [len(truck_1), len(truck_2), len(truck_3), len(truck_4), len(truck_5), len(truck_6), len(truck_7)],
        'Bagger 2': [len(ex_2_truck_1), len(ex_2_truck_2), len(ex_2_truck_3), len(ex_2_truck_4), len(ex_2_truck_5),
                     len(ex_2_truck_6), len(ex_2_truck_7)],
        'Bagger 3': [len(ex_3_truck_1), len(ex_3_truck_2), len(ex_3_truck_3), len(ex_3_truck_4), len(ex_3_truck_5),
                     len(ex_3_truck_6), len(ex_3_truck_7)],
        'CAT_Loader': [len(ex_4_truck_1), len(ex_4_truck_2), len(ex_4_truck_3), len(ex_4_truck_4), len(ex_4_truck_5),
                       len(ex_4_truck_6), len(ex_4_truck_7)],
        'Doosan': [len(ex_5_truck_1), len(ex_5_truck_2), len(ex_5_truck_3), len(ex_5_truck_4), len(ex_5_truck_5),
                   len(ex_5_truck_6), len(ex_5_truck_7)],
        'Liebherr': [len(ex_6_truck_1), len(ex_6_truck_2), len(ex_6_truck_3), len(ex_6_truck_4), len(ex_6_truck_5),
                     len(ex_6_truck_6), len(ex_6_truck_7)],
        'Silo': [len(ex_7_truck_1), len(ex_7_truck_2), len(ex_7_truck_3), len(ex_7_truck_4), len(ex_7_truck_5),
                 len(ex_7_truck_6), len(ex_7_truck_7)],
        'Volvo_Loader': [len(ex_8_truck_1), len(ex_8_truck_2), len(ex_8_truck_3), len(ex_8_truck_4), len(ex_8_truck_5),
                         len(ex_8_truck_6), len(ex_8_truck_7)]}

df6 = pd.DataFrame(data, columns=['Dump truck','Bagger 1', 'Bagger 2', 'Bagger 3', 'CAT_Loader', 'Doosan', 'Liebherr', 'Silo',
                                  'Volvo_Loader'])

#df6.to_excel('Loader and dumprtucks.xlsx', index=False)

# ex_7 = (df.loc[df['loader_numberplate'] == 'Silo'])
# ex_7_truck_1 = (ex_7.loc[ex_7['truck_numberplate'] == 'Articulated_Lkw'])
# ex_7_truck_2 = (ex_7.loc[ex_7['truck_numberplate'] == 'Knickgelenkte Mulde M4'])
# ex_7_truck_3 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 1'])
# ex_7_truck_4 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 10'])
# ex_7_truck_5 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 11'])
# ex_7_truck_6 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 2'])
# ex_7_truck_7 = (ex_7.loc[ex_7['truck_numberplate'] == 'Mulde 6'])
#
# print(len(ex_7_truck_1))
# print(len(ex_7_truck_2))
# print(len(ex_7_truck_3))
# print(len(ex_7_truck_4))
# print(len(ex_7_truck_5))
# print(len(ex_7_truck_6))
# print(len(ex_7_truck_7))


print('one two one two')