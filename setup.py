from setuptools import setup, find_packages


def readme():
    with open('README.en.md', encoding='utf-8') as f:
        content = f.read()
    return content

# install_requires里面是干什么的#
install_requires = [
]

setup(name="erpipc",
      version="0.1.0",
      author='Ding Yuqing',
      author_email='1024670883@qq.com',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://gitee.com/shuhebing/erpipc',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      python_requires='>=3.7,<3.10',
      entry_points={
          'console_scripts': [
          ],
      })
