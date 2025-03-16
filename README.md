----------------------------------------------------------------------------------------------------

# The Seating of Diogenes Club

## a

If there are no rules, any person cuold seats in any place.

    X X X X X X X X X X     = 10 places

So in the firts place any of 10 people could seats, in the second any of 10-1 people could sits.
We have to subtract a person cause is sits in the first place, and so on...

Finally we have:

    10*9*8*7*6*5*4*3*2*1 = 3.628.800 (10!)

## b

Since two people has to sit next to each other we have (10-2 = 8) free places.

    X X X X X X X X = 8 places

But we can treat them also as 1 unit to simplify the computation.

    X X X X X X X X X = 9 places

So we have to compute:

    9! = 362.880

To complete the computation we have to take into account the possibility of changing seats between them.

They are just 2, so we have basically to compute:

    9! * 2! = 362.880 * 2 = 725.760

## c

We have 2 categories: A and B

Two person of the same categories cannot seats next to each other.

So for example they have to seats in this way:

    A B A B A B A B A B

So the first group could seats in 5! possible ways.

Also the second group could seats in 5! possible ways.

So to compute the all possible combinations we have to do:

    5! * 5! = 14.400

## d

5 Pairs

Each pair is: {informant, handler}

Each pair is inseparable, they must sits together

Similar to the exercise B we can treat each pair as a single unit  --> 5 units

At this point we have to compute the number of ways to arrange the 5 units:

    5! = 5 * 4 * 3 * 2 * 1 = 120

To complete the computation we have to take into account the possibility of changing seats between them.

They are just 2, so for each pair we have 2 possible combination:

    5! * 2^5 = 120 * 32 = 3840

----------------------------------------------------------------------------------------------------

# The Cipher Arrays of Irene Adler

N: number of possible integers
K: array dimension

    example:

    [ X X X X X X X X X X ]
    
    K = 10

To find the number of ways to choose K DISTINCT integers from a set of N integers we have to compute:

    Combination(N, K) = N! / ( K! * (N-K)! )

We have to use the combination since they are independent and the order doesn't matter.

----------------------------------------------------------------------------------------------------

# The Paths of the Hound

## a

Consider a grid of N*M
We can move only (right) or (down)

Without any bounds it's possible to have:

N - 1 possible horizontal moves (right)

M - 1 possible vertical moves (down)

So the total number of possible moves (horizontal & vertical):

    (N-1) + (M-1) = N + M - 2 --> TOT

At this point for compute how many trails can we have with no bounds we have to compute the
combination of (N-1) or (M-1) steps on the total number of possible moves:

Combination(TOT, (M-1))

### example

grid (3*2) n = 3; m = 2

    X   X   X
    x   x   x

In this case we have:

2 possible horizontal moves (right)

1 possible vertical moves (down)

So the total number of possible moves (horizontal & vertical) is:

    (3-1) + (2-1) = 3

At this point for compute how many trails can we have with no bounds we have to compute the
combination of (N-1) or (M-1) steps on the total number of possible moves:

    Combination(3, (2-1)) = (3, 1) = 3! / ( 1! * (3-1)! ) = 3

## b

Since the first step is to move to the right we have N - 2 possible horizontal moves

So the procedure is the same as the first step

So the total number of possible moves (horizontal & vertical):

    (N-2) + (M-1) = N + M - 2 --> TOT

At this point for compute how many trails can we have with no bounds we have to compute the
combination of (N-2) or (M-1) steps on the total number of possible moves:

    Combination(TOT, (M-1))

## c

Now we have to do exactly 3 switch of direction during the path.

This means that we have 3 steps less in the total number of possible moves; so we can rewrite the
total number of possible moves in this way:

    (N - 1) + (M - 1) - 3 --> TOT

We are basically subtracting 3 steps from the total, since we want exactly 3 switches of direction.

We have also to cumpute where these possible switches of direction cuold be in the path.

So we finally have to compute the combination of 3 steps on the Total possible moves.

    Combination (TOT, 3)

----------------------------------------------------------------------------------------------------

# The Poker Game at Reichenbach

