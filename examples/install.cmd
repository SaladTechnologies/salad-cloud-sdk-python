python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\salad_cloud_sdk-0.9.0-alpha.5-py3-none-any.whl --force-reinstall
