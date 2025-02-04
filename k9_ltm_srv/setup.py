from setuptools import find_packages, setup

package_name = 'k9_ltm_srv'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hopkira',
    maintainer_email='hopkira@googlemail.com',
    description='Long term memory service for K9 robot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'service = k9_ltm_srv.service_long_term_memory:main',
        ],
    },
)
