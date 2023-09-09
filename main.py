import argparse
import logging
from model import preprocess, split_data, train_model, test_model

LOGGER = logging.getLogger()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", help="path to source dataset csv")
    parser.add_argument(
        "--benchmark",
        help="train and benchmark using independent data",
        action="store_true",
    )
    args = parser.parse_args()

    X_train, y_train = preprocess(args.dataset)
    if args.benchmark:
        X_train, X_test, y_train, y_test = split_data(X_train, y_train)

    LOGGER.info("Training a new model")
    path = train_model(X_train, y_train)

    if args.benchmark:
        LOGGER.info("Starting benchmark on never seen data")
        test_model(path, X_test, y_test)
