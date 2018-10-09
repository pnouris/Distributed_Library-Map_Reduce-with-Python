from mrjob.job import MRJob
from mrjob.step import MRStep


class MRAvarage(MRJob):


    def steps(self):
 	      return [
	  	    MRStep(mapper=self.mapper),
      		MRStep(mapper=self.mapperTwo),
      		MRStep(reducer=self.reducer),
        #    MRStep(reducer=self.reducerTwo)
      		    ]

    def mapper(self,key,line):
        words = line.split()
        for word in words:
            #print(word)
            yield (word, 1)

    def mapperTwo(self,word,groups):
        print(word)
        yield(word,1)

    def reducer(self,word,groups):
        for i in groups:
            u = tuple(word)
        yield(1,u)
    # def reducerTwo(self,wordB,groups):

                # for u in groups:
                #     u = word[u]
                #     for v in groups:
                #         v = word[v+1]
                #         for w in groups:
                #             w = word[w+2]
                #             if(v == w):
                #                 yield(word,(u,v,w))





if __name__ == '__main__':
    MRAvarage.run()
