##Simple To Do App

A simple To Do list implemented in Django and Django Rest Framework.


###Summary

This To-do app is build using Django and DRF. Firstly, you need to 
create a Django User to start creating your To-do list. Follow the
instructions to create a User.

You can then login and start adding To-do items. You can prioritise
your items by clicking `edit` and setting the priority. The list will
sort out accordingly, putting the top priority items first.

You can check the items to mark them as done. There is additional
`hide completed` filter to remove the done items from the list. 
You can see all items by clicking the `show all` link.

Finally, install the app by following these simple instructions, enjoy!


###Install

1.	Install Docker Engine and Docker Machine using Docker Toolbox 
    installer, follow instructions [here](https://www.docker.com/products/docker-toolbox).

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
