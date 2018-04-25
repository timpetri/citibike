import requests
import time
import json
import random
import os

feed_endpoint = 'https://layer.bicyclesharing.net/map/v1/nyc/stations'


num_iterations = 1

def run():
	grab_and_save()


def create_file_name():
	return time.strftime("%Y%m%d-%H%M%S")


def grab_and_save():
	reponse = requests.get(feed_endpoint)
	data = r.json()
	file_name = f'./data/{create_file_name()}-citidata.json' 
	with open(file_name, 'w') as f:
		json.dump(data, f)


def main():
    run()

if __name__ == "__main__":
    main()
