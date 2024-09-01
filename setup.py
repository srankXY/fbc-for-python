from setuptools import setup, find_packages

GFICLEE_VERSION = '1.6'

setup(
    name='FBC',
    version=GFICLEE_VERSION,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
    },
    install_requires=[
        "requests"
    ],
    url='https://github.com/Yxiaoyang/srkSUB',
    license='GNU General Public License v3.0',
    author='srank',
    author_email='625593240@qq.com',
    description='FBC指纹浏览器 RPA SDK for python'
)