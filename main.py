import os
import argparse
from pathlib import Path

def make_project(target,directory):
	''' this function creates the whole project '''
	# final project path
	path = Path(target, directory)
	try:
		os.mkdir(path)
		create_html(path)
		create_css(path)
		create_js(path)
		create_assets(path)
	except Exception as e:
		print(e)


def create_html(path):
	# creates index.html
	index_path = path / "index.html"
	f = open(index_path, "w")
	f.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body>
	<h2>Hello World </h2>
</body>
</html>""")
	f.close()

def create_css(path):
	# creates a folder css and make file style.css in it
	css_path = path / "css"
	try:
		os.mkdir(css_path)
	except Exception as e:
		print(e)

	style = css_path / "style.css"

	f = open(style, "w")
	f.close()

def create_js(path):
	# creates a folder js and make file main.js in it
	js_path = path / "js"
	try:
		os.mkdir(js_path)
	except Exception as e:
		print(e)

	javascript = js_path / "main.js"

	f = open(javascript, "w")
	f.close()

def create_assets(path):
	# creates assets folder for images etc
	assets_path = path / "assets"
	try:
		os.mkdir(assets_path)
	except Exception as e:
		print(e)
	
if __name__ == '__main__':
	# construct the argument parse and parse the arguments
	parser = argparse.ArgumentParser(description= "Create Boiler plate for HTML,CSS,JS")
	parser.add_argument("--startproject" ,type = str,help="Boiler plate name")
	args = vars(parser.parse_args())
	dir_name = args['startproject']
	target = './'
	make_project(target,dir_name)
	print("Created boiler plate at {}!!".format(args['startproject']))

