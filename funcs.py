import os
import argparse
from pathlib import Path

#Default fly ----------------------------------------------------------------------------------

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
	<div id = "head">
		<h1 class="glow">Welcome to Deco</h1>
	</div>
	
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


#head{
	margin-top: 30px;
}

img {
	height: 300px;
	width: 300px;
}

#logo{
	text-align: center;
	margin-top: 40px;
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


# Bootstrap ----------------------------------------------------------------------------------------

def create_bootstrap_html(path):
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
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	<!-- font awesome -->
    	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">
	
	<!-- local css -->
	<link rel="stylesheet" type="text/css" href="css/style.css">
	
	<title>Deco App</title>
</head>
<body>
	<div id = "head">
		<h1 class="glow">Welcome to Deco</h1>
	</div>
	
	<div id = "logo">
		<img src="https://cdnb.artstation.com/p/assets/images/images/005/731/019/original/david-bautista-fire2.gif?1493342838" alt="landing_img">
	</div>	


	<!-- local javascript -->
	<script src="js/main.js"></script>
	<!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>""")

	f.close()


