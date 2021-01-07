import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def run_quickstart():

	import io
	import os
	
	from google.cloud import vision
	from google.cloud.vision import types

	credentials=GoogleCredentials.get_application_default()

	client=vision.ImageAnnotatorClient()
	
	for i in range(2):
		with io.open('/home/pi/New/img%s.jpg' %i,'rb') as image_file:
			content=image_file.read()

		image=types.Image(content=content)
	
		response=client.logo_detection(image=image)
		logos=response.logo_annotations

		print ('logo')

		for logo in logos:
			print(logo.description)
		
	print('\n')

if __name__ == '__main__':
	run_quickstart()