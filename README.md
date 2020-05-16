# ScriptCLOCbyReleases
A .py that generates a JSON file containing info about lines of code of your repo by releases.

## Usage

1. Download CLOC

```
apt-get install cloc
```

2. Put your repository link in the repositoryLink variable (line 27)
  ```python
#Download the repository
repositoryLink = "https://github.com/videolan/vlc-android"
```
3. Paste the file script.py to your repository folder.

4. Run script.py
```
python3 script.py
```

5. The result is named data.json and is located in the same folder that you have been pasted the script.py file

## Example of output
  ```json
{
   "Valores": [
      {
         "Registro": [
            {
               "lineas": [
                  {
                     "language": "C/C++ Header",
                     "files": 547,
                     "blank": 16296,
                     "code": 36014
                  },
                  {
                     "language": "Java",
                     "files": 131,
                     "blank": 5373,
                     "code": 10199
                  },
                  {
                     "language": "C",
                     "files": 8,
                     "blank": 311,
                     "code": 364
                  }
               ],
               "commit": "19ffebd3a9dedfc61a4b74fa44273b96decf9e37",
               "tag": "refs/tags/0.0.1"
            }
         ]
      },
      {
         "Registro": [
            {
               "lineas": [
                  {
                     "language": "C/C++ Header",
                     "files": 547,
                     "blank": 16296,
                     "code": 36014
                  },
                  {
                     "language": "Java",
                     "files": 131,
                     "blank": 5373,
                     "code": 10199
                  },
                  {
                     "language": "C",
                     "files": 8,
                     "blank": 311,
                     "code": 364
                  }
               ],
               "commit": "780303847001f0722a786d6a3d99c0e4378a0843",
               "tag": "refs/tags/0.0.1^{}"
            }
         ]
      },
      {
         "Registro": [
            {
               "lineas": [
                  {
                     "language": "C/C++ Header",
                     "files": 547,
                     "blank": 16296,
                     "code": 36014
                  },
                  {
                     "language": "Java",
                     "files": 163,
                     "blank": 6740,
                     "code": 12759
                  },
                  {
                     "language": "C",
                     "files": 39,
                     "blank": 484,
                     "code": 1315
                  }
               ],
               "commit": "e38c5e95119ac007701be1a2e1496a1c5843b080",
               "tag": "refs/tags/0.0.10"
            }
         ]
      }
   ]
}
```
