import os
import random
from datetime import datetime
from dotenv import load_dotenv
from boto3 import client, resource

load_dotenv()

class S3FileManagement:
    def __init__(self):
        self.S3_BUCKET = os.getenv("S3_BUCKET")
        self.client = client("s3")
        self.s3 = resource('s3')

    def createDirectory(self, path):
        path_arr = path.rstrip("/").split("/")
        if len(path_arr) == 1:
            return self.client.create_bucket(Bucket=path_arr[0])

        bucket = self.s3.Bucket(self.S3_BUCKET)
        status = bucket.put_object(Key="/".join(path_arr[1:]) + "/")
        return status

    def sendFile(self, file, directory=None):
        if directory is None:
            directory = os.path.basename(file)

        try:
            dt = datetime.now()
            ts = datetime.timestamp(dt)
            tmp_filename = str(int(ts)) + str(int(random.randint(0, 1000))) + "." + file.filename

            self.client.upload_fileobj(
                file,
                self.S3_BUCKET,
                directory + tmp_filename,
                ExtraArgs={
                    "ContentType": file.content_type  # Set appropriate content type as per the file
                }
            )

            return directory + tmp_filename
        except Exception as e:
            print(e)
            return False

    def deleteFile(self, path):
        key = path

        s3_resource = self.s3
        my_bucket = s3_resource.Bucket(self.S3_BUCKET)
        my_bucket.Object(key).delete()

        return True

    def recoverFile(self, path):
        my_bucket = self.s3.Bucket(self.S3_BUCKET)

        file_obj = my_bucket.Object(path).get()
        print(file_obj)
        return file_obj
