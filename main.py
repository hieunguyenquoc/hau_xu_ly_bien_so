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
input = input("Nhap vao bien so :")


def main(input):
    if (input[0:2] in quan_doi) and (len(input)==6):
        return xe_quan_doi(input)
    elif (len(input)==7):
        return xe_ca_nhan_co_quan_nha_nuoc(input)
    elif (len(input)==8):
        if input[2] == "L":
            input = replacer(input,"D",3)
        elif input[2] == "D":
            input = replacer(input,"A",3)
        elif input[2] == "M":
            input = replacer(input,"K",3)
        elif input[2] == "T":
            input = replacer(input,"Đ",3)
        elif input[2] == "H":
            input = replacer(input,"C",3)
        elif input[3] == "D":
            input = replacer(input,"L",2)
        elif input[3] == "A":
            input = replacer(input,"D",2)
        elif input[3] == "K":
            input = replacer(input,"M",2)
        elif input[3] == "Đ":
            input = replacer(input,"T",2)
        elif input[3] == "C":
            input = replacer(input,"H",2)
        return xe_ca_nhan_co_quan_nha_nuoc(input)
    elif (len(input)==9):
        if (check_type_of_character(input[2:5])) >= 2:
            if input[5] == "N":
                input = replacer(input,"G",6)
            elif input[6] == "N" or input[6] == "G":
                input = replacer(input,"N",5)
            return xe_nuoc_ngoai(input)
        else:
            if input[2] == "L":
                input = replacer(input,"D",3)
            elif input[2] == "D":
                input = replacer(input,"A",3)
            elif input[2] == "M":
                input = replacer(input,"K",3)
            elif input[2] == "T":
                input = replacer(input,"Đ",3)
            elif input[2] == "H":
                input = replacer(input,"C",3)
            elif input[3] == "D":
                input = replacer(input,"L",2)
            elif input[3] == "A":
                input = replacer(input,"D",2)
            elif input[3] == "K":
                input = replacer(input,"M",2)
            elif input[3] == "Đ":
                input = replacer(input,"T",2)
            elif input[3] == "C":
                input = replacer(input,"H",2)
            elif input[2] == "N":
                input = replacer(input,"G",3)
            if input[2:4] in ma_nuoc_ngoai:
                return xe_nuoc_ngoai(input)
            elif input[2:4] in xe_dac_biet:
                return xe_ca_nhan_co_quan_nha_nuoc(input)
            else:
                print("Khong the sua bien so :",input)
                return input
    # elif (len(input) > 9):
    else:
        print("Bien khong thuoc loai nao het")
        return input

print(main(input))
            