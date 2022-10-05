from operator import index
import pandas as pd
from re import I


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
input = input("Nhap vao bien so :")

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

def check_type_of_character(bien_so):
    count = 0
    for i in bien_so:
        if i.isnumeric() == True:
            count += 1
    return count


def xe_ca_nhan_co_quan_nha_nuoc(bien_so):
    print("Xe ca nhan, nha nuoc vao day")
    bien_so_co_dinh = bien_so
    print("Bien so truoc chinh sua :",bien_so_co_dinh)
    if (len(bien_so) < 7):
        return bien_so
    else:
        if bien_so[2:4] in xe_dac_biet:
            
            for i in range(0,2):
                if bien_so[i] == "l" or bien_so[i] == "L":
                    bien_so = replacer(bien_so,"1",i)
                if bien_so[i] == "Z" or bien_so[i] == "z":
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
                        int(bien_so[4:])
                        print("Bien so sau khi chinh sua :",bien_so)
                        return bien_so
                    except ValueError as ve:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh

                elif len(bien_so[4:]) == 5:
                    for i in range(4,9):
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
                        int(bien_so[4:])
                        print("Bien so sau khi chinh sua :",bien_so)
                        return bien_so
                    except ValueError as ve:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh    

        elif bien_so[4:] == 4:
            for i in range(4,8):
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
                int(bien_so[4:])
                print("Bien so sau khi chinh sua :",bien_so)
                return bien_so
            except ValueError as ve:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
                
        elif bien_so[4:] == 5:
            for i in range(4,9):
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
                int(bien_so[4:])
                print("Bien so sau khi chinh sua :",bien_so)
                return bien_so
            except ValueError as ve:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
        else:
            if len(bien_so[3:]) == 4:
                for i in range(0,2):
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
                            int(bien_so[3:])
                            print("Bien so sau khi chinh sua :",bien_so)
                            return bien_so
                        except ValueError as ve:
                            print("Khong the sua bien so :",bien_so_co_dinh)
                            return bien_so_co_dinh
                        
            elif len(bien_so[3:]) == 5:
                for i in range(0,2):
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
                if bien_so[0:2] not in ma_tinh:
                    print("Khong the sua bien so :",bien_so_co_dinh)
                    return bien_so_co_dinh
                else:
                    if bien_so[2] == "2":
                        bien_so = replacer(bien_so,"Z",2)
                    if bien_so[2] == "8":
                        bien_so = replacer(bien_so,"B",2)
                    if bien_so[2] == "1":
                        bien_so = replacer(bien_so,"L",2)
                    if bien_so[2] not in seri_dang_ky_chu:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh
                    else:
                        for i in range(3,8):
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
                            int(bien_so[3:])
                            print("Bien so sau khi chinh sua :",bien_so)
                            return bien_so
                        except ValueError as ve:
                            print("Khong the sua bien so :",bien_so_co_dinh)
                            return bien_so_co_dinh

