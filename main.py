import os
import argparse
from pathlib import Path
import webbrowser
import platform

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
	
	<!-- icon -->
	<link rel="icon" href="https://cdnb.artstation.com/p/assets/images/images/005/731/019/original/david-bautista-fire2.gif?1493342838" type="image/gif" sizes="16x16">
	
	<!-- font awesome -->
    	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">
	
	<!-- local css -->
	<link rel="stylesheet" type="text/css" href="css/style.css">
	
	<title>Deco App</title>
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

def start_server(args):
	try:
		new = 2 # open in a new tab, if possible

		# open an HTML file on my own (Windows) computer
		url = "{}/index.html".format(args.app)

		#check OS
		os_platform = platform.system()

		# MacOS
		if(os_platform == 'Darwin'):
			chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

		# Windows
		elif(os_platform == 'Windows'):
			chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

		# Linux
		elif(os_platform == 'Darwin'):
			chrome_path = '/usr/bin/google-chrome %s'

		webbrowser.get(chrome_path).open(url)

	except Exception as e:
		print(e)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(title="commands", dest="command")
	#Start project
	parser_start = subparsers.add_parser('startproject')
	parser_start.add_argument('dir',type=str)
	parser_start.set_defaults(func=startproject)

	#start_server
	parser_server = subparsers.add_parser('startserver')
	parser_server.add_argument('app',type=str)
	parser_server.set_defaults(func = start_server)

	args = parser.parse_args()

	if (args.command == 'startproject'):
		args.func(args)
	elif(args.command == 'startserver'):
		args.func(args)

