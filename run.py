from main import main
import time

if __name__ == "__main__":
    bien_so = input("Nhập vào biển số :")
    start = time.time()
    print("Bắt đầu hậu xử lý biển số")

    main(bien_so)

    end = time.time()
    print("Kết thúc hậu xử lý văn bản. Thời gian :",end - start," giây")