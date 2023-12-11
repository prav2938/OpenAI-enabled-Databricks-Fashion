import boto3
from botocore.exceptions import NoCredentialsError
import json

class AWSSecretManager:
    def __init__(self):
        self.client = self._create_secrets_manager_client()
    
    def _create_secrets_manager_client(self):
        try:
            session = boto3.session.Session()
            return session.client(service_name='secretsmanager')
            
        except NoCredentialsError as e:
            print(f"Error: {e}")
            
    def get_secret(self, secret_name):
        try:
            response = self.client.get_secret_value(SecretId=secret_name)
            secret_string = response['SecretString']
            
            if secret_string:
                return json.loads(secret_string)
                
            else:
                return response
            
        except Exception as e:
            print(f"Error: {e}")
            
    @staticmethod        
    def get_host_name():
        aws_secret_manager = AWSSecretManager()
        db_credentials = aws_secret_manager.get_secret("HACKATHON-2023")
        if isinstance(db_credentials, dict):
            hostname = db_credentials.get("DATABRICKS_HOSTNAME")
            return hostname
            
    @staticmethod        
    def get_http_url():        
        aws_secret_manager = AWSSecretManager()
        db_credentials = aws_secret_manager.get_secret("HACKATHON-2023")
        if isinstance(db_credentials, dict):
            http_path = db_credentials.get("DATABRICKS_HTTP_PATH")
            return http_path
            
    @staticmethod        
    def get_token():        
        aws_secret_manager = AWSSecretManager()
        db_credentials = aws_secret_manager.get_secret("HACKATHON-2023")
        if isinstance(db_credentials, dict):
            token = db_credentials.get("DATABRICKS_TOKEN")
            return token        
            

        
        




