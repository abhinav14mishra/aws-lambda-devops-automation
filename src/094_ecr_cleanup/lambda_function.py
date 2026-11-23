import os, json, boto3
ecr = boto3.client("ecr")

def lambda_handler(event, context):
    repo = event.get("repository") or os.environ["REPOSITORY"]
    keep = int(event.get("keep", os.environ.get("KEEP","10")))
    images = ecr.describe_images(repositoryName=repo, filter={"tagStatus":"UNTAGGED"}).get("imageDetails",[])
    images.sort(key=lambda x:x.get("imagePushedAt",0), reverse=True)
    delete=[{"imageDigest":x["imageDigest"]} for x in images[keep:]]
    if delete:
        ecr.batch_delete_image(repositoryName=repo,imageIds=delete)
    return {"statusCode":200,"body":json.dumps({"repository":repo,"deleted":len(delete)})}