def xe_nuoc_ngoai(bien_so):
    print("Xe nuoc ngoai vao day")
    bien_so_co_dinh = bien_so
    print("Bien so truoc chinh sua :",bien_so_co_dinh)
    if bien_so[2:4] in ma_nuoc_ngoai:
        for i in range(0,2):
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
        if bien_so[0:2] not in ma_tinh:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
        else:
            for i in range(4,7):
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
            if bien_so[5:7] == "11" :
                bien_so = replacer(bien_so,"0",4)
            elif bien_so[5:7] == "26" :
                bien_so = replacer(bien_so,"0",4)
            elif bien_so[5:7] == "41" :
                bien_so = replacer(bien_so,"0",4)
            elif bien_so[5:7] == "61" :
                bien_so = replacer(bien_so,"0",4)
            elif bien_so[5:7] == "66" :
                bien_so = replacer(bien_so,"0",4)
            elif bien_so[5:7] == "21" :
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[5:7] == "56" :
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[5:7] == "91" :
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[5:7] == "06" :
                bien_so = replacer(bien_so,"2",4)
            elif bien_so[5:7] == "96" :
                bien_so = replacer(bien_so,"2",4)    
            elif bien_so[5:7] == "97" :
                bien_so = replacer(bien_so,"2",4)   
            elif bien_so[5:7] == "01" :
                bien_so = replacer(bien_so,"3",4)   
            elif bien_so[5:7] == "31" :
                bien_so = replacer(bien_so,"3",4)
            elif bien_so[5:7] == "36" :
                bien_so = replacer(bien_so,"3",4)
            elif bien_so[5:7] == "46" :
                bien_so = replacer(bien_so,"3",4)
            elif bien_so[5:7] == "64" :
                bien_so = replacer(bien_so,"3",4)
            elif bien_so[5:7] == "76" :
                bien_so = replacer(bien_so,"3",4)
            elif bien_so[5:7] == "81" :
                bien_so = replacer(bien_so,"3",4)      
            elif bien_so[5:7] == "41" :
                bien_so = replacer(bien_so,"4",4)
            elif bien_so[5:7] == "47" :
                bien_so = replacer(bien_so,"5",4) 
            elif bien_so[5:7] == "48" :
                bien_so = replacer(bien_so,"5",4) 
            elif bien_so[5:7] == "49" :
                bien_so = replacer(bien_so,"5",4)  
            elif bien_so[5:7] == "81" :
                bien_so = replacer(bien_so,"5",4)   
            elif bien_so[5:7] == "91" :
                bien_so = replacer(bien_so,"6",4)  
            elif bien_so[5:7] == "88" :
                bien_so = replacer(bien_so,"8",4)      
            elif bien_so[4] == "0" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"1",5) 
            elif bien_so[4] == "0" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"2",5) 
            elif bien_so[4] == "0" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"4",5)
            elif bien_so[4] == "0" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"6",5)
            elif bien_so[4] == "1" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"2",5)
            elif bien_so[4] == "1" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"5",5)
            elif bien_so[4] == "2" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"0",5) 
            elif bien_so[4] == "2" and bien_so[6] == "7":
                bien_so = replacer(bien_so,"9",5)
            elif bien_so[4] == "3" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"0",5) 
            elif bien_so[4] == "3" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"3",5)
            elif bien_so[4] == "3" and bien_so[6] == "4":
                bien_so = replacer(bien_so,"6",5)
            elif bien_so[4] == "4" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"4",5)  
            elif bien_so[4] == "4" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"4",5)
            elif bien_so[4] == "5" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"0",5)
            elif bien_so[4] == "5" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"0",5)
            elif bien_so[4] == "5" and bien_so[6] == "7":
                bien_so = replacer(bien_so,"4",5) 
            elif bien_so[4] == "5" and bien_so[6] == "8":
                bien_so = replacer(bien_so,"4",5)
            elif bien_so[4] == "5" and bien_so[6] == "9":
                bien_so = replacer(bien_so,"4",5)
            elif bien_so[4] == "6" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"0",5)
            elif bien_so[4] == "6" and bien_so[6] == "6":
                bien_so = replacer(bien_so,"0",5)
            elif bien_so[4] == "7" and bien_so[6] == "1":
                bien_so = replacer(bien_so,"3",5)
            elif bien_so[4] == "8" and bien_so[6] == "8":
                bien_so = replacer(bien_so,"8",5) 
            elif bien_so[4:6] == "01":
                bien_so = replacer(bien_so,"1",6) 
            elif bien_so[4:6] == "02":
                bien_so = replacer(bien_so,"1",6)      
            elif bien_so[4:6] == "04":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "06":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "12":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "15":
                bien_so = replacer(bien_so,"6",6) 
            elif bien_so[4:6] == "16":
                bien_so = replacer(bien_so,"6",6)
            elif bien_so[4:6] == "19":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "20":
                bien_so = replacer(bien_so,"6",6) 
            elif bien_so[4:6] == "29":
                bien_so = replacer(bien_so,"6",6)
            elif bien_so[4:6] == "30":
                bien_so = replacer(bien_so,"1",6) 
            elif bien_so[4:6] == "33":
                bien_so = replacer(bien_so,"1",6) 
            elif bien_so[4:6] == "34":
                bien_so = replacer(bien_so,"6",6) 
            elif bien_so[4:6] == "36":
                bien_so = replacer(bien_so,"4",6)
            elif bien_so[4:6] == "37":
                bien_so = replacer(bien_so,"6",6)
            elif bien_so[4:6] == "38":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "44":
                bien_so = replacer(bien_so,"1",6)    
            elif bien_so[4:6] == "45":
                bien_so = replacer(bien_so,"6",6)
            elif bien_so[4:6] == "50":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "52":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "54":
                bien_so = replacer(bien_so,"6",6) 
            elif bien_so[4:6] == "56":
                bien_so = replacer(bien_so,"6",6) 
            elif bien_so[4:6] == "58":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "60":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "62":
                bien_so = replacer(bien_so,"6",6)
            elif bien_so[4:6] == "63":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "69":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "73":
                bien_so = replacer(bien_so,"1",6)
            elif bien_so[4:6] == "88":
                bien_so = replacer(bien_so,"8",6)
                                             
            try:
                int(bien_so[4:7])
                
            except ValueError as ve:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
            else:
                if bien_so[4:7] in bien_so_nuoc_ngoai:
                    for i in range(7,9):
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
                    
                    try :
                        int(bien_so[4:7])
                        print("Bien so sau khi chinh sua :",bien_so)
                        return bien_so
                    except ValueError:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh
                else:
                    print("Khong the sua bien so :",bien_so_co_dinh)
                    return bien_so_co_dinh

    elif bien_so[5:7] in ma_nuoc_ngoai:
        # if bien_so[2:5] in bien_so_nuoc_ngoai:
        for i in range(0,2):
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
        
        if bien_so[0:2] not in ma_tinh:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
        else:
            for i in range(2,5):
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
            if bien_so[3:5] == "11" :
                bien_so = replacer(bien_so,"0",2)
            elif bien_so[3:5] == "26" :
                bien_so = replacer(bien_so,"0",2)
            elif bien_so[3:5] == "41" :
                bien_so = replacer(bien_so,"0",2)
            elif bien_so[3:5] == "61" :
                bien_so = replacer(bien_so,"0",2)
            elif bien_so[3:5] == "66" :
                bien_so = replacer(bien_so,"0",2)
            elif bien_so[3:5] == "21" :
                bien_so = replacer(bien_so,"1",2)
            elif bien_so[3:5] == "56" :
                bien_so = replacer(bien_so,"1",2)
            elif bien_so[3:5] == "91" :
                bien_so = replacer(bien_so,"1",2)
            elif bien_so[3:5] == "06" :
                bien_so = replacer(bien_so,"2",2)
            elif bien_so[3:5] == "96" :
                bien_so = replacer(bien_so,"2",2)    
            elif bien_so[3:5] == "97" :
                bien_so = replacer(bien_so,"2",2)   
            elif bien_so[3:5] == "01" :
                bien_so = replacer(bien_so,"3",2)   
            elif bien_so[3:5] == "31" :
                bien_so = replacer(bien_so,"3",2)
            elif bien_so[3:5] == "36" :
                bien_so = replacer(bien_so,"3",2)
            elif bien_so[3:5] == "46" :
                bien_so = replacer(bien_so,"3",2)
            elif bien_so[3:5] == "64" :
                bien_so = replacer(bien_so,"3",2)
            elif bien_so[3:5] == "76" :
                bien_so = replacer(bien_so,"3",2)
            elif bien_so[3:5] == "81" :
                bien_so = replacer(bien_so,"3",2)      
            elif bien_so[3:5] == "41" :
                bien_so = replacer(bien_so,"4",2)
            elif bien_so[3:5] == "47" :
                bien_so = replacer(bien_so,"5",2) 
            elif bien_so[3:5] == "48" :
                bien_so = replacer(bien_so,"5",2) 
            elif bien_so[3:5] == "49" :
                bien_so = replacer(bien_so,"5",2)  
            elif bien_so[3:5] == "81" :
                bien_so = replacer(bien_so,"5",2)   
            elif bien_so[3:5] == "91" :
                bien_so = replacer(bien_so,"6",2)  
            elif bien_so[3:5] == "88" :
                bien_so = replacer(bien_so,"8",2)      
            elif bien_so[2] == "0" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"1",3) 
            elif bien_so[2] == "0" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"2",3) 
            elif bien_so[2] == "0" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"4",3)
            elif bien_so[2] == "0" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"6",3)
            elif bien_so[2] == "1" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"2",3)
            elif bien_so[2] == "1" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"5",3)
            elif bien_so[2] == "2" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"0",3) 
            elif bien_so[2] == "2" and bien_so[4] == "7":
                bien_so = replacer(bien_so,"9",3)
            elif bien_so[2] == "3" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"0",3) 
            elif bien_so[2] == "3" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"3",3)
            elif bien_so[2] == "3" and bien_so[4] == "4":
                bien_so = replacer(bien_so,"6",3)
            elif bien_so[2] == "4" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"4",3)  
            elif bien_so[2] == "4" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"4",3)
            elif bien_so[2] == "5" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"0",3)
            elif bien_so[2] == "5" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"0",3)
            elif bien_so[2] == "5" and bien_so[4] == "7":
                bien_so = replacer(bien_so,"4",3) 
            elif bien_so[2] == "5" and bien_so[4] == "8":
                bien_so = replacer(bien_so,"4",3)
            elif bien_so[2] == "5" and bien_so[4] == "9":
                bien_so = replacer(bien_so,"4",3)
            elif bien_so[2] == "6" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"0",3)
            elif bien_so[2] == "6" and bien_so[4] == "6":
                bien_so = replacer(bien_so,"0",3)
            elif bien_so[2] == "7" and bien_so[4] == "1":
                bien_so = replacer(bien_so,"3",3)
            elif bien_so[2] == "8" and bien_so[4] == "8":
                bien_so = replacer(bien_so,"8",3) 
            elif bien_so[2:4] == "01":
                bien_so = replacer(bien_so,"1",4) 
            elif bien_so[2:4] == "02":
                bien_so = replacer(bien_so,"1",4)      
            elif bien_so[2:4] == "04":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "06":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "12":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "15":
                bien_so = replacer(bien_so,"6",4) 
            elif bien_so[2:4] == "16":
                bien_so = replacer(bien_so,"6",4)
            elif bien_so[2:4] == "19":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "20":
                bien_so = replacer(bien_so,"6",4) 
            elif bien_so[2:4] == "29":
                bien_so = replacer(bien_so,"6",4)
            elif bien_so[2:4] == "30":
                bien_so = replacer(bien_so,"1",4) 
            elif bien_so[2:4] == "33":
                bien_so = replacer(bien_so,"1",4) 
            elif bien_so[2:4] == "34":
                bien_so = replacer(bien_so,"6",4) 
            elif bien_so[2:4] == "36":
                bien_so = replacer(bien_so,"4",4)
            elif bien_so[2:4] == "37":
                bien_so = replacer(bien_so,"6",4)
            elif bien_so[2:4] == "38":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "44":
                bien_so = replacer(bien_so,"1",4)    
            elif bien_so[2:4] == "45":
                bien_so = replacer(bien_so,"6",4)
            elif bien_so[2:4] == "50":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "52":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "54":
                bien_so = replacer(bien_so,"6",4) 
            elif bien_so[2:4] == "56":
                bien_so = replacer(bien_so,"6",4) 
            elif bien_so[2:4] == "58":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "60":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "62":
                bien_so = replacer(bien_so,"6",4)
            elif bien_so[2:4] == "63":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "69":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "73":
                bien_so = replacer(bien_so,"1",4)
            elif bien_so[2:4] == "88":
                bien_so = replacer(bien_so,"8",4)
            
            try:
                int(bien_so[2:5])
                
            except ValueError:
                print("Khong the sua bien so :",bien_so_co_dinh)
                return bien_so_co_dinh
                
            else:
                if bien_so[2:5] in bien_so_nuoc_ngoai:
                    for i in range(7,9):
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
                        int(bien_so[7:])
                        print("Bien so sau khi chinh sua :",bien_so)
                        return bien_so
                    except ValueError as ve:
                        print("Khong the sua bien so :",bien_so_co_dinh)
                        return bien_so_co_dinh
                else:
                    print("Khong the sua bien so :",bien_so_co_dinh)
                    return bien_so_co_dinh
    else:
        print("Khong the chinh sua bien so :",bien_so_co_dinh)
        return bien_so_co_dinh

    # elif bien_so[5:7] not in ma_nuoc_ngoai:
    #     print("Khong the chinh sua bien so :",bien_so_co_dinh)
    #     return bien_so_co_dinh
                
