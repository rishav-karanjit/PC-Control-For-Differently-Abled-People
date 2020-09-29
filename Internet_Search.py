import nltk
import wikipedia

class Search:
    def Wiki_Result(self,query):
        tokens = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(tokens)
        for i in tagged:
            if i[1] == "NN":
                search = i[0]
        try:
            result = wikipedia.summary(search,sentences=3)
            return "According to wikipedia" + result
        except wikipedia.DisambiguationError as e:
            result = wikipedia.summary(e.options[1],sentences=3)
            return "According to wikipedia" + result