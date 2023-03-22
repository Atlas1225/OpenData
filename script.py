import xml.etree.ElementTree as ET
import nltk as nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from lxml import etree


def action(folderPath, folderComplPath, wcf, lolf, fpaf):
        
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        if not os.path.exists(folderComplPath):
            os.makedirs(folderComplPath)
        if not os.path.exists(wcf):
            os.makedirs(wcf)
        if not os.path.exists(lolf):
            os.makedirs(lolf)
        if not os.path.exists(fpaf):
            os.makedirs(fpaf)

        num_figures = []
        global stop_words
        stop_words = set(stopwords.words('english'))
        for filename in os.listdir(folderPath):
            if os.path.isfile(os.path.join(folderPath, filename)):

                #Creating keywordCloud
                print(folderPath+filename)
                # load xml file
                tree = ET.parse(folderPath+filename)
                root = tree.getroot()

                # namespace prefix
                xmlns = root.tag[root.tag.find('{')+1 : root.tag.find('}')]
                ns = {'tei': xmlns}

                # extract abstract label
                abTag = root.find('.//tei:abstract/tei:p', ns)
                if abTag is None:
                    continue
                abstract = abTag.text

                # tokenize critical words
                tokens = word_tokenize(abstract.lower())
                tokens = [token for token in tokens if not token in stop_words]

                # frequency distribution
                freq_dist = nltk.FreqDist(tokens)

                # word cloud from the frequency distribution
                wordcloud = WordCloud().generate_from_frequencies(freq_dist)

                # save as PNG
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis("off")
                plt.savefig(wcf+'/'+ filename[0:filename.find('.')] +'.png')

                #Number of figures per article
                print(folderComplPath, filename)
                # parse the XML file using lxml
                tree = etree.parse(os.path.join(folderComplPath, filename))
                # find the number of figure elements in the file
                num_figures_in_file = len(tree.xpath("//tei:figure", namespaces=ns))
                print(num_figures_in_file)
                # append the number of figures to the list
                for i in range(num_figures_in_file):
                    num_figures.append(filename)
                #create list of links
                
                f = open(lolf+"/"+  filename[0:filename.find('.')] +'.txt', "w")
                # find all the biblStruct elements
                biblstructs = tree.xpath("//tei:biblStruct", namespaces=ns)

                # print the contents of each biblStruct element
                for biblstruct in biblstructs:
                    f.write(etree.tostring(biblstruct, pretty_print=True, encoding='unicode') + '\n')
                f.close()
        # create a histogram of the number of figures per article
        plt.clf()
        plt.hist(list(el[0: el.find('.')] for el in num_figures), bins=range(len(num_figures)), width= 0.8)

        plt.xlabel("Name of Articles", fontsize=12)
        plt.xticks(rotation=25, ha='right', fontsize=8)
        plt.subplots_adjust(bottom=0.4, left=0.3)
        plt.ylabel("Number of Figures")
        plt.savefig(fpaf +'/figure.png')


action('outputs/header/', 'outputs/', 'wordClouds', 'listOfLinks', 'figuresperArticle')       
        







 


