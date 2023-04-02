#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import cufflinks as cf
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
cf.go_offline() # required to use plotly offline (no account required).
py.init_notebook_mode() # graphs charts inline (IPython).
import plotly.io as pio
pio.renderers.default = "browser"

class Analysis():


    def make_dict(self, dataframe):
        dic = dict(dataframe.value_counts())
        total = len(dataframe)
        for k, v in dic.items():
            dic[k] = round((v * 100) / total, 2)

        return dic

    def plot_data_fnc(self, dataframe1, dataframe2, timeframe_name):
        zero_d_on = self.make_dict(dataframe1['zeroshot_label'])
        # print('zero: ', zero_d_on)
        zero_d_bc = self.make_dict(dataframe2['zeroshot_label'])
        # print('zero: ', zero_d_bc)

        bertt_d_on = self.make_dict(dataframe1['bertweet_label'])
        # print('bert: ', bertt_d_on)
        bertt_d_bc = self.make_dict(dataframe2['bertweet_label'])
        # print('bert: ', bertt_d_bc)

        rober_d_on = self.make_dict(dataframe1['robertweet_label'])
        # print('rob: ', rober_d_on)
        rober_d_bc = self.make_dict(dataframe2['robertweet_label'])
        # print('rob: ', rober_d_bc)

        flair_d_on = self.make_dict(dataframe1['flairtweet_label'])
        # print('flair_d: ', flair_d_on)
        flair_d_bc = self.make_dict(dataframe2['flairtweet_label'])
        # print('flair_d: ', flair_d_bc)

        # using plotly for ploting during Ontario
        fig_1 = make_subplots(rows=4, cols=4,
                              subplot_titles=("Bert_Tweet_ON", "Bert_Tweet_BC",
                                              "Flair_Tweet_ON","Flair_Tweet_BC","Roberta_Tweet_ON", "Roberta_Tweet_BC", "Zero_Shot_ON","Zero_Shot_BC"))

        # bertweet
        fig_1.add_trace(
            go.Bar(x=list(bertt_d_on.keys()), y=list(bertt_d_on.values()), name='bertweet', marker=dict(color='#83c5be'),
                   text=list(bertt_d_on.values())), row=1, col=1)
        # robertweet
        fig_1.add_trace(
            go.Bar(x=list(rober_d_on.keys()), y=list(rober_d_on.values()), name='robertweet', marker=dict(color='#83c5be'),
                   text=list(rober_d_on.values())), row=2, col=1)
        # flairtweet
        fig_1.add_trace(
            go.Bar(x=list(flair_d_on.keys()), y=list(flair_d_on.values()), name='flairtweet', marker=dict(color='#83c5be'),
                   text=list(flair_d_on.values())), row=1, col=3)
        # zeroshot
        fig_1.add_trace(
            go.Bar(x=list(zero_d_on.keys()), y=list(zero_d_on.values()), name='zero-shot', marker=dict(color='#83c5be'),
                   text=list(zero_d_on.values())), row=2, col=3)

        # bertweet
        fig_1.add_trace(
            go.Bar(x=list(bertt_d_bc.keys()), y=list(bertt_d_bc.values()), name='bertweet', marker=dict(color='#e29578'),
                   text=list(bertt_d_bc.values())), row=1, col=2)
        # robertweet
        fig_1.add_trace(
            go.Bar(x=list(rober_d_bc.keys()), y=list(rober_d_bc.values()), name='robertweet', marker=dict(color='#e29578'),
                   text=list(rober_d_bc.values())), row=2, col=2)
        # flairtweet
        fig_1.add_trace(
            go.Bar(x=list(flair_d_bc.keys()), y=list(flair_d_bc.values()), name='flairtweet', marker=dict(color='#e29578'),
                   text=list(flair_d_bc.values())), row=1, col=4)
        # zeroshot
        fig_1.add_trace(
            go.Bar(x=list(zero_d_bc.keys()), y=list(zero_d_bc.values()), name='zero-shot', marker=dict(color='#e29578'),
                   text=list(zero_d_bc.values())), row=2, col=4)

        # updating labels of x axis and y axis
        fig_1['layout']['xaxis']['title'] = 'Label'
        fig_1['layout']['yaxis']['title'] = 'Frequency Count'

        fig_1['layout']['xaxis2']['title'] = 'Label'
        fig_1['layout']['yaxis2']['title'] = 'Frequency Count'

        fig_1['layout']['xaxis3']['title'] = 'Label'
        fig_1['layout']['yaxis3']['title'] = 'Frequency Count'

        fig_1['layout']['xaxis4']['title'] = 'Label'
        fig_1['layout']['yaxis4']['title'] = 'Frequency Count'

        fig_1['layout']['xaxis5']['title'] = 'Label'
        fig_1['layout']['yaxis5']['title'] = 'Frequency Count'

        fig_1['layout']['xaxis6']['title'] = 'Label'
        fig_1['layout']['yaxis6']['title'] = 'Frequency Count'

        fig_1['layout']['xaxis7']['title'] = 'Label'
        fig_1['layout']['yaxis7']['title'] = 'Frequency Count'

        fig_1['layout']['xaxis8']['title'] = 'Label'
        fig_1['layout']['yaxis8']['title'] = 'Frequency Count'

        fig_1.update_layout(height=1400, width=1400, title_text=timeframe_name, showlegend=False)
        fig_1.update_traces(texttemplate='%{text}', textposition='inside')
        fig_1.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", yaxis=dict(ticksuffix='%'),
                            yaxis2=dict(ticksuffix='%'), yaxis3=dict(ticksuffix='%'), yaxis4=dict(ticksuffix='%'),
                            yaxis5=dict(ticksuffix='%'),yaxis6=dict(ticksuffix='%'),yaxis7=dict(ticksuffix='%'),
                            yaxis8=dict(ticksuffix='%'))

        fig_1.update_xaxes(showgrid=False)
        fig_1.update_yaxes(showgrid=False)

        fig_1.update_yaxes(range=[0.0, 80.0], row=1, col=1)
        fig_1.update_yaxes(range=[0.0, 80.0], row=2, col=2)
        fig_1.update_yaxes(range=[0.0, 80.0], row=3, col=3)
        fig_1.update_yaxes(range=[0.0, 80.0], row=4, col=4)
        fig_1.update_yaxes(range=[0.0, 80.0], row=1, col=1)
        fig_1.update_yaxes(range=[0.0, 80.0], row=2, col=2)
        fig_1.update_yaxes(range=[0.0, 80.0], row=3, col=3)
        fig_1.update_yaxes(range=[0.0, 80.0], row=4, col=4)

        fig_1.show()

    def majority_count(self):
        """
        This function performs corpus analysis.

        """
        b_o = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_before_covid_ON_v2.csv")
        d_o = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_during_covid_ON_v2.csv")
        a_o = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_after_covid_ON_v2.csv")


        b_b = pd.read_csv("/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_before_covid_BC_v1.csv")
        d_b = pd.read_csv("/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_during_covid_BC_v1.csv")
        a_b = pd.read_csv("/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_after_covid_BC_v1.csv")


        # Before On Majority value count
        before_on_d = self.make_dict(b_o['Final_label'])
        print('before_on_d: ', before_on_d)
        before_bc_d = self.make_dict(b_b['Final_label'])
        print('before_bc_d: ', before_bc_d)
        # During On Majority value count
        during_on_d = self.make_dict(d_o['Final_label'])
        print('during_on_d ', during_on_d)
        during_bc_d = self.make_dict(d_b['Final_label'])
        print('during_bc_d ', during_bc_d)
        # After On Majority value count
        after_on_d = self.make_dict(a_o['Final_label'])
        print('after_on_d: ', after_on_d)
        after_bc_d = self.make_dict(a_b['Final_label'])
        print('after_bc_d: ', after_bc_d)

        # Before On Majority value count
        fig_4 = make_subplots(rows=1, cols=2,
                              subplot_titles=("ON","BC"))

        fig_4.add_trace(go.Bar(x=list(before_on_d.keys()), name='Before Covid19',
                                 marker=dict(color='#0074B7'), text=list(before_on_d.values())),row =1, col =1)
