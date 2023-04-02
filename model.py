#importing necessary libraries
import pandas as pd
from numpy import argmax
from transformers import pipeline
from flair.models import TextClassifier
from flair.data import Sentence
from tqdm import tqdm

class Model():

    def __init__(self, path):

        self.path = path
        self.original_df = pd.read_csv(self.path)
        self.tweet_list = self.original_df['TWEET'].to_list()


        # Using bertweet-base sentiment analysis
        self.bertweet_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

        # Twitter roberta base model
        self.twt_roberta_model = pipeline(model="cardiffnlp/twitter-roberta-base-sentiment")

        # Emotion bert base model
        self.Emotion_bert = pipeline(model='bhadresh-savani/distilbert-base-uncased-emotion')

        # Flair model
        self.flair_classifier = TextClassifier.load('en-sentiment')

        # zero_shot
        self.zsl_classifier = pipeline("zero-shot-classification",
                                  model="oigele/Fb_improved_zeroshot")

        print("all models loaded sucessfully.....!")

        self.bertweet, self.robertatweet, self.emotiontweet, self.flairtweet, self.zero_shot = {'label': [], 'score': []}, \
                                                                               {'label': [], 'score': []}, \
                                                                               {'label': [], 'score': []}, \
                                                                               {'label': [], 'score': []}, \
                                                                               {'label': [], 'score': []}


    def category_encoding(self, label):
        """
        This function synchronize all the model outputs to standard labels.
        :param label: pridicted label from model
        :return: encoded label
        """
        look_up = {'positive': ['POS', 'LABEL_2'],
                   'neutral': ['NEU', 'LABEL_1'],
                   'negative': ['NEG', 'LABEL_0']}
        for key, val in look_up.items():
            if label in val:
                return key

    def output_label_score(self, model, check=True):
        """
        This function performs label encoding depending on type of model
        :param model: large language model
        :param check: to confirm the type of model and its output
        :return: label and score based on model
        """
        if check:
            label = self.category_encoding(model[0]['label'])
            score = model[0]['score']

        else:
            label = model[0]['label']
            score = model[0]['score']
        return label, score

    def output_label_score_flair(self, model):
        for label in model.labels:
            label1 = label.value
            score1 = label.score
        return label1.lower(), score1

    def classifier(self):
        self.stress_labels = ['positive', 'neutral', 'negative']

        for tweet in tqdm(self.tweet_list):
            # for bert
            bert = self.bertweet_model(tweet)
            labelb, scoreb = self.output_label_score(bert)
            self.bertweet['label'].append(labelb)
            self.bertweet['score'].append(scoreb)


            # for roberta
            roberta = self.twt_roberta_model(tweet)
            labelr, scorer = self.output_label_score(roberta)
            self.robertatweet['label'].append(labelr)
            self.robertatweet['score'].append(scorer)

            # for emotion
            emotion = self.Emotion_bert(tweet)
            labele, scoree = self.output_label_score(emotion, check=False)
            self.emotiontweet['label'].append(labele)
            self.emotiontweet['score'].append(scoree)

            # for flair
            flair = Sentence(tweet)
            self.flair_classifier.predict(flair)
            labelf, scoref = self.output_label_score_flair(flair)
            self.flairtweet['label'].append(labelf)
            self.flairtweet['score'].append(scoref)

            # for zero_shot
            res = self.zsl_classifier(tweet, self.stress_labels)
            SCORES = res["scores"]
            CLASSES = res["labels"]
            BEST_INDEX = argmax(SCORES)
            predicted_class = CLASSES[BEST_INDEX]
            predicted_score = SCORES[BEST_INDEX]
            self.zero_shot['label'].append(predicted_class)
            self.zero_shot['score'].append(predicted_score)

    def make_dataframe(self):
        """
        This function creates a pandas dataframe.
        :return: Combines all the models output in a single dataframe
        """

        bert_df = pd.DataFrame.from_dict(self.bertweet)
        bert_df.rename(columns={'label': 'bertweet_label', 'score': 'bertweet_score'}, inplace=True)

        robert_df = pd.DataFrame.from_dict(self.robertatweet)
        robert_df.rename(columns={'label': 'robertweet_label', 'score': 'robertweet_score'}, inplace=True)

        emotion_df = pd.DataFrame.from_dict(self.emotiontweet)
        emotion_df.rename(columns={'label': 'emotiontweet_label', 'score': 'emotiontweet_score'}, inplace=True)

        flair_df = pd.DataFrame.from_dict(self.flairtweet)
        flair_df.rename(columns={'label': 'flairtweet_label', 'score': 'flairtweet_score'}, inplace=True)

        zeroshot_df = pd.DataFrame.from_dict(self.zero_shot)
        zeroshot_df.rename(columns={'label': 'zeroshot_label', 'score': 'zeroshot_score'}, inplace=True)

        tweet_df_final = pd.concat([self.original_df, bert_df, robert_df, emotion_df, flair_df, zeroshot_df], axis=1)
        tweet_df_final['Final_label'] = tweet_df_final[['bertweet_label', 'robertweet_label', 'flairtweet_label', 'zeroshot_label']].mode(axis=1)[0]
        to_save = "result_" + str(self.path.split('/')[-1])
        tweet_df_final.to_csv('/Users/krishna/PycharmProjects/stress_analysis/data/model_results/' + to_save)

        return tweet_df_final



if __name__ == '__main__':
    #modify these path to replicate the output

    on_path = ["/Users/krishna/PycharmProjects/stress_analysis/data/preproceseed/Final_before_covid_ON.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/preproceseed/Final_during_covid_ON.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/preproceseed/Final_after_covid_ON.csv"]

    bc_path = ["/Users/krishna/PycharmProjects/stress_analysis/data/preproceseed/Final_before_covid_BC.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/preproceseed/Final_during_covid_BC.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/preproceseed/Final_after_covid_BC.csv"]

    for op in on_path[:1]:
        dc = Model(op)
        dc.classifier()
        dc.make_dataframe()







