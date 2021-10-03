import dropbox
import os
import shutil
from dropbox.files import WriteMode

class TransferData(object):
    
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode("overwrite"))

def main():
    access_token = ''
    transferData = TransferData(access_token)
    file_from = input("Enter your file path here: -")
    file_to = input("Enter the full patht to upload it to Dropbox: -")

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

main()
