## Stress among Canadian Medical Professionals: A Twitter Analysis (v 1.0)
The outbreak of COVID-19 has placed healthcare workers under psychological stress. In Canada, ongoing crises like burnout, increased workload, and limited medical supplies have affected healthcare workers and their mental health, leading to symptoms like anxiety, depression and post-traumatic stress disorder.

## Files
- BERTopic : performed topic modeling using BERTopic.
- Data : dataset used in this project.
- Results: output of analysis and final models result.
- analysis.py : performs stress analysis.
- data_preprocess.py : clean and filter data.
- keep_words.txt : selected stress related words.
- model.py : final model implementation python file.
- requirements.txt : required imports to run the program successfuly.
- Tweet_Handles_BC.csv : list of tweet handles of medical professionals in British Columbia.
- Tweet_Handles_ON.csv : list of tweet handles of medical professionals in Ontario.

## Description
This research aims to examine the levels of stress experienced by healthcare workers during the pandemic by analyzing their Twitter activity in two major Canadian provinces, British Columbia and Ontario. This study utilizes both quantitative and qualitative analysis of Twitter data to investigate the mental wellness of healthcare workers in Canada _before, during, and after_ the COVID-19 pandemic. The study employs topic modeling technique and large language models, to analyze tweets and categorize them into positive, negative, and neutral sentiments, each with a confidence score ranging from 0 to 1. The results are visualized in the form of graphs to facilitate interpretation. The analysis reveals that negative sentiments have increased significantly during and after the pandemic, with sadness, anger, and fear being the dominant negative emotions and remain elevated in both provinces, with a higher peak observed in Ontario.
``` python
for o, b, name in zip(on_path, bc_path, timeframe):
        dfon = pd.read_csv(o)
        dfbc = pd.read_csv(b)
        a.plot_data_fnc(dataframe1=dfon, dataframe2=dfbc, timeframe_name=name)
``` 
## Installation
(Optional) setup a virtual environment to install necessary packages.
``` commandline
virtualenv .venv
source .venv/bin/activate
```
Install the packages listed in Requirement.txt file
```shell
pip install -r requirements.txt
```
Run Program!

## Usage
This program is simple and can be run using command line in system where python is already installed.
To perform an analysis run this file.
```shell
Python analysis.py
```
To run the models used in this project run this file.
```shell
Python model.py
```

## Support
Please email your questions and comments to:

* __Email__: [Krishna Gandhi](mailto:kgandhi1@lakeheadu.ca)
* __Email__: [Grishma Shah](mailto:gshah1@lakeheaadu.ca)
* __Email__: [Thrylokya Vegulla](mailto:tvegulla@lakeheadu.ca)
* __Email__: [Prof. Vijay Mago](mailto:vmago@lakeheadu.ca)

## Acknowledgment
I would like to give credit to
* BERTopic: BERTopic developers for open sourcing the best topic modeling model.[Github](https://github.com/MaartenGr/BERTopic)
* Hugging Face: For all the large language models.[Website](https://huggingface.co/models) 
* Flair: A very simple framework for state-of-the-art NLP.[Github](https://github.com/flairNLP/flair)
* Dr. Vijay Mago, Associate Professor, Computer Science Department, Lakehead University, Thunder Bay, CA.[Profile](https://www.lakeheadu.ca/users/M/vmago/node/25295)

## License
This project uses all the open-source models provided by Hugging Face, Flair community and BERTopic model. Please ensure to follow all the community guidelines provided by them.

## Project Status
This project is currently under-development. There will be future improvements. 
* __Last modification__:- 04/01/2023 (mm/dd/yy)


