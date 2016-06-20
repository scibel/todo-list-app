##Origin Coding Challenge

A simple To Do list implemented in Django and Django Rest Framework.


###Install

1.	Install Docker Engine and Docker Machine using Docker Toolbox installer, follow instructions [here](https://www.docker.com/products/docker-toolbox).

2.	Create a new Docker VM

	```docker-machine create --driver virtualbox todoapp```

3.	Connect your Docker client to the newly created Docker VM

	```eval "$(docker-machine env todoapp)"```

4.	List all Docker VM's and check if your new VM is selected

	```docker-machine ls```

5.	From the root of the project run

	```docker-compose build```
	```docker-compose up```

6.  Run DB migrations

    ```docker-compose run web /usr/local/bin/python manage.py migrate```

7.  Create couple of users

    ```docker-compose run web /usr/local/bin/python manage.py createsuperuser```

8.	Get your Docker VM IP address

	```docker-machine ip todoapp```

9.  Start Docker services

    ```docker-compose up```

10.	You should now be able to use the app here

	  http://{IP-ADDRESS}:8000/
