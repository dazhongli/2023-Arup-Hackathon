# Design Report

How do do we generate calculation report using Arup's digital infrastructure? 

## Attempt - ArupCompute driven by python

[python module](https://designcheck.arup.com/docs/dc2fpy/)

1. Create an python environment 

``` shell
conda create -n dcpy python=3.9
conda activate dcpy
```
2. Install required package

``` shell
conda install jupyter 
pip install ipykernel
pip install https://packages.arup.com/dc2frameworkpy.tar
python -m ipykernel install --name dcpy
```

## Errors and solution

I ran into this error `Assembly not subscrible`, the solution to this is to install the loader

``` shell
pip install clr-loader==0.1.7
```