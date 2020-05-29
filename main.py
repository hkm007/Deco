import os

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
	target = './'
	directory = input('Enter project name: ')
	make_project(target,directory)
	print("Boiler Plate Created successfully at {}".format(directory))

