import json, os, boto3
cw = boto3.client("cloudwatch")

def lambda_handler(event, context):
    namespace = event.get("namespace","AWS/EC2")
    metric = event.get("metric","CPUUtilization")
    threshold = float(event.get("threshold", os.environ.get("CPU_THRESHOLD","80")))
    r = cw.get_metric_statistics(Namespace=namespace,MetricName=metric,
        Dimensions=[{"Name":"InstanceId","Value":event["instance_id"]}],
        StartTime=__import__("datetime").datetime.utcnow()-__import__("datetime").timedelta(minutes=10),
        EndTime=__import__("datetime").datetime.utcnow(),Period=300,Statistics=["Average"])
    datapoints=r.get("Datapoints",[])
    avg=max([x["Average"] for x in datapoints], default=0)
    return {"statusCode":200,"body":json.dumps({"average":avg,"threshold":threshold,"high":avg>=threshold})}
