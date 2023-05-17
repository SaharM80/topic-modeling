# Topic Modeler

Using Bert Transformer model and fine-tuning it to predict topics

## Introduction

[Google Drive Project Folder Link](https://drive.google.com/drive/folders/1D34L8irmRaHmPRQd6ni67sEmM3dHjy1r?usp=share_link)

### Folder Structure

```
topic-modeling
│   README.md
|
└───models
|    │
│    └────bert_topic_modeling
|    |    │   vocab.txt
│    |    │   training_args.bin
│    |    │   tokenizer.json
|    |    |   ...
|    |
|    └───  LSTM_topic_modeling
|          │   variables
│          │   assets
│          │   ...
|
└───notebooks
│   │   1_Data_Cleaning.ipynb
│   │   2_Training_Bert_Model.ipynb
|   |   3_Training_LSTM_Model.ipynb
│
└───src
    │   __init__.py
    │   main.py
    |   topic_modeler.py
    |   utils.py
```

Notebook 1_Data_Clearning contains the first part of the given task. For the second part of the task, Two models were trained. Notebook 2_Training_Bert_model contains the training of the first model that was fine-tuned on Bert. This model was turned into an app and had better results. Notebook 3_Training_LSTM_Model contains the training of the second model that used `GloVe` to tokenize the text and `Keras` library to train an LSTM model.

The models are saved in bert_topic_modeling and LSTM_topic_modeling inside the models folder.

**Note:** Only the model with the better results is turned into an app and the rest of the README file is about that model.

### Training

Training was done on google colab gpus, training notebook can be found at `topic-modeling/notebooks`.
Training includes two steps:

1. Tokenizing the text
2. Fine-tunning the pretrained `bert-base-uncased` model on the given dataset. it was trained for `12 epochs` and `20 percent` of the data was kept for testing.

<hr>

### Testing And Evaluation

Model achieved `0.49 percent accuracy` an `F1 Score of 0.75` and an `Roc Auc of 0.85`.

| Epoch | Training Loss | Validation Loss | F1       | Roc Auc  | Accuracy |
| ----- | ------------- | --------------- | -------- | -------- | -------- |
| 1     | No log        | 0.159075        | 0.669535 | 0.770418 | 0.400582 |
| 2     | 0.190100      | 0.130444        | 0.752364 | 0.837775 | 0.496605 |
| 3     | 0.190100      | 0.128395        | 0.750346 | 0.840385 | 0.495635 |
| 4     | 0.092600      | 0.133844        | 0.743528 | 0.837340 | 0.494665 |
| 5     | 0.092600      | 0.137840        | 0.742001 | 0.840522 | 0.477207 |
| 6     | 0.051200      | 0.146526        | 0.747595 | 0.851005 | 0.483026 |
| 7     | 0.051200      | 0.147835        | 0.756739 | 0.854945 | 0.498545 |
| 8     | 0.027600      | 0.151331        | 0.752964 | 0.855980 | 0.488846 |
| 9     | 0.027600      | 0.152192        | 0.753556 | 0.855015 | 0.490786 |
| 10    | 0.018000      | 0.153424        | 0.757686 | 0.857449 | 0.496605 |
| 11    | 0.018000      | 0.154139        | 0.756436 | 0.857270 | 0.495635 |
| 12    | 0.015300      | 0.154104        | 0.757686 | 0.857449 | 0.498545 |

### Web App

Used `FastAPI` a web app that was designed for more user friendly interactions. After running the app you can input a text and see the results. **Note:** if you are running the app for the first time it will take a while because it needs to download trained models from google drive.

<hr><hr>

## How to install

1. Clone the repo into your local device.
2. Move to clone project directory (you should be in `topic-modeling`)
3. install pipenv
   ```
   pip install pipenv
   ```
4. activate your virtual environment:
   ```
   pipenv shell
   ```
5. Install requirements using command below:
   ```
   pipenv install
   ```
6. Move to topic-modeling\src folder:
   ```
   cd src
   ```
7. Run the following command to start the app:
   ```
   pipenv run uvicorn main:app --reload
   ```
8. After app starts, open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
<hr><hr>

## Challenges And Improvement Ideas:

1. There are other ways of training a multi-label classification nlp model such as using tf-idf and classic ML models to train a classifier.
2. Changing the architecture of the LSTM model could improve it's results. I tried stacking Dense and LSTM layers and adding Dropout layers in between to improve it's results but the accuracy got worse, But there could be a better architecture.
3. The training dataset is imbalanced. We can fix this by oversampling instances of the minority class or undersampling instances of the majority class or use advanced techniques like SMOTE(Synthetic Minority Over-sampling Technique) to help create new synthetic instances from minority class.
