import argparse
from commands import fly,fly_Bootstrap

version = '1.0.0'

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title="commands", dest="command")

#Start project
parser_start = subparsers.add_parser('fly',help = "Start deco project")
parser_start.add_argument('dir',type=str)
parser_start.set_defaults(func=fly)

#Add 
parser_add = parser_start.add_argument('--add',type = str,help = "Add external components")

if __name__ == '__main__':
	try:
		args = parser.parse_args()

		if (args.command == 'fly' and args.add == None):
			args.func(args)

		elif(args.command == 'fly' and args.add.lower() == 'bootstrap'):
			fly_Bootstrap(args)

	except Exception as e:
		print("Deco command not found")
