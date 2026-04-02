class ConCho:
    def __init__(self, ten, mau_sac, giong):
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong

    def sua(self):
        print(f"{self.ten} đang sủa: Gâu gâu!")
    
    def chay(self):
        print(f"{self.ten} đang chạy!")

class Oto:
    def __init__(self, hang_xe, mau_sac, gia):
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
        self.gia = gia

    def tang_toc(self):
        print(f"{self.hang_xe} đang tăng tốc!")

    def dam(self):
        print(f"{self.hang_xe} đang đâm vào vật cản!")

class TaiKhoan:
    def __init__(self, ten_nguoi_dung, so_tk, ngan_hang, so_du):
        self.ten_nguoi_dung = ten_nguoi_dung
        self.so_tk = so_tk
        self.ngan_hang = ngan_hang
        self.so_du = so_du
    
    def rut_tien(self, so_tien):
        if so_tien > self.so_du:
            print("Số dư không đủ để rút tiền.")
        else:
            self.so_du -= so_tien
            print(f"Rút {so_tien} thành công. Số dư còn lại: {self.so_du}")
    
    def nap_tien(self, so_tien):
        self.so_du += so_tien
        print(f"Nạp {so_tien} thành công. Số dư hiện tại: {self.so_du}")
    
    def kiem_tra_so_du(self):
        print(f"Số dư hiện tại của {self.ten_nguoi_dung} là: {self.so_du}")