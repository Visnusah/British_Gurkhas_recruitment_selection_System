def get_splitted_name(fullname):
    splitted_name = fullname.split()
    if len(splitted_name) == 1:
        f= splitted_name[0]
        m,l = "",""
    elif len(splitted_name) == 2:
        f= splitted_name[0]
        l= splitted_name[1]
        m=""
    elif len(splitted_name) == 3:
        f= splitted_name[0]
        m= splitted_name[1]
        l= splitted_name[2]
    else:
        f,m,l="","",""
    return [f,m,l]