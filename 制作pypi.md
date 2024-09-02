

## 步骤

> 注意新建目录，代码放到该目录下，并创建`__init__.py`

- 复制setup.py

- 修改setup.py

- 安装

  > #安装或更新setuotools和wheel
  >
  > pip install  --upgrade setuptools wheel

- 打包

  > python setup.py sdist

- 上传pypi

  > pip install --upgrade twine
  >
  > python -m twine upload dist/*

- 安装

  > pip install xxxx