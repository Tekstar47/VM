import nltk
from nltk import FreqDist

nltk.download('gutenberg')
from nltk.corpus import gutenberg

from flask import Flask
app = Flask(__name__)

nltk.download('stopwords')
from nltk.corpus import stopwords


@app.route("/")
def cout_words():
    # Define the stopword set
    stopWords = set(stopwords.words('english'))
    
    # Grab Sense and Sensibilty; tokenize; filter stop words;
    # get frequency distribution
    tokens = gutenberg.words('austen-sense.txt')
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stopWords]
    fdist = FreqDist(tokens)
    common = fdist.most_common(500)

    words = []
    for word, frequency in common:
        words.append(word)
    words.sort()

    highCount = common[0][1]
    
    html = '''
    <html>
    <head>
        <title>Frequency Distribution</title>
    </head>
    <body>
        <h1>List of words from Austen Sense by their frequency distribution</h1>
    '''
    
    for word in words:
        size = str(int(15 + fdist[word] / float(highCount) * 150))
        colour = str(hex(int(0.8 * fdist[word] / \
            float(highCount) * 256**3)))
        colour = colour[-(len(colour) - 2):]
        while len(colour) < 6:
            colour = "0" + colour

        html = html + '<span style="font-size: ' + size + \
                'px; color: #' + colour + \
                '">' +  word + '</span> '

    html_end = '''
    </body>
    </html>
    '''
    html = html + html_end

    return html

if __name__ == "__main__":
    app.run()

