# --------------
#Code starts here

#Function to read file
def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close()
    return sentence

#call the function to read file
sample_message = read_file(file_path)

#Print the line
print(sample_message)

#Function to fuse message
def fuse_msg(message_a, message_b):

    #Integer division
    quot=(int(message_b)//int(message_a))

    #Return Quotient in String
    return str(quot)

#Call function to read file
message_1 = read_file(file_path_1)
print(message_1)

#Call function to read file
message_2 = read_file(file_path_2)

#Call function fuse_msg
secret_msg_1 = fuse_msg(message_1, message_2)
print(secret_msg_1)

#Function to substitute the message
def substitute_msg(message_c):

    #ifelse to compare
    if message_c=='Red':
        sub = 'Army General'
    elif message_c=='Green':
        sub = 'Data Scientist'
    elif message_c=='Blue':
        sub = 'Marine Biologist'

    #Return substitute 
    return sub

#Call to read file
message_3 = read_file(file_path_3)

#Call substitute_msg
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)

#Function to compare
def compare_msg(message_d, message_e):

    #Splitting message to List
    a_list = message_d.split()

    #Splitting message to List
    b_list = message_e.split()

    #Compare elements of both lists
    c_list = [i for i in a_list if i not in b_list]

    #Combining the words
    final_msg = ' '.join(c_list)

    #Return Sentence
    return final_msg

#Call to read file
message_4 = read_file(file_path_4)

#Call to read file
message_5 = read_file(file_path_5)

#Call compare_msg
secret_msg_3 = compare_msg(message_4, message_5)
print(secret_msg_3)

#Function to filter
def extract_msg(message_f):

    #Splitting message to List
    a_list = message_f.split()

    #Create Lambda function to identify even lenght
    even_word = lambda x: (len(x)%2==0)

    #Splitting the messsage
    b_list = (filter(even_word, a_list))

    #Combining Words
    final_msg = ' '.join(b_list)

    #Return sentence
    return final_msg

#Call to read file
message_6 = read_file(file_path_6)

#Call filter_msg
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)

#Secret Mgs in correct order
message_parts = [secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path = user_data_dir + '/secret_msg.txt'

#Cobining secret msg part
secret_msg = ' '.join(message_parts)

#Function to write inside file
def write_file(secret_msg, path):

    #Open secret_message
    file = open(path, 'a+')

    #Write to file
    file.write(secret_msg)

    #close file
    file.close()

#Calling function to write
write_file(secret_msg, final_path)

#Print entire secret message
print(secret_msg)

#Code Ends Here


