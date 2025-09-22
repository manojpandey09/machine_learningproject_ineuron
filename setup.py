from setuptools import setup, find_packages



def get_requirements() -> list[str]:

	requirments_list = list[str]()	
	return requirments_list



setup(
	name='sensor',
	version='0.1.0',
	author='manoj',
	author_email='pandeymannu54@gmail.com',
	packages=find_packages(),
    install_requires=['pymongo==4.2.0']
)