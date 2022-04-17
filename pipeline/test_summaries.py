from unittest import TestCase
import unittest
import datetime
import pandas as pd
from summaries import zipcode_summary, zipcode_summary_time, yearly_stats, overall_stats

class TestSummaries (unittest.TestCase):

    def test_zipcode_summary(self):
        input_df=pd.DataFrame([
        {'zipcode':12345,'city':'ABC','county':'County1','year':'1234','count_lightning':3},
        {'zipcode':12345,'city':'LAC','county':'County2','year':'1234','count_lightning':3},
        {'zipcode':12345,'city':'LAC','county':'County2','year':'1234','count_lightning':5},
        {'zipcode':12345,'city':'DEF','county':'County3','year':'1234','count_lightning':3}
        ])

        expected_output_df = pd.DataFrame([
        {'zipcode':12345,'city':'ABC','county':'County1','year':'1234','count_lightning':3},
        {'zipcode':12345,'city':'DEF','county':'County3','year':'1234','count_lightning':3},
        {'zipcode':12345,'city':'LAC','county':'County2','year':'1234','count_lightning':8}
        ])

        actual_output_df= zipcode_summary(input_df)
        self.assertEqual(actual_output_df.shape,expected_output_df.shape,msg='Equal')

    def test_zipcode_summary_time(self):
        input_df=pd.DataFrame([
        {'zipcode':12345,'date':datetime.datetime(1,2,3),'count_lightning':3},
        {'zipcode':23456,'date':datetime.datetime(1,2,3),'count_lightning':3},
        {'zipcode':12345,'date':datetime.datetime(1,2,3),'count_lightning':4}
        ])
        expected_output_df = pd.DataFrame([
        {'zipcode':12345,'date':datetime.datetime(1,2,3),'count_lightning':7},
        {'zipcode':23456,'date':datetime.datetime(1,2,3),'count_lightning':3},
        {'zipcode':'Total','date':datetime.datetime(1,2,3),'count_lightning':10}
        ])
        actual_output_df= zipcode_summary_time(input_df)
        self.assertEqual(actual_output_df.shape,expected_output_df.shape,msg='Equal')

    def test_stats_maxes_equal(self):
        input_df=pd.DataFrame([
        {'zipcode':90027,'city':'LA', 'county':'Los Angeles County','year':	1987,'count_lightning':6},
        {'zipcode':90027,'city':'LA', 'county':'Los Angeles County','year':	1988,'count_lightning':7},
        {'zipcode':90027,'city':'LA', 'county':'Los Angeles County','year':	1990,'count_lightning':500}
        ])
        output1= yearly_stats(input_df)['max'].max()
        output2 = overall_stats(input_df)['count_lightning'][3]
        self.assertEqual(output1,output2,msg='Equal')


if __name__ == '__main__':
    unittest.main()
