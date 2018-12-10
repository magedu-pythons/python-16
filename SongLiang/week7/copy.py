from pathlib import Path
import shutil

def copy_file(srcfile,dstfile,srcpath='.',dstpath='.'):
	fsrc = str(Path(srcpath) / srcfile)
	fdst = str(Path(dstpath) / dstfile)
	with open(fsrc) as f1:
		with open(fdst, 'w+') as f2:
			shutil.copyfileobj(f1,f2)

copy_file('test.txt','test7',srcpath='E:')