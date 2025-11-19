import subprocess
import time
import configparser


def check_service_status(service_name):
    try:
        # Run systemctl is-active command
        result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the service is active
        if result.stdout.strip() == 'active':
            return 1
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def monitor_service(service_name):
    while True:
        status = check_service_status(service_name)
        if status == 1:
            print(f"{service_name} is running.")
            return 1
        else:
            print(f"{service_name} is not running.")
            return 0
        
        # Wait for 60 seconds before checking again
        time.sleep(60)


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
    
    gesamserver = 1
    for service in services_list:
        status = check_service_status(service)
        if status == 1:
            print(f"{service} is running.")
        else:
            print(f"{service} is not running.")
            gesamserver = 0
            
            
# Webclient Separat
# Alle Services in eine Tabelle
# Gesamt Server Separate

# Alle Services in eine Tabelle -> SystemdStatus
        #+--------------+--------------+------+-----+---------+-------+
        #| Field        | Type         | Null | Key | Default | Extra |
        #+--------------+--------------+------+-----+---------+-------+
        #| id           | int(11)      | NO   | PRI | NULL    |       |
        #| time         | datetime     | NO   |     | NULL    |       |
        #| server       | varchar(255) | NO   |     | NULL    |       |
        #| service_name | varchar(255) | NO   |     | NULL    |       |
        #| status       | int(11)      | NO   |     | NULL    |       |
        #+--------------+--------------+------+-----+---------+-------+
        
# Gesamt Server Separate -> ServerStatus
#+--------------+--------------+------+-----+---------+-------+
        #| Field        | Type         | Null | Key | Default | Extra |
        #+--------------+--------------+------+-----+---------+-------+
        #| id           | int(11)      | NO   | PRI | NULL    |       |
        #| time         | datetime     | NO   |     | NULL    |       |
        #| server       | varchar(255) | NO   |     | NULL    |       |
        #| status       | int(11)      | NO   |     | NULL    |       |
        #+--------------+--------------+------+-----+---------+-------+
        
# Webclient

#        +--------------+--------------+------+-----+---------+-------+
        #| Field        | Type         | Null | Key | Default | Extra |
        #+--------------+--------------+------+-----+---------+-------+
        #| id           | int(11)      | NO   | PRI | NULL    |       |
        #| time         | datetime     | NO   |     | NULL    |       |
        #| server       | varchar(255) | NO   |     | NULL    |       |
        #| systemdStatus| int(11)      | NO   |     | NULL    |       |
        #| ping         | int(11)      | NO   |     | NULL    |       |
        #+--------------+--------------+------+-----+---------+-------+
   