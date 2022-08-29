# The orginal list
icecreams_flav = ['chocolate', 'vanilla', 'mango', 'cotton candy']

# if we uncommented this it will cause an error, because the index 4 is out of reach
# (there is no item in the list that has the index of 4)..
# we start the index count from 0 so in the list the last item has the index of 3 not 4..

#popped_item = icecreams_flav.pop(4)


popped_item = icecreams_flav.pop(3)
print(popped_item)

