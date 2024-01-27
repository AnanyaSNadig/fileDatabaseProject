# File Database Project

This project consists of three Python scripts: apiApp.py, listFiles.py, and filesDB.py. 
The main script, apiApp.py, utilizes the functionalities provided by the listFiles and filesDB libraries.

## Project Structure

- apiApp.py: Main script that uses the functionalities provided by listFiles and filesDB.
- listFiles.py: Library with methods to list files and update files.
- filesDB.py: Library with methods to interact with the database.

## Usage

### To run the python script

To run apiApp.py, run the following command with the required parameters:
```console
python3 apiApp.py --input_path=/path/to/directory --time_frame=time_in_minutes --str_to_find=searchString --str_to_replace=replaceString
```

### API Usage

To use the API provided by apiApp.py, follow these steps:

1. Ensure Flask is installed:

    ```bash
    pip install Flask
    ```

2. Run the Flask API by running the main pyhton script:


3. Access the API using your browser or a tool like curl

   
## Installation

To install the required dependencies, run the following command:

```console
pip install -r requirements.txt
```


## Running on AWS EC2

1. Launch an EC2 instance and connect to it.
   
2. Copy your project files to the EC2 instance using scp command.
   
   ```console
   scp -i your-key.pem your-file.tgz ec2-user@your-ec2-instance-ip:/path/on/ec2
   ```
   
3. Install required packages
   
4. Run the python script


## Setting up the environment variables

### Set the environment variable values using the following command:

```console
export MYSQL_DB="your_database_name"
export MYSQL_HOST="your_host_name"
export MYSQL_USER="your_user_name"
export MYSQL_PASSWORD="your_password"
export MYSQL_PORT="mysql_port_number"
```

### To check the value of an environment variable:

```console
echo $MYSQL_DB
```


## Creating Database using Docker

1. Install docker on the EC2 instance.

2. Pull the MySQL Docker image and start the container:

3. Access the MYSQL container.

  ```console
   docker exec -it container_name mysql -u user_name -p your_password
```

4. Create a database.

5. Create a table with following columns:
   
  ```sql
    CREATE TABLE files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filePath VARCHAR(255),
    searchString VARCHAR(255),
    replaceString VARCHAR(255),
    replacedTime DATETIME
    );
```

5. View the table to check the output:

   ```sql
   USE fileDatabase;
   SELECT * FROM files;
   ```

6. Exit the container
  ```console
  exit
  ```
