from Replacer import replacer
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