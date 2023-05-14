# CS379SP23-HW1
### Biometric systems - performance evaluation
### Spring 2023, Bucknell University 
### Due date: Feb 10th, 2023, Midnight (11:59)| submissions would be accepted through GitHub only unless stated otherwise.

### Your full name: 
### Time taken to complete:

Make sure you read the [general setup instructions](https://docs.google.com/document/d/1A1BGTjrnIgJXBYV0qg_ZrlOLL4x0hzlaSt6ryFXMbQE/edit?usp=sharing) before you start!



### Description: 

Let B1, B2, and B3 are three biometric systems based on three different modalities M1, M2, and M3. 

Let G1 = {g11, g12, g13, ..., g1p}, G2 = {g21, g22, g23, ..., g2q}, and G3={g31, g32, g33, ..., g3r} are the sets of genuine match scores 

obtained after genuine access attempt on B1, B2, and B3. 

Similarly, let I1={i11, i12, i13, ..., i1p}, I2={i21, i22, i23, ..., i2q}, and I3 ={i31, i32, i33, ..., i3r} are the sets of impostor 
scores for impostor attempts on B1, B2, and B3. 

Your job is to compare the performances of B1, B2, and B3 using the following metrics:

(1) ROC plots [Read this document for more details and understanding](https://people.inf.elte.hu/kiss/11dwhdm/roc.pdf)

(2) DET plots (similar to ROC except the fact that it plots FAR vs. FRR instead TAR vs. FPR [Read this document for more details](https://ccc.inaoep.mx/~villasen/bib/martin97det.pdf)

(3) Equal Error Rate (EER): EER is a point on the DET curve where FAR and FRR become equal

(4) Overlap of the histograms formed from the genuine and impostor scores of the respective systems
[Read the following to know how to find histogram overlap]
(https://mpatacchiola.github.io/blog/2016/11/12/the-simplest-classifier-histogram-intersection.html)

# Tasks: 
Implement the plot_roc, plot_det, compute_eer, and get_hists_overlap functions given in PerformanceEvaluation.py 

Use the above implementations of these functions to answer the following questions:

Compare the three systems by:

(1) Plotting ROCs of all three biometric systems on Figure1

(2) Plotting DETs of all three biometric systems with EER line on it on Figure2 

(3) Plotting the intersection of histograms of genuine and impostor scores (use 100 bins) on Figure 3
Which of the three systems do you think is the best and which is the worst? Justify your answer.

Note: 

Assume that the genuine and impostor scores represent the similarity measure

That means the higher the score is the better the match

Stick to using only numpy, pandas, and matplotlib packages unless stated otherwise

Use np.random.seed(1846) so the results are reproducible 

----------------Improvement 
Make it autograded. 
Specifically ask for interpretation of the figures and relationship between the histoverlap and EER?

