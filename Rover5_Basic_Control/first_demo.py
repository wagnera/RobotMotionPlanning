#!/usr/bin/python

# Demo of some programming concepts in Python
# Initial code written by: Jason Ziglar <jpz@vt.edu>
# Extended and modified by: Anthony Wagner <wagnera@vt.edu>

# Define a function which computes the harmonic series
def harmonic_series(num_terms):
  '''Function which computes some number of terms from the harmonic series.
  num_terms: the number of terms to add together.
  returns: The value computed'''
  #Create variable to store result, set to some initial value
  value = 0
  num_terms=int(num_terms) 
  if num_terms == 0 or num_terms < 0:
    #checks that the user entered a logical input
	 value = 0; 
  	#sets value to zero for an inproper input
  else:
    #range produces a sequence of numbers, [0, num_terms), and executes the loop
    # with ii set to each value
    for ii in range(num_terms):
      #Set value to the value plus the next term
      # Note: Computers start counting at 0, so we have to add 1 to be safe
      value = value + (1.0 / (ii + 1))

  # Return the value to whomever called this function
  return value

def harmonic_series_while(num_terms):
  '''Function which computes some number of terms from the harmonic series, using a while loop.
  num_terms: the number of terms to add together.
  returns: The sum of the first n terms of the series'''

  #Create variable to store summation
  value = 0
  #A counter to keep track of how many terms have been computed
  counter = 0
 
  if num_terms == 0 or num_terms < 0:
    #checks that the user entered a logical input
        value = 0;
        #sets value to zero for an inproper input
  else:
    # This will run until "counter <= num_terms" returns a false statement
    while counter < num_terms:
      value = value + (1.0 / (counter + 1))
      # Very important - while runs until it sees false, so we have to make sure
      # the test will eventually fail
      counter = counter + 1

  # Return value
  return value

def pi_approx(num_terms):
  '''Function approximates pi using an infinite series that uses a defined number of summations to approximate'''
   #Create variable to store summation
  value = 0
  #A counter to keep track of how many terms have been computed
  counter = 1
  if num_terms == 0 or num_terms < 0:
    #checks that the user entered a logical input
        value = 0;
        #sets value to zero for an inproper input
  else:
    # This will run until "counter <= num_terms" returns a false statement
    while counter < num_terms:
      #using 1/n^2 infinite series to approximate pi
      value = value + (1.0 / (counter ** 2))
      # Very important - while runs until it sees false, so we have to make sure
      # the test will eventually fail
      counter = counter + 1
      #since series approximates pi^2/6 this solves for pi
    piAPRX=(value*6.0)**(0.5)
    #return approximation for pi
  return piAPRX

def main():
   #Starting here, the program begins execution, since the previous statements were describing functions, but not actually calling them
  # Print a welcome
  print "Welcome to a simple harmonic series approximation program."
  #Ask the user to select a function
  request = raw_input("Select which function to use: 1) For loop 2) While loop: 3)Approximate Pi")
  #Convert that input to an integer
  request = int(request)

  while request != 1 and request != 2 and request !=3:
    print "Invalid Entry. Please enter either 1 or 2 or 3 or type 4 to quit"
    request = raw_input("Select which function to use: 1) For loop 2) While loop: ")
    #Convert that input to an integer
    request = int(request)
    #if the user wants to quit
    if request ==4:
      exit()

  #Same as before, but in a single line.
  iterations = raw_input("How many terms should I use? ")

  #attempt to convert input to an int will fail if a floting point is entered
  try:
    #convert the raw input to an int
     iterations = int(iterations)
  #if converting to an int fails IE floating point entered
  except:
    #convert raw input to a floating point number
    iterations = float(iterations)
  #convert floating point number to an interger
  iterations = int(iterations)

  # Test input

  if request == 1:
    # Get value form function
    result = harmonic_series(iterations)
    # Print using a technique known as string interpolation. %s means "take the next value after the string and insert as a string"
    # So it will look at the list of values after the % and grab the next (only) one
    # For more details, look here: https://docs.python.org/2/library/stdtypes.html#string-formatting
    print "For loop produces: %s" % result
  elif request == 3:
    result = pi_approx(iterations)
    print "Pi approximated using series: %s" % result
  else:
    # Same as previous statement, but notice you don't have to store a value in a variable before using it, if it makes sense.
    print "While loop produces %s" % harmonic_series_while(iterations)
main()