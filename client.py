from helper import *


class PickleClient():
    def __init__(self, server_url, SECRET_KEY=SECRET_KEY):
        # doesn't matter if server_url contains an '/' at the end
        self.server_url = server_url
        self.SECRET_KEY = SECRET_KEY

    def load(self, filename):
        data = get(
            (self.server_url + '/load/' + filename + '?key=' + self.SECRET_KEY).replace('//load', 'load'))
        if 'status' in str(data.content) and 'false' in str(data.content):
            raise AttributeError(data.json()['note'])
        data = data.content
        return pickle.loads(data)

    def dump(self, obj, filename):
        serialized_obj = pickle.dumps(obj)
        return post((self.server_url + '/dump/' + filename + '?key=' + self.SECRET_KEY).replace('//dump', 'dump'),
                    data=serialized_obj).json()


if __name__ == '__main__':
    client = PickleClient('http://127.0.0.1:2100', '')
    data = client.load('test.db')
    print("here is the loaded data:")
    print(data)
    data2 = {'test2': 'hello there'}
    response = client.dump(data2, 'test2.db')
    print("here is the message after you have dumped an object:")
    print(response)
