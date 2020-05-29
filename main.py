import os
import argparse

def make_project(target,directory):
	''' this function creates the whole project '''
	# final project path
	path = os.path.join(target, directory)
	try:
		os.mkdir(path)
	except Exception as e:
		print(e)

	# creates index.html
	index = path+"/index.html"

	f = open(index, "w")
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

	# creates a folder css and make file style.css in it
	css_path = path+"/css"
	try:
		os.mkdir(css_path)
	except Exception as e:
		print(e)

	style = css_path+"/style.css"

	f = open(style, "w")
	f.close()

	# creates a folder js and make file main.js in it
	js_path = path+"/js"
	try:
		os.mkdir(js_path)
	except Exception as e:
		print(e)

	javascript = js_path+"/main.js"

	f = open(javascript, "w")
	f.close()

	# creates assets folder for images etc
	assets_path = path+"/assets"
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

