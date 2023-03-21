# Rationale

The purpose of this document is to explain some asummptions I take it during the development of this project and how I found the solution for that problem.


## Draw a keyword cloud based on the abstract information
For the keyword cloud, I have tokenized every non-stop word of the abstract section in the header xml file of each document and then used for the word cloud figure. Since there are not too much specifications in the task description I only count text from abstract section for the word cloud. Figures are in folder `wordClouds`.  

The way I validated this answer is counting in the text those keywords and see if it is the same.

## Create a visualization showing the number of figures per articles

For this task, I created a histogram and saved as a figure in folder `figuresperArticle`.

For the validation in this task I just counted the number of figures in the document since there are not too many.

## Create a list of the links found in each paper

Since there are not links in documents I have chosen apart from grobid links (https://github.com/kermitt2/grobid), I decided to list the references in the bibliography.

The manner I validated this is just checking that the reference section is the same as the list.