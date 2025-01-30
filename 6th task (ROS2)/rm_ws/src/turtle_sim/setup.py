from setuptools import find_packages, setup

package_name = 'turtle_sim'

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
    maintainer='kamal',
    maintainer_email='kamal@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': ["goal=turtle_sim.goal:main",
                            "controller=turtle_sim.controller:main",
                            "draw_circle=turtle_sim.draw_circle:main",
                            "d=turtle_sim.d_:main",
                            "polygon=turtle_sim.polygon:main"
        ],
    },
)
