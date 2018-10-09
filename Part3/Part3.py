from mrjob.job import MRJob
from mrjob.step import MRStep


class MRAvarage(MRJob):

    #references:
    #http://pythonhosted.org/mrjob/guides/quickstart.html#writing-your-first-job
    #http://stackoverflow.com/questions/30943555/how-to-get-the-average-number-of-words-in-a-text-in-mrjob

    def steps(self):
 	      return [
	  	    MRStep(mapper=self.mapper),
      		MRStep(mapper=self.mapperTwo),
      		MRStep(reducer=self.reducer)
      		    ]
    def mapper(self, key, line):

         for number in line.split(','):
            #print(number)
            yield (int(number),1)

    def mapperTwo(self, number, values):
        
        yield(1, number)

    def reducer(self, key, values):
        total= 0
        elem = 0

        for i in values:
            total += i
            elem += 1
        # print(total)
        # print(elem)
        #print(i)
        yield ("The mean is:", total/ float(elem))


if __name__ == '__main__':
    MRAvarage.run()
