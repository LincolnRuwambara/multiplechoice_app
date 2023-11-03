class questions:

    def __init__(self,prompt,answer):

        self.prompt = prompt
        self.answer = answer
        
        questions=[
            "What is the primary goal of data preprocessing in data science?\na) Data visualization\nb) Data cleaning and transformation\nc) Model training\nd) Feature engineering\n\n",
            "Which of the following is NOT a supervised learning algorithm?/na) Linear Regression\nb) Decision Tree\nc) K-Means Clustering\nd) Support Vector Machine\n\n"  
            "In a classification problem, what is the target variable or output typically referred to as?\na) Feature\nb) Predictor\nc) Label\nd) Input"
            ]
        
   
        for question in questions:
            print(question)


