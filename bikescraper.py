import requests
import time
import json
import random
import os
import time

feed_endpoint = 'https://layer.bicyclesharing.net/map/v1/nyc/stations'


num_iterations = 1

def run():
	counter = 0
	while True:
		counter += 1
		grab_and_save(counter)
		time.sleep(30)

def create_file_name():
	return time.strftime("%Y-%m-%d-%H-%M-%S")


def grab_and_save(counter):
	response = requests.get(feed_endpoint)
	data = response.json()
	file_name = f'./data/{create_file_name()}.json' 
	print(f"Iteration #{counter}")
	print(f"Status code: {response.status_code}")
	print(f"File name: {file_name}")
	print("===================================")
	with open(file_name, 'w') as f:
		json.dump(data, f)


def main():
    run()

if __name__ == "__main__":
    main()
