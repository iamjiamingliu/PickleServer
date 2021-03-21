from flask import Flask, request, jsonify, send_from_directory
from requests import get, post
import pickle, os

# used for class PickleServer __init__
SECRET_KEY = ''
INVALID_DEV_KEY = {"status": False,
                   "note": "Invalid secret key. The secret key you provided does not match the secret key of the PickleServer"}
WELCOME_MESSAGE = {"status": True, "note": "Welcome to PickleServer"}
DUMP_SUCCESS = {"status": True, "note": "Dump operation successful"}
NONEXISTING_FILE = {"status": False,
                    "note": "File does not exist. Please try another filename that might contain the pickle data you are looking for"}

DEBUG = False
PORT = 2100
HOST = '127.0.0.1'
STORAGE_DIRECTORY = 'data'
isThreaded = True
