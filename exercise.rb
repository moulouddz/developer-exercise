class Exercise

  # Assume that "str" is a sequence of words separated by spaces.
  # Return a string in which every word in "str" that exceeds 4 characters is replaced with "marklar".
  # If the word being replaced has a capital first letter, it should instead be replaced with "Marklar".
  def self.marklar(str)
    # TODO: Implement this method
    sentence = Array.new
    #split the string str and put each individual word or punctuation in an array
    sentence = str.split(/(\W+)|([[:punct:]])/)

    #looping through the array elements
    for i in 0..sentence.length-1
      #checking if the word exceeds 4 characters
      if sentence[i].length > 4
        #checking if the word is capitalized (first letter is capital)
        #and replacing it with capitalize 'Marklar' if so
        if sentence[i] == sentence[i].capitalize
          sentence[i] = 'Marklar'
        else
          #replacing the word with 'marklar'
          sentence[i] = 'marklar'
        end
      end
    end
    #join the array elements and form a new string
    new_sentence = sentence.join
  end


  # Return the sum of all even numbers in the Fibonacci sequence, up to
  # the "nth" term in the sequence
  # eg. the Fibonacci sequence up to 6 terms is (1, 1, 2, 3, 5, 8),
  # and the sum of its even numbers is (2 + 8) = 10
  def self.even_fibonacci(nth)
    # TODO: Implement this method
    #since the two first two sequence are not even number
    #we should return zero for the sum of even numbers in these cases
    if (nth == 1 || nth == 2)
      return 0
    #calculating Fibonacci sequence up to nth term if nth is greater than 2
    #and assign each sequence to an array element
    elsif nth > 2
      fibonacci = Array.new
      #assigning the two first elements of the Fibonacci sequence to start with
      fibonacci[0]=1
      fibonacci[1]=1
      #declaring the sum of even numbers and assign zero to it
      sum_even = 0
      #looping through the array starting from the 3rd element up to nth-1
      for i in 2..nth-1
        #calculating the ith sequence based on the last previous two elements in the array
        fibonacci[i] = fibonacci[-1] + fibonacci[-2]
        #check if the ith sequence is an even number
        #and add it to the sum_even if so
        if fibonacci[i] % 2 == 0
          sum_even += fibonacci[i]
        end
      end
      return sum_even
    #print a warning statment if nth is negative or equal to zero
    else
      puts "please enter a number greater than one"
    end

  end
end
