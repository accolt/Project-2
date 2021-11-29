import pandas as pd

df = pd.read_excel(
    r'D:\Montan University\2021 Summer semester\Monitoring Techniques, Data Handling\Case study\Case study 1.xlsx')

loading_march20 = (df.loc[df['start_time_load'].str.contains('2020-03') & (df['load_location_name'])])
loading_place_1 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_1']
loading_place_2 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_2']
loading_place_3 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_3']
loading_place_4 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_4']
loading_place_5 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_5']
loading_place_6 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_6']
loading_place_7 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_7']
loading_place_8 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_8']
loading_place_9 = loading_march20.loc[loading_march20['load_location_name'] == 'Loading_Place_9']

# print(len(loading_place_1))

loading_april = (df.loc[df['start_time_load'].str.contains('2020-04') & (df['load_location_name'])])
apr_lp_1 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_1']
apr_lp_2 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_2']
apr_lp_3 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_3']
apr_lp_4 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_4']
apr_lp_5 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_5']
apr_lp_6 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_6']
apr_lp_7 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_7']
apr_lp_8 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_8']
apr_lp_9 = loading_april.loc[loading_april['load_location_name'] == 'Loading_Place_9']

loading_may = (df.loc[df['start_time_load'].str.contains('2020-05') & (df['load_location_name'])])
may_lp_1 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_1']
may_lp_2 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_2']
may_lp_3 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_3']
may_lp_4 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_4']
may_lp_5 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_5']
may_lp_6 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_6']
may_lp_7 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_7']
may_lp_8 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_8']
may_lp_9 = loading_may.loc[loading_may['load_location_name'] == 'Loading_Place_9']

loading_june = (df.loc[df['start_time_load'].str.contains('2020-06') & (df['load_location_name'])])
jun_lp_1 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_1']
jun_lp_2 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_2']
jun_lp_3 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_3']
jun_lp_4 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_4']
jun_lp_5 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_5']
jun_lp_6 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_6']
jun_lp_7 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_7']
jun_lp_8 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_8']
jun_lp_9 = loading_june.loc[loading_june['load_location_name'] == 'Loading_Place_9']

loading_july = (df.loc[df['start_time_load'].str.contains('2020-07') & (df['load_location_name'])])
jul_lp_1 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_1']
jul_lp_2 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_2']
jul_lp_3 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_3']
jul_lp_4 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_4']
jul_lp_5 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_5']
jul_lp_6 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_6']
jul_lp_7 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_7']
jul_lp_8 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_8']
jul_lp_9 = loading_july.loc[loading_july['load_location_name'] == 'Loading_Place_9']

loading_august = (df.loc[df['start_time_load'].str.contains('2020-08') & (df['load_location_name'])])
aug_lp_1 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_1']
aug_lp_2 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_2']
aug_lp_3 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_3']
aug_lp_4 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_4']
aug_lp_5 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_5']
aug_lp_6 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_6']
aug_lp_7 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_7']
aug_lp_8 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_8']
aug_lp_9 = loading_august.loc[loading_august['load_location_name'] == 'Loading_Place_9']

loading_sep = (df.loc[df['start_time_load'].str.contains('2020-09') & (df['load_location_name'])])
sep_lp_1 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_1']
sep_lp_2 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_2']
sep_lp_3 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_3']
sep_lp_4 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_4']
sep_lp_5 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_5']
sep_lp_6 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_6']
sep_lp_7 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_7']
sep_lp_8 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_8']
sep_lp_9 = loading_sep.loc[loading_sep['load_location_name'] == 'Loading_Place_9']

loading_oct = (df.loc[df['start_time_load'].str.contains('2020-10') & (df['load_location_name'])])
oct_lp_1 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_1']
oct_lp_2 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_2']
oct_lp_3 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_3']
oct_lp_4 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_4']
oct_lp_5 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_5']
oct_lp_6 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_6']
oct_lp_7 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_7']
oct_lp_8 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_8']
oct_lp_9 = loading_oct.loc[loading_oct['load_location_name'] == 'Loading_Place_9']

loading_nov = (df.loc[df['start_time_load'].str.contains('2020-11') & (df['load_location_name'])])
nov_lp_1 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_1']
nov_lp_2 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_2']
nov_lp_3 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_3']
nov_lp_4 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_4']
nov_lp_5 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_5']
nov_lp_6 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_6']
nov_lp_7 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_7']
nov_lp_8 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_8']
nov_lp_9 = loading_nov.loc[loading_nov['load_location_name'] == 'Loading_Place_9']

loading_dec = (df.loc[df['start_time_load'].str.contains('2020-12') & (df['load_location_name'])])
dec_lp_1 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_1']
dec_lp_2 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_2']
dec_lp_3 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_3']
dec_lp_4 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_4']
dec_lp_5 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_5']
dec_lp_6 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_6']
dec_lp_7 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_7']
dec_lp_8 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_8']
dec_lp_9 = loading_dec.loc[loading_dec['load_location_name'] == 'Loading_Place_9']

