from helper import *


class PickleServer():
    def __init__(self,
                 SECRET_KEY=SECRET_KEY, debug=DEBUG, port=PORT, host=HOST, STORAGE_DIRECTORY=STORAGE_DIRECTORY,
                 isThreaded=isThreaded):
        # the second part of all kwargs refer to the default values set in helper.py
        self.host_server = Flask(__name__)
        self.host_server.secret_key = SECRET_KEY
        self.debug = debug
        self.port = port
        self.host = host
        self.STORAGE_DIRECTORY = STORAGE_DIRECTORY
        self.isThreaded = isThreaded

        @self.host_server.route('/')
        def index():
            if request.args.get('key', '') != self.host_server.secret_key:
                return jsonify(INVALID_DEV_KEY)
            return jsonify(WELCOME_MESSAGE)

        @self.host_server.route('/load/<filename>')
        def load(filename):
            if request.args.get('key', '') != self.host_server.secret_key:
                return jsonify(INVALID_DEV_KEY)
            if not os.path.exists(self.STORAGE_DIRECTORY + '/' + filename):
                msg = NONEXISTING_FILE
                msg[
                    'note'] = f"File {filename} does not exist. Please try another filename that might contain the pickle data you are looking for"
                return jsonify(msg)
            return pickle.dumps(pickle.load(open(self.STORAGE_DIRECTORY + '/' + filename, 'rb')))

        @self.host_server.route('/dump/<filename>', methods=['GET', 'POST'])
        def dump(filename):
            if request.args.get('key', '') != self.host_server.secret_key:
                return jsonify(INVALID_DEV_KEY)
            dump_data = request.data
            pickle.dump(pickle.loads(dump_data), open(self.STORAGE_DIRECTORY + '/' + filename, 'wb'))
            return jsonify(DUMP_SUCCESS)

    def run(self):
        self.host_server.run(debug=self.debug, host=self.host, port=self.port, threaded=self.isThreaded)


if __name__ == '__main__':
    server = PickleServer()
    server.run()
