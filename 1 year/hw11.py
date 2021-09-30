import requests
import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud

limit = 50
start = 'https://forumspb.com/'

def get_data(start_link):
    connects = []
    domains = set()
    visited = set()
    queue = [start_link]
    while queue and (len(visited) < limit):
        try:
            i = 0
            if queue[0] not in visited:
                page = requests.get(queue[0]).text
                soup = BeautifulSoup(page, 'lxml')
                for a in soup.find_all('a', href=True):
                    if i > 9:
                        break
                    if 'http' in a['href']:
                        connects.append((queue[0].split('?')[0].split('://')[1].split('#')[0],
                                         a['href'].split('?')[0].split('://')[1].split('#')[0]))
                        queue.append(a['href'])
                        domains.add(a['href'].split('?')[0].split('/')[2])
                        i += 1
                domains.add(queue[0].split('?')[0].split('/')[2])
                visited.add(queue[0])
                queue.pop(0)
            else:
                queue.pop(0)
        except:
            queue.pop(0)
    return connects, list(domains)


def domain_cloud(domains):
    """
    Draw the cloud of words
    Args:
        domains (list of str): ['domain1', 'domain2'...]
    """
    word_string = ' '.join(domains)
    params = dict(background_color="white", width=1200, height=1000, max_words=len(set(domains)))
    wordcloud = WordCloud(**params).generate(word_string)
    plt.imshow(wordcloud)
    plt.show()


def graph(connections, with_labels=False):
    """
    Draw the graph based on a connections
    Args:
        connections (list of tuple): [(A, B), (B, C)...] links from A to B, B to C, etc
        with_labels (bool): plot the labels or not
    """
    g = nx.Graph()
    g.add_edges_from(connections)
    nx.draw(g, verticalalignment='bottom', horizontalalignment='center', with_labels=with_labels, node_size=30)
    plt.show()


conn, dom = get_data(start)
graph(conn)
domain_cloud(dom)