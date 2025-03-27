import pymysql
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def mysql_to_excel(host, user, password, database, output_file):
    try:
        # Connect to MySQL database
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        
        # Fetch all table names
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        
        # Create a new Excel workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Database Export"
        
        for table in tables:
            query = f"SELECT * FROM {table}"
            df = pd.read_sql(query, connection)
            
            # Add table name as a header
            ws.append([f"Table: {table}"])
            
            # Write data
            for r in dataframe_to_rows(df, index=False, header=True):
                ws.append(r)
            
            # Add space between tables
            ws.append([])
            ws.append([])
        
        # Save the Excel file
        wb.save(output_file)
        print(f"All tables exported successfully to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        connection.close()

# Usage example
mysql_to_excel(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database',
    output_file='output.xlsx'
)
