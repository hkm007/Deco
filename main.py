import os
from pathlib import Path

def make_project(target, directory):
	''' this function creates the whole project '''
	# final project path
	# path = os.path.join(target, directory)
	path = Path(target, directory)

	try:
		os.mkdir(path)
	except Exception as e:
		print(e)

	# creates index.html
	index = path / "index.html"

	f = open(index, "w")
	f.write("Welcome to Deno")
	f.close()


	# creates a folder css and make file style.css in it
	css_path = path / "css"
	try:
		os.mkdir(css_path)
	except Exception as e:
		print(e)

	style = css_path / "style.css"

	f = open(style, "w")
	f.close()

	# creates a folder js and make file main.js in it
	js_path = path / "js"
	try:
		os.mkdir(js_path)
	except Exception as e:
		print(e)

	javascript = js_path / " main.js"

	f = open(javascript, "w")
	f.write("console.log('working!')")
	f.close()

	# creates assets folder for images etc
	assets_path = path / "assets"
	try:
		os.mkdir(assets_path)
	except Exception as e:
		print(e)

if __name__ == '__main__':
	deco_dir = __file__
	target = deco_dir[0 : len(deco_dir)-12]
	directory = input('Enter project name: ')

	make_project(target, directory)

	print("Project successfully created!")