from setuptools import setup, find_packages

setup(
    name='strictaccess',
    version='0.1.2',
    description='Enforces strict access control for Python classes, with strict mode and access decorators.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jhoel Peralta',
    author_email='jhoelperaltap@gmail.com',
    url='https://github.com/jhoelperaltap/strictaccess',
    packages=find_packages(),
    python_requires='>=3.7',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
