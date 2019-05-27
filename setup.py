import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='down',
    version='1.0',
    author='Siddharth Dushantha',
    author_email='siddharth.dushantha@gmail.com',
    description='A CLI tool to check if a site or a list of sites are down or up',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sdushantha/down',
    packages=setuptools.find_packages(),
    scripts=['down/down'],
    install_requires=['requests']
)
