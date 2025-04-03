from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='azure-iot-hub-api',
    version='0.2.1',
    description='Azure iot hub api with azure cli backend',
    long_description_content_type="text/markdown",
    long_description=README,
    license='GNU',
    packages=find_packages(),
    author='M.Shaeri',
    
    keywords=['Azure', 'IoT', 'Azure IoT hub', 'azure cli'],
    url='https://github.com/birddevelper/azure-iot-hub-api',
    download_url='https://github.com/birddevelper/azure-iot-hub-api'
)

install_requires = [
    'azure-cli==2.71.0',
    'python-dateutil~=2.9'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
