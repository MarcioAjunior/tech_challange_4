from prometheus_client import Histogram

# Histogram to monitor inference time
REQUEST_TIME = Histogram("model_inference_time_seconds", "Time spent in inference")
