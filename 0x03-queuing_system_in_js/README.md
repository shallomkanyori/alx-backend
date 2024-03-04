# Queing System in JS

## Tasks

### Task 0
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/download/):
```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

- Start Redis in the background with `src/redis-server`
```
$ src/redis-server &
```

- Make sure that the server is working with a ping `src/redis-cli ping`
```
PONG
```

- Using the Redis client again, set the value `School` for the key `Holberton`
```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

- Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)
```
$ kill [PID_OF_Redis_Server]
```

Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

Requirements:
- Running `get Holberton` in the client, should return `School`

### Task 1
Install `node_redis` using `npm`

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:
- It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly
- It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work

Requirements:
- To import the library, you need to use the keyword `import`

### Task 2
In a file `1-redis_op.js`, copy the code you previously wrote (`0-redis_client.js`).

Add two functions:
- `setNewSchool`:
	- It accepts two arguments `schoolName`, and `value`.
	- It should set in Redis the value for the key `schoolName`
	- It should display a confirmation message using `redis.print`
- `displaySchoolValue`:
	- It accepts one argument `schoolName`.
	- It should log to the console the value for the key passed as argument

At the end of the file, call:
- `displaySchoolValue('Holberton');`
- `setNewSchool('HolbertonSanFrancisco', '100');`
- `displaySchoolValue('HolbertonSanFrancisco');`

Requirements:
- Use callbacks for any of the operation, we will look at async operations later

### Task 3
In a file `2-redis_op_async.js`, let’s copy the code from the previous exercise (`1-redis_op.js`)

Using `promisify`, modify the function `displaySchoolValue` to use ES6 `async / await`

Same result as `1-redis_op.js`

### Task 4
In a file named `4-redis_advanced_op.js`, let’s use the client to store a hash value

Create Hash:
Using `hset`, let’s store the following:
- The key of the hash should be `HolbertonSchools`
- It should have a value for:
	- `Portland=50`
	- `Seattle=80`
	- `New York=20`
	- `Bogota=20`
	- `Cali=40`
	- `Paris=2`
- Make sure you use `redis.print` for each `hset`

Display Hash:
Using `hgetall`, display the object stored in Redis.

Requirements:
- Use callbacks for any of the operation, we will look at async operations later

### Task 5
In a file named `5-subscriber.js`, create a redis client:
- On connect, it should log the message `Redis client connected to the server`
- On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
- It should subscribe to the channel `holberton school channel`
- When it receives message on the channel `holberton school channel`, it should log the message to the console
- When the message is `KILL_SERVER`, it should unsubscribe and quit

In a file named `5-publisher.js`, create a redis client:
- On connect, it should log the message `Redis client connected to the server`
- On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`
- Write a function named `publishMessage`:
	- It will take two arguments: `message` (string), and `time` (integer - in ms)
	- After `time` millisecond:
		- The function should log to the console `About to send MESSAGE`
		- The function should publish to the channel `holberton school channel`, the message passed in argument after the time passed in arguments
- At the end of the file, call:
```
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
```

Requirements:
- You only need one Redis server to execute the program
- You will need to have two node processes to run each script at the same time