loading_jan = (df.loc[df['start_time_load'].str.contains('2021-01') & (df['load_location_name'])])
jan_lp_1 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_1']
jan_lp_2 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_2']
jan_lp_3 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_3']
jan_lp_4 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_4']
jan_lp_5 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_5']
jan_lp_6 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_6']
jan_lp_7 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_7']
jan_lp_8 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_8']
jan_lp_9 = loading_jan.loc[loading_jan['load_location_name'] == 'Loading_Place_9']

loading_feb = (df.loc[df['start_time_load'].str.contains('2021-02') & (df['load_location_name'])])
feb_lp_1 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_1']
feb_lp_2 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_2']
feb_lp_3 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_3']
feb_lp_4 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_4']
feb_lp_5 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_5']
feb_lp_6 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_6']
feb_lp_7 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_7']
feb_lp_8 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_8']
feb_lp_9 = loading_feb.loc[loading_feb['load_location_name'] == 'Loading_Place_9']

loading_march21 = (df.loc[df['start_time_load'].str.contains('2021-03') & (df['load_location_name'])])
march21_lp_1 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_1']
march21_lp_2 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_2']
march21_lp_3 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_3']
march21_lp_4 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_4']
march21_lp_5 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_5']
march21_lp_6 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_6']
march21_lp_7 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_7']
march21_lp_8 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_8']
march21_lp_9 = loading_march21.loc[loading_march21['load_location_name'] == 'Loading_Place_9']

data = {
    'Loading location': ['Place 1', 'Place 2', 'Place 3', 'Place 4', 'Place 5', 'Place 6', 'Place 7', 'Place 8',
                         'Place 9'],
    'March 2020': [len(loading_place_1), len(loading_place_2), len(loading_place_3), len(loading_place_4),
                   len(loading_place_5), len(loading_place_6), len(loading_place_7), len(loading_place_8),
                   len(loading_place_9)],
    'April 2020': [len(apr_lp_1), len(apr_lp_2), len(apr_lp_3), len(apr_lp_4), len(apr_lp_5), len(apr_lp_6),
                   len(apr_lp_7), len(apr_lp_8), len(apr_lp_9)],
    'May 2020': [len(may_lp_1), len(may_lp_2), len(may_lp_3), len(may_lp_4), len(may_lp_5), len(may_lp_6),
                 len(may_lp_7), len(may_lp_8), len(may_lp_9)],
    'June 2020': [len(jun_lp_1), len(jun_lp_2), len(jun_lp_3), len(jun_lp_4), len(jun_lp_5), len(jun_lp_6),
                  len(jun_lp_7), len(jun_lp_8), len(jun_lp_9)],
    'July 2020': [len(jul_lp_1), len(jul_lp_2), len(jul_lp_3), len(jul_lp_4), len(jul_lp_5), len(jul_lp_6),
                  len(jul_lp_7), len(jul_lp_8), len(jul_lp_9)],
    'August 2020': [len(aug_lp_1), len(aug_lp_2), len(aug_lp_3), len(aug_lp_4), len(aug_lp_5), len(aug_lp_6),
                    len(aug_lp_7), len(aug_lp_8), len(aug_lp_9)],
    'September 2020': [len(sep_lp_1), len(sep_lp_2), len(sep_lp_3), len(sep_lp_4), len(sep_lp_5), len(sep_lp_6),
                       len(sep_lp_7), len(sep_lp_8), len(sep_lp_9)],
    'October 2020': [len(oct_lp_1), len(oct_lp_2), len(oct_lp_3), len(oct_lp_4), len(oct_lp_5), len(oct_lp_6),
                     len(oct_lp_7), len(oct_lp_8), len(oct_lp_9)],
    'November 2020': [len(nov_lp_1), len(nov_lp_2), len(nov_lp_3), len(nov_lp_4), len(nov_lp_5), len(nov_lp_6),
                      len(nov_lp_7), len(nov_lp_8), len(nov_lp_9)],
    'December 2020': [len(dec_lp_1), len(dec_lp_2), len(dec_lp_3), len(dec_lp_4), len(dec_lp_5), len(dec_lp_6),
                      len(dec_lp_7), len(dec_lp_8), len(dec_lp_9)],
    'January 2021': [len(jan_lp_1), len(jan_lp_2), len(jan_lp_3), len(jan_lp_4), len(jan_lp_5), len(jan_lp_6),
                     len(jan_lp_7), len(jan_lp_8), len(jan_lp_9)],
    'February 2021': [len(feb_lp_1), len(feb_lp_2), len(feb_lp_3), len(feb_lp_4), len(feb_lp_5), len(feb_lp_6),
                      len(feb_lp_7), len(feb_lp_8), len(feb_lp_9)],
    'March 2021': [len(march21_lp_1), len(march21_lp_2), len(march21_lp_3), len(march21_lp_4), len(march21_lp_5),
                   len(march21_lp_6), len(march21_lp_7), len(march21_lp_8), len(march21_lp_9)]}

df2 = pd.DataFrame(data, columns=['Loading location', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020',
                                  'August 2020', 'September 2020', 'October 2020', 'November 2020', 'December 2020',
                                  'January 2021', 'February 2021', 'March 2021'])

#df2.to_excel('Loading places.xlsx', index=False)

print("Yo Yo")
