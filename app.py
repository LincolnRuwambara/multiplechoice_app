from Questions import Questions
   

quest=[
            "What is the primary goal of data preprocessing in data science?\na) Data visualization\nb) Data cleaning and transformation\nc) Model training\nd) Feature engineering\n\n",
            "Which of the following is NOT a supervised learning algorithm?\na) Linear Regression\nb) Decision Tree\nc) K-Means Clustering\nd) Support Vector Machine\n\n" , 
            "In a classification problem, what is the target variable or output typically referred to as?\na) Feature\nb) Predictor\nc) Label\nd) Input\n\n"
            "Which data visualization technique is most suitable for displaying the distribution of a single continuous variable?\na) Scatter plot\nb) Histogram\nc) Bar chart\nd) Box plot\n\n",
            "Which programming language is commonly used for data analysis and machine learning in data science?\na) Java\nb) Python\nc) C++\nd) Ruby\n\n",
            "What is the purpose of cross-validation in machine learning?\na) Testing the model on unseen data\nb) Dividing data into training and test sets\nc) Evaluating the model's performance with multiple train/test splits\nd) Fine-tuning hyperparameters\n\n",
            "What does the term 'overfitting' refer to in the context of machine learning?\na) The model performs well on training data but poorly on test data\nb) The model performs well on both training and test data\nc) The model is too simple to capture the underlying patterns in the data\nd) The model has too many features\n\n",
            "Which algorithm is often used for text classification and sentiment analysis?\na) Linear Regression\nb) K-Means Clustering\nc) Naive Bayes\nd) Random Forest\n\n",
            "Which statistical measure is used to evaluate the performance of a classification model when the classes are imbalanced?\na) Accuracy\nb) Precision\nc) Recall\nd) F1-score\n\n",
            "What is the purpose of dimensionality reduction techniques like Principal Component Analysis (PCA) in data science?\na) To create new features\nb) To increase the dimensionality of the data\nc) To reduce the computational complexity of models\nd) To eliminate irrelevant or redundant features\n\n"]




"""ansers=[
    b) Data cleaning and transformation
c) K-Means Clustering
c) Label
b) Histogram
b) Python
c) Evaluating the model's performance with multiple train/test splits
a) The model performs well on training data but poorly on test data
c) Naive Bayes
d) F1-score
d) To eliminate irrelevant or redundant features

]"""





questions=[
    
        Questions(quest[0],"b"),
        Questions(quest[1],"c"),
        Questions(quest[3],"c"),
        Questions(quest[4],"b"),
        Questions(quest[5],"b"),
        Questions(quest[6],"c"),
        Questions(quest[7],"a"),
        Questions(quest[8],"d"),
        Questions(quest[9],"d")

]



def run(questions):
    score=0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score +=1
    print(score)        


run(questions)