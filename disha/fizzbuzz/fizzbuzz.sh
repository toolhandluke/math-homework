#!/bin/sh

sum = 0; 

for ((i=1; i<=$1; i++)); do
  echo -n $i
  if ! ((i%3)); then
    sum=$((sum + i))
    echo -n Fizz
  elif ! ((i%5)); then
    sum=$((sum + i))
    echo -n Buzz
  fi;
  echo ''
done

echo "total sum of all multiples of three and all multiples of five is $sum" 
  
