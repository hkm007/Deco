import argparse
from funcs import version
from commands import fly,fly_Bootstrap
from components import embed

def main():
	parser = argparse.ArgumentParser(description='Welcome to Deco :) . Build quicktime boiler plates for websites with some of these useful commands.',epilog='Enjoy using Deco! :)\n')

	subparsers = parser.add_subparsers(title="commands", dest="command")


	#Start project (fly)
	parser_start = subparsers.add_parser('fly',help = "Start deco project")
	parser_start.add_argument('dir',type=str)
	parser_start.set_defaults(func=fly)

	#Add optional for fly
	parser_add = parser_start.add_argument('--add',type = str,help = "Add external frameworks (such as bootstrap)")

	#Version
	parser.add_argument('--version', action='version', version=version)

	#Embed Components
	parse_file = subparsers.add_parser('./',help = "Add the file name")
	parse_file.add_argument('file',type=str,help = "Html filename")
	parse_file.add_argument('--embed',type = str,help = "embed external components in the html")

	try:
		args = parser.parse_args()

		if (args.command == 'fly' and args.add == None):
			args.func(args)

		elif(args.command == 'fly' and args.add.lower() == 'bootstrap'):
			fly_Bootstrap(args)
		
		elif(args.command == './' and args.embed != None):
			embed(args)

	except Exception as e:
		print("Deco command not found")

if __name__ == '__main__':
	main()
