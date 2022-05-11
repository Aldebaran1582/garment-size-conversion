# Garment size conversion tool


[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)




### # Methodology: 
### My approach was based on trying to find out the starting locale size index after importing the siszing.csv to retrieve the equivalente target size value.
My approach was based on trying to find out the starting locale index in order to retrieve the equivalente target size


# 1.- Simple command line garment conversion

#### Usage: input the start locale, size and target locale.

```python

 ~/garment-size-conversion/ python3 gst.py 
  Enter your start locale: US
  Enter you cloth size: 18
  Enter your target locale: FR
  Converted size is:  50
  Enter 'quit' to exit or any key to continue:

```
             
# 2.- CSV File conversion.
### Usage:

```python

 ~/garment-size-conversion/ python3 gspy.py -h
 
 usage: test.py [-h] [-f FILE] [-t TARGET]

 Additional commands to process CSV files.

 optional arguments:
 -h, --help            show this help message and exit
 -f FILE, --file FILE  Type the csv file name to convert.
 -t TARGET, --target TARGET Type your target locale.

 
 ~/garment-size-conversion/ python3 test.py -f garments.csv -t ALPHA 
 100%████████████████████████████████████████████████████████| 100000/100000 [00:03<00:00, 32226.15it/s]
 Conversion completed! 
```

## Notes:

 ####  For the file conversion, in case the target size matches the csv file record size, it will show  "SAME SIZE".
 ####  Also, when the target size is ALPHA, those records without equivalent size will show "No equivalent size available".
 #### I assumed the csv source file will be already formatted ( I did't add any additional csv format validation).


