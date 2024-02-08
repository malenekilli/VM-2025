# Installation guide for the GIB2 code skeleton

**this installation guide is written for Linux, but should be similar for macOS (using brew instead of apt). Windows users has to search for installers because their terminal is not as helpful.**

## Installing the project and dependencies
The first thing to do is to download the project and unzip it where you want it. By using the terminal, navigate into the project. 
```bash
# ~/
$ cd Documents/GIB2
```

If not already installed, you need to acquire python 3, this is the programming language that will handle most of our application logic. Do the following command:

```bash
# ~/Documents/GIB2
$ sudo apt install python3
```

If installed correctly, writing either `python` or `python3` in the terminal window, should produce something like this:

```bash
# ~/Documents/GIB2
$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

if the version displayed is `Python 3.something.something`, you should be good. Exit the interactive python mode by typing `exit()`:

 ```bash
# ~/Documents/GIB2
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
$
 ```

Next we need to create a virtual environment, this is where all the different packages used in the project will exist in. There are a lot of dependencies, by adding the packages in a virtual environment specific for the project, you circumvent future problems, if for example you need a newer version of a framework for another project.

Python 3 has the functionality to create a virtual environment, but on some systems you have to manually install it. You do that by using the following command.

```bash
# ~/Documents/GIB2
$ sudo apt-get install python3-venv
```

  The general command is structured like this: `python3 -m venv/path/to/new/virtual/environment`
Since we already are in the location where we want our virtual environment, we type the following command to create an environment for our project with the name venv (this could be anything):

```bash
# ~/Documents/GIB2
$ python3 -m venv venv
```

This will create a folder in the project that contains all the necessary dependencies for the project. We have to activate the environment in order to install and use the dependencies already installed. After activating, this will be indicated by the `(venv)` prefix to the terminal line. This is done by using the following command, this has to be done every time you run the project. 

```bash
# ~/Documents/GIB2
$ source venv/bin/activate
(venv) $
```

Now, with the virtual environment (venv) activated, we can install the dependencies for the project. python 3 should come with something called `pip3` , that's python's own package manager. All we need is to make sure it's up-to-date, and supply it with our list of dependencies. Those are written down in  our `requirements.txt` file in the project. All of this is done using the following commands. **warning: the installation can take some time** 

```bash 
# ~/Documents/GIB2
(venv) $ pip3 install --upgrade pip
(venv) $ pip3 install -r requirements.txt
```

## Installing the postgreSQL-server

Next, we have to set up a local instance of the database, this will serve our application with storage of the room- and booking-data. This project uses postgreSQL, a free and open-source relational database management system (RDBMS). This is installed using the following command.

```bash
# Anywhere
$ sudo apt update
$ sudo apt install postgresql postgresql-contrib
```

With postgreSQL installed (and running, but that happens automatically), we need to configure both the default user and our database, in order for our application to connect to the database. Below are the given parameters we will configure.

``` bash
user = postgres # already provided, its the default user
password = password # this one we have to set
databasename = postgres # this one we have to set
port = 5432 # already provided, its the default port
host = localhost # already provided, its the default host
```

First, set the password for our postgres-user, this done by first accessing the Postgres prompt.

```bash
# Anywhere
$ sudo -u postgres psql
```

Entering this command will present us with the following prompt.

```bash
psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
Type "help" for help.

postgres=# 
```

In this prompt, we will write a command in Postgres-syntax, this will change (or set) the password of the `postgres` - user to `password` If successful, you will be greeted by the message `ALTER ROLE`

```
psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
Type "help" for help.

postgres=# ALTER USER postgres WITH PASSWORD 'password';
ALTER ROLE
```

Next, while still in the postgres-prompt, we can quickly create our database with name `postgres`by typing the following command

```
psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
Type "help" for help.

postgres=# createdb postgres
```

After that, all the configuration needed in this prompt is finished, you exit the Postgres-prompt by typing the following.

```bash
psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
Type "help" for help.

postgres=# \q
# And we back in the good old familiar terminal
$ 
```

Next up on the chopping block is the extension for postgreSQL called **postgis**. This package will allow us to store spatially referenced data structures in our database. It can easily be installed using the command line. 

 ```
# Anywhere
$ sudo apt install postgis
 ```

With the extension installed, we have to enable it in postgreSQL, this can be achieved by entering the psql-command line once again! 

```bash
# Anywhere
$ sudo -u postgres psql
```

By default, we are in the `postgres`-database, logged in as user `postgres`. All we have to do to add the extension is to type the following command. 

```bash
psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
Type "help" for help.

postgres=# CREATE EXTENSION postgis;
```

You will be greeted by  `CREATE EXTENSION` if successful. 

## Initialize the database

Alright, we have configured the project enough at this point that we are able to add the tables to our database. That is done by running the following, the `init` command will create a migrations folder if not already created. 

```
# ~/Documents/GIB2
$ python3 manage.py db init
```

After that, we have to make the migrations for the classes defined in `/GIB2/app/models.py`.

```bash
# ~/Documents/GIB2
$ python3 manage.py db migrate
```

```bash
# ~/Documents/GIB2
$ python3 manage.py db upgrade
```

**You are good to go!**

Run the flask application using the following command, and check to see if you can see "hello world" printed when you visit the web-address that appears in the prompt.  
```bash
# ~/Documents/GIB2
$ flask run
```

I would strongly reccomend to use git for version controlling the application. In a multideveloper environment, it will serve both as a backup for when you make mistakes, but also as a tool for people to work on different aspects of the application at the same time. 
























