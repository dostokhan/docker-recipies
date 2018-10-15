#!/usr/bin/env python


with open('.env', 'w+') as f:
    print('Creating .env')
    f.write(f"MYSQL_DATABASE=appdb\n"\
            "MYSQL_USER=dbUser\n"\
            "MYSQL_PASSWORD=dbPass\n"\
            "MYSQL_ROOT_PASSWORD=r00t1sg0d\n"
            "PMA_HOST=mariadb\n"

            "CONTAINER_MARIADB=mariadb\n"
            "CONTAINER_PHPMYADMIN=phpmyadmin\n"
            )

