from abc import ABC, abstractmethod 
from databricks import sql
import boto3
from botocore.exceptions import ClientError
from secretManager import AWSSecretManager

class DatabricksConnection(ABC):
    
    def __init__(self):
            self.server_hostname = AWSSecretManager.get_host_name()
            self.http_path = AWSSecretManager.get_http_url()
            self.token = AWSSecretManager.get_token()
        
        
       
    def make_connect(self):
        connection = sql.connect(server_hostname = self.server_hostname,
                                 http_path       = self.http_path,
                                 access_token    = self.token)
        return connection                         
                                 
    @abstractmethod
    def execute_query(self, query):
        pass
    
    