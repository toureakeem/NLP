import spacy 
nlp = spacy.load('en_core_web_md')

# Code to read the txt file provided.

with open('movies.txt','r') as file:
   movies = file.readlines()

# Hulk description.
Planet_Hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator'

doc = nlp(Planet_Hulk)

hulk_description = [sent.text for sent in doc.sents]

# The following variables are in place to help find the maximum similarity.
max_similarity = 0
max_similarity_movie = ''

for token in hulk_description:
    token = nlp(token)
    for token_ in movies:
        token_ = nlp(token_)
        similarity_score = token.similarity(token_)
        
        # The following would compute the maximum similarity and give us an output of the movie name.
        if similarity_score > max_similarity:
            max_similarity = similarity_score
            max_similarity_movie = token_
        
print('The most similar movie based on your watch history would be the following:\n',max_similarity_movie)
        
        
