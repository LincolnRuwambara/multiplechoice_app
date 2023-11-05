from Questions import Questions
   

quest=[
            "What is the primary goal of data preprocessing in data science?\na) Data visualization\nb) Data cleaning and transformation\nc) Model training\nd) Feature engineering\n\n",
            "Which of the following is NOT a supervised learning algorithm?\na) Linear Regression\nb) Decision Tree\nc) K-Means Clustering\nd) Support Vector Machine\n\n" , 
            "In a classification problem, what is the target variable or output typically referred to as?\na) Feature\nb) Predictor\nc) Label\nd) Input\n\n"
            ]





questions=[
        Questions(quest[0],"a"),
        Questions(quest[1],"b"),
        Questions(quest[2],"c")
]



def run(questions):
    score=0
    for i in questions:
        answer = input(i.prompt)
        if answer == i.answer:
            score +=1
    print(score)        


run(questions)