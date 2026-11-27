import json, boto3
ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    sg_id = event.get("security_group_id")
    if not sg_id:
        return {"statusCode":400,"body":json.dumps({"error":"security_group_id is required"})}
    sg = ec2.describe_security_groups(GroupIds=[sg_id])["SecurityGroups"][0]
    findings=[]
    for rule in sg.get("IpPermissions",[]):
        for ip in rule.get("IpRanges",[]):
            if ip.get("CidrIp") == "0.0.0.0/0":
                findings.append({"protocol":rule.get("IpProtocol"),"from":rule.get("FromPort"),"to":rule.get("ToPort")})
    return {"statusCode":200,"body":json.dumps({"security_group":sg_id,"public_rules":findings})}
