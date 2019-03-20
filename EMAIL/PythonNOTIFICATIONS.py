from pynotify import pynotify as pn

@pn.ExecutionNotifierDecorator('yashmate54@gmail.com', 'abcxyz12', ['2017.yash.mate@ves.ac.in'])
def hello():
	print ("Hello world!")
	
hello()
