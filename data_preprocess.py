# text cleaning
import preprocessor as p
import re
# Importing libraries
import pandas as pd
import numpy as np
import string


class DataCreation:

    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(self.path)
        print(f"DataFrame loaded with shape {self.df.shape}")
        print(f"FILENAME: {self.path.split('/')[-1]}")

    def remove_punct(self, text):

        text = "".join([char for char in text if char not in string.punctuation])
        text = re.sub('[0-9]+', '', text)
        return text

    def preprocess(self):
        """
        This function preprocesses the data based on a keep word list
        :return: saves final csv on PWD.
        """
        keep_words = ['loneliness', 'depression', 'death', 'sad', 'loss', 'lost'
            , 'burnout', 'stress', 'suicide', 'depressed', 'depressive',
                      'emotional', 'stressors', 'anxiety']

        covid_cleaned_tweet = [p.clean(t) for t in self.df.tweet]
        self.df['cleaned_tweet'] = [self.remove_punct(x) for x in covid_cleaned_tweet]
        self.df["Number of Words"] = self.df["cleaned_tweet"].apply(lambda n: len(n.split()))
        covid_copy = self.df.loc[self.df["Number of Words"] > 2]
        covid_copy['cleaned_tweet'] = covid_copy['cleaned_tweet'].str.lower()
        covid_copy.reset_index()
        list_of_words_during_covid = covid_copy['cleaned_tweet'].to_list()
        date_ = covid_copy['new_date'].to_list()
        time_ = covid_copy['Time'].to_list()
        username_ = covid_copy['username'].to_list()

        date_toappend = []
        time_toappend = []
        zero_shot_input_list = []
        username_toappend = []

        for date, time, sent, uname in zip(date_, time_, list_of_words_during_covid, username_):
            for word in keep_words:
                if word in sent:
                    zero_shot_input_list.append(sent)
                    date_toappend.append(date)
                    time_toappend.append(time)
                    username_toappend.append(uname)
                    break

        # CSV OF ZERO_SHOT
        data = {'TWEET': zero_shot_input_list,
                'USERNAME': username_toappend,
                'DATE': date_toappend,
                'TIME': time_toappend}

        data_ = pd.DataFrame(data, columns=['TWEET', 'USERNAME', 'DATE', 'TIME'])
        to_save = "Final_" + str(self.path.split('/')[-1])
        # print(to_save)
        data_.to_csv('/Users/krishna/PycharmProjects/stress_analysis/data/' + to_save)
        # return data_


if __name__ == '__main__':
    #modify paths to replicate the output.
    on_path = ["/Users/krishna/PycharmProjects/stress_analysis/data/ON/before_covid_ON.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/ON/during_covid_ON.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/ON/after_covid_ON.csv"]
    bc_path = ["/Users/krishna/PycharmProjects/stress_analysis/data/BC/before_covid_BC.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/BC/during_covid_BC.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/BC/after_covid_BC.csv"]

    for op in on_path:
        dc = DataCreation(op)
        dc.preprocess()
    for bp in bc_path:
        dc1 = DataCreation(bp)
        dc1.preprocess()
