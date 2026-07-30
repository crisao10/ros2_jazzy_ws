from setuptools import find_packages, setup

package_name = 'inspeccion_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cris',
    maintainer_email='cris@todo.todo',
    description='Nodo de inspeccion visual de calidad',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'inspeccion = inspeccion_pkg.nodo_inspeccion:main',
        ],
    },
)