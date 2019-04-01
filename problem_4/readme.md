From the program “The Health” Anya learned that it is recommended to sleep at least A hours a day, but to pour in is also harmful and you should not sleep more than B hours. Now Anya is sleeping H hours a day. If Ani's sleep mode satisfies the recommendations of the “Health” program, output “This is normal”. If Anya sleeps less than A hours, output “Not enough sleep”, if more than B hours, then output “Peresyp”.

The resulting number A is always less than or equal to B.

At the entrance to the program in three lines, variables are supplied in the following order: A, B, H.

Pay attention to the case of characters: the output must exactly match the one described in the task, that is, if the program should output Peresyp, the outputs of the Peresyp, Peresyp, Peresyp and others will not be considered valid.

This first is not the most trivial task for a conditional expression. In cases where the program is divided into several directions, you should carefully consider all the conditions that should be used. Particular attention should be paid to the rigor of the conditional operators used: distinguish <and ≤; > and ≥. In order to understand which one is worth using, carefully read the quest condition.

#### Sample Input 1:

6

10

8

#### Sample Output 1:

Это нормально

#### Sample Input 2:

7

9

10

#### Sample Output 2:

Пересып

Sample Input 3:

7

9

2

#### Sample Output 3:

Недосып
