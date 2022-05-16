#! /opt/anaconda3/envs/learningp37/bin/python python3.7
# Exercise 13.12.9 / From "Think Python"
# Learning and experimentation with the book "Think Python" (by Allen Downey)
# Code by José Delpino

# Exercise 13.12.9: Zipf's Law: Mathematics and Natural Languages

from random import shuffle
import matplotlib.pyplot as plt
from e13_01_04_book_works1 import make_book_hist


def make_ranks_freqs(histogram):
    rf_pairs = list()
    # Sort the list of frequencies in decreasing order
    freqs = list(histogram.values())
    freqs.sort(reverse=True)
    # Enumerate the ranks and frequencies
    rf_pairs = [(rank + 1, freq) for rank, freq in enumerate(freqs)]
    return rf_pairs


def plot_ranks(histograms, scale='log'):
    """Creates a plot of rank (x) against
     frequency (y) using a list up to 20 histograms.
    (1) histograms: A dict of histograms that map a label with an histogram.
    Each histogram maps words to frequencies from a file.
    (2) scale: A string 'linear', 'log', 'symlog', "logit"...
    """
    # Calculates the number of histograms it will process:
    num_histograms = len(histograms)
    # Defines and sets properties for the plot figure:
    colors = {
        'blue': '#0343df', 'green': '#15b01a', 'red': '#e50000',
        'cyan': '#00ffff', 'magenta': '#c20078', 'yellow': '#ffff14',
        'black': '#000000', 'purple': '#7e1e9c', 'pink': '#ff81c0',
        'violet': '#7e1e9c', 'olive': '#6e750e', 'salmon': '#ff796c',
        'neon green': '#0cff0c', 'puke green': '#9aae07',
        'brick red': '#8f1402', 'golden rod': '#f9bc08',
        'neon blue': '#04d9ff', 'peacock blue': '#016795',
        'brown yellow': '#b29705', 'orange': '#f97306'
    }
    # Randomize the list of colors for the histograms:
    color_codes = list(colors.values())
    shuffle(color_codes)
    # Defines and sets properties for the plot figure:
    plt.clf()
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    # Prepare the x–ranks–, y–freqs– values.
    i = 0
    for label in histograms:
        # Get the loop base variables: color, histogram
        color = color_codes[i]
        histogram = histograms[label]
        # Prepare the x, y pairs and separate them
        rf_pairs = make_ranks_freqs(histogram)
        print(label, rf_pairs[0][0], rf_pairs[0][1])
        print(label, rf_pairs[99][0], rf_pairs[99][1])
        print(label, rf_pairs[999][0], rf_pairs[999][1])
        print(label, rf_pairs[-1][0], rf_pairs[-1][1])
        ranks, freqs = zip(*rf_pairs)
        # Plot the line for each book
        plt.plot(ranks, freqs, color, linewidth=1, label=label)
        i = (i + 1) % num_histograms
    plt.legend()
    plt.show()


def main():
    books = {
        'Madamme Bovary': 'files/emma.txt',
        'Grimm\'s Tales': 'files/grimms_tales.txt',
        'Gulliver\'s': 'files/gulliver_s_travels.txt',
        'Huckleberry': 'files/huckleberry_finn.txt',
        'Mobydick': 'files/moby_dick_or_the_whale.txt',
        'Secret Island': 'files/secret_island.txt',
        'Don Quijote': 'files/don_quijote.txt'
    }
    histograms = dict()
    for label in books:
        filename = books[label]
        histogram = make_book_hist(filename)
        histograms[label] = histogram

    plot_ranks(histograms)


if __name__ == '__main__':
    main()
