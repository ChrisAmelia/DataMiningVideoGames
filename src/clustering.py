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

def clusterData(lst, display_clusters_key = False):
    """Cluster the given list (containing game's description and publishers) and
    returns the vectorizer and the model to train.
    Source: https://stackoverflow.com/questions/27889873/clustering-text-documents-using-scikit-learn-kmeans-in-python

    Args:
        lst (list): game's informations (e.g. ["Best game ever by Valve"]).
        display_clusters_key (boolean): True to print the clusters' details, else false.

    Returns:
        a vectorizer and the model to train
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

    return vectorizer, model

def getCluster(game):
    """Predict in which cluster the given game belongs to and
    returns the cluster index.

    Args:
        game (dict): format must be game['name'] = '...' and game['description'] = ['...',].

    Returns:
        the cluster index.
    """
    name = game['name']
    description = game['description']

    documents = vectorizeData()
    vectorizer, model = clusterData(documents, display_clusters_key = True)
    X_test = vectorizer.transform(description)
    cluster_ind = model.predict(X_test)
    print(name + " belongs to cluster: " + str(cluster_ind))
    return cluster_ind
