import boto3
from PIL import Image
from io import BytesIO
from decouple import config
from datetime import datetime as dt


class Fashion_Generator_Handler():    
    def __init__(self):
        self.s3 = boto3.resource(service_name = 's3',
                                region_name = 'ap-south-1',
                                aws_access_key_id = 'AKIAV3NQCJC5BYKAI4X7',
                                aws_secret_access_key='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')
        self.s3_bucket = self.s3.Bucket(config("BUCKET"))

    def upload_to_s3_bucket(self,bucket, filepath, key:str):
            bucket.upload_fileobj(filepath,key)
            return 'https://shelly-ml-data-bucket.s3.ap-south-1.amazonaws.com/'+key

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
