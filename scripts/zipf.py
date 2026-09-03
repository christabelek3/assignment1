import argparse
from collections import Counter
from math import log
from matplotlib import pyplot as plt


def get_ranks_and_frequencies(infile):
    """Produces a list of rank, frequency pairs for each word in a text file
    :param infile: a text file
    :return: a list containing rank, frequency pairs for each word
    """
    with open(infile) as f:
        contents = f.read()
    c = Counter(contents.split())
    # TODO: create a list called ranks_and_frequencies that stores (rank,
    # frequency) pairs for each word in the file

    # Sort the dictionary by value (ascending)
    sorted_c = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))

    rank=1
    ranks_and_frequencies = []

    for key in sorted_c:
        frequency = sorted_c[key]
        ranks_and_frequencies.append((rank, frequency))
        rank += 1

    return ranks_and_frequencies


def plot(infile):
    """
    Plots rank and frequency pairs to demonstrate Zipf's Law
    :param infile: a text file
    :return: None, produces a matplotlib plot
    """
    ranks_and_frequencies = get_ranks_and_frequencies(infile)

    # TODO: use the (rank, frequency) pairs to plot the data
    # and use a log scale on both axes
    # You will display the plot using plt.show(), which is already written
    ranks = [rank for rank, frequency in ranks_and_frequencies]
    frequencies = [frequency for rank, frequency in ranks_and_frequencies]

    plt.plot(ranks, frequencies)

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Log Rank')
    plt.ylabel('Log Frequency')
    plt.title('Christabel Ekeocha')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Constructs a curve '
                                                 'demonstrating Zipf\'s Law '
                                                 'by plotting a rank, '
                                                 'frequency plot.')
    parser.add_argument('--path', type=str, required=True, help='Path to file')
    args = parser.parse_args()
    plot(args.path)

# The data points form an approximate straight diagonal downward sloping line
# demonstrating Zipf's Law: word frequency in the selected book is inversely proportional to
# its rank (frequency ~ 1/rank). A tiny number of words have very high frequencies, 
# while a most other words have very low frequencies throughout the book.