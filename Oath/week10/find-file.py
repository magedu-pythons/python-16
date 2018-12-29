#21、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）
import os
from pathlib import Path
import logging
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

class FindFile:
	def __init__(self, src:str, follow_symlinks=True):
		if not follow_symlinks and os.path.islink(src):
			self.path = Path(os.readlink(src))
		else:
			self.path = Path(src)

	def handle(self, path):
		try:
			for p in path.iterdir():
				if p.is_dir():
					yield from self.handle(p)
				elif p.is_file():
					yield p
		except Exception as e:
			logging.info(f'{self.path} is not exist')

	def file_endwith(self, src:str):
		for f_src in self.handle(self.path):
			if f_src.suffix == src:
				yield f_src

f = FindFile('.')

for i in f.file_endwith('.py'):
	print(i)