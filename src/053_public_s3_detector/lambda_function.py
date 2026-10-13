import json, boto3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    buckets = s3.list_buckets()["Buckets"]
    findings = []
    for b in buckets:
        name = b["Name"]
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            public = any(g.get("Grantee",{}).get("URI","").endswith("/AllUsers") for g in acl.get("Grants",[]))
            if public:
                findings.append(name)
        except Exception:
            pass
    return {"statusCode":200,"body":json.dumps({"public_acl_buckets":findings})}
