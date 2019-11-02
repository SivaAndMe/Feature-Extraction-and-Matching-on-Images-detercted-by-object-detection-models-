import operator,csv

# CALCULATE SUM OF ABSOLUTE DIFFERENCE b/w two strings(rows are passed as strings)
def sad_dist(str1,str2):
    sum_abs = 0
    for i in range(2048):
        a = int(str1[i])
        b = int(str2[i])
        sum_abs+=abs(a-b)
    return sum_abs

#read csv which contains the feature vectors
file = open('brief.csv','r') # OPEN THE CSV WITH FEATURES
csvreader = csv.reader(file)
# To write the nearer neighbour image names of a given image
csvfile = open('final.csv','w')
writer = csv.writer(csvfile)
#Headers
writer.writerow(['Image','Match-1','Match-2','Match-3','Match-4','Match-5'])

for query_image_num in range(1,4):#number of query images #here iterating through all images
    num_of_best_matches = 3#can change this
    n_rows = int(len(list(csvreader))/2);# TOTAL NUMBER OF IMAGES

    file.seek(0)# to undone the conversion into list
    query_image_row_num=query_image_num-1 #lite

    # iterate to the query row
    iterate = (query_image_num)*2# for the sake of iteration to query row to collect feature data

    # find the query image  row and it's name
    for i in range(iterate):
        qrow=next(csvreader)
        if(i==iterate-2):
            query_image_name = qrow[0][2:]

    # keys : image names & Values :SUM of absolute differences with other images
    best_match_dict = {}

    file.seek(0) #Undone the previous iteration

    for i in range(n_rows):
        row = next(csvreader)
        image_name = row[0]
        row = next(csvreader)
        sum_abs_dif = sad_dist(qrow,row)
        best_match_dict[image_name] = sum_abs_dif

    x = best_match_dict
    # sort the dictionary based on the values
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    # sorted_x is a list of tuples with each element as a string i.e.,[('img1','12'),('img2','20'),.....]
    # contains first n-best matches of a given image
    best_list=[]
    for k in range(num_of_best_matches):
        print(sorted_x[k][0][2:])
        # dont add the image itself to the  best_list
        if(sorted_x[k][0][2:]!=query_image_name):
            best_list.append(sorted_x[k][0][2:])
    print("------><-------")
    best_list.insert(0,query_image_name)
    # with open('final.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(best_list)
    file.seek(0)# undone iteration for next FOR loop
