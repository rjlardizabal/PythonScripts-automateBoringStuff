import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNum in range(35):

    questionsFile = open('capitalsquiz_question' + str(quizNum +1) + '.txt','w')
    answersFile = open('capitalsquiz_answer' + str(quizNum +1) + '.txt','w')


    questionsFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    questionsFile.write((' '*20) + 'State Capital Quiz Form '+str(quizNum+1))
    questionsFile.write('\n\n')

    

    states = list(capitals.keys())
    random.shuffle(states)


    for i,state in enumerate(states):
        correctAnswer = capitals[state]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        choices = random.sample(wrongAnswers,3)
        choices.append(correctAnswer)
        random.shuffle(choices)
        answersFile.write('%s. %s\n' %(str(i+1), 'ABCD'[choices.index(correctAnswer)]))
        
        
        questionsFile.write(str(i+1)+'. What is the capital of '+state+'\n\n')
        for j,choice in enumerate(choices):
            questionsFile.write('\t'+'ABCD'[j]+'. '+choice+'\n\n')
    questionsFile.close()
    answersFile.close()
