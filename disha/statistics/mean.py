import math
sum=0 
count=0
sumdeviance = 0
for line in open('randomnumbers.txt'):
  sum= sum + int(line)
  count = count +1

mean=sum/count
print ('the mean is %f' % ( sum/count) )


for line in open('randomnumbers.txt'):
  
  print ('%s deviates from the mean %d by %f' % (line, mean, (int(line) - mean)* (int(line) - mean)))
  sumdeviance=sumdeviance +(int(line) - mean)* (int(line) - mean)


print ('the mean of the deviance is %f' %(sumdeviance/count))
print ('the sqrt mean of the deviance is %f' %(math.sqrt(sumdeviance/count)))
