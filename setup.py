from setuptools import setup

OPTIONS={
    "py2app": {
        "resources": ["web"]
    }
}

setup(
    name='pyqtlet2',
#    app=["playground.py"],
    version='0.4.3',
    description='Bringing leaflet maps to PyQt',
    author='Leon Friedmann',
    author_email='leon.friedmann@tum.de',
    options=OPTIONS,
    package_dir={"": "pyqtlet2"},
    url='https://github.com/JaWeilBaum/pyqtlet2',
    keywords=['leaflet', 'pyqt', 'maps', 'python', 'python3'],
    classifiers=[],
    include_package_data=True,
)
