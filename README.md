# Churn Prediction
![build badge](https://github.com/tomaskender/churn-prediction/actions/workflows/main.yml/badge.svg?event=push)

Predict leaving of customers.

## Inspiration
Soner Yıldırım's article [Churn Prediction with Machine Learning](https://towardsdatascience.com/churn-prediction-with-machine-learning-ca955d52bd8c) on Medium.

## Setup

### Dataset
You can download the dataset from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). If you don't want to register, you can also find it in other [Github repos](https://github.com/treselle-systems/customer_churn_analysis/blob/master/WA_Fn-UseC_-Telco-Customer-Churn.csv).

### Run checks and tests
```
tox
```

### Train & Benchmark
When training in benchmark mode, only 80% of dataset is used for training, while the rest is used to measure accuracy.
```console
python main.py Telco-Customer-Churn.csv --benchmark
```
> **_NOTE:_**  You need to have downloaded the dataset from above first.

### Train & Infere
When training in a non-benchmark mode, all of the data is used to train the best possible model.
```console
python main.py Telco-Customer-Churn.csv
```
> **_NOTE:_**  You need to have downloaded the dataset from above first.
