from aws_embedded_metrics import metric_scope

@metric_scope
def lambda_handler(event, context, metrics):
    metrics.set_namespace("PingStatus")
    metrics.put_metric("Ping", 1, "Count")
    print("Writing metric as EMF")


    


