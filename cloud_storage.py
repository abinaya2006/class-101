from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)


def main():
    access_token="Q0VB-VfGXgwAAAAAAAAAAaL2U9tn1iUtFzzQQbGjfILT55olkKQD_B32eWeZ_Fmg"
    transferData=TransferData(access_token)

    file_from="E:\python path.txt"
    file_to="/testing/python path.txt"

    transferData.upload_files(file_from,file_to)
    print("The file has been moved.")

main()



