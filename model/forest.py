import joblib
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tempfile

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


def preprocess(dataset_path):
    LOGGER.info(f"Loading dataset from file {dataset_path}")
    df = pd.read_csv(dataset_path)

    LOGGER.info("Preprocessing in progress..")

    df.drop(
        ["customerID", "gender", "PhoneService", "Contract", "TotalCharges"],
        axis=1,
        inplace=True,
    )

    cat_features = [
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "PaperlessBilling",
        "PaymentMethod",
    ]
    X = pd.get_dummies(df, columns=cat_features, drop_first=True)

    sc = MinMaxScaler()
    a = sc.fit_transform(df[["tenure"]])
    b = sc.fit_transform(df[["MonthlyCharges"]])
    X["tenure"] = a
    X["MonthlyCharges"] = b
    X.Churn = X.Churn.astype(str).map(dict(Yes=1, No=0))

    X_no = X[X.Churn == 0]
    X_yes = X[X.Churn == 1]

    X_yes_upsampled = X_yes.sample(n=len(X_no), replace=True, random_state=42)
    X_upsampled = pd.concat([X_no, X_yes_upsampled], ignore_index=True)

    X = X_upsampled.drop(["Churn"], axis=1)  # features (independent variables)
    y = X_upsampled["Churn"]  # target (dependent variable)

    return X, y


def split_data(X, y):
    LOGGER.info("Splitting dataset into training and testing subset")
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train):
    # Train
    LOGGER.info("Training in progress..")
    clf_forest = RandomForestClassifier(n_estimators=150, max_depth=20)
    clf_forest.fit(X_train, y_train)

    # Save to temporary file
    model_file = tempfile.NamedTemporaryFile(delete=False)
    joblib.dump(clf_forest, model_file, compress=3)
    LOGGER.info(f"Saving new model to {model_file.name}")

    # Test
    test_model(model_file.name, X_train, y_train)

    return model_file.name


def test_model(model_path, X_test, y_test):
    LOGGER.info(f"Loading model from {model_path}")
    model = joblib.load(model_path)
    LOGGER.info("Testing model in progress..")
    pred = model.predict(X_test)
    LOGGER.info(f"Model accuracy is {accuracy_score(y_test, pred)}")
