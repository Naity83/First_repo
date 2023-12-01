from setuptools import setup, find_namespace_packages

setup(
    name='sorted_pack_hw7_1122',
    version='0.0.1',
    description='Sorted code',
    url='https://github.com/Naity83/First_repo',
    author='Nataliya Khomenko',
    author_email='NataliHomenko83@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:clean']}
)