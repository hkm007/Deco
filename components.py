def embed(args):
    if (args.embed.lower() == 'navbar'):
        navbar(args)
    elif(args.embed.lower() == 'footer'):
        footer(args)
    else:
        print("Oops! Component not found")


# Embed Components
def navbar(args):
    print("Embedded Navbar in {}.html".format(args.file))

def footer(args):
    print("Embedded Footer in {}.html".format(args.file))