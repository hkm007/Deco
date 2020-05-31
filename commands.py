import os
import argparse
from pathlib import Path
from funcs import create_html,create_css,create_assets,create_bootstrap_html,create_js,create_license,version

# Default project
def fly(args):
	''' this function creates the whole project '''
	# final project path
	target = './'
	path = Path(target, args.dir)
	try:
		os.mkdir(path)
		create_html(path)
		create_license(path)
		create_css(path)
		create_js(path)
		create_assets(path)
		print("Deco successfully created project : {}.".format(args.dir))
		print("You are using Deco version {}".format(version))
		print("Happy Coding!")
	except Exception as e:
		print("Project cannot be created.")
		print("A directory with same name already exists!")
		exit()


# Project with Bootstrap
def fly_Bootstrap(args):
	''' this function creates the whole project with Bootstrap '''
	# final project path
	target = './'
	path = Path(target, args.dir)
	try:
		os.mkdir(path)
		create_bootstrap_html(path)
		create_license(path)
		create_css(path)
		create_js(path)
		create_assets(path)
		print("Deco successfully created project : {} with bootstrap 4".format(args.dir))
		print("You are using Deco version {}".format(version))
		print("Happy Coding!")
	except Exception as e:
		print("Deco project cannot be created.")
		print("A directory with the same name already exists!")
		exit()