Common Data:

    52 cards

    5 cards in a hand

    4 suits

    13 cards for a suit

So the total numbers of possible hands is given by:

    Combination (52, 5) = 52! / (2! * (52-5)!) = 2.598.960 --> TOT

## a

To obtain the chance of a flush we have to compute the combination of 5 cards out of 13.

    Combination (13, 5) = 13! / (5! * (13-5)! ) = 1287

Now we have the possible combination of flush for one suit, for obtain the chance of a flush among
all the 4 suits we have to multiply the output for 4.

    Combination (13, 5) * 4 = 5148 --> Result

To compute the probability we have to divide the outcome found by the total numbers of possible
hands in this way:

    Probability = Result / TOT = 0,19%

## b

Obtain the chance of 2 pairs with distinct value means:

    X X Y Y Z

    where X, Y, Z are cards with the same values (es: X X  -> 3 of hearts, 3 of clubs)

So we first compute the ways to choose X and Y knowing that we can choose them among 13 cards:

    Combination (13, 2) = 13! / ( 2! * (13-2)! ) = 78  --> J

Then we have to choose 2 cards for a single pair knowing we have 4 suits for value.

    Combination (4, 2) = 4! / ( 2! * (4-2)! ) = 6

Since we want to have 2 pairs in our hand we have to compute it also for the other:

    Total Combination for 2 pairs = Combination (4, 2) * Combination (4, 2) = 6 * 6 = 36 --> K

At this point the first part is finished, we have to compute the chance to choose Z, that can't be
equal as X or Y in terms of values.

This means that we can choose it among 11 (13 -2) possible cards for a suit.

Since we have 4 suits we can compute it in this way:

    Possible cards for a suit * N suits = 11 * 4 = 44  --> H

To compute the total chance of 2 pairs with distinct value:

   J * K * H = 78 * 36 * 44 = 123.552 --> Result

To compute the probability we have to divide the outcome found by the total numbers of possible
hands in this way:

    Result / TOT = 4,7%

## c

Obtain the chance of a hand of 4 cards of a kind means:

    X X X X Y

    where X are all cards of the same suits

To compute the chance to obtain a hand with 4 cards of a kind we have to first compute in how many
possibilities i can choose the main card (X):

    I can choose it in 13 possible cards (for a suit) --> X

At this point we have to compute in which way we can obtain the last card (Y).
I have 12 possibilities (13 -1) since 1 values is occuped by the first 4 cards.
12 is my possibilities to obtain another card different from X of 1 suit.
To obtain the possibilities for all the suits i have to compute:

    Possibilities for a suit * N suits = 12 * 4 = 48 --> Y

The total combination to obtain a hand of 4 of a kind is:

    X * Y = 13 * 48 = 624 --> Result

To compute the total chance to obtain a hand of 4 cards of a kind is:

   Result / TOT = 0,024%

----------------------------------------------------------------------------------------------------

# The Binary Telegram of Baskerville

The message is composed by N + M bits.

N: 1
M: 0

R must be < (N + M)

K must be < R

    X X X X X X X X X X
    -------------------  N + M
    -------------        R
    -----                K

We have to compute the chance of the first R bits of contain exactly K ones.

We first compute the combination of k elements on N (ones). ---> CKN

Then we compute the combination of the remaining (R - K) bits of containing just 0 bits (M). ---> CMRK

In the end we compute the total probability to choice R bits from the complete message (N + M).  ---> CRNM

We have to combine all this pieces to compute the probability of having exactly K one's in the first
R bits:

	P(X = K) = (CKN * CMRK) / CRNM = ?

ho pensato di usare la formula della distribuzione binomiale ma non va bene (qua è senza rimpiazzo)

----------------------------------------------------------------------------------------------------

# The Menagerie of Moriarty

3 from 8 Birds

4 from 6 Reptiles

## a

To compute in how many ways he can choose 3 birds out of 8:

    Combination (8, 3) = 8! / ( 3! * (8-3)! )) = 56  --> Birds

To compute in how many ways he can choose 3 reptiles out of 6:

    Combination (6, 3) = 6! / ( 3! * (6-3)! ) = 20  --> Reptiles

