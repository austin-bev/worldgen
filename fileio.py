import os
def parseCsv(filename) -> list[list[str]]: 
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, filename)
    f = open(my_file, "r", encoding='utf-8-sig')

    # Initialize 2 empty lists
    s0=[]
    s1=[]
    s2=[]

    # Loop over the remaining lines
    for l in f:
        # Create a list by separating the line at commas
        d = l.split(",")
        if d[0]:
            s0.append(d[0])
        if d[1]:
            s1.append(d[1].replace("\n",""))
        if len(d) >= 3 and d[2]: #Only used for people as of now (firstname, lastname, gender)
            s2.append(d[2].replace("\n",""))
    # Close the file
    f.close()
    return s0,s1,s2