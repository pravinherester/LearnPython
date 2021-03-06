Instructions
You are going to write a program that tests the compatibility between two people.

To work out the Friendship score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word FRIEND occurs. Then combine these numbers to make a 2 digit number.

For Friendship Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Friendship Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Pravin

name2 = "Yadu"

T occurs 0 times

R occurs 1 time

U occurs 1 times

E occurs 0 times

Total = 2

F occurs 0 times
R occurs 1 times
I occurs 1 times
E occurs 0 times
N occurs 1 times
D occurs 1 times

Total = 4

Friend Score = 24

Print: "Your Friendship score is 24"T

The testing code will check for print output that is formatted like one of the lines below:

"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."

Hint
The lower() function changes all the letters in a string to lower case.
https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

The count() function will give you the number of times a letter occurs in a string.
https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

