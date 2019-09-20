import boto3
import os
 
def upload_files(path):
    session = boto3.Session(
        aws_access_key_id='AKIAIMETMMXKSQMDHGIQ',
        aws_secret_access_key='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'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('argo-mta')
   
 
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                print(full_path)
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
 
if __name__ == "__main__":
    upload_files('/Users/amber/Documents/MTA_ARGO')