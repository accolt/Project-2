import pandas as pd

df = pd.read_excel(
    r'D:\Montan University\2021 Summer semester\Monitoring Techniques, Data Handling\Case study\Case study 1.xlsx')

# print(df.columns)
# print(df.loc[(df['start_time_load'] == '2020-03-12T05:21:21+00:00') & (df['truck_numberplate'] == 'Articulated_Lkw')])

# Calculating distance of Articulated_Lkw

distance_march20 = (
    df.loc[df['start_time_load'].str.contains('2020-03') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_march20 = distance_march20['distance_road_total_cycle']
print(summary_march20.sum())

distance_april = (
    df.loc[df['start_time_load'].str.contains('2020-04') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_april = distance_april['distance_road_total_cycle']

distance_may = (df.loc[df['start_time_load'].str.contains('2020-05') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_may = distance_may['distance_road_total_cycle']

distance_june = (df.loc[df['start_time_load'].str.contains('2020-06') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_june = distance_june['distance_road_total_cycle']

distance_july = (df.loc[df['start_time_load'].str.contains('2020-07') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_july = distance_july['distance_road_total_cycle']

distance_august = (
    df.loc[df['start_time_load'].str.contains('2020-08') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_august = distance_august['distance_road_total_cycle']

distance_september = (
    df.loc[df['start_time_load'].str.contains('2020-09') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_september = distance_september['distance_road_total_cycle']

distance_october = (
    df.loc[df['start_time_load'].str.contains('2020-10') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_october = distance_october['distance_road_total_cycle']

distance_november = (
    df.loc[df['start_time_load'].str.contains('2020-11') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_november = distance_november['distance_road_total_cycle']

distance_december = (
    df.loc[df['start_time_load'].str.contains('2020-12') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_december = distance_december['distance_road_total_cycle']

distance_january = (
    df.loc[df['start_time_load'].str.contains('2021-01') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_january = distance_january['distance_road_total_cycle']

distance_february = (
    df.loc[df['start_time_load'].str.contains('2021-02') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_february = distance_february['distance_road_total_cycle']

distance_march21 = (
    df.loc[df['start_time_load'].str.contains('2021-03') & (df['truck_numberplate'] == 'Articulated_Lkw')])
summary_march21 = distance_march21['distance_road_total_cycle']

# Calculating distance of Knickgelenkte Mulde M4

distance_march20 = (
    df.loc[df['start_time_load'].str.contains('2020-03') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_march20 = distance_march20['distance_road_total_cycle']

distance_april = (
    df.loc[df['start_time_load'].str.contains('2020-04') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_april = distance_april['distance_road_total_cycle']

distance_may = (
    df.loc[df['start_time_load'].str.contains('2020-05') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_may = distance_may['distance_road_total_cycle']

distance_june = (
    df.loc[df['start_time_load'].str.contains('2020-06') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_june = distance_june['distance_road_total_cycle']

distance_july = (
    df.loc[df['start_time_load'].str.contains('2020-07') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_july = distance_july['distance_road_total_cycle']

distance_august = (
    df.loc[df['start_time_load'].str.contains('2020-08') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_august = distance_august['distance_road_total_cycle']

distance_september = (
    df.loc[df['start_time_load'].str.contains('2020-09') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_september = distance_september['distance_road_total_cycle']

distance_october = (
    df.loc[df['start_time_load'].str.contains('2020-10') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_october = distance_october['distance_road_total_cycle']

distance_november = (
    df.loc[df['start_time_load'].str.contains('2020-11') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_november = distance_november['distance_road_total_cycle']

distance_december = (
    df.loc[df['start_time_load'].str.contains('2020-12') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_december = distance_december['distance_road_total_cycle']

distance_january = (
    df.loc[df['start_time_load'].str.contains('2021-01') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_january = distance_january['distance_road_total_cycle']

distance_february = (
    df.loc[df['start_time_load'].str.contains('2021-02') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_february = distance_february['distance_road_total_cycle']

distance_march21 = (
    df.loc[df['start_time_load'].str.contains('2021-03') & (df['truck_numberplate'] == 'Knickgelenkte Mulde M4')])
summary1_march21 = distance_march21['distance_road_total_cycle']

# Calculating distance of Mulde 1

distance_march20 = (
    df.loc[df['start_time_load'].str.contains('2020-03') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_march20 = distance_march20['distance_road_total_cycle']

distance_april = (
    df.loc[df['start_time_load'].str.contains('2020-04') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_april = distance_april['distance_road_total_cycle']

distance_may = (
    df.loc[df['start_time_load'].str.contains('2020-05') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_may = distance_may['distance_road_total_cycle']

distance_june = (
    df.loc[df['start_time_load'].str.contains('2020-06') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_june = distance_june['distance_road_total_cycle']

distance_july = (
    df.loc[df['start_time_load'].str.contains('2020-07') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_july = distance_july['distance_road_total_cycle']

distance_august = (
    df.loc[df['start_time_load'].str.contains('2020-08') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_august = distance_august['distance_road_total_cycle']

distance_september = (
    df.loc[df['start_time_load'].str.contains('2020-09') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_september = distance_september['distance_road_total_cycle']

distance_october = (
    df.loc[df['start_time_load'].str.contains('2020-10') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_october = distance_october['distance_road_total_cycle']

distance_november = (
    df.loc[df['start_time_load'].str.contains('2020-11') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_november = distance_november['distance_road_total_cycle']

distance_december = (
    df.loc[df['start_time_load'].str.contains('2020-12') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_december = distance_december['distance_road_total_cycle']

distance_january = (
    df.loc[df['start_time_load'].str.contains('2021-01') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_january = distance_january['distance_road_total_cycle']

distance_february = (
    df.loc[df['start_time_load'].str.contains('2021-02') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_february = distance_february['distance_road_total_cycle']

distance_march21 = (
    df.loc[df['start_time_load'].str.contains('2021-03') & (df['truck_numberplate'] == 'Mulde 1')])
summary2_march21 = distance_march21['distance_road_total_cycle']

# Calculating distance of Mulde 10

distance_march20 = (
    df.loc[df['start_time_load'].str.contains('2020-03') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_march20 = distance_march20['distance_road_total_cycle']

distance_april = (
    df.loc[df['start_time_load'].str.contains('2020-04') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_april = distance_april['distance_road_total_cycle']

distance_may = (
    df.loc[df['start_time_load'].str.contains('2020-05') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_may = distance_may['distance_road_total_cycle']

distance_june = (
    df.loc[df['start_time_load'].str.contains('2020-06') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_june = distance_june['distance_road_total_cycle']

distance_july = (
    df.loc[df['start_time_load'].str.contains('2020-07') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_july = distance_july['distance_road_total_cycle']

distance_august = (
    df.loc[df['start_time_load'].str.contains('2020-08') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_august = distance_august['distance_road_total_cycle']

distance_september = (
    df.loc[df['start_time_load'].str.contains('2020-09') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_september = distance_september['distance_road_total_cycle']

distance_october = (
    df.loc[df['start_time_load'].str.contains('2020-10') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_october = distance_october['distance_road_total_cycle']

distance_november = (
    df.loc[df['start_time_load'].str.contains('2020-11') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_november = distance_november['distance_road_total_cycle']

distance_december = (
    df.loc[df['start_time_load'].str.contains('2020-12') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_december = distance_december['distance_road_total_cycle']

distance_january = (
    df.loc[df['start_time_load'].str.contains('2021-01') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_january = distance_january['distance_road_total_cycle']

distance_february = (
    df.loc[df['start_time_load'].str.contains('2021-02') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_february = distance_february['distance_road_total_cycle']

distance_march21 = (
    df.loc[df['start_time_load'].str.contains('2021-03') & (df['truck_numberplate'] == 'Mulde 10')])
summary3_march21 = distance_march21['distance_road_total_cycle']

# Calculating distance of Mulde 11

distance_march20 = (
    df.loc[df['start_time_load'].str.contains('2020-03') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_march20 = distance_march20['distance_road_total_cycle']

distance_april = (
    df.loc[df['start_time_load'].str.contains('2020-04') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_april = distance_april['distance_road_total_cycle']

distance_may = (
    df.loc[df['start_time_load'].str.contains('2020-05') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_may = distance_may['distance_road_total_cycle']

distance_june = (
    df.loc[df['start_time_load'].str.contains('2020-06') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_june = distance_june['distance_road_total_cycle']

distance_july = (
    df.loc[df['start_time_load'].str.contains('2020-07') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_july = distance_july['distance_road_total_cycle']

distance_august = (
    df.loc[df['start_time_load'].str.contains('2020-08') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_august = distance_august['distance_road_total_cycle']

distance_september = (
    df.loc[df['start_time_load'].str.contains('2020-09') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_september = distance_september['distance_road_total_cycle']

distance_october = (
    df.loc[df['start_time_load'].str.contains('2020-10') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_october = distance_october['distance_road_total_cycle']

distance_november = (
    df.loc[df['start_time_load'].str.contains('2020-11') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_november = distance_november['distance_road_total_cycle']

distance_december = (
    df.loc[df['start_time_load'].str.contains('2020-12') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_december = distance_december['distance_road_total_cycle']

distance_january = (
    df.loc[df['start_time_load'].str.contains('2021-01') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_january = distance_january['distance_road_total_cycle']

distance_february = (
    df.loc[df['start_time_load'].str.contains('2021-02') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_february = distance_february['distance_road_total_cycle']

distance_march21 = (
    df.loc[df['start_time_load'].str.contains('2021-03') & (df['truck_numberplate'] == 'Mulde 11')])
summary4_march21 = distance_march21['distance_road_total_cycle']

# Calculating distance of Mulde 2

distance_march20 = (
    df.loc[df['start_time_load'].str.contains('2020-03') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_march20 = distance_march20['distance_road_total_cycle']

distance_april = (
    df.loc[df['start_time_load'].str.contains('2020-04') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_april = distance_april['distance_road_total_cycle']

distance_may = (
    df.loc[df['start_time_load'].str.contains('2020-05') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_may = distance_may['distance_road_total_cycle']

distance_june = (
    df.loc[df['start_time_load'].str.contains('2020-06') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_june = distance_june['distance_road_total_cycle']

distance_july = (
    df.loc[df['start_time_load'].str.contains('2020-07') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_july = distance_july['distance_road_total_cycle']

distance_august = (
    df.loc[df['start_time_load'].str.contains('2020-08') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_august = distance_august['distance_road_total_cycle']

distance_september = (
    df.loc[df['start_time_load'].str.contains('2020-09') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_september = distance_september['distance_road_total_cycle']

distance_october = (
    df.loc[df['start_time_load'].str.contains('2020-10') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_october = distance_october['distance_road_total_cycle']

distance_november = (
    df.loc[df['start_time_load'].str.contains('2020-11') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_november = distance_november['distance_road_total_cycle']

distance_december = (
    df.loc[df['start_time_load'].str.contains('2020-12') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_december = distance_december['distance_road_total_cycle']

distance_january = (
    df.loc[df['start_time_load'].str.contains('2021-01') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_january = distance_january['distance_road_total_cycle']

distance_february = (
    df.loc[df['start_time_load'].str.contains('2021-02') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_february = distance_february['distance_road_total_cycle']

distance_march21 = (
    df.loc[df['start_time_load'].str.contains('2021-03') & (df['truck_numberplate'] == 'Mulde 2')])
summary5_march21 = distance_march21['distance_road_total_cycle']

# Calculating distance of Mulde 6

distance_march20 = (
    df.loc[df['start_time_load'].str.contains('2020-03') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_march20 = distance_march20['distance_road_total_cycle']

distance_april = (
    df.loc[df['start_time_load'].str.contains('2020-04') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_april = distance_april['distance_road_total_cycle']

distance_may = (
    df.loc[df['start_time_load'].str.contains('2020-05') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_may = distance_may['distance_road_total_cycle']

distance_june = (
    df.loc[df['start_time_load'].str.contains('2020-06') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_june = distance_june['distance_road_total_cycle']

distance_july = (
    df.loc[df['start_time_load'].str.contains('2020-07') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_july = distance_july['distance_road_total_cycle']

distance_august = (
    df.loc[df['start_time_load'].str.contains('2020-08') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_august = distance_august['distance_road_total_cycle']

distance_september = (
    df.loc[df['start_time_load'].str.contains('2020-09') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_september = distance_september['distance_road_total_cycle']

distance_october = (
    df.loc[df['start_time_load'].str.contains('2020-10') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_october = distance_october['distance_road_total_cycle']

distance_november = (
    df.loc[df['start_time_load'].str.contains('2020-11') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_november = distance_november['distance_road_total_cycle']

distance_december = (
    df.loc[df['start_time_load'].str.contains('2020-12') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_december = distance_december['distance_road_total_cycle']

distance_january = (
    df.loc[df['start_time_load'].str.contains('2021-01') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_january = distance_january['distance_road_total_cycle']

distance_february = (
    df.loc[df['start_time_load'].str.contains('2021-02') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_february = distance_february['distance_road_total_cycle']

distance_march21 = (
    df.loc[df['start_time_load'].str.contains('2021-03') & (df['truck_numberplate'] == 'Mulde 6')])
summary6_march21 = distance_march21['distance_road_total_cycle']

# Calculating distance of testmaschine2


data = {
    'Dump truck': ['Articulated Lkw', 'Knickgelenkte Mulde M4', 'Mulde 1', 'Mulde 10', 'Mulde 11', 'Mulde 2',
                   'Mulde 6'],
    'March 2020': [summary_march20.sum(), summary1_march20.sum(), summary2_march20.sum(), summary3_march20.sum(),
                   summary4_march20.sum(), summary5_march20.sum(), summary6_march20.sum()],
    'April 2020': [summary_april.sum(), summary1_april.sum(), summary2_april.sum(), summary3_april.sum(),
                   summary4_april.sum(), summary5_april.sum(), summary6_april.sum()],
    'May 2020': [summary_may.sum(), summary1_may.sum(), summary2_may.sum(), summary3_may.sum(), summary4_may.sum(),
                 summary5_may.sum(), summary6_may.sum()],
    'June 2020': [summary_june.sum(), summary1_june.sum(), summary2_june.sum(), summary3_june.sum(),
                  summary4_june.sum(), summary5_june.sum(), summary6_june.sum()],
    'July 2020': [summary_july.sum(), summary1_july.sum(), summary2_july.sum(), summary3_july.sum(),
                  summary4_july.sum(), summary5_july.sum(), summary6_july.sum()],
    'August 2020': [summary_august.sum(), summary1_august.sum(), summary2_august.sum(), summary3_august.sum(),
                    summary4_august.sum(), summary5_august.sum(), summary6_august.sum()],
    'September 2020': [summary_september.sum(), summary1_september.sum(), summary2_september.sum(),
                       summary3_september.sum(), summary4_september.sum(), summary5_september.sum(),
                       summary6_september.sum()],
    'October 2020': [summary_october.sum(), summary1_october.sum(), summary2_october.sum(), summary3_october.sum(),
                     summary4_october.sum(), summary5_october.sum(), summary6_october.sum()],
    'November 2020': [summary_november.sum(), summary1_november.sum(), summary2_november.sum(), summary3_november.sum(),
                      summary4_november.sum(), summary5_november.sum(), summary6_november.sum()],
    'December 2020': [summary_december.sum(), summary1_december.sum(), summary2_december.sum(), summary3_december.sum(),
                      summary4_december.sum(), summary5_december.sum(), summary6_december.sum()],
    'January 2021': [summary_january.sum(), summary1_january.sum(), summary2_january.sum(), summary3_january.sum(),
                     summary4_january.sum(), summary5_january.sum(), summary6_january.sum()],
    'February 2021': [summary_february.sum(), summary1_february.sum(), summary2_february.sum(), summary3_february.sum(),
                      summary4_february.sum(), summary5_february.sum(), summary6_february.sum()],
    'March 2021': [summary_march21.sum(), summary1_march21.sum(), summary2_march21.sum(), summary3_march21.sum(),
                   summary4_march21.sum(), summary5_march21.sum(), summary6_march21.sum()]}

df1 = pd.DataFrame(data, columns=['Dump truck', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020',
                                  'August 2020', 'September 2020', 'October 2020', 'November 2020', 'December 2020',
                                  'January 2021', 'February 2021', 'March 2021'])

#df1.to_excel('Articulated Lkw.xlsx', index=False)

print('Hello Nick')
