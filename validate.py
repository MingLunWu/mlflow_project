import mlflow
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("regularization", help="fake hyperparameter 2")
args = parser.parse_args()

with mlflow.start_run():
    mlflow.log_param("regularization", args.regularization)