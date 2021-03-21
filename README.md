# PickleServer
A package that offers Client-Server operations for Pickling any python data

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Pickle Server is a open source, pure python package that offers client-server operatiosn for pickling python data.

- Uses Flask for running server, Pickle for pickling data
- 100 % Python
- Super Reliable

## Features

- class "PickleServer" for running pickle server
- class "PickleClient" for connecting to the pickle server, loading and dumping data
- error handling & preventing data loss when failed to dump a pickle object

## Example usages

Importing the Module:

```py
from pickleserver import PickleServer, PickleClient
```

Running the Pickle Server:

```py
p_server = PickleServer(SECRET_KEY="blahblahblah", debug=False, port=12138, host="127.0.0.1")
# There are other optional kwargs, of course. Feel free to play around with them!
p.run()
```


Creating the Pickle Client:

```py
p_client = PickleClient("http://127.0.0.1:12138", SECRET_KEY="blahblahblah")
# The first and only argument is the server url (full url), whereas the SECRET_KEY must match the secret key of the PickleServer you are trying to connect
```

Dumping and Loading some Data:
```
data = p_client.load('test.db')
print("here is the loaded data:")
print(data)
data2 = {'test2': 'hello there'}
response = p_client.dump(data2, 'test2.db')
print("here is the message after you have dumped an object:")
print(response)

# This what the result of the above code looks like, if you have the pickle server running and client connected properly:
here is the loaded data:
{'test': 'hi'}
here is the message after you have dumped an object:
{'note': 'Dump operation successful', 'status': True}
```

#### Conclusion
That's it! That's what PickleServer can do for you! It's extremely simple to use, yet powerful!
Have fun and hope this helps!

@ PickleServer 2021, MIT Licensed
