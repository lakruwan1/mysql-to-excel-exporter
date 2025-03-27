# MySQL to Excel Export Tool

## Overview
This Python script allows you to export all tables from a MySQL database to a single Excel file. It uses `pymysql` for database connection, `pandas` for data manipulation, and `openpyxl` for Excel file creation.

## Prerequisites

### Python Libraries
Ensure you have the following Python libraries installed:
- pymysql
- pandas
- openpyxl

You can install these libraries using pip:
```bash
pip install pymysql pandas openpyxl
```

### MySQL Database Access
- You'll need access credentials for the MySQL database
- Ensure you have read permissions for the database tables

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mysql-to-excel-export.git
cd mysql-to-excel-export
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Database Connection Parameters
Edit the script and replace the following placeholders with your actual database credentials:
- `your_host`: MySQL server hostname or IP address
- `your_username`: MySQL username
- `your_password`: MySQL user password
- `your_database`: Name of the database to export
- `output_file`: Desired name for the output Excel file (e.g., 'output.xlsx')

## Usage

### Run the Script
```bash
python mysql_to_excel.py
```

### Example
```python
mysql_to_excel(
    host='localhost',
    user='myuser',
    password='mypassword',
    database='mydatabase',
    output_file='database_export.xlsx'
)
```

## Features
- Exports all tables from a MySQL database
- Creates a single Excel file
- Includes table names as headers
- Adds spacing between table exports for readability

## Error Handling
- The script includes basic error handling
- Prints error messages if connection or export fails
- Ensures database connection is closed after export

## Troubleshooting
- Verify database credentials
- Check network connectivity
- Ensure sufficient permissions
- Confirm required libraries are installed

## Security Recommendations
- Do not hardcode database credentials in the script
- Use environment variables or secure credential management
- Limit database user permissions to read-only access

## Contributing
Contributions are welcome! Please submit pull requests or open issues on the repository.

## Author
Lakruwan Kasun
