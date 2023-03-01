#!/bin/sh

echo "Enter the number you want to add:"
read number

# Loop over each line in the file
while read line; do
  # Prepend the desired number to the beginning of the line
  new_line="${number}${line}"
  # Output the modified line
  echo "$new_line"
done < "telefoonnummers.txt"