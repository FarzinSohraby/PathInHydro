This repo is the content used in the paper entitled "PathInHydro, a set of machine learning models to identify unbinding pathways of gas molecules in [NiFe] hydrogenases" by Farzin Sohraby, Jing-yao Guo, Ariane Nunes-Alves.

Here you can find a description of the datasets and the codes used to train and evaluate 2 machine learning models for predicting unbinding pathways of ligands in complex with [NiFe] hydrogenases.

![up](https://github.com/FarzinSohraby/PathInHydro/assets/172061891/6db3344c-2e1e-430c-bd40-5fd1c12c119c)


Datasets: there are a total 4 data sets, each containing labels (designated unbinding paths) and features (ligand-residue contacts) collected from a set of simulations:

1- Df-H2ase-CO.csv: dissociation of CO from the [NiFe] hydrogenase from Desulfovibrio fructosovorans.

2- Df-H2ase-H2.csv: dissociation of H2 from the [NiFe] hydrogenase from Desulfovibrio fructosovorans.

3- Df-H2ase-O2.csv: dissociation of O2 from the [NiFe] hydrogenase from Desulfovibrio fructosovorans.

4- Mdg-H2ase-CO.csv: dissociation of CO from the [NiFe] hydrogenase from Megalodesulfovibrio gigas.

Jupyter notebooks: containing the python codes for visualization of data distribution, performing grid search, training, testing and validation of two machine learning models (binary and multiclass classification).

1- Data-Distribution-Binary.ipynb: containing the code for plotting the distribution of the data set for the binary model (2 classes: primary and secondary).

2- Data-Distribution-Multiclass.ipynb: containing the code for plotting the distribution of the data set for the multiclass model (9 classes: T1-T9).

3- tSNE.ipynb: containing the code for visualization of the data distribution using the t-SNE algorithm.

4- Algorithm-Selection-Grid-Search-Binary-Model.ipynb: containing the code for the selection of algorithm and corresponding hyperpatameters for the binary classification, using the grid search method. 

5- GridSearch-HyperparameterTuning-MulticlassModel.ipynb: containing the code for hyperparameter tuning of the multiclass model through grid search.

6- Training-Test-Binary-Model.ipynb: containing the code for training and testing the binary model, then generating the figures in the paper (ROC curve and Confusion Matrix).

7- Training-Test-MultiClass-Model.ipynb: containing the code for training and testing the multiclass model, then generating the figures in the paper (Confusion Matrix).
