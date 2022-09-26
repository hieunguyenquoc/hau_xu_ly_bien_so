ma_tinh = ["11", "12", "14", "15", "16", "17", "18", "19", "20", "21", "22", 
           "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", 
           "40", "34", "35", "36", "37", "38", "43", "47", "48", "49", "41", 
           "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "39", 
           "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", 
           "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", 
           "82", "83", "84", "85", "86", "88", "89", "90", "92", "93", "94", 
           "95", "97", "98", "99"]
seri_dang_ky_chu = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# seri_dang_ky_so = ["1","2","3","4","5","6","7","8","9"]
xe_dac_biet = ["LD","DA","MK","TĐ","HC"]
ma_nuoc_ngoai = ["NG","NN"]
bien_so_nuoc_ngoai = ["011", "026", "041", "061", "066", 
                      "121", "156", "166", "191", "206", 
                      "296", "297", "301", "331", "336", 
                      "346", "364", "376", "381", "441", 
                      "446", "456", "501", "506", "521", 
                      "546", "547", "548", "549", "566", 
                      "581", "601", "606", "626", "631", 
                      "636", "691", "731", "888"]
quan_doi = ["TM", "TC", "TH", "TT", "TK", "TN", "KA", "KB", "KC", "KD", "KV", 
            "KP", "KK", "KT", "AA", "AB", "AC", "AD", "QA", "QH", "QB", "QC", 
            "QM", "BL", "BB", "BC", "BK", "BP", "BH", "BT", "HA", "HB", "HC", 
            "HE", "HD", "HH", "HT", "HQ", "HN", "PA", "PG", "PK", "PQ", "PM", 
            "PX", "PP-10", "PP-40", "PP-60", "AV", "AT", "AN", "AX", "AM", "VT", 
            "CA", "CB", "CD", "CH", "CK", "CM", "CN", "CP", "CT", "CV"]
input = "30NG88801"

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def xe_ca_nhan_co_quan_nha_nuoc(bien_so):
    bien_so_co_dinh = bien_so
    print("Bien so truoc chinh sua :",bien_so_co_dinh)
    if (len(bien_so) < 7) or (len(bien_so) > 9):
        return bien_so
    else:
        if bien_so[2:4] in xe_dac_biet:

            for i in range(0,2):
                if bien_so[i] == "l":
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
            if bien_so[0:2] not in ma_tinh:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
            else:
                if len(bien_so[4:]) == 4:
                    for i in range(4,8):
                        if bien_so[i] == "l":
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
                        int(bien_so[4:])
                        print("Bien so sau khi chinh sua :",bien_so)
                        return bien_so
                    except ValueError as ve:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh

                elif len(bien_so[4:]) == 5:
                    for i in range(4,9):
                        if bien_so[i] == "l":
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
                        int(bien_so[4:])
                        print("Bien so sau khi chinh sua :",bien_so)
                        return bien_so
                    except ValueError as ve:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh    

        elif bien_so[4:] == 4:
            for i in range(4,8):
                if bien_so[i] == "l":
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
                int(bien_so[4:])
                print("Bien so sau khi chinh sua :",bien_so)
                return bien_so
            except ValueError as ve:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
                
        elif bien_so[4:] == 5:
            for i in range(4,9):
                if bien_so[i] == "l":
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
                int(bien_so[4:])
                print("Bien so sau khi chinh sua :",bien_so)
                return bien_so
            except ValueError as ve:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
        else:
            if len(bien_so[3:]) == 4:
                for i in range(0,2):
                    if bien_so[i] == "l":
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
                if bien_so[0:2] not in ma_tinh:
                    print("Khong the sua bien so :",bien_so_co_dinh)
                    return bien_so_co_dinh
                else:
                    if bien_so[2] == "2":
                        bien_so = replacer(bien_so,"Z",2)
                    if bien_so[2] == "8":
                        bien_so = replacer(bien_so,"B",2)
                    if bien_so[2] not in seri_dang_ky_chu:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh
                    else:
                        for i in range(3,7):
                            if bien_so[i] == "l":
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
                            int(bien_so[3:])
                            print("Bien so sau khi chinh sua :",bien_so)
                            return bien_so
                        except ValueError as ve:
                            print("Khong the sua bien so :",bien_so_co_dinh)
                            return bien_so_co_dinh
                        
            elif len(bien_so[3:]) == 5:
                for i in range(0,2):
                    if bien_so[i] == "l":
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
                if bien_so[0:2] not in ma_tinh:
                    print("Khong the sua bien so :",bien_so_co_dinh)
                    return bien_so_co_dinh
                else:
                    if bien_so[2] == "2":
                        bien_so = replacer(bien_so,"Z",2)
                    if bien_so[2] == "8":
                        bien_so = replacer(bien_so,"B",2)
                    if bien_so[2] not in seri_dang_ky_chu:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh
                    else:
                        for i in range(3,8):
                            if bien_so[i] == "l":
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
                            int(bien_so[3:])
                            print("Bien so sau khi chinh sua :",bien_so)
                            return bien_so
                        except ValueError as ve:
                            print("Khong the sua bien so :",bien_so_co_dinh)
                            return bien_so_co_dinh

def xe_nuoc_ngoai(bien_so):
    bien_so_co_dinh = bien_so
    print("Bien so truoc chinh sua :",bien_so_co_dinh)
    if bien_so[2:4] in ma_nuoc_ngoai:
        for i in range(0,2):
            if bien_so[i] == "l":
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
        if bien_so[0:2] not in ma_tinh:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
        else:
            for i in range(4,9):
                if bien_so[i] == "l":
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
                int(bien_so[4:])
                print("Bien so sau khi chinh sua :",bien_so)
                return bien_so
            except ValueError as ve:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh

    elif bien_so[5:7] in ma_nuoc_ngoai:
        for i in range(0,2):
            if bien_so[i] == "l":
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
        if bien_so[0:2] not in ma_tinh:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
        else:
            for i in range(2,5):
                if bien_so[i] == "l":
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
                int(bien_so[2:5])
                
            except ValueError:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
                
            else:
                for i in range(7,9):
                    if bien_so[i] == "l":
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
                    int(bien_so[7:])
                    print("Bien so sau khi chinh sua :",bien_so)
                    return bien_so
                except ValueError as ve:
                    print("Khong the sua bien so :",bien_so_co_dinh)
                    return bien_so_co_dinh
                
def xe_quan_doi(bien_so):
    bien_so_co_dinh = bien_so
    print("Bien so truoc chinh sua :",bien_so_co_dinh)
    if len(bien_so) < 6:
        return bien_so
    else: 
        for i in range(2,6):
            if bien_so[i] == "l":
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

if __name__ == "__main__":
    if (input[0:2] in quan_doi) and (len(input)==6):
        xe_quan_doi(input)
    elif ((input[2:4] in ma_nuoc_ngoai) or (input[5:7] in ma_nuoc_ngoai)) and (len(input)==9):
        xe_nuoc_ngoai(input)
    else:
        xe_ca_nhan_co_quan_nha_nuoc(input)

    