The total number of exhibits that he can craft is:

   Birds * Reptiles = 56 * 20 = 1120 --> TOT

## b

The hawk and the raven cannot coexist in the same exhibit.

So we are going to compute the case where they are chosen together and then we subtract this number from the total number of exhibits.

For the reptiles nothing changes:

    Combination (6, 3) = 6! / ( 3! * (6-3)! ) = 20  --> Reptiles

For the birds, since we have just chosen the hawk and the raven we have to compute the number of
ways of we can choose 1 birds from the remaining birds (8 - hawk - raven = 6)

    Combination (6, 1) = 6! / ( 1! * (6-1)! ) = 6  --> Birds

So the total number of exhibits that include the hawk and the raven is:

    Reptiles * Birds = 20 * 6 = 120  -> H&R

At the end, the number of exhibits where the hawk and the raven are not together is:

    TOT - H&R = 1120 - 120 = 1000

## c

The problem is similar to the previous one.

The cobra and the parrot cannot coexist in the same exhibit.

So we are going to compute the case where they are chosen together and then we subtract this number from the total number of exhibits.

For the birds, since we have just chosen the parrot, we have to compute the number of ways of we
can choose the 2 birds from the remaining birds (8 - parrot = 7)

   Combination (7, 2) = 7! / ( 2! * (7-2)! ) = 21  --> Birds

For the reptiles, since we have just chosen the cobra, we have to compute the number of ways of we
can choose the 2 reptiles from the remaining reptiles (6 - cobra = 5)

   Combination (5, 2) = 5! / ( 2! * (5-2)! ) = 10  --> Reptiles

So the total number of exhibits that include the cobra and the parrot is:

    Reptiles * Birds = 21 * 10 = 210  -> C&P

At the end, the number of exhibits where the hawk and the raven are not together is:

    TOT - C&P = 1120 - 210 = 910

----------------------------------------------------------------------------------------------------

# The Investments of Baker Street

We have 20 million to distribute for 4 enterprises.

1. Min (1 Million)

2. Min (2 Million)

3. Min (3 Million)

4. Min (4 Million)

## a

Invest in all enterprises means that i have to give the minimum request by them at the start.

    So i have to give 1M + 2M + 3M + 4M = 10M.

    Now my balance is 20M - 10M = 10M

To compute all the possible strategies i have to use the Combination with repetitions.

    Combination (Balance + N enterprises -1, enterprises -1) = (10 + 4 -1, 4 - 1) = (13, 3)
    = 13! / ( 3! * (13-3)! ) = 286

## b

Invest in at least 3 of them means that i have to choose 1 enterprises to remove.

    I have literally 4 possibilities

Since i want anyway to invest in all of them (3) i have to compute all the possible cases:

    Remove Enterprise 1

    Balance = 20M - (2M + 3M + 4M) = 11M

Now we compute the possible ways to distribute the balance among the 3 enterprises:

    Combination (Balance + N enterprises -1, enterprises -1) = (11 + 3 -1, 3-1) = (13, 2)
    = 13! / (2! * (13-2)! ) = 78 --> E1

    Remove Enterprise 2

    Balance = 20M - (1M + 3M + 4M) = 12M

Now we compute the possible ways to distribute the balance among the 3 enterprises:

    Combination (Balance + N enterprises -1, enterprises -1) = (12 + 3 -1, 3-1) = (14, 2)
    = 14! / ( 2! * (14-2)! ) = 91 --> E2

    Remove Enterprise 3

    Balance = 20M - (1M + 2M + 4M) = 13M

Now we compute the possible ways to distribute the balance among the 3 enterprises:

    Combination (Balance + N enterprises -1, enterprises -1) = (13 + 3 -1, 3-1) = (15, 2)
    = 15! / ( 2! * (15-2)! ) = 105 --> E3

    Remove Enterprise 4

    Balance = 20M - (1M + 2M + 3M) = 14M

Now we compute the possible ways to distribute the balance among the 3 enterprises:

    Combination (Balance + N enterprises -1, enterprises -1) = (14 + 3 -1, 3-1) = (16, 2)
    = 16! / ( 2! * (16-2)! ) = 120 --> E4

