# SlopeFields
A slope field generator and grapher written in Python

![figure_5](https://cloud.githubusercontent.com/assets/5304541/12706974/7736c270-c85b-11e5-830b-7acaf35b4331.png)

# Usage

``` bash
python slopeFields2.py "(3*x^2+1)/(2*y)"
```

```
usage: slopeFields.py [-h] [--xMin XMIN] [--xMax XMAX] [--yMin YMIN]
                      [--yMax YMAX] [--initX INITX] [--initY INITY] [--dX DX]
                      [--line] [--approximate APPROXIMATE]
                      equation

Generate a slope field for a given function.

positional arguments:
  equation              The equation

optional arguments:
  -h, --help            show this help message and exit
  --xMin XMIN           Minimum x value.
  --xMax XMAX           Maximum x value.
  --yMin YMIN           Minimum y value.
  --yMax YMAX           Maximum y value.
  --initX INITX         The initial x value.
  --initY INITY         The initial y value.
  --dX DX               The dX value used in euler's method.
  --line                If you want to draw a line connecting the dots. Note
                        this may cause problems on functions with asymptotes.
  --approximate APPROXIMATE
                        If you want to approximate f(a).
```

# Dependencies 

``` bash
pip install matplotlib numpy
```
