This directory is meant to house and pre-process data. The scripts provided follow the pre-processing method described in the original paper<sup>[1](#fn1)</sup>.

### Requirements
* [Avisynth](https://sourceforge.net/projects/avisynth2/) with [FFMS2](https://github.com/FFMS/ffms2)
* [x264](https://www.videolan.org/developers/x264.html)

## Usage
Place raw input files in the `in` directory, and run `FilterAll.bat`. Note that scripts may fail to process file names that contain certain non-alphanumeric characters.
For subsequent feature extractiom, label your data in the `out` directory after pre-processing by moving files to the `Animation` and `NotAnimation` directories.

<a name="fn1">1</a>: Zumer, R. & Ratté, S. Int J Multimed Info Retr (2018) 7: 187. https://doi.org/10.1007/s13735-018-0146-2
