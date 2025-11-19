
import configparser
import os, sys

import mariadb
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()


class DBConnection:
    
    def connect_to_db(self, debug=False):
        user = os.environ.get("DB_USER")
        password = os.environ.get("DB_PASSWORD")
        host = os.environ.get("DB_HOST")
        database = os.environ.get("DB_DATABASE")
        port = int(os.environ.get("DB_PORT")
                   ) if os.environ.get("DB_PORT") else 0
        
        if(debug):
            print(f"user: {user}")
            print(f"password: {password}")
            print(f"host: {host}")
            print(f"port: {port}")
            print(f"database: {database}")
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        self.cur = self.conn.cursor()

    def create_table(self, table_name):
        
        #+--------------+--------------+------+-----+---------+-------+
        #| Field        | Type         | Null | Key | Default | Extra |
        #+--------------+--------------+------+-----+---------+-------+
        #| id           | int(11)      | NO   | PRI | NULL    |       |
        #| time         | datetime     | YES  |     | NULL    |       |
        #| server       | varchar(255) | YES  |     | NULL    |       |
        #| service_name | varchar(255) | YES  |     | NULL    |       |
        #| status       | int(11)      | YES  |     | NULL    |       |
        #+--------------+--------------+------+-----+---------+-------+
        
        
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT PRIMARY KEY,
            time DATETIME,
            server VARCHAR(255),
            service_name VARCHAR(255),
            status INT
        ) """

        self.cur.execute(query)
        print("Successful table created")

    def close_connection(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        
def read_services(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Retrieve all services under the [services] section
    services = []
    if 'services' in config:
        for key in config['services']:
            services.append(config['services'][key])
    return services


if __name__ == "__main__":
    
    config_path = 'services.conf'  # The path to your config file
    services_list = read_services(config_path)
    print(services_list)
    db = DBConnection()
    for service in services_list:
        service_name = service.split(".")[0]
        service_table_name = service_name + "_service_status"
        print(service_table_name)

        db.connect_to_db()
        db.create_table(service_table_name)
        db.close_connection()