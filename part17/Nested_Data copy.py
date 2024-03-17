
# now we can  test the another question:
nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]

# Print the value associated with key 'c' in the second dictionary (90)
print(nested2[1]['c'])

# Print the value associated with key 'b' in the third dictionary
print(nested2[2]['b'])

# Add a fourth dictionary at the end of the list
nested2.append({'x': 10, 'y': 20})
print(nested2)

# Change the value associated with 'c' in the third dictionary from "yes" to "no"
nested2[2]['c'] = "jo"
print(nested2)


