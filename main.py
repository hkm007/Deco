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
	except:
		print("Project cannot be created.")
		print("A directory with same name already exists!")
		exit()



def create_html(path):
	# creates index.html
	index_path = path / "index.html"
	try:
		# os.mkdir(index_path)
		f = open(index_path, "w")
		f.write("""<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">

		<!-- local css -->
		<link rel="stylesheet" type="text/css" href="css/style.css">

		<title>Deco</title>
	</head>
	<body>
		<center><p><b>Welcome to Deco</b></p></center><br><br>

		<center>
			<img src="https://cdnb.artstation.com/p/assets/images/images/005/731/019/original/david-bautista-fire2.gif?1493342838" alt="landing_img">
		</center>	

		<!-- local javascript -->
		<script src="js/main.js"></script>
	</body>
	</html>""")
		f.close()

	except Exception as e:
		print(e)


def create_css(path):
	# creates a folder css and make file style.css in it
	css_path = path / "css"
	try:
		os.mkdir(css_path)
		style = css_path / "style.css"

		f = open(style, "w")
		f.write("""/* write your css here */
	body {
		background-color: #000000;
	}

	p {
		color: white;
		font-size: 50px;
	}

	img {
		height: 300px;
		width: 300px;
	}""")
		f.close()
	except Exception as e:
		print(e)


def create_js(path):
	# creates a folder js and make file main.js in it
	js_path = path / "js"
	try:
		os.mkdir(js_path)
		javascript = js_path / "main.js"
		f = open(javascript, "w")
		f.write("console.log('working!')")
		f.close()
	except Exception as e:
		print(e)

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
	parser.add_argument("--startproject" ,type = str,help="Boiler plate project name")
	args = vars(parser.parse_args())
	dir_name = args['startproject']
	target = './'
	make_project(target,dir_name)
	print("Project successfully created as '{}'!".format(dir_name))