def xe_quan_doi(bien_so):
    print("Xe quan doi vao day")
    bien_so_co_dinh = bien_so
    print("Bien so truoc chinh sua :",bien_so_co_dinh)
    if len(bien_so) < 6:
        return bien_so
    elif (len(bien_so) == 6): 
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
    
def main(input):
    #nếu là xe quân đội
    if (input[0:2] in quan_doi) and (len(input)==6):
        return xe_quan_doi(input)
    #nếu input có 7 ký tự
    elif (len(input)==7):
        #tìm vị trí của đặc biệt của xe quân đội
        ket_qua_quan_doi = ""
        for i in quan_doi:
            if i in input:
                ket_qua_quan_doi = i
                break
        # ket_qua_quan_doi = (i for i in quan_doi if i in input)
        # ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
        p_quan_doi = input.index(ket_qua_quan_doi)

        #sửa biển số xe quân đội thừa trước
        if (input[p_quan_doi:p_quan_doi+2] in quan_doi) and (len(input[:p_quan_doi])>=1):
            for i in input[:p_quan_doi]:
                input = replacer(input,"",input.index(i))
                return xe_quan_doi(input)
            
        #sửa biển số xe quân đội thừa sau
        elif (input[p_quan_doi:p_quan_doi+2] in quan_doi) and (len(input[p_quan_doi+6:]) >= 1):
            for i in input[p_quan_doi+6:]:
                input = replacer(input,"",input.index(i))
                return xe_quan_doi(input)
        #nếu không phải xe quân đội
        else:
            return xe_ca_nhan_co_quan_nha_nuoc(input)
    elif (len(input)==8):
        #tìm vị trí của ký tự đặc biệt của biển số xe quân đội
        for i in quan_doi:
            if i in input:
                #tìm vị trí đặc biệt của xe quân đội
                ket_qua_quan_doi = ""
                for i in quan_doi:
                    if i in input:
                        ket_qua_quan_doi = i
                        break
                # ket_qua_quan_doi = (i for i in quan_doi if i in input)
                # ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
                p_quan_doi = input.index(ket_qua_quan_doi)
                
                #sửa biển số xe quân đội nếu thừa trước
                if (input[p_quan_doi:p_quan_doi+2] in quan_doi):
                
                    #sửa biển số xe quân đội nếu thừa trước và sau
                    if ((len(input[:p_quan_doi]) >= 1) and (len(input[p_quan_doi+6:]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        for j in input[6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input)
                        
                    #sửa biển số xe quân đội nếu thừa trước
                    elif ((len(input[:p_quan_doi]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        return xe_quan_doi(input) 
                    
                    #sửa biển số xe quân đội nếu thừa sau
                    elif ((len(input[p_quan_doi+6:]) >= 1)):
                        for j in input[p_quan_doi+6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input) 
            else:
                ket_qua_xe_dac_biet = ""
                #tìm vị trí biển xe đặc biệt
                for j in xe_dac_biet:
                    if j in input:
                        ket_qua_xe_dac_biet = j
                        break
                # ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                # ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
                p_xe_dac_biet = input.index(ket_qua_xe_dac_biet)
            
                if (input[p_xe_dac_biet:p_xe_dac_biet+2] in xe_dac_biet):
                    #sửa biển số xe cá nhân và cơ quan thừa trước và sau
                    if ((len(input[:p_xe_dac_biet]) >= 3)):
                        for i in input[:p_xe_dac_biet-2]:
                            input = replacer(input,"",input.index(i))
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
                    #đúng thì ko sửa gì 
                    else:
                        return xe_ca_nhan_co_quan_nha_nuoc(input)

                #nếu ko phải xe đặc biệt 
                elif (check_type_of_character(input[2:5])) < 2:
                    if input[2] == "L":
                        input = replacer(input,"D",3)
                    if input[2] == "D":
                        input = replacer(input,"A",3)
                    if input[2] == "M":
                        input = replacer(input,"K",3)
                    if input[2] == "T":
                        input = replacer(input,"Đ",3)
                    if input[2] == "H":
                        input = replacer(input,"C",3)
                    if input[3] == "D":
                        input = replacer(input,"L",2)
                    if input[3] == "A":
                        input = replacer(input,"D",2)
                    if input[3] == "K":
                        input = replacer(input,"M",2)
                    if input[3] == "Đ":
                        input = replacer(input,"T",2)
                    if input[3] == "C":
                        input = replacer(input,"H",2)
                    if input[2] == "N":
                        input = replacer(input,"G",3)
                    return xe_ca_nhan_co_quan_nha_nuoc(input)
                else:
                    #tìm vị trí của seri đăng ký của biển số xe cá nhân và cơ quan 
                    ket_qua_xe_thuong = ""
                    for j in seri_dang_ky_chu:
                        if j in input:
                            ket_qua_xe_thuong = j
                            break
                    # ket_qua_xe_thuong = (j for j in seri_dang_ky_chu if j in input)
                    # ket_qua_xe_thuong = ''.join(ket_qua_xe_thuong)
                    p_xe_thuong = input.index(ket_qua_xe_thuong)  
                    
                    #sửa biển số xe cá nhân và cơ quan thừa trước
                    if (input[p_xe_thuong] in seri_dang_ky_chu):
                        if ((len(input[:p_xe_thuong]) >= 3)):
                            for i in input[:p_xe_thuong-2]:
                                input = replacer(input,"",input.index(i))
                            return xe_ca_nhan_co_quan_nha_nuoc(input)

                        else:
                            return xe_ca_nhan_co_quan_nha_nuoc(input)
            break
        
    elif (len(input)==9):
        for i in quan_doi:
            if i in input:
                #tìm vị trí đặc biệt của xe quân đội
                ket_qua_quan_doi = ""
                for j in quan_doi:
                    if j in input:
                        ket_qua_quan_doi = j
                        break
                # ket_qua_quan_doi = (i for i in quan_doi if i in input)
                # ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
                p_quan_doi = input.index(ket_qua_quan_doi)
                
                #sửa biển số xe quân đội nếu thừa trước
                if (input[p_quan_doi:p_quan_doi+2] in quan_doi):
                
                    #sửa biển số xe quân đội nếu thừa trước và sau
                    if ((len(input[:p_quan_doi]) >= 1) and (len(input[p_quan_doi+5:]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        for j in input[6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input)
                        
                    #sửa biển số xe quân đội nếu thừa trước
                    elif ((len(input[:p_quan_doi]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        return xe_quan_doi(input) 
                    
                    #sửa biển số xe quân đội nếu thừa sau
                    elif ((len(input[p_quan_doi+6:]) >= 1)):
                        for j in input[p_quan_doi+6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input) 
            else:
                #tìm vị trí biển xe đặc biệt
                ket_qua_xe_dac_biet = ""
                for j in xe_dac_biet:
                    if j in input:
                        ket_qua_xe_dac_biet = j
                        break
                # ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                # ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
                p_xe_dac_biet = input.index(ket_qua_xe_dac_biet)
            
                if (input[p_xe_dac_biet:p_xe_dac_biet+2] in xe_dac_biet):
                
                    #sửa biển số xe cá nhân và cơ quan thừa trước và sau
                    if ((len(input[:p_xe_dac_biet]) >= 3)):
                        for i in input[:p_xe_dac_biet-2]:
                            input = replacer(input,"",input.index(i))
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
                    else:
                        if input[2] == "L":
                            input = replacer(input,"D",3)
                        if input[2] == "D":
                            input = replacer(input,"A",3)
                        if input[2] == "M":
                            input = replacer(input,"K",3)
                        if input[2] == "T":
                            input = replacer(input,"Đ",3)
                        if input[2] == "H":
                            input = replacer(input,"C",3)
                        if input[3] == "D":
                            input = replacer(input,"L",2)
                        if input[3] == "A":
                            input = replacer(input,"D",2)
                        if input[3] == "K":
                            input = replacer(input,"M",2)
                        if input[3] == "Đ":
                            input = replacer(input,"T",2)
                        if input[3] == "C":
                            input = replacer(input,"H",2)
                        if input[2] == "N":
                            input = replacer(input,"G",3)
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
                    # break   
                    # else:        
                #sửa biển số nước ngoài và xe đặc vi
                elif (check_type_of_character(input[2:5])) >= 2:

                    if input[5] == "N":
                        input = replacer(input,"G",6)
                    if input[6] == "N" or input[6] == "G":
                        input = replacer(input,"N",5)
                        return xe_nuoc_ngoai(input)
                    else:
                        ket_qua_xe_thuong = ""
                        for j in seri_dang_ky_chu:
                            if j in input:
                                ket_qua_xe_thuong = j
                                break
                        # ket_qua_xe_thuong = (j for j in seri_dang_ky_chu if j in input)
                        # ket_qua_xe_thuong = ''.join(ket_qua_xe_thuong)
                        # print(ket_qua_xe_thuong)
                        p_xe_thuong = input.index(ket_qua_xe_thuong)  
                        if (input[p_xe_thuong] in seri_dang_ky_chu):
                            if ((len(input[:p_xe_thuong]) >= 3)):
                                for i in input[:p_xe_thuong-2]:
                                    input = replacer(input,"",input.index(i))
                                return xe_ca_nhan_co_quan_nha_nuoc(input)
                            elif ((len(input[7:])) >= 1):
                                for i in range(7,8):
                                    input = replacer(input,"",8)
                                return xe_ca_nhan_co_quan_nha_nuoc(input)
                else:
                    if input[2] == "L":
                        input = replacer(input,"D",3)
                    if input[2] == "D":
                        input = replacer(input,"A",3)
                    if input[2] == "M":
                        input = replacer(input,"K",3)
                    if input[2] == "T":
                        input = replacer(input,"Đ",3)
                    if input[2] == "H":
                        input = replacer(input,"C",3)
                    if input[3] == "D":
                        input = replacer(input,"L",2)
                    if input[3] == "A":
                        input = replacer(input,"D",2)
                    if input[3] == "K":
                        input = replacer(input,"M",2)
                    if input[3] == "Đ":
                        input = replacer(input,"T",2)
                    if input[3] == "C":
                        input = replacer(input,"H",2)
                    if input[2] == "N":
                        input = replacer(input,"G",3)
                    if input[3] == "N" or input[3] == "G":
                        input = replacer(input,"N",2)
                    if input[2:4] in xe_dac_biet:
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
                    else:
                        # input = replacer(input,"N",2)
                        return xe_nuoc_ngoai(input)

            break

    elif (len(input)==10):
        for i in quan_doi:
            if i in input:
                #tìm vị trí đặc biệt của xe quân đội
                ket_qua_quan_doi = ""
                for j in quan_doi:
                    if j in input:
                        ket_qua_quan_doi = j
                        break
                # ket_qua_quan_doi = (i for i in quan_doi if i in input)
                # ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
                p_quan_doi = input.index(ket_qua_quan_doi)
                
                #sửa biển số xe quân đội nếu thừa trước
                if (input[p_quan_doi:p_quan_doi+2] in quan_doi):
                
                    #sửa biển số xe quân đội nếu thừa trước và sau
                    if ((len(input[:p_quan_doi]) >= 1) and (len(input[p_quan_doi+5:]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        for j in input[6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input)
                          
                    #sửa biển số xe quân đội nếu thừa trước
                    elif ((len(input[:p_quan_doi]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        return xe_quan_doi(input) 
                    
                    #sửa biển số xe quân đội nếu thừa sau
                    elif ((len(input[p_quan_doi+6:]) >= 1)):
                        for j in input[p_quan_doi+6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input) 
            else:
                #tìm vị trí biển xe đặc biệt
                ket_qua_xe_dac_biet = ""
                for j in xe_dac_biet:
                    if j in input:
                        ket_qua_xe_dac_biet = j
                        break
                # ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                # ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
                p_xe_dac_biet = input.index(ket_qua_xe_dac_biet)
                if (input[p_xe_dac_biet:p_xe_dac_biet+2] in xe_dac_biet):
                    
                    #sửa biển số xe cá nhân và cơ quan thừa trước
                    if ((len(input[:p_xe_dac_biet]) >= 3)):
                        for i in input[:p_xe_dac_biet-2]:
                            input = replacer(input,"",input.index(i))
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
                    
                    #sửa biển số xe cá nhân và cơ quan thừa sau
                    elif ((len(input[p_xe_dac_biet + 6:]) >= 1)):
                        for i in range(0,len(input[p_xe_dac_biet + 7:])):
                            input = replacer(input,"",p_xe_dac_biet + 7)
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
                    
                    #nếu không phải biển xe cá nhân và cơ quan
                    else:
                        if input[2] == "L":
                            input = replacer(input,"D",3)
                        if input[2] == "D":
                            input = replacer(input,"A",3)
                        if input[2] == "M":
                            input = replacer(input,"K",3)
                        if input[2] == "T":
                            input = replacer(input,"Đ",3)
                        if input[2] == "H":
                            input = replacer(input,"C",3)
                        if input[3] == "D":
                            input = replacer(input,"L",2)
                        if input[3] == "A":
                            input = replacer(input,"D",2)
                        if input[3] == "K":
                            input = replacer(input,"M",2)
                        if input[3] == "Đ":
                            input = replacer(input,"T",2)
                        if input[3] == "C":
                            input = replacer(input,"H",2)
                        if input[2] == "N":
                            input = replacer(input,"G",3)
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
            
                else: 
                    #kiểm tra xem có phải biển nước ngoài không
                    # if (check_type_of_character(input[2:5])) >= 2:
                        # xem vị trí của biển số nước ngoài
                    ket_qua_xe_nuoc_ngoai = ""
                    for j in ma_nuoc_ngoai:
                        if j in input:
                            ket_qua_xe_nuoc_ngoai = j
                            break
                    # ket_qua_xe_nuoc_ngoai = (i for i in ma_nuoc_ngoai if i in input)
                    # ket_qua_xe_nuoc_ngoai = ''.join(ket_qua_xe_nuoc_ngoai)
                    p_xe_nuoc_ngoai = input.index(ket_qua_xe_nuoc_ngoai)

                    if (input[p_xe_nuoc_ngoai:p_xe_nuoc_ngoai+2] in ma_nuoc_ngoai):
                        
                        #sửa biển số xe nước ngoài thừa trước
                        if((len(input[:p_xe_nuoc_ngoai]) >= 6)):
                            for i in input[:p_xe_nuoc_ngoai-5]:
                                input = replacer(input,"",input.index(i))
                            return xe_nuoc_ngoai(input)

                        #sửa biển số xe nước ngoài thừa sau
                        elif ((len(input[p_xe_nuoc_ngoai + 4:]) >= 1)):
                            for j in range(0,len(input[p_xe_nuoc_ngoai + 4:])):
                                input = replacer(input,"",p_xe_nuoc_ngoai + 4)
                            return xe_nuoc_ngoai(input)
                    else:
                        ket_qua_xe_nuoc_ngoai = ""
                        for j in ma_nuoc_ngoai:
                            if j in input:
                                ket_qua_xe_nuoc_ngoai = j
                                break
                        # ket_qua_xe_nuoc_ngoai = (i for i in ma_nuoc_ngoai if i in input)
                        # ket_qua_xe_nuoc_ngoai = ''.join(ket_qua_xe_nuoc_ngoai)
                        p_xe_nuoc_ngoai = input.index(ket_qua_xe_nuoc_ngoai)
 
                        if (input[p_xe_nuoc_ngoai:p_xe_nuoc_ngoai+2] in ma_nuoc_ngoai):
                            
                            #sửa biển số xe nước ngoài thừa trước
                            if((len(input[:p_xe_nuoc_ngoai]) >= 3)):
                                for i in input[:p_xe_nuoc_ngoai-2]:
                                    input = replacer(input,"",input.index(i))
                                return xe_nuoc_ngoai(input)

                            #sửa biển số xe nước ngoài thừa sau
                            elif ((len(input[p_xe_nuoc_ngoai + 6:]) >= 1)):
                                for j in range(0,len(input[p_xe_nuoc_ngoai + 7:])):
                                    input = replacer(input,"",p_xe_nuoc_ngoai + 7)
                                return xe_nuoc_ngoai(input)
                        else:
                        #tìm vị trí của xe cá nhân, cơ quan
                            ket_qua_xe_thuong = ""
                            for j in seri_dang_ky_chu:
                                if j in input:
                                    ket_qua_xe_thuong = j
                                    break
                            # ket_qua_xe_thuong = (j for j in seri_dang_ky_chu if j in input)
                            # ket_qua_xe_thuong = ''.join(ket_qua_xe_thuong)
                            p_xe_thuong = input.index(ket_qua_xe_thuong)  
                            if (input[p_xe_thuong] in seri_dang_ky_chu):
                                #sửa vị trí xe cá nhân, cơ quan thừa trước và sau
                                if ((len(input[:p_xe_thuong]) >= 3) and (len(input[p_xe_thuong + 6:])) >= 1):
                                    for i in input[:p_xe_thuong-2]:
                                        input = replacer(input,"",input.index(i))
                                    for j in range(p_xe_thuong + 5,p_xe_thuong + 5 + len(input[p_xe_thuong + 6:]) + 1) :
                                        input = replacer(input,"",j)
                                    return xe_ca_nhan_co_quan_nha_nuoc(input)
                                
                                #sửa vị trí xe cá nhân, cơ quan thừa trước
                                elif ((len(input[:p_xe_thuong]) >= 3)):
                                    for i in input[:p_xe_thuong-2]:
                                        input = replacer(input,"",input.index(i))
                                    return xe_ca_nhan_co_quan_nha_nuoc(input)

                                #sửa vị trí xe cá nhân, cơ quan thừa sau 
                                elif ((len(input[p_xe_thuong + 5:])) >= 1):
                                    for i in range(0,len(input[p_xe_thuong + 6:])):
                                        input = replacer(input,"",p_xe_thuong + 3)
                                    return xe_ca_nhan_co_quan_nha_nuoc(input)
                                
                                else:
                                    return xe_ca_nhan_co_quan_nha_nuoc(input)
            break
    elif (len(input) > 10):
        for i in quan_doi:
            if i in input:
                #tìm vị trí đặc biệt của xe quân đội
                ket_qua_quan_doi = ""
                for j in quan_doi:
                    if j in input:
                        ket_qua_quan_doi = j
                        break
                # ket_qua_quan_doi = (i for i in quan_doi if i in input)
                # ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
                p_quan_doi = input.index(ket_qua_quan_doi)
                
                #sửa biển số xe quân đội nếu thừa trước
                if (input[p_quan_doi:p_quan_doi+2] in quan_doi):
                
                    #sửa biển số xe quân đội nếu thừa trước và sau
                    if ((len(input[:p_quan_doi]) >= 1) and (len(input[p_quan_doi+5:]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        for j in input[6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input)
                        
                    #sửa biển số xe quân đội nếu thừa trước
                    elif ((len(input[:p_quan_doi]) >= 1)):
                        for i in input[:p_quan_doi]:
                            input = replacer(input,"",input.index(i))
                        return xe_quan_doi(input) 
                    
                    #sửa biển số xe quân đội nếu thừa sau
                    elif ((len(input[p_quan_doi+6:]) >= 1)):
                        for j in input[p_quan_doi+6:]:
                            input = replacer(input,"",input.index(j))
                        return xe_quan_doi(input) 
            else:
                #tìm vị trí biển xe đặc biệt
                ket_qua_xe_dac_biet = ""
                for j in xe_dac_biet:
                    if j in input:
                        ket_qua_xe_dac_biet = j
                        break
                # ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                # ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
                p_xe_dac_biet = input.index(ket_qua_xe_dac_biet)
                if (input[p_xe_dac_biet:p_xe_dac_biet+2] in xe_dac_biet):
                    #sửa biển số xe cá nhân và cơ quan thừa trước và sau
                    if (len(input[:p_xe_dac_biet]) >= 3) and (len(input[p_xe_dac_biet + 6:]) >= 1):
                        for i in input[:p_xe_dac_biet-2]:
                            input = replacer(input,"",input.index(i))
                        print(input)
                        for i in range(0,len(input[2 + 7:])):
                            input = replacer(input,"",2 + 7)
                        return xe_ca_nhan_co_quan_nha_nuoc(input)

                    #sửa biển số xe cá nhân và cơ quan thừa trước
                    elif ((len(input[:p_xe_dac_biet]) >= 3)):
                        for i in input[:p_xe_dac_biet-2]:
                            input = replacer(input,"",input.index(i))
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
                    
                    #sửa biển số xe cá nhân và cơ quan thừa sau
                    elif ((len(input[p_xe_dac_biet + 6:]) >= 1)):
                        for i in range(0,len(input[p_xe_dac_biet + 7:])):
                            input = replacer(input,"",p_xe_dac_biet + 7)
                        return xe_ca_nhan_co_quan_nha_nuoc(input)
            
                else: 
                    #kiểm tra xem có phải biển nước ngoài không
                    # if (check_type_of_character(input[2:5])) >= 2:
                        # xem vị trí của biển số nước ngoài
                    ket_qua_xe_nuoc_ngoai = ""
                    for j in ma_nuoc_ngoai:
                        if j in input:
                            ket_qua_xe_nuoc_ngoai = j
                            break
                    # ket_qua_xe_nuoc_ngoai = (i for i in ma_nuoc_ngoai if i in input)
                    # ket_qua_xe_nuoc_ngoai = ''.join(ket_qua_xe_nuoc_ngoai)
                    p_xe_nuoc_ngoai = input.index(ket_qua_xe_nuoc_ngoai)
                    if (input[p_xe_nuoc_ngoai:p_xe_nuoc_ngoai+2] in ma_nuoc_ngoai):
                        
                        #sửa biển số xe nước ngoài thừa trước và sau với biển mới
                        if ((len(input[:p_xe_nuoc_ngoai]) >= 6) and (len(input[p_xe_nuoc_ngoai + 3:]) >= 1) and (input[p_xe_nuoc_ngoai-3:p_xe_nuoc_ngoai] in bien_so_nuoc_ngoai)):
                            for i in input[:p_xe_nuoc_ngoai-5]:
                                input = replacer(input,"",input.index(i))
                            for j in range(0,len(input[5 + 4:])):
                                input = replacer(input,"",5 + 4)
                            return xe_nuoc_ngoai(input)

                        #sửa biển số xe nước ngoài thừa trước với biển mới
                        elif((len(input[:p_xe_nuoc_ngoai]) >= 6) and (input[p_xe_nuoc_ngoai-3:p_xe_nuoc_ngoai] in bien_so_nuoc_ngoai)):
                            for i in input[:p_xe_nuoc_ngoai-5]:
                                input = replacer(input,"",input.index(i))
                            return xe_nuoc_ngoai(input)

                        #sửa biển số xe nước ngoài thừa sau với biển mới
                        elif ((len(input[p_xe_nuoc_ngoai + 4:]) >= 1) and (input[p_xe_nuoc_ngoai-3:p_xe_nuoc_ngoai] in bien_so_nuoc_ngoai)):
                            for j in range(0,len(input[p_xe_nuoc_ngoai + 4:])):
                                input = replacer(input,"",p_xe_nuoc_ngoai + 4)
                            return xe_nuoc_ngoai(input)

                        elif ((len(input[:p_xe_nuoc_ngoai]) >= 3) and (len(input[p_xe_nuoc_ngoai + 6:]) >= 1) and (input[p_xe_nuoc_ngoai+2:p_xe_nuoc_ngoai+5] in bien_so_nuoc_ngoai)):
                            for i in input[:p_xe_nuoc_ngoai-2]:
                                input = replacer(input,"",input.index(i))
                            for j in range(0,len(input[2 + 7:])):
                                input = replacer(input,"",2 + 7)
                            return xe_nuoc_ngoai(input)

                        #sửa biển số xe nước ngoài thừa trước với biển cũ
                        elif((len(input[:p_xe_nuoc_ngoai]) >= 3) and input[p_xe_nuoc_ngoai+2:p_xe_nuoc_ngoai+5] in bien_so_nuoc_ngoai):
                            for i in input[:p_xe_nuoc_ngoai-2]:
                                input = replacer(input,"",input.index(i))
                            return xe_nuoc_ngoai(input)

                        #sửa biển số xe nước ngoài thừa sau với biển cũ
                        elif ((len(input[p_xe_nuoc_ngoai + 6:]) >= 1) and input[p_xe_nuoc_ngoai+2:p_xe_nuoc_ngoai+5] in bien_so_nuoc_ngoai):
                            for j in range(0,len(input[p_xe_nuoc_ngoai + 7:])):
                                input = replacer(input,"",p_xe_nuoc_ngoai + 7)
                            return xe_nuoc_ngoai(input)
                          
                    else:
                    #tìm vị trí của xe cá nhân, cơ quan
                        ket_qua_xe_thuong = ""
                        for j in seri_dang_ky_chu:
                            if j in input:
                                ket_qua_xe_thuong = j
                                break
                        # ket_qua_xe_thuong = (j for j in seri_dang_ky_chu if j in input)
                        # ket_qua_xe_thuong = ''.join(ket_qua_xe_thuong)
                        p_xe_thuong = input.index(ket_qua_xe_thuong)
                        print(p_xe_thuong)
                        if (input[p_xe_thuong] in seri_dang_ky_chu):
                            #sửa vị trí xe cá nhân, cơ quan thừa trước và sau
                            if ((len(input[:p_xe_thuong]) >= 3) and (len(input[p_xe_thuong + 6:])) >= 1):
                                for i in input[:p_xe_thuong-2]:
                                    input = replacer(input,"",input.index(i))
                                for j in range(0,len(input[p_xe_thuong + 6:])+5):
                                    input = replacer(input,"",8)
                                return xe_ca_nhan_co_quan_nha_nuoc(input)
                            
                            #sửa biển số xe cá nhân bị thiếu trước
                            elif ((len(input[:p_xe_thuong]) <= 2)):
                                print("Khong the sua bien so :",input)
                                return input

                            #sửa vị trí xe cá nhân, cơ quan thừa trước
                            elif ((len(input[:p_xe_thuong]) >= 3)):
                                for i in input[:p_xe_thuong-2]:
                                    input = replacer(input,"",input.index(i))
                                return xe_ca_nhan_co_quan_nha_nuoc(input)

                            #sửa vị trí xe cá nhân, cơ quan thừa sau 
                            elif ((len(input[p_xe_thuong + 5:])) >= 1):
                                print(len(input[p_xe_thuong + 6:]))
                                for i in range(0,len(input[p_xe_thuong + 6:])):
                                    input = replacer(input,"",8)
                                return xe_ca_nhan_co_quan_nha_nuoc(input)
                            
                            elif ((len(input[:p_xe_thuong]) <= 2)):
                                print("Khong the sua bien so :",input)
                                return input

                            else:
                                return xe_ca_nhan_co_quan_nha_nuoc(input)
            break
    else:
        print("Khong the sua bien so :",input)
        return input
print(main(input))


# df = pd.read_excel("bienso.xlsx")
# for i in range(0,len(df)):
#     print(df._get_value(i,'Biển số nhận dạng AI'))
#     df.iat[i ,df.columns.get_loc('Biển số sau khi được hậu xử lý')] = main(str(df._get_value(i,'Biển số nhận dạng AI')))
# print(df.head())
# df.to_excel("bienso_hauxuly.xlsx")

            