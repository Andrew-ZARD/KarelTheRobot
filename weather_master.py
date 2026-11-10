"""
File: weather_master.py
Name:Andrew
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100

def main():
	"""
	This program finds the highest, Lowest,and Average
	among user inputs.
	"""
	print("StandCode \"Weather Master 4.0\"!")
	temperature = int(input("Next temperature:(or -100 to quit)"))

	if temperature == EXIT:
		print("No temperature were entered.")
	else:
		summation = temperature
		times = 1
		highest = temperature
		lowest = temperature
		cool_days = 1
		while True:

			temperature = int(input("Next temperature:(or -100 to quit)"))
			if temperature == EXIT:
				print("No temperature were entered.")
				break
			if temperature < 16:
				cool_days +=1

			if temperature > highest:
				times += 1
				highest = temperature
				summation += temperature
			elif lowest < temperature < highest:
				times += 1
				summation += temperature
			else:
				times += 1
				summation += temperature
				lowest = temperature

		print("highest temperature = "+str(highest))
		# print(str(times)) 測試用的
		# print(str(summation)) 測試用的
		print("Lowest temperature = " + str(lowest))
		average = summation/times
		print("Average = "+str(average))
		print(str(cool_days)+" cool day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
