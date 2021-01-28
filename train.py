import mlflow
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", help="fake hyperparameter")
parser.add_argument("datafile", help="fake hyperparameter 2")
args = parser.parse_args()

with mlflow.start_run():
    mlflow.log_param('regularization', args.r)
    mlflow.log_artifact(args.datafile)