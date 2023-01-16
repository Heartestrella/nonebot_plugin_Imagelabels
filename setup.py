#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import pathlib
here=pathlib.Path(__file__).parent.resolve()
long_description=(here / 'README.md').read_text(encoding='utf-8')

setup(
    name='nonebot_plugin_Imagelabels',
    version='1.0.0',
    description=(
        '基于yolov5实现的图像标注的Nonebot插件'
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
    python_requires='>=3.8',
    install_requires=[
    "nonebot2>=2.0.0rc1,<3.0.0",
    "nonebot-adapter-onebot",
    'matplotlib>=3.2.2',
    'numpy>=1.18.5',
    'opencv-python>=4.1.2',
    'Pillow>=7.1.2',
    'PyYAML>=5.3.1',
    'requests>=2.23.0',
    'scipy>=1.4.1',
    'torch>=1.7.0',
    'torchvision>=0.8.1',
    'tqdm>=4.41.0',
    'tensorboard>=2.4.1',
    'pandas>=1.1.4',
    'seaborn>=0.11.0',
    'httpx'
]
)
