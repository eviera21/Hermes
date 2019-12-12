# Hermes
Hermes Programming Language facilitates communication between a local and an external server.

Written by: Nomar Medina and Enrique Viera

The aim of this project is to implement a programming language that can contact different servers at a time to communicate with each of them.
By doing this we can send information in String format to one another. The project is written with Python and various external libraries like:
PLY, socket, threading, requests, etc. 

## Quick Start: The Main Commands
```
start server serv
start server otherserv
start client me
me connect serv
serv connect otherserv
a = "hey"
me post serv a
b = 10
b
c=5.54
c
d=c^2
d
e=b+c-d
e
stop me
stop serv
stop otherserv
```
The above detailed code shows many commands of Hermes. We also included variable management, a calculator and simple String usage.

First let's look at that first line. ```start``` serves as to create a new ```server``` or ```client```, then goes the name of this server. This expression is shown to be:

```start (server or client) (variable_name)```

So after the third line we created two servers and a client. 
Then we connect these two servers.
To do so we use the word ```connect``` between
 the two variable names. We also connect the client to on of the servers.

Then we have some simple variable association using the 
character ```=``` like in Java or Python. 
The next big part is we can send a message from a client 
or a server to another. We use the following order:

```(servername1) post (servername2) (String|Integer|Float|Variable of the previous)```

Now whe've started to communicate between these two 
servers. Next we have some mathematical functions but 
that is very simple and will be detailed later. 

The final part of this quick guide is how to close connections between servers and essentially delete them. In Hermes, we use the ```stop``` command.
Simply put:

```stop (server or client name)```

After this we've succesfully communicated between servers using sockets, and then succesfully closing them. A lot goes behind the scenes like IPs, ports, but essentially with Hermes you do not have to worry about that. 

##Documentation
####Server Functions
```start```:
Start is used to define servers or clients by stating the name of it after ```start server``` or ```start client```.

```stop```:
Stop is used to end the use of a server, essentially closing and deleting them. First we write ```stop server``` or ```stop client``` following the name of this client or server.


```connect```: Connect is used to bind two servers or clients together to send information between them. We simply write ```connect``` between two server or client names.
The program manages port and ip declaration so you don't have to.
    

```post```: Post sends information from a server to another.
 You must follow the next structure:
  ```(servername1) post (servername2) (String|Integer|Float|Variable of the previous)```
  
  Example: ```server1 post server2 5.61```  ```client1 post server1 "I sell chicken."```
  
The message can be one of the following: String, Integer, Float, or a variable of the previous.
  
  
```get```: This function returns multiple information of a certain client or server like the IP Address and the Port used. Simply type the name of the variable after ```get```.


#### Other Functions
```exit```: This function is used to exit the programming language. Similar to Python's ```exit()``` command.

```integer1 + integer2```: perform addition.

```integer1 - float1```: perform subtraction.

```integer1 * integer2```: perform multiplication.

```float1 / float2```: perform division.

```float1 ^ integer1```: perform exponentiation.
```var = "String"```: variable assignment.
