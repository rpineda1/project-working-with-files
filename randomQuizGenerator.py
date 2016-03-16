# Ricardo Pineda#
#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random, os
os.makedirs(os.path.join('./answers'), exist_ok=True)#this tells the program to create folders named Answers, and if the folder already exist then it returns true.
os.makedirs(os.path.join('./quizzes'), exist_ok=True)#theis tells the program to create folders named quizzes, and if the folder already exists then it returns true.
            
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 
            'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

            #TODO: follow the 'generating random quiz files' project in the textbook to fill in this file.
            #TODO: however, make the following modificatiosn to the instructions on the textbook:
            #       1. instead of making 35 quiz versions, you'll only make 5 quiz versions
            #       2. instead of creating quiz and answer files in the current working directory, create a folder titled 'quizzes' and another folder titled 'answers'.
            #       3. place the randomly-generated quizzes in the 'quizzes' directory.
            #       4. plaec the corresponding answers in the 'answers' directory.
            
for quizNum in range(5):
    quizFile = open('./quizzes/capitalsquiz%s.txt' % (quizNum + 1), 'w')# this opens and assigns random quiz files to the quizzes directory.
    answerKeyFile = open('./answers/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')# this opens and assigns random answers to the answer directory.
    #this creates the headder for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    #this shuffles all the states in random order.
    states = list(capitals.keys())
    random.shuffle(states)
    
    for questionNum in range(50):#the range of questions is 1-50.
        correctAnswer = capitals[states[questionNum]]#this tells the program to select the correct answer.
        wrongAnswers = list(capitals.values())#assigns the wrong answers from the capitals directory to wrong answers.
        del wrongAnswers[wrongAnswers.index(correctAnswer)]#takes out the worng answers from the quiz.
        wrongAnswers = random.sample(wrongAnswers, 3)#picks 3 wrong asnswers from the directory.
        answerOptions = wrongAnswers + [correctAnswer]#this lays out the format to have different options in the quiz.
        random.shuffle(answerOptions)#shuffles the answers so they won't be the same.
    
        quizFile.write('%s. What is the capital of %s\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('%s. %s\n' % ('ABCD'[i], answerOptions[i]))# places 4 answers in the quiz.
            quizFile.write('\n')
    
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))
        
quizFile.close()
answerKeyFile.close()