At the end i think that we have just to sum all these results to compute the total ways to
distribute the entire balance among the 3 enterprises:

    TOT = E1 + E2 + E3 + E4 = 78 + 91 + 105 + 120 = 394

----------------------------------------------------------------------------------------------------

# The Coding Conundrum of Scotland Yard

100 agents --> TOT

27 Java | 28 C++ | 20 Python

12 Java && C++ | 5 Java && Python | 8 C++ && Python

2 Java && C++ && Python

## a

To compute the probability of selecting a random agent that evade all courses we have to do:

    Chance that X evade = Agents that evade all courses / Tot Agents

To find the number of agents that evade all courses we have to compute before the number of agents
that follow at least one course:

    27 + 28 + 20 = 75  --> Sum of the agents that follow a single course

    75 - ( 12 + 5 + 8 ) = 50 --> Subtract the agents that follow 2 courses because we have count it in the previous step (ex: Java && Python) (intersection)

    50 + 2 = 52 --> Add the agents that follow all the courses beacuse they have been removed in the previous step (Agents that follow at least one course)

    Agents evading all courses = TOT - Agents that follow at least one course = 100 - 52 = 48

    Chance that X evade = 48 / 100 = 0,48% 

## b

To find the chance that an agent X follow exactly one course we have to find the number of agents
that study exactly one course and divide it for the total.

Agents that follow only Java:

    27 - 12 - 5 + 2 = 12  --> Java

Agents that follow only C++:

    28 - 12 - 8 + 2 = 10  --> C++

Agents that follow only Python:

    20 - 5 - 8 + 2 = 9  --> Python

Agents that follow only 1 course are:

    Java + C++ + Python = 12 + 10 + 9 = 31  -> Agents1Course

Chance that an agent X follow exactly one course is:

   Agents1Course / TOT = 31 / 100 = 0,31% 

## c

The probability that an agent X doesn't follow any course is : 0,48%

So for 2 agents is:

    0,48 * 0,48 = 0,23

At the end the probability that given 2 random agents, at least one of them follow one course is:

    1 - Prob. that 2 agents doesn't follow any course = 1 - 0,23 = 0,76 = 76%

----------------------------------------------------------------------------------------------------

# The Passwords of the Naval Treaty

N distinct passwords

## a

WITH DISCARDING

The chance to guess the right password at the k-th attempt is:

    1 / N

The probability is always the same for all the attempts

## b

WITHOUT DISCARDING

We have basically to compute the probability of fail for the first k-1 attempts and to find the
right password at the k-th attempt.

Fail for the first k-1:

    ( (N - 1) / N )^k-1

    where: ( N - 1 ) / N is the probability to fail

    where: k -1 is for how many times we have to repeat the probability to fail

Guess the right password at the k-th attempt:

    1 / N

So for compute the probability to success at the k-th attempt without discarding is:

    ( (N - 1) / N )^k-1 * (1 / N)

We have to compute it like that since each attempt is indipendent with respect to the others
    
----------------------------------------------------------------------------------------------------

# The Dice of the Speckled Band

## a

We have 2 dice (6 faces each)

1 dice : 1, 2, 3, 4, 5, 6
2 dice : 1, 2, 3, 4, 5, 6

We roll the dice 6 times and we have to select 2 numbers that must appear 3 times each.

1 number: X
2 number: Y

So to decide the 2 numbers that will be appear exactly 3 times each we have to compute:

Combination (6, 2): 6*5*4*3*2*1 / 2 * (6-2) = 15

At this point we need to understand wich 3 of the 6 rolls will output the first number (X)
and wich the second (Y); for doing that we compute the combination of 3 on 6:

Combination (6, 3) = 20

Now we can compute the number of right output:

15 * 20 = 300

This value must be divided for the total number of possible combinations from rolling effectively a dice 6 times.

So the probability of rolling two numbers that each appear exactly three times is:

300 / Tot

where Tot = 6*6*6*6*6*6 = 6^6 = 46.656

so: 300 / 46.656 = 0,0064

