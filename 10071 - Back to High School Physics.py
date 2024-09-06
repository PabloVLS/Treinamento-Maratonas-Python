#A particle has initial velocity and acceleration. If its velocity after certain time is v then what will its
#displacement be in twice of that time?
#Input
#The input will contain two integers in each line. Each line makes one set of input. These two integers
#denote the value of v (−100 ≤ v ≤ 100) and t (0 ≤ t ≤ 200) (t means at the time the particle gains
#that velocity)
#Output
#For each line of input print a single integer in one line denoting the displacement in double of that time.
#Sample Input
#0 0
#5 12
#Sample Output
#0
#120
import sys

for linha in sys.stdin:
    num1,num2= map(int, linha.split())
    resultado = (num1*num2)*2
    print(resultado)
