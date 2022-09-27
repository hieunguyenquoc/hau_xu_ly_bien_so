from Replacer import replacer
def xe_quan_doi(bien_so):
    print("Xe quan doi vao day")
    bien_so_co_dinh = bien_so
    print("Bien so truoc chinh sua :",bien_so_co_dinh)
    if len(bien_so) < 6:
        return bien_so
    else: 
        for i in range(2,6):
            if bien_so[i] == "l" or bien_so[i] == "L":
                bien_so = replacer(bien_so,"1",i)
            if bien_so[i] == "Z":
                bien_so = replacer(bien_so,"2",i)
            if bien_so[i] == "b":
                bien_so = replacer(bien_so,"6",i)
            if bien_so[i] == "B":
                bien_so = replacer(bien_so,"8",i)
            if bien_so[i] == "q":
                bien_so = replacer(bien_so,"9",i)
            if bien_so[i] == "O":
                bien_so = replacer(bien_so,"0",i)   
        try:
            int(bien_so[2:])     
            print("Bien so sau khi chinh sua :",bien_so)
            return bien_so 
        except ValueError:
            print("Khong the sua bien so :",bien_so_co_dinh)
            return bien_so_co_dinh