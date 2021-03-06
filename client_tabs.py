from json import dumps
import json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
from sys import argv, exit

def main(argv):

    if len(argv) != 2:
        print(f'Usage: {argv[0]} <Song Name>')
        exit(1)

    song_name = argv[1]
    tabs(song_name)


def tabs(song_name):
    nameStr = str(song_name)
    if nameStr.isdigit():
        print("\nname must be string")
        exit(1)
    response = requests.get("http://localhost:3001/song_name?name="+ nameStr)
    tabs = response.json()
    print(f"Tabs of {nameStr} \n {tabs}" )    
    return tabs

if __name__ == '__main__':
    main(argv)