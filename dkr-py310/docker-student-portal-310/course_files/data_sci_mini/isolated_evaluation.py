"""You've got way to much stuff conflated - much easier to isolate
   code and conquer one bit at a time.   Here, you just want to look
   at the evaluation of billing seconds."""

import math

#default argument values are easy to update in call to function
def evaluate(second, minimum=30, incr=15):
	"""put the evaluation in a function - this makes it amenable
	   to testing as an isolated operation.
	   
	   The approach here avoids transforming numbers to strings.
	   It also avoids map() and filter() operations, instead
	     applying Boolean logic - a little more transparent, I think.
	"""

	if second:  ##a None object fails this test
		if second <= minimum:	#minimum billing is 30 seconds	
			return minimum
		#bill in <incr> second intervals, rounding up
		return math.ceil(second/incr) * incr #easier than dorking around with %


	else: #None object encountered
		return 0


if __name__=='__main__':
	#expected individual results with test data
	secs=    [0,    15, 30, 35, 50, 75, 90, None]
	targets= [0,    30, 30, 45, 60, 75, 90, 0]
	
	total=0
	
	#this checks each test value against expected
	for sec, target in zip(secs, targets):
		answer=evaluate(sec)
		assert(target== answer)
		total+=answer
		
	#this makes sure we got the total right
	assert(total==sum(targets))
	print("Yea!  That worked just fine.")
	from pprint import pprint
	
	pprint(globals())
	pprint(locals())	