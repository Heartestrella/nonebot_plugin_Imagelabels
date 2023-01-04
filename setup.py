#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import pathlib
here=pathlib.Path(__file__).parent.resolve()
long_description=(here / 'README.md').read_text(encoding='utf-8')

setup(
    name='nonebot_plugin_Imagelabels',
    version='0.1',
    description=(
        '基于yolov5实现的图像标注'
    ),
    author='Shen_heart',
    author_email='692644718@qq.com',
    maintainer='Heart',
    maintainer_email='qsu666947@163.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/istrashguy/nonebot_plugin_Imagelabels',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',        
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.8'
)
