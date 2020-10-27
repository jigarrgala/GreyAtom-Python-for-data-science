# --------------
class_1 = ['Geoffrey', 'Hinton', 'Carla Gentry', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corina Cortes']

#Concatenate both Class
new_class = (class_1 + class_2)

#Print the new class
print(new_class)

#Add new element
new_class.append('Peter Warden')

print(new_class)

#create dictionary
courses = {'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}

#add marks
total = (courses['Math']+courses['English']+courses['History']+courses['French']+courses['Science'])
print(total)

#calculate percentage
percentage = ((total/500)*100)
print(percentage)

#create dictionary mathematics
mathematics = {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}

#Calculate max value
topper = max(mathematics,key = mathematics.get)
print(topper)

#print topper name
first_name = topper.split()[0]
last_name = topper.split()[1]
print(first_name)
print(last_name)

#full name
full_name = (str(last_name) + ' ' + str(first_name))

certificate_name = full_name.upper()
print(certificate_name)


