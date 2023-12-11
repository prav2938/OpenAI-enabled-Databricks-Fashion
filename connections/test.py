from databricks_connection import DatabricksConnection

class Test(DatabricksConnection):
    
    def execute_query(self):
        cursor = self.make_connect().cursor()
        cursor.execute("select * from hackathon2023.default.customer limit 5 ")
        result = cursor.fetchall()
        for row in result:
            print(row)
            
            
testing = Test()
testing.execute_query()