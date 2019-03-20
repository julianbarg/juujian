import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(name='juujian',
                 version='0.0.1',
                 description='Various web scraping and data science related tools. ',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 author='Julian Barg',
                 author_email='barg.julian@gmail.com',
                 packages=[],
                 install_requires=[]
                 )