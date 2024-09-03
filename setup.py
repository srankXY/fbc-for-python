from setuptools import setup, find_packages

GFICLEE_VERSION = '2.0'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='fbc_for_python',
    version=GFICLEE_VERSION,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
    },
    install_requires=[
        "requests"
    ],
    url='https://github.com/srankXY/fbc-for-python',
    license='GNU General Public License v3.0',
    author='srank',
    author_email='625593240@qq.com',
    description='FBC指纹浏览器 RPA SDK for python',
    long_description=long_description,    # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown"
)