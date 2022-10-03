from Replacer import replacer
from CheckType import check_type_of_character
from XeCaNhanCoQuan import xe_ca_nhan_co_quan_nha_nuoc
from XeNuocNgoai import xe_nuoc_ngoai
from XeQuanDoi import xe_quan_doi

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
seri_dang_ky_chu = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]            
input = input("Nhap vao bien so :")


def main(input):
    #nếu là xe quân đội
    if (input[0:2] in quan_doi) and (len(input)==6):
        xe_quan_doi(input)
    #nếu input có 7 ký tự
    elif (len(input)==7):
        #tìm vị trí của đặc biệt của xe quân đội
        ket_qua_quan_doi = (i for i in quan_doi if i in input)
        ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
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
                ket_qua_quan_doi = (i for i in quan_doi if i in input)
                ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
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
                        xe_quan_doi(input) 
            else:
                #tìm vị trí biển xe đặc biệt
                ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
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
                    ket_qua_xe_thuong = (j for j in seri_dang_ky_chu if j in input)
                    ket_qua_xe_thuong = ''.join(ket_qua_xe_thuong)
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
                ket_qua_quan_doi = (i for i in quan_doi if i in input)
                ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
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
                ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
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
                        xe_ca_nhan_co_quan_nha_nuoc(input)
                    # break   
                    # else:        
                #sửa biển số nước ngoài
                elif (check_type_of_character(input[2:5])) >= 2:
                    if input[5] == "N":
                        input = replacer(input,"G",6)
                    if input[6] == "N" or input[6] == "G":
                        input = replacer(input,"N",5)
                        return xe_nuoc_ngoai(input)
                    else:
                        ket_qua_xe_thuong = (j for j in seri_dang_ky_chu if j in input)
                        ket_qua_xe_thuong = ''.join(ket_qua_xe_thuong)
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
                    if input[2] == "N":
                        input = replacer(input,"G",3)
                    if input[3] == "N" or input[6] == "G":
                        input = replacer(input,"N",2)
                    return xe_nuoc_ngoai(input)
            break

    elif (len(input)==10):
        for i in quan_doi:
            if i in input:
                #tìm vị trí đặc biệt của xe quân đội
                ket_qua_quan_doi = (i for i in quan_doi if i in input)
                ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
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
                ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
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
                    ket_qua_xe_nuoc_ngoai = (i for i in ma_nuoc_ngoai if i in input)
                    ket_qua_xe_nuoc_ngoai = ''.join(ket_qua_xe_nuoc_ngoai)
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
                        ket_qua_xe_nuoc_ngoai = (i for i in ma_nuoc_ngoai if i in input)
                        ket_qua_xe_nuoc_ngoai = ''.join(ket_qua_xe_nuoc_ngoai)
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
                            for j in seri_dang_ky_chu:
                                if j in input:
                                    ket_qua_xe_thuong = j
                                    break
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
    elif(len(input) > 10):
        for i in quan_doi:
            if i in input:
                #tìm vị trí đặc biệt của xe quân đội
                ket_qua_quan_doi = (i for i in quan_doi if i in input)
                ket_qua_quan_doi = ''.join(ket_qua_quan_doi)
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
                ket_qua_xe_dac_biet = (j for j in xe_dac_biet if j in input)
                ket_qua_xe_dac_biet = ''.join(ket_qua_xe_dac_biet)
                p_xe_dac_biet = input.index(ket_qua_xe_dac_biet)
                if (input[p_xe_dac_biet:p_xe_dac_biet+2] in xe_dac_biet):
                    #sửa biển số xe cá nhân và cơ quan thừa trước và sau
                    if (len(input[:p_xe_dac_biet]) >= 3) and (len(input[p_xe_dac_biet + 6:]) >= 1):
                        for i in input[:p_xe_dac_biet-2]:
                            input = replacer(input,"",input.index(i))
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
                    ket_qua_xe_nuoc_ngoai = (i for i in ma_nuoc_ngoai if i in input)
                    ket_qua_xe_nuoc_ngoai = ''.join(ket_qua_xe_nuoc_ngoai)
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
                        ket_qua_xe_thuong = (j for j in seri_dang_ky_chu if j in input)
                        ket_qua_xe_thuong = ''.join(ket_qua_xe_thuong)
                        p_xe_thuong = input.index(ket_qua_xe_thuong)
                        if (input[p_xe_thuong] in seri_dang_ky_chu):
                            #sửa vị trí xe cá nhân, cơ quan thừa trước và sau
                            if ((len(input[:p_xe_thuong]) >= 3) and (len(input[p_xe_thuong + 6:])) >= 1):
                                for i in input[:p_xe_thuong-2]:
                                    input = replacer(input,"",input.index(i))
                                print(len(input[8:]))
                                for j in range(0,len(input[8:])):
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
                                for i in range(0,len(input[p_xe_thuong + 6:])):
                                    input = replacer(input,"",8)
                                return xe_ca_nhan_co_quan_nha_nuoc(input)
                            
                            else:
                                return xe_ca_nhan_co_quan_nha_nuoc(input)
            break
    else:
        print("Khong the sua bien so :",input)
        return input
            