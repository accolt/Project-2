import pandas as pd

df = pd.read_excel(
    r'D:\Montan University\2021 Summer semester\Monitoring Techniques, Data Handling\Case study\Use_Case_1.xlsx')

cycle_1 = df.loc[df['truck_numberplate'] == 'Articulated_Lkw']
av_cycle_1 = cycle_1['full_cycle'].mean()
print(av_cycle_1)

cycle_2 = df.loc[df['loader_numberplate'] == 'Knickgelenkte Mulde M4']
av_cycle_2 = cycle_2['full_cycle'].mean()
print(av_cycle_2)

cycle_3 = df.loc[df['loader_numberplate'] == 'Mulde 1']
av_cycle_3 = cycle_3['full_cycle'].mean()
print((av_cycle_3))

cycle_4 = df.loc[df['loader_numberplate'] == 'Mulde 10']
av_cycle_4 = cycle_4['duration_cycle_time'].mean()
# print(av_cycle_4)

cycle_5 = df.loc[df['loader_numberplate'] == 'Mulde 11']
av_cycle_5 = cycle_5['duration_cycle_time'].mean()

cycle_6 = df.loc[df['loader_numberplate'] == 'Mulde 2']
av_cycle_6 = cycle_6['duration_cycle_time'].mean()

cycle_7 = df.loc[df['loader_numberplate'] == 'Mulde 6']
av_cycle_7 = cycle_7['duration_cycle_time'].mean()

cycle_8 = df.loc[df['loader_numberplate'] == 'testmaschine2']
av_cycle_8 = cycle_8['duration_cycle_time'].mean()

cycle_9 = df.loc[df['loader_numberplate'] == 'testmaschine4']
av_cycle_9 = cycle_9['duration_cycle_time'].mean()

data = {
    'Dumptruck': ['Articulated_Lkw', 'Knickgelenkte Mulde M4', 'Mulde 1', 'Mulde 10', 'Mulde 11', 'Mulde 2', 'Mulde 6',
                  'testmaschine2', 'testmaschine4'],
    'Average cycle time': [av_cycle_1, av_cycle_2, av_cycle_3, av_cycle_4, av_cycle_5, av_cycle_6, av_cycle_7,
                           av_cycle_8, av_cycle_9]}

df5 = pd.DataFrame(data, columns=['Dumptruck', 'Average cycle time'])

# df5.to_excel('Average cycle time.xlsx', index=False)

print('oooh my')
