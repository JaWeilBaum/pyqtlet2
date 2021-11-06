from distutils.core import setup

setup(
    name='pyqtlet2',
    packages=[
        'pyqtlet2',
        'pyqtlet2.web',
        'pyqtlet2.web.modules.leaflet_171',
        'pyqtlet2.web.modules.leaflet_171.images',
        'pyqtlet2.web.modules.leaflet_draw_414',
        'pyqtlet2.web.modules.leaflet_draw_414.dist',
        'pyqtlet2.web.modules.leaflet_draw_414.dist.images',
        'pyqtlet2.leaflet',
        'pyqtlet2.leaflet.control',
        'pyqtlet2.leaflet.core',
        'pyqtlet2.leaflet.layer',
        'pyqtlet2.leaflet.layer.marker',
        'pyqtlet2.leaflet.layer.tile',
        'pyqtlet2.leaflet.layer.vector',
        'pyqtlet2.leaflet.layer.icon',
        'pyqtlet2.leaflet.map',
    ],
    package_data={
        'pyqtlet2.web': ['*'],
        'pyqtlet2.web.modules': ['*'],
        'pyqtlet2.web.modules.leaflet_171': ['*'],
        'pyqtlet2.web.modules.leaflet_171.images': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.src': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.src.edit': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.src.edit.handler': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.src.draw.handler': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.src.ext': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.src.images': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.dist': ['*'],
        'pyqtlet2.web.modules.leaflet_draw_414.dist.images': ['*'],
    },
    version='0.4.9',
    description='Bringing leaflet maps to PyQt',
    author='Leon Friedmann',
    author_email='leon.friedmann@tum.de',
    url='https://github.com/JaWeilBaum/pyqtlet2',
    keywords=['leaflet', 'pyqt', 'maps', 'python', 'python3'],
    classifiers=[],
)


