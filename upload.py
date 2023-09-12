from azure.storage.blob import BlobServiceClient

storage_account_key = "KMCpaWPAOuFCX8Kwc1syUDZqThT6V55TfykNi0aaESGTotThbbj/cgUh8LLB5rHuOa3zC23YnMPz+AStr7tAeg=="
storage_account_name = "mystorage321d"
connection_string = "DefaultEndpointsProtocol=https;AccountName=mystorage321d;AccountKey=KMCpaWPAOuFCX8Kwc1syUDZqThT6V55TfykNi0aaESGTotThbbj/cgUh8LLB5rHuOa3zC23YnMPz+AStr7tAeg==;EndpointSuffix=core.windows.net"
container_name= "pythoncontainer"


def uploadToBlobStorage(file_path, file_name):
    blob_service_client= BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob= file_name )
    

    with open (file_path, "rb") as data:
        blob_client.upload_blob(data)
        print("uploaded"+file_name+"file")


uploadToBlobStorage('C:\\Users\\Alex\\Desktop\\INFORMATICA 8TH\\CLOUD COMPUTING\\pythonBlolb\\test\index.php', 'index')