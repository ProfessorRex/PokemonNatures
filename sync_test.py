import concurrent.futures

# SYNC TEST

#ShTID = TID XOR SID
#ShPID = PID1 XOR PID2

def Output_ShTID_vs_ShPID():
        results = read_ShTID_results()
        f = open("ShTID_Full_Results.txt", "a")
        for i in range(0, 65536):
                curr = results[i]
                f.write("Shiny TID: " + str(i) +"\n")
                f.write("Shiny PIDs: " + str(sum(curr[:-1])) + "\n")
                f.write(get_delta(curr[:-1]))
                f.write(str(curr[:-1]))
                f.write("\n\n")
        print("DONE")

def find_big():
        results = read_ShTID_results()
        for result in results:
                if max(result[:-1]) > 22000:
                        print(max(result[:-1]))
                        print(result)

def get_delta(ShTID_results):
    lst = []
    for tup in ShTID_results:
        lst.append(tup)
    mini = min(lst) if min(lst) > 0 else 0.1
    maxi = max(lst) if max(lst) > 0 else 0.1
    num_result = str((1-(20_971.52/maxi)) * 100)
    num_result = (num_result[:6]) if len(num_result) > 6 else num_result
    result = "Min Nature: " + str(min(lst)) + "\nMax Nature: " + str(max(lst)) + "\nDelta: " + num_result + "%\n"
    return result

#def test_ShTID(ShTID, mini=0):
    ## Returns a breakdown of how many shinys are available to a TID/SID by nature
    #with concurrent.futures.ProcessPoolExecutor() as executor:
        #futures = []
        #results = []
        #for x in range(mini, 25):
            #future = executor.submit(test_ShTID_nature, ShTID, x)
            #futures.append(future)
        #for f in concurrent.futures.as_completed(futures):
            #results += [f.result()]
    #return results


#def test_ShTID_nature(ShTID, nature):
    ## Tests all possible PIDS that match a specific nature
    ##returns the total number of found shinys
    #shinys = 0
    #i = nature
    #while i < 4_294_967_296:
        #if is_shiny (ShTID, i):
            #shinys += 1
        #i += 25
    #return (nature, shinys)


# Make tool for shiny checking
#def is_shiny(ShTID, PID):
    #PID1 = int(PID/65536)
    #PID2 = PID % 65536
    #return (ShTID ^ PID1 ^ PID2) < 8
    
def test_ShTID_vs_ShPID():
    ShPID_natures = read_ShPID_results()
    natures_by_ShTID = []
    # Get results for each ShTID
    for ShTID in range(0, 65_536):
        natures_by_ShTID.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ShTID])
        for ShPID in range(0, 65_536):
            if is_shiny(ShTID, ShPID):
                curr = natures_by_ShTID[ShTID]
                for i in range(0, 25):
                    curr[i] += ShPID_natures[ShPID][i]
                natures_by_ShTID[ShTID] = curr
        print(curr)
    return natures_by_ShTID

# Make tool for shiny checking (Using ShTID and ShPID)
def is_shiny(ShTID, ShPID):
    return (ShTID ^ ShPID) < 8


def ShPID_nature_spreads():
    ''' Used to generate a list of the nature spreads for each ShPID '''
    lst = []
    for i in range(0,65536):
        lst.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, i])
    for PID in range(0, 4_294_967_296):
        PID1 = int(PID/65536)
        PID2 = PID % 65536
        nature = PID % 25
        ShPID = PID1 ^ PID2
        lst[ShPID][nature] += 1
    return lst

def get_ShPID_results():
    results = ShPID_nature_spreads()
    f = open("ShPID.txt", "a")
    for result in results:
        f.write(str(result)+"\n")
    f.close()
    print("DONE")

def get_ShTID_vs_results():
    results = test_ShTID_vs_ShPID()
    f = open("ShTID.txt", "a")
    for result in results:
        f.write(str(result)+"\n")
    f.close()
    print("DONE")

def read_ShPID_results():
    f = open("ShPID.txt", "r")
    lines = f.readlines()
    # Strips the newline character
    lines_stripped = []
    for line in lines:
        curr = list(line.strip().strip('][').split(', '))
        curr = [ int(x) for x in curr]
        lines_stripped.append(curr)
    return lines_stripped

def read_ShTID_results():
    f = open("ShTID.txt", "r")
    lines = f.readlines()
    # Strips the newline character
    lines_stripped = []
    for line in lines:
        curr = list(line.strip().strip('][').split(', '))
        curr = [ int(x) for x in curr]
        lines_stripped.append(curr)
    return lines_stripped

def sum_lst_of_lists(lst):
    x = 0
    for curr in lst:
        x += sum(curr[:-1])
    return x

if __name__ == "__main__":
        #get_ShTID_vs_results()
        pass