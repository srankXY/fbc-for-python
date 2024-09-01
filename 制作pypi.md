

## 步骤

- 复制setup.py

- 修改setup.py

- 安装

  > #安装或更新setuotools和wheel
  > pip install  --upgrade setuptools wheel

- 打包

  > python3 setup.py sdist bdist_wheel

- 上传pypi

  > pip install --user --upgrade twine
  >
  > twine upload dist/*
  >
  > 注意：其中username输入`__token__`，password输入token值

- 安装

  > pip install xxxx