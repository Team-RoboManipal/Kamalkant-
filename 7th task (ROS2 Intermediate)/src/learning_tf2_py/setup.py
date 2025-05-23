from setuptools import find_packages, setup
import glob
import os
package_name = 'learning_tf2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*launch.[pxy]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kamal',
    maintainer_email='itzkamalkant@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    entry_points={
        'console_scripts': ['static_turtle_tf2_broadcaster = learning_tf2_py.static_turtle_tf2_broadcaster:main',
                            'turtle_tf2_broadcaster = learning_tf2_py.turtle_tf2_broadcaster:main',
                            'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',
                            'fixed_frame_tf2_broadcaster = learning_tf2_py.fixed_frame_tf2_broadcaster:main',
                            'dynamic_frame_tf2_broadcaster = learning_tf2_py.dynamic_frame_tf2_broadcaster:main',
        ],
    },
)
