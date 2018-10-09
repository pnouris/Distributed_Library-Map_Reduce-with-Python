from mrjob.job import MRJob
from mrjob.step import MRStep



class MRMaxNum(MRJob):

	#reference: http://pythonhosted.org/mrjob/guides/quickstart.html#writing-your-first-job
	#define the multiple steps in my job
	def steps(self):

		return [
		MRStep(mapper=self.mapper,
			reducer=self.reducer),
		MRStep(reducer=self.Maximum_reducer)
		]

	#yield each number in the lines
	def mapper(self,_, line):
		for number in line.split(','):

			yield (int(number),0)

	def reducer(self, number, values):
		max_number=0

		for i in values:
			if max_number < number:

				max_number = number

		yield None,(max_number, sum(values))


	def Maximum_reducer(self, _, max_number):

			yield "The max number is:",max(max_number)




if __name__ == '__main__':

 	MRMaxNum.run()
