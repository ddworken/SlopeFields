# SlopeFields
A slope field generator and grapher written in Python

![figure_1](https://cloud.githubusercontent.com/assets/5304541/12697204/5f73cdd8-c74b-11e5-9cff-0c7e8f0818c0.png)
![figure_2](https://cloud.githubusercontent.com/assets/5304541/12697203/5f633db0-c74b-11e5-95fd-1a486c8d801a.png)
![figure_3](https://cloud.githubusercontent.com/assets/5304541/12697274/672e5154-c74d-11e5-98da-6cfe54eabce3.png)


# Usage

``` bash
python slopeFields2.py "(3*x^2+1)/(2*y)"
```

```
usage: slopeFields.py [-h] [--xMin XMIN] [--xMax XMAX] [--yMin YMIN]
                      [--yMax YMAX] [--initX INITX] [--initY INITY] [--dX DX]
                      equation

Generate a slope field for a given function.

positional arguments:
  equation       The equation

optional arguments:
  -h, --help     show this help message and exit
  --xMin XMIN    Minimum x value.
  --xMax XMAX    Maximum x value.
  --yMin YMIN    Minimum y value.
  --yMax YMAX    Maximum y value.
  --initX INITX  The initial x value.
  --initY INITY  The initial y value.
  --dX DX        The dX value used in euler's method.
```

# Dependencies 

``` bash
pip install matplotlib numpy
```
