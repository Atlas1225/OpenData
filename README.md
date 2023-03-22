[![DOI](https://zenodo.org/badge/599152914.svg)](https://zenodo.org/badge/latestdoi/599152914)
# OpenData

## Description

The script is automatizated, so you only need to generate the main and the header xml file of your article and put it in `outputs` and `outputs/header` folder to let the script do its job.

## Requirements

Gradle >= 7.0.0

maven >=3.6.0

java 11.x

python 3.8.x

## Documentation

Command for running the sript is 
```
python3 script.py
```

If you want to try this script, it is necessary to generate a grobid xml main and header file and put it in the corresponding folder. (It will be mentioned during `Grobid generation` section).

## Installation & execution instructions

### Grobid generation

The way I generated the grobid xml files is using [grobid_client](https://github.com/kermitt2/grobid_client_python) repository and[grobid server](https://github.com/kermitt2/grobid).

<span style="color:green">Command for running grobid server is: 
</span>
```
foo@bar:~$ ./gradlew clean install 
```

and then:

```
foo@bar:~$ ./gradlew run   
```

<span style="color:green">Command for generating header file with grobid client is: 
</span>
```
foo@bar:~$ grobid_client --input ~/Documents/OpenData/inputs --output ~/Documents/OpenData/outputs/header --n 20 processHeaderDocument  
```
<span style="color:green">Command for generating main file with grobid client is: 
</span>
```
foo@bar:~$ grobid_client --input ~/Documents/OpenData/inputs --output ~/tmp/out processFulltextDocument 
```

### Anaconda enviroment

Firstly you must install [Anaconda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) and then use these commands:

```
foo@bar:~$ conda config --add channels conda-forge    
```

```
foo@bar:~$ conda create -n opendata python=3.8 nltk wordcloud matplotlib lxml pytest
```

```
foo@bar:~$ conda activate opendata
```

## Running Examples

Running examples are in the project already. 

`inputs` folder contains all articles used for the example, and `outputs` folder contains xml files generated with Grobid.
`figuresperArticle`, `listOfLinks` and `wordClouds` folders contains the outcome of the project.

## Preferred citation 
If you use our code or results in your research, please cite our paper:

```bib
@article{Opendata,
  title   = {{Opendata}},
  author  = {SHENGXING LU},
  year    = {2022},
  doi     = {https://zenodo.org/badge/latestdoi/599152914}
}