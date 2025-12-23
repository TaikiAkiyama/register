from setuptools import find_packages, setup

package_name = 'register'

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
    maintainer='Taiki Akiyama',
    maintainer_email='s24c1005hq@s.chibakoudai.jp',
    description='数字を入力すると商品名が出てきます',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'scanner = register.scanner:main',
            'display = register.display:main',
        ],
    },
)
