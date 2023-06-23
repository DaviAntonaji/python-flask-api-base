from boto3 import client, resource
import random
from datetime import datetime
import os
from dotenv                                                 import load_dotenv
load_dotenv()
import json

class S3FileManagement:

    def __init__(self):
        
        self.S3_BUCKET = os.getenv("S3_BUCKET")
        self.client = client("s3")
        self.s3 = resource('s3')

    def CreateDirectory(self, path):
        path_arr = path.rstrip("/").split("/")
        if len(path_arr) == 1:
            return self.client.create_bucket(Bucket=path_arr[0])
        
        bucket = self.s3.Bucket(self.S3_BUCKET)
        status = bucket.put_object(Key="/".join(path_arr[1:]) + "/")
        return status
    
    
 

    def SendFile(self, File, Directory=None):

        if Directory is None:
            Directory = os.path.basename(File)

        try:
          
            dt = datetime.now()
            ts = datetime.timestamp(dt)
            tmp_filename = str(int(ts)) + str(int(random.randint(0,1000))) + "." + File.filename
            
           
            self.client.upload_fileobj(
            File,
            self.S3_BUCKET,
            Directory + tmp_filename,
            ExtraArgs={
                "ContentType": File.content_type    #Set appropriate content type as per the file
            }
        )
           
           

            return Directory + tmp_filename
            
            
        except Exception as e:
            print(e)
            return False

    def DeleteFile(self, Path):
        key = Path

        s3_resource = self.s3
        my_bucket = s3_resource.Bucket(self.S3_BUCKET)
        my_bucket.Object(key).delete()

        return True


    def RecoverFile(self, Path):
       
        my_bucket = self.s3.Bucket(self.S3_BUCKET)
        
        file_obj = my_bucket.Object(Path).get()
        print(file_obj)
        return file_obj
