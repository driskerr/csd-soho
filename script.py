from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
food_categories = Trie()
for type in types:
  food_categories.insert(type)


#Write code to insert restaurant data into a data structure here. The data is in data.py
restaurant_directory = HashMap(len(types))
for type in types:
  restaurant_directory.assign(type, LinkedList())
  
for i in restaurant_data:
  business_hash = HashMap(len(i)-1)
  business_hash.assign('name',i[1])
  business_hash.assign('price',i[2])
  business_hash.assign('rating',i[3])
  business_hash.assign('address',i[4])
  restaurant_directory.retrieve(i[0]).insert_beginning(business_hash)

#print(restaurant_directory.array)


      
#Write code for user interaction here
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    #Search for user_input in food types data structure here
    results = food_categories.search(user_input)
    if len(results) > 1:
      print("\nWith those beginning letters, your choices are {}".format(sorted(results)))
    elif len(results) == 0:
      print("No categories begin with '{}'. Please try again.".format(user_input))
    elif len(results) == 1:
      while True:
      	user_input2 = str(input("\nThe only option with those beginning letter is {0} Do you want to look at {0} restuarants? Enter 'y' for yes and 'n' for no.\n".format(results[0].capitalize()))).lower()
      
      	#After finding food type write code for retrieving restaurant data here
      	if user_input2 == 'n':
        	break
      	elif user_input2 == 'y':
          category_list = restaurant_directory.retrieve(results[0])
          current_node = category_list.get_head_node()
          while current_node.get_value() is not None:
            print("------------------")
            print("Name: {}".format(current_node.get_value().retrieve('name')))
            print("Price: {}/5".format(current_node.get_value().retrieve('price')))
            print("Rating: {}/5".format(current_node.get_value().retrieve('rating')))
            print("Address: {}".format(current_node.get_value().retrieve('address')))
            current_node = current_node.get_next_node()
          user_input3 = str(input("\nDo you want to find other restaurants? Enter 'y' for yes and 'n' for no.\n")).lower()
          if user_input3 == 'y':
            break
          else:
            quit()
      	else:
        	print("Please enter a valid response: 'y' or 'n'.")

    
