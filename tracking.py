import mlflow

with mlflow.start_run():
    mlflow.log_param("fake1", 2.77)
    mlflow.log_param("fake2", 3.2)

    mlflow.log_metrics({"metric1":0.9855, "metric2":2.31})
    mlflow.log_artifact("./fake_ckpt.txt")