## b

In this case we have just 1 number that must be extracted exactly 3 times.
So similar as above we have to compute the combination of choose 1 number on 6 possibilities.

    Combination (6, 1) = 6

At this point we need to understand which 3 of the 6 rolls will output the chosen number.

So we make the similar process as above:

    Combination (6, 3) = 20

BUT, we have to take into account that the other launches has not to extract the chosen number.

So we compute the combination of 5 possible number on 3 dice rolls

    Combination (5, 3) = 10

We have to assign the remaining numbers to the remaining rolls

    3! = 6

Now we can compute the number of right output:

    Combination (6, 1) * Combination (6, 3) * Combination (5, 3) * 3! = 7200

So the probability of rolling one number that appear exactly 3 times, no more, no less is:

    7200 / Tot

Where Tot is the same as above, so:

    Tot = 6^6 = 46.656

    Output: 7200 / 46.656 = 0.15

----------------------------------------------------------------------------------------------------

# The Letters of the Red-Headed League

20 DISTINCT letters

12 unique informants

    X X X X X X X X X X X X

    -------                     4 of them get exactly 2 letters
           ------               3 of them get exactly 4 letters
                 ----------     5 of them get 0 letters

First we compute the possible ways to distribute the letters among the informants, so:

For the 4 of them that get 2 letters:

    Combination(12, 4) = 12! / ( 4! * (12-4)! ) = 495 --> From 12 informants we choose 4 --> A

For the 4 of them that get 2 letters:

    Combination(8, 3) = 8! / ( 3! * (8-3)! ) = 56 --> From the remaining informants (8) we choose 3  --> B

For the remaining informants we have just 1 way to assign 0 letters each

    1

Now we have to distribute the letters among the 12 informants, so we can compute:

    Combination(20,2) * Combination(18, 2) * Combination(16,2) * Combination(14, 2) *

    Combination(12, 4) * Combination(8, 4) * Combination(4,4)  --> C

To find the total favorable ways to distribute the letters is given by:

    A * B * C = Combination(12,4) * Combination(8, 3) * 

    Combination(20,2) * Combination(18, 2) * Combination(16,2) * Combination(14, 2) *

    Combination(12, 4) * Combination(8, 4) * Combination(4,4)  --> Output

To get the probability we have to divide the outcome for the total numbers of possible distributions:

   Output / 12^20 = ? 

----------------------------------------------------------------------------------------------------

# The Buckets of Bohemia

M clues

N buckets

N^M outcomes are equal

The probability that a clue is hashed into a bucket is:

    P = 1 / N

If X is the number of clues that are going to be hashed in the first bucket:

    X = Bin(M, P)  -> X = Bin(M, 1/N)

So to compute the probability that K clues will be hashed in the first bucket we have to use a binomial distribution:

    P(X=K) = (M, K) * (1/N)^K * (1 - (1/N))^M-K

----------------------------------------------------------------------------------------------------

# Coding - The game of the final problem

I decided to create a simple, sequential, and understandable code without functions that allows the solution to the problem.

To run the code, you only need to have Python installed since no external libraries are used.
Simply open the terminal in the Git repository and run the following command:

    $ python excercise.py
    OR
    $ python3 excercise.py

This depends on the installed version of Python.
My suggestion is to install Python 3 if it's not already present.

    import random

    #variable that count how many times Moriarty wins
    win_moriarty = 0

    #total number of rounds
    tot = 100000

    for _ in range(tot):

        #variable for the sum
        s = 0

        while s <=100:

            holmes = random.randint(1,100) #generate random number
            s = s + holmes #add the random number generated to 's'

        while s <=200:

            moriarty = random.randint(1,100) #generate random number
            s = s + moriarty #add the random number generated to 's'

        if(moriarty > holmes):

            win_moriarty = win_moriarty + 1 #count how many times Moriarty wins

    probability_moriarty_wins = win_moriarty/100000
    probability_moriarty_wins = probability_moriarty_wins * 100

    print(f'The probability of moriarty winning is {probability_moriarty_wins}%')

----------------------------------------------------------------------------------------------------
