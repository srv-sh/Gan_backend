import boto3
from PIL import Image
from io import BytesIO
from decouple import config
from datetime import datetime as dt


class Fashion_Generator_Handler():    
    def __init__(self):
        self.s3 = boto3.resource(service_name = 's3',
                                region_name = config("AWS_REGION_NAME"),
                                aws_access_key_id = config("AWS_ACCESS_KEY_ID"),
                                aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"))
        self.s3_bucket = self.s3.Bucket(config("BUCKET"))
        self.bucket_url = config("BUCKET_URL")

    def upload_to_s3_bucket(self,bucket, filepath, key:str):
            bucket.upload_fileobj(filepath,key)
            return self.bucket_url+key

    ## FUNCTION TO GENERATE IMAGE
    def generate_img(self,prompt):
        print(prompt)

        ##### call the generating function here

        membuf = BytesIO()
        img = Image.open('face.jpg')
        img.save(membuf, format="png") 
        img = Image.open(membuf)
        key= 'generated-image/'+str(int(dt.now().timestamp()*1000000))+'.png'
        membuf.seek(0)
        url = self.upload_to_s3_bucket(self.s3_bucket, membuf, key)
        return url
