class Exercise

  # Assume that "str" is a sequence of words separated by spaces.
  # Return a string in which every word in "str" that exceeds 4 characters is replaced with "marklar".
  # If the word being replaced has a capital first letter, it should instead be replaced with "Marklar".
  def self.marklar(str)
    # TODO: Implement this method
    sentence = Array.new
    #new_sentence = Array.new
    sentence = str.split(/\W+/)
    lenght = sentence.lenght
    for i in 0..lenght
      if sentence[i].lenght > 4
        if sentence[i] = sentence[i].capitalize
          sentence[i] = 'Marklar'
        else
          sentence[i] = 'marklar'

    new_sentence = sentence.join(" ")

  end

  # Return the sum of all even numbers in the Fibonacci sequence, up to
  # the "nth" term in the sequence
  # eg. the Fibonacci sequence up to 6 terms is (1, 1, 2, 3, 5, 8),
  # and the sum of its even numbers is (2 + 8) = 10
  def self.even_fibonacci(nth)
    # TODO: Implement this method
  end

end
