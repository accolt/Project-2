import pandas as pd

df = pd.read_excel(
    r'D:\Montan University\2021 Summer semester\Monitoring Techniques, Data Handling\Case study\Case study 1.xlsx')

unloading_march20 = (df.loc[df['start_time_unload'].str.contains('2020-03') & (df['unload_location_name'])])
Unloading_Place_1 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_1']
Unloading_Place_2 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_2']
Unloading_Place_3 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_3']
Unloading_Place_4 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_4']
Unloading_Place_5 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_5']
Unloading_Place_6 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_6']
Unloading_Place_7 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_7']
Unloading_Place_8 = unloading_march20.loc[unloading_march20['unload_location_name'] == 'Unloading_Place_8']

# print(len(Unloading_Place_1))

unloading_april = (df.loc[df['start_time_unload'].str.contains('2020-04') & (df['unload_location_name'])])
apr_lp_1 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_1']
apr_lp_2 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_2']
apr_lp_3 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_3']
apr_lp_4 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_4']
apr_lp_5 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_5']
apr_lp_6 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_6']
apr_lp_7 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_7']
apr_lp_8 = unloading_april.loc[unloading_april['unload_location_name'] == 'Unloading_Place_8']

unloading_may = (df.loc[df['start_time_unload'].str.contains('2020-05') & (df['unload_location_name'])])
may_lp_1 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_1']
may_lp_2 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_2']
may_lp_3 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_3']
may_lp_4 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_4']
may_lp_5 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_5']
may_lp_6 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_6']
may_lp_7 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_7']
may_lp_8 = unloading_may.loc[unloading_may['unload_location_name'] == 'Unloading_Place_8']

unloading_june = (df.loc[df['start_time_unload'].str.contains('2020-06') & (df['unload_location_name'])])
jun_lp_1 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_1']
jun_lp_2 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_2']
jun_lp_3 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_3']
jun_lp_4 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_4']
jun_lp_5 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_5']
jun_lp_6 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_6']
jun_lp_7 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_7']
jun_lp_8 = unloading_june.loc[unloading_june['unload_location_name'] == 'Unloading_Place_8']

unloading_july = (df.loc[df['start_time_unload'].str.contains('2020-07') & (df['unload_location_name'])])
jul_lp_1 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_1']
jul_lp_2 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_2']
jul_lp_3 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_3']
jul_lp_4 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_4']
jul_lp_5 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_5']
jul_lp_6 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_6']
jul_lp_7 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_7']
jul_lp_8 = unloading_july.loc[unloading_july['unload_location_name'] == 'Unloading_Place_8']

unloading_august = (df.loc[df['start_time_unload'].str.contains('2020-08') & (df['unload_location_name'])])
aug_lp_1 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_1']
aug_lp_2 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_2']
aug_lp_3 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_3']
aug_lp_4 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_4']
aug_lp_5 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_5']
aug_lp_6 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_6']
aug_lp_7 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_7']
aug_lp_8 = unloading_august.loc[unloading_august['unload_location_name'] == 'Unloading_Place_8']

unloading_sep = (df.loc[df['start_time_unload'].str.contains('2020-09') & (df['unload_location_name'])])
sep_lp_1 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_1']
sep_lp_2 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_2']
sep_lp_3 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_3']
sep_lp_4 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_4']
sep_lp_5 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_5']
sep_lp_6 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_6']
sep_lp_7 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_7']
sep_lp_8 = unloading_sep.loc[unloading_sep['unload_location_name'] == 'Unloading_Place_8']

unloading_oct = (df.loc[df['start_time_unload'].str.contains('2020-10') & (df['unload_location_name'])])
oct_lp_1 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_1']
oct_lp_2 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_2']
oct_lp_3 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_3']
oct_lp_4 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_4']
oct_lp_5 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_5']
oct_lp_6 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_6']
oct_lp_7 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_7']
oct_lp_8 = unloading_oct.loc[unloading_oct['unload_location_name'] == 'Unloading_Place_8']

unloading_nov = (df.loc[df['start_time_unload'].str.contains('2020-11') & (df['unload_location_name'])])
nov_lp_1 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_1']
nov_lp_2 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_2']
nov_lp_3 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_3']
nov_lp_4 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_4']
nov_lp_5 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_5']
nov_lp_6 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_6']
nov_lp_7 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_7']
nov_lp_8 = unloading_nov.loc[unloading_nov['unload_location_name'] == 'Unloading_Place_8']

unloading_dec = (df.loc[df['start_time_unload'].str.contains('2020-12') & (df['unload_location_name'])])
dec_lp_1 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_1']
dec_lp_2 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_2']
dec_lp_3 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_3']
dec_lp_4 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_4']
dec_lp_5 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_5']
dec_lp_6 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_6']
dec_lp_7 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_7']
dec_lp_8 = unloading_dec.loc[unloading_dec['unload_location_name'] == 'Unloading_Place_8']