#y=list(before_on_d.values())
        # During On Majority value count
        fig_4.add_trace(go.Bar(x=list(during_on_d.keys()), name='During Covid19',
                               marker=dict(color='#60A3D9'), text=list(during_on_d.values())),row =1, col =1)

        # After On Majority value count
        fig_4.add_trace(go.Bar(x=list(after_on_d.keys()), name='After Covid19',
                               marker=dict(color='#BFD7ED '), text=list(after_on_d.values())),row =1, col =1)

        fig_4.add_trace(go.Bar(x=list(before_bc_d.keys()), y=list(before_bc_d.values()), name='Before Covid19',
                                 marker=dict(color='#c9184a'), text=list(before_bc_d.values())),row =1, col =2)

        # During On Majority value count
        fig_4.add_trace(go.Bar(x=list(during_bc_d.keys()), y=list(during_bc_d.values()), name='During Covid19',
                               marker=dict(color='#ff8fab'), text=list(during_bc_d.values())),row =1, col =2)

        # After On Majority value count
        fig_4.add_trace(go.Bar(x=list(after_bc_d.keys()), y=list(after_bc_d.values()), name='After Covid19',
                               marker=dict(color='#ffb3c1 '), text=list(after_bc_d.values())),row =1, col =2)

        fig_4.update_traces(texttemplate='%{text}', textposition='outside')
        fig_4.update_layout(barmode='stack', height=550, width=700,
                            title_text='Comparsion of Before Vs During Vs After COVID-19 sentiments')
        fig_4.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                            # yaxis=dict(ticksuffix='%',autorange = True),
                            # yaxis2=dict(ticksuffix='%',autorange = True)
                            )
        fig_4.update_xaxes(showgrid=False)
        fig_4.update_yaxes(showgrid=False)
        # fig_4.update_yaxes(range=[0.0, 210.0])
        # fig_4.update_yaxes(range=[0.0, 210.0])
        fig_4.show()
        # fig_4.write_image("sentiments.png", scale=2)

    def emotion_anl(self):
        # during_on['Final_label'].value_counts().iplot(kind='bar')
        # ONTARIO
        b_o = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_before_covid_ON_v2.csv")
        d_o = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_during_covid_ON_v2.csv")
        a_o = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_after_covid_ON_v2.csv")

        #BRITISH COLUMBIA
        b_b = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_before_covid_BC_v1.csv")

        d_b = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_during_covid_BC_v1.csv")

        a_b = pd.read_csv(
            "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_after_covid_BC_v1.csv")

    #ONTARIO
        before_on_dd = dict(b_o['emotiontweet_label'].value_counts())
        before_on_dd.pop('joy', None)
        # print('before_on_dd: ', before_on_dd)
        during_on_dd = dict(d_o['emotiontweet_label'].value_counts())
        during_on_dd.pop('joy', None)
        # print('during_on_dd: ', during_on_dd)
        after_on_dd = dict(a_o['emotiontweet_label'].value_counts())
        after_on_dd.pop('joy', None)
        # print('after_on_dd: ', after_on_dd)

    #BRITISH COLUMBIA
        before_bc_dd = dict(b_b['emotiontweet_label'].value_counts())
        before_bc_dd.pop('joy', None)
        # print('before_on_dd: ', before_on_dd)
        during_bc_dd = dict(d_b['emotiontweet_label'].value_counts())
        during_bc_dd.pop('joy', None)
        # print('during_on_dd: ', during_on_dd)
        after_bc_dd = dict(a_b['emotiontweet_label'].value_counts())
        after_bc_dd.pop('joy', None)
        # print('after_on_dd: ', after_on_dd)
        # using plotly for ploting during Ontario
        fig_5 = make_subplots(rows=2, cols=3, subplot_titles=("Before COVID-19 ON", "During COVID-19 ON", "After COVID-19 ON",
                                                              "Before COVID-19 BC", "During COVID-19 BC", "After COVID-19 BC"))
        # During On Majority value count
        fig_5.add_trace(
            go.Bar(x=list(before_on_dd.keys()), y=list(before_on_dd.values()), marker=dict(color='#faab36')), row=1,
            col=1)
        # Before On Majority value count
        fig_5.add_trace(
            go.Bar(x=list(during_on_dd.keys()), y=list(during_on_dd.values()), marker=dict(color="#f78104")), row=1,
            col=2)
        # After On Majority value count
        fig_5.add_trace(go.Bar(x=list(after_on_dd.keys()), y=list(after_on_dd.values()), marker=dict(color="#fd5901")),
                        row=1, col=3)
        #BRITISH COLUMBIA
        fig_5.add_trace(go.Bar(x=list(before_bc_dd.keys()), y=list(before_bc_dd.values()), marker=dict(color="#249ea0")),
                        row=2, col=1)
        fig_5.add_trace(go.Bar(x=list(during_bc_dd.keys()), y=list(during_bc_dd.values()), marker=dict(color="#008083")),
                        row=2, col=2)
        fig_5.add_trace(go.Bar(x=list(after_bc_dd.keys()), y=list(after_bc_dd.values()), marker=dict(color="#005f60")),
                        row=2, col=3)

        # updating labels of x axis and y axis
        fig_5['layout']['xaxis']['title'] = 'Emotions'
        fig_5['layout']['yaxis']['title'] = 'Frequency Count'

        fig_5['layout']['xaxis2']['title'] = 'Emotions'
        fig_5['layout']['yaxis2']['title'] = 'Frequency Count'

        fig_5['layout']['xaxis3']['title'] = 'Emotions'
        fig_5['layout']['yaxis3']['title'] = 'Frequency Count'

        fig_5['layout']['xaxis4']['title'] = 'Emotions'
        fig_5['layout']['yaxis4']['title'] = 'Frequency Count'

        fig_5['layout']['xaxis5']['title'] = 'Emotions'
        fig_5['layout']['yaxis5']['title'] = 'Frequency Count'

        fig_5['layout']['xaxis6']['title'] = 'Emotions'
        fig_5['layout']['yaxis6']['title'] = 'Frequency Count'

        fig_5.update_layout(height=550, width=850,
                            title_text="Before vs During vs After COVID-19 emotion analysis ",
                            showlegend=False)
        fig_5.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(size=8))
        fig_5.for_each_xaxis(lambda axis: axis.title.update(font=dict(size=9)))
        fig_5.for_each_yaxis(lambda axis: axis.title.update(font=dict(size=9)))
        fig_5.update_xaxes(showgrid=False)
        fig_5.update_yaxes(showgrid=False)
        fig_5.update_yaxes(range=[0.0, 400.0])
        fig_5.update_yaxes(range=[0.0, 400.0])
        # fig_5.show()
        fig_5.write_image("Fig5.png", scale=2)


if __name__ == "__main__":
    a = Analysis()
    timeframe = ["Before covid ON and BC","During covid ON and BC","After covid ON and BC"]
    on_path = ["/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_before_covid_ON_v2.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_during_covid_ON_v2.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_after_covid_ON_v2.csv"]
    bc_path = ["/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_before_covid_BC_v1.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_during_covid_BC_v1.csv",
               "/Users/krishna/PycharmProjects/stress_analysis/data/model_results/Final_after_covid_BC_v1.csv"]

    for o, b, name in zip(on_path, bc_path, timeframe):
        dfon = pd.read_csv(o)
        dfbc = pd.read_csv(b)
        a.plot_data_fnc(dataframe1=dfon, dataframe2=dfbc, timeframe_name=name)

    a.majority_count() # Corpus Analysis (Produces Fig.4 in research paper)
    a.emotion_anl() # Emotion Analysis (Produces Fig.5 in research paper)



