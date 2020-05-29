import os
import argparse


def create_html():
	filename = 'index.html'
	with open(filename,'w') as f:
		f.write("<h1>Hello world</h1>")

def create_css():
	filename = 'style.css'
	with open(filename,'w') as f:
		f.write("body{ padding:0; margin:0 }")

def create_js():
	filename = 'script.js'
	with open(filename,'w') as f:
		f.write("<h1>Hello world</h1>")

def create_project():
	create_html()
	create_css()
	create_js()
	
if __name__ == '__main__':
	# construct the argument parse and parse the arguments
	parser = argparse.ArgumentParser(description= "Create Boiler plate for HTML,CSS,JS")
	parser.add_argument("boiler_plate",type = str,help="Boiler plate name")
	args = vars(parser.parse_args())
	# display a friendly message to the user
	print("Created boiler plate for {}!!".format(args.boiler_plate))
