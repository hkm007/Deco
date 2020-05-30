import os
import argparse
from pathlib import Path
from funcs import create_html,create_css,create_assets,create_bootstrap_html,create_js

# Default project
def fly(args):
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
		print("Boiler template created for project: {}".format(args.dir))
	except Exception as e:
		print("Project cannot be created.")
		print("A directory with same name already exists!")
		exit()


# Project with Bootstrap
def fly_Bootstrap(args):
	''' this function creates the whole project '''
	# final project path
	target = './'
	path = Path(target, args.dir)
	try:
		os.mkdir(path)
		create_bootstrap_html(path)
		create_css(path)
		create_js(path)
		create_assets(path)
		print("Boiler template with Bootstrap support created for project:  {}".format(args.dir))
	except Exception as e:
		print("Project cannot be created.")
		print("A directory with same name already exists!")
		exit()