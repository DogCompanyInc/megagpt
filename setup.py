from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='megagpt',
  version='1.0.0',
  author='dogie',
  author_email='pavelt1234567890@gmail.com',
  description='Unofficial blackbox api library for python',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/DogCompanyInc/megagpt',
  packages=find_packages(),
  install_requires=['requests>=2.25.1', 'json5', 'logging'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='megagpt mega api chatGPT GPT dogie',
  project_urls={
    'GitHub': 'https://github.com/DogCompanyInc'
  },
  python_requires='>=3.6'
)
