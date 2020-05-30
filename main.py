import os
import argparse
from pathlib import Path

def startproject(args):
	''' this function creates the whole project '''
	# final project path
	target = './'
	path = Path(target, args.dir)
	try:
		os.mkdir(path)
		create_html(path)
		create_css(path)
		create_js(path)
		create_assets(path)
		print("Boiler template created for {}".format(args.dir))
	except Exception as e:
		print("Project cannot be created.")
		print("A directory with same name already exists!")
		exit()


def create_html(path):
	# creates index.html
	index_path = path / "index.html"
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
	<h1 class="glow">Welcome to Deco</h1>
	<div id = "logo">
		<img src="https://cdnb.artstation.com/p/assets/images/images/005/731/019/original/david-bautista-fire2.gif?1493342838" alt="landing_img">
	</div>	
	<!-- local javascript -->
	<script src="js/main.js"></script>
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
	f.write("""/* write your css here */
body {
	background-color: #000000;
}

img {
	height: 300px;
	width: 300px;
}

#logo{
	text-align: center;
}


.glow {
	font-size: 80px;
	text-align: center;
	font-family: cursive;
	padding-top: 40px;
	color: #fff;
	text-align: center;
	-webkit-animation: glow 1s ease-in-out infinite alternate;
	-moz-animation: glow 1s ease-in-out infinite alternate;
	animation: glow 1s ease-in-out infinite alternate;
  }
  
@-webkit-keyframes glow {
	from {
	  text-shadow: 0 0 10px rgb(253, 236, 3), 0 0 20px rgb(247, 203, 5), 0 0 30px #f8b705, 0 0 40px #ffae00, 0 0 50px #fd7e06, 0 0 60px #ff6905, 0 0 70px #e63600;
	}
	
	to {
	  text-shadow: 0 0 20px #03e9f4, 0 0 30px #03e9f4, 0 0 40px #03e9f4, 0 0 50px #03e9f4, 0 0 60px #03e9f4, 0 0 70px #03e9f4, 0 0 80px #03e9f4;
	}
}""")
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
	f.write("console.log('Deco ran successfully')")
	f.close()

def create_assets(path):
	# creates assets folder for images etc
	assets_path = path / "assets"
	try:
		os.mkdir(assets_path)
	except Exception as e:
		print(e)
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers()
	parser_bar = subparsers.add_parser('startproject')
	parser_bar.add_argument('dir',type=str)
	parser_bar.set_defaults(func=startproject)
	args = parser.parse_args()
	args.func(args)

