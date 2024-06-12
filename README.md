# physemg
UCLA PHYSICS 4AL Project Analysis repository. The C.U.T. Using B.U.L.K.:
Exploring the Relationship Between Muscle Contraction and Weight Lifted Using an EMG.

## Description
Data is found in `/data`. Figures are found in `/output`. Code is all within
`/preanalysis.ipynb`.

## Setup
For this project, Python 3 version 3.9.18 is used. Other versions may also
work. It is also assumed that LaTeX is setup correctly for pdf generation. This
varies system to system, so instructions are not listed here.

It is recommended to use a virtual environment. For example,
```sh
/usr/bin/env python3 -m venv venv
source venv/bin/activate
```

To check the Python version,
```sh
python3 --version
```
should output some supported Python 3 version.

Requirements are found in `/requirements.txt`. These can be installed as
follows.
```sh
pip install -r requirements.txt
```

## Usage

### Export Notebook
To generate to pdf,
```sh
jupyter nbconvert --execute preanalysis.ipynb --to pdf  
```

Other output formats can be specified similarly e.g. html.
```sh
jupyter nbconvert --execute preanalysis.ipynb --to html  
```

See nbconvert documentation for other output options.

### Figures
The notebook generates the following figures:
- `alldata.png`: Data displayed in 4 x 5 grid.
- `allrangecentral.png`: Data subsetted into ranges with measures of central
  tendencies calculated, then fit with linear fit.
- `allrangedata.png`: Data subsetted into ranges, then fit with linear fit.
- `allrangeloglog.png`: Data subsetted into ranges, then taking log and log-log
  regression.
- `e20data.png`: Example dataset: Ena 20 lbs.
- `e20ranges.png`: Example dataset with ranges: Ena 20 lbs.
- `k17data.png`: Example erroneous dataset: Khanh 17.5 lbs.
