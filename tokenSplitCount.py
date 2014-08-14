inString = "What ECE ECE in a b c d aa bb cc dd a   ECE"
def tokenSplitCount(queryString):
    tokens = queryString.split()
    tokens.sort()
    queryList = []
    for index in range(len(tokens)):
        if (index == 0):
            queryList.append(tokens[index])
        elif (tokens[index-1] != tokens[index]):
            queryList.append(tokens[index])
    print "The submitted query contains "+str(len(tokens)) + " words"
    for token in queryList:
        print token + ' ' + str(queryString.count(token))
tokenSplitCount(inString)
