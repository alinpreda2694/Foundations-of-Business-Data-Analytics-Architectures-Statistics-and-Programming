f = open('/home/aleen/Downloads/voting_record_dump109-1.txt')
my_list = list(f)
f.close()

##### 1 #####
def create_voting_dict(str_list):
    """Returns a disctionary that maps the last name of a senator to a list of votes."""
    voting_dict = {}
    for str in str_list:
        votes_list = []
        s = str.replace('\n','')
        for i in s.split(' ')[3:]:
            x = int(i)
            votes_list.append(x)
            voting_dict[s.split(' ')[0]] = votes_list
    return voting_dict

voting_dict = create_voting_dict(my_list)
##### 2 #####
def policy_compare(sen_a, sen_b, voting_dict):
    """Returns the dot product representing the degree of similarity between two senator's voting policies."""
    dot_product = 0
    for i in range(0, len(voting_dict[sen_a])):
        dot_product += voting_dict[sen_a][i] * voting_dict[sen_b][i]
    return dot_product

sen_a = "Akaka"
sen_b = "Kennedy"
print(policy_compare(sen_a, sen_b, voting_dict))
##### 3 #####
def most_similar(sen, voting_dict):
    """Returns the name of the senator whose political mindset is most like the input senator, excluding, of course, the input senator"""
    max = 0
    #del voting_dict[sen]
    for comp_sen in voting_dict.keys():
        if comp_sen != sen:
            dot_product = policy_compare(sen, comp_sen, voting_dict)
            if dot_product > max:
                max = dot_product
                most_similar = comp_sen
    return most_similar + ' is the most similar to ' + sen + ' with a degree of ' + str(max) + '.'

print(most_similar("Akaka", voting_dict))
print(most_similar("Alexander", voting_dict))
print(most_similar("Sununu", voting_dict))
print('\n')
##### 4 #####
def least_similar(sen, voting_dict):
    """Returns the name of the senator whose voting record agrees the least with the input senator sen's political views."""
    min = 9999
    #del voting_dict[sen]
    for comp_sen in voting_dict.keys():
        if comp_sen != sen:
            dot_product = policy_compare(sen, comp_sen, voting_dict)
            if dot_product < min:
                min = dot_product
                most_similar = comp_sen
    return most_similar + ' is the least similar to ' + sen + ' with a degree of ' + str(min) + '.'
print(least_similar("Akaka", voting_dict))
print(least_similar("Kennedy", voting_dict))
print(least_similar("Sununu", voting_dict))
##### 5: OBAMA #####
print('\n')
print(most_similar("Obama", voting_dict))
print(least_similar("Obama", voting_dict))
##### 6 #####
print('\n')
sen_set = ["McCain", "Gregg", "Salazar", "Biden", "Clinton"]
def find_average_similarity(sen, sen_set, voting_dict):
    """Given the name of a senator, compares his/her voting record to the voting records of all senators whose names are in sen_set, computing
    a dot product for each, and then returns the average dot product. """
    sum = 0
    for s in sen_set:
        sum += policy_compare(sen, s, voting_dict)
    avg = sum / len(sen_set)
    return avg
print(find_average_similarity("Obama", sen_set, voting_dict))
print(find_average_similarity("Kennedy", sen_set, voting_dict))
#############################################
#############################################
#############################################
a = [1,2,3,4]
b = [5,6,7,8]
def dot_product(a,b):
    dot_product = 0
    for i in range(0,len(a)):
        dot_product += a[i] * b[i]
    return dot_product
print(dot_product(a,b))
print(dot_product(b,a))
#############################################
#############################################
#############################################
print('\n')
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[8,4,7],[12,14,6],[1,2,1]]
c = [7,19,4]
def vector_scalar_multiplication(num,vector):
    result_vector = []
    for i in range(0, len(vector)):
        result_vector.append(num * vector[i])
    return result_vector
vector_scalar_multiplication(2,c)

def vector_addition(v1,v2):
    result_vector = []
    for i in range(0,len(v1)):
        result_vector.append(v1[i] + v2[i])
    return result_vector
vector_addition(c,[1,2,3])

# def vector_matrix_product(vector,matrix):
#     resulting_matrix = []
#     resulting_vector = []
#     temp = []
#     if len(vector) == len(matrix):
#         for i in range(0,len(vector)):
#             resulting_matrix.append(vector_scalar_multiplication(vector[i], matrix[i]))
#     else:
#         print("Error. Illegal matrix operation.")
#     for i in range(0,len(matrix[0])):
#         resulting_vector.append
#     for i in range(0,len(resulting_matrix)-1):
#         temp.append(vector_addition(resulting_matrix[i], resulting_matrix[i+1]))
#     return resulting_vector
# print(vector_matrix_product(c,A))
# print(vector_matrix_product([3,4],[[1,2,3],[10,20,30]]))
