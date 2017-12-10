import json, os

from pprint import pprint
from utilities import cleanHTML

# Clustering features
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

def vectorizeData():
    """Returns a list containing the description of each game present in 'filtered_data.json'.
    Returns:
        a list; description + publishers
    """
    lst = []
    curdir = os.curdir
    try:
        new_path = curdir + "/../res/"
        os.chdir(new_path)
        filename = 'filtered_data.json'
        data = json.load(open(filename))
        for key in data:
            description = data[key]['detailed_description']
            publishers = ''.join(data[key]['publishers'])
            # Remove HTML tags, tabs, newlines
            description = cleanHTML(description)
            description = description.replace("\t", "")
            description = description.replace("\n", "")
            description = description.replace("\r", "")
            # 'Publishers' is believed to be an important key, this is why it's added twice
            result = description + " " + publishers + " " + publishers
            lst.append(result)
    except Exception as e:
        raise e
    finally:
        os.chdir(curdir)
    return lst

def cluster_data(lst, display_clusters_key = False):
    """TODO: Docstring for cluster_data.

    Source: https://stackoverflow.com/questions/27889873/clustering-text-documents-using-scikit-learn-kmeans-in-python
    :lst: TODO
    :returns: TODO

    """
    documents = lst
    vectorizer = TfidfVectorizer(stop_words = 'english')
    X = vectorizer.fit_transform(documents)

    # Cluster documents
    true_k = 10
    model = KMeans(n_clusters = true_k, init = 'k-means++', max_iter = 100, n_init = 1)
    model.fit(X)

    if display_clusters_key:
        # Print top terms per cluster clusters
        print("Top terms per cluster:")
        order_centrois = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        for i in range(true_k):
            print("Cluster {:d}".format(i))
            for ind in order_centrois[i, :10]:
                print(" {:s}".format(terms[ind]))
            print()

cluster_data(vectorizeData(), display_clusters_key = True)
