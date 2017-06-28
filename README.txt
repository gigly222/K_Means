
-README

**********************************************
K Means Clustering
**********************************************

-Pycharm2016.2.3 was used for development.

The dataset used was from the following link:
http://www.utdallas.edu/~axn112530/cs6375/unsupervised/test_data.txt
*I provided a data set that has already been converted to having "clrf" at the end of each line. When reading in the file from the website, it is not in proper format. Might need to do something like dos2Unix. 
You could use the data set I provided in the "dataset" folder for ease. 


*************************************************************************************************
To Run the part one program, type in something following the format below (such as using MobaXterm):
*************************************************************************************************

python K_Means_Main.py "3" "test_data.txt"

*************************************************************************************************
Where "3" is the number of clusters, "test_data.txt" is the path to the datafile. 
Make sure you provide the complete path to the files, or put the needed files in the folder with the program. 


Please note***

I have used matplotlibs pyplot to show a visual representation of the data clustered around its centroid. There are limited colors available so it only plots only up to number of clusters k = 7. After reaching 7,
it no longer plots, but the program will continue working as usual. The plot is for enjoyment and visualization purposes. It was not required in the assingment but it provides a good visual aid to the project. 
When the program runs, if the plot appears, you can exit out of it by clicking the "x" in the upp