unloading_jan = (df.loc[df['start_time_unload'].str.contains('2021-01') & (df['unload_location_name'])])
jan_lp_1 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_1']
jan_lp_2 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_2']
jan_lp_3 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_3']
jan_lp_4 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_4']
jan_lp_5 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_5']
jan_lp_6 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_6']
jan_lp_7 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_7']
jan_lp_8 = unloading_jan.loc[unloading_jan['unload_location_name'] == 'Unloading_Place_8']

unloading_feb = (df.loc[df['start_time_unload'].str.contains('2021-02') & (df['unload_location_name'])])
feb_lp_1 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_1']
feb_lp_2 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_2']
feb_lp_3 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_3']
feb_lp_4 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_4']
feb_lp_5 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_5']
feb_lp_6 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_6']
feb_lp_7 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_7']
feb_lp_8 = unloading_feb.loc[unloading_feb['unload_location_name'] == 'Unloading_Place_8']

unloading_march21 = (df.loc[df['start_time_unload'].str.contains('2021-03') & (df['unload_location_name'])])
march21_lp_1 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_1']
march21_lp_2 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_2']
march21_lp_3 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_3']
march21_lp_4 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_4']
march21_lp_5 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_5']
march21_lp_6 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_6']
march21_lp_7 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_7']
march21_lp_8 = unloading_march21.loc[unloading_march21['unload_location_name'] == 'Unloading_Place_8']

data = {
    'Unloading location': ['Place 1', 'Place 2', 'Place 3', 'Place 4', 'Place 5', 'Place 6', 'Place 7', 'Place 8'],
    'March 2020': [len(Unloading_Place_1), len(Unloading_Place_2), len(Unloading_Place_3), len(Unloading_Place_4),
                   len(Unloading_Place_5), len(Unloading_Place_6), len(Unloading_Place_7), len(Unloading_Place_8)],
    'April 2020': [len(apr_lp_1), len(apr_lp_2), len(apr_lp_3), len(apr_lp_4), len(apr_lp_5), len(apr_lp_6),
                   len(apr_lp_7), len(apr_lp_8)],
    'May 2020': [len(may_lp_1), len(may_lp_2), len(may_lp_3), len(may_lp_4), len(may_lp_5), len(may_lp_6),
                 len(may_lp_7), len(may_lp_8)],
    'June 2020': [len(jun_lp_1), len(jun_lp_2), len(jun_lp_3), len(jun_lp_4), len(jun_lp_5), len(jun_lp_6),
                  len(jun_lp_7), len(jun_lp_8)],
    'July 2020': [len(jul_lp_1), len(jul_lp_2), len(jul_lp_3), len(jul_lp_4), len(jul_lp_5), len(jul_lp_6),
                  len(jul_lp_7), len(jul_lp_8)],
    'August 2020': [len(aug_lp_1), len(aug_lp_2), len(aug_lp_3), len(aug_lp_4), len(aug_lp_5), len(aug_lp_6),
                    len(aug_lp_7), len(aug_lp_8)],
    'September 2020': [len(sep_lp_1), len(sep_lp_2), len(sep_lp_3), len(sep_lp_4), len(sep_lp_5), len(sep_lp_6),
                       len(sep_lp_7), len(sep_lp_8)],
    'October 2020': [len(oct_lp_1), len(oct_lp_2), len(oct_lp_3), len(oct_lp_4), len(oct_lp_5), len(oct_lp_6),
                     len(oct_lp_7), len(oct_lp_8)],
    'November 2020': [len(nov_lp_1), len(nov_lp_2), len(nov_lp_3), len(nov_lp_4), len(nov_lp_5), len(nov_lp_6),
                      len(nov_lp_7), len(nov_lp_8)],
    'December 2020': [len(dec_lp_1), len(dec_lp_2), len(dec_lp_3), len(dec_lp_4), len(dec_lp_5), len(dec_lp_6),
                      len(dec_lp_7), len(dec_lp_8)],
    'January 2021': [len(jan_lp_1), len(jan_lp_2), len(jan_lp_3), len(jan_lp_4), len(jan_lp_5), len(jan_lp_6),
                     len(jan_lp_7), len(jan_lp_8)],
    'February 2021': [len(feb_lp_1), len(feb_lp_2), len(feb_lp_3), len(feb_lp_4), len(feb_lp_5), len(feb_lp_6),
                      len(feb_lp_7), len(feb_lp_8)],
    'March 2021': [len(march21_lp_1), len(march21_lp_2), len(march21_lp_3), len(march21_lp_4), len(march21_lp_5),
                   len(march21_lp_6), len(march21_lp_7), len(march21_lp_8)]}

df3 = pd.DataFrame(data,
                   columns=['Unloading location', 'March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020',
                            'August 2020', 'September 2020', 'October 2020', 'November 2020', 'December 2020',
                            'January 2021', 'February 2021', 'March 2021'])

#df3.to_excel('Unloading places.xlsx', index=False)

print("Mic check")
