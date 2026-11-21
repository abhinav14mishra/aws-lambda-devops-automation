import os, json, boto3
ce = boto3.client("ce")

def lambda_handler(event, context):
    days = int(event.get("days", os.environ.get("DAYS","1")))
    end = __import__("datetime").date.today()
    start = end - __import__("datetime").timedelta(days=days)
    r = ce.get_cost_and_usage(TimePeriod={"Start":str(start),"End":str(end)},
        Granularity="DAILY", Metrics=["UnblendedCost"], GroupBy=[{"Type":"DIMENSION","Key":"SERVICE"}])
    return {"statusCode":200,"body":json.dumps(r,default=str)}
