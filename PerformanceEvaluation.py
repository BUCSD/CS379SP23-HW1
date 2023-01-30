# Importing the required packages
# Stick to using only numpy, pandas, and matplotlib packages unless stated otherwise
import numpy as np
from matplotlib import pyplot as plt
def plot_roc(gen_scores, imp_scores):
    # ROC: Receiver Operating Curve
    # This functions plots an ROC curve for the given match scores
    # Remove/comment the following pass keyword before you start the implementation
    pass

def plot_det(gen_scores, imp_scores):
    # DET: Decision Error Treadoff
    # This functions plots an DET curve for the given match scores
    # Remove/comment the following pass keyword before you start the implementation
    pass

def compute_eer(gen_scores, imp_scores):
    # This functions computes the equal error rate for the given match scores
    # Remove/comment the following pass keyword before you start the implementation
    pass

def get_hists_overlap(gen_scores, imp_scores):
    # This function returns the intersection of histograms of the input scores
    # Read the following link to understand how can you find the intersection of two histograms
    # (https://mpatacchiola.github.io/blog/2016/11/12/the-simplest-classifier-histogram-intersection.html)
    pass


if __name__ == "__main__":
    # Consider the genuine and impostor scores represent the similarity measure
    # That means the higher the score is the better the match
    # 0 <= thresholds <=1
    # 0 <= genuine_scores <= 1, 0 <= impostor_score <= 1
    # Use 100 bins for all the experiments

    # A toy example of hitogram, just to play with:
    np.random.seed(1833)  # setting the random seed so the exp are reproducible
    num_bins = 100
    mu_1 = 0.2  # mean of the impostor scores
    mu_2 = 0.85  # mean of the genuine scores
    imp = np.random.normal(mu_1, 0.3, 1000)
    gen = np.random.normal(mu_2, 0.1, 1000)

    plt.hist(imp, bins=100, range=[0,1])
    plt.hist(gen, bins=100, range=[0,1])
    plt.show()

    # Biometric system B1: Histograms of genuine and imposter scores have no overlap
    # Create the G1, and I1 using the hint given in the toy example


    # Biometric system B2: Histograms of genuine and imposter scores have 5-10% overlap
    # Create the G2, and I2 using the hint given in the toy example

    # Biometric system B3: Histograms of genuine and imposter scores have about 50% overlap
    # Create the G3, and I3 using the hint given in the toy example

    # Compare B1, B2, and B3
