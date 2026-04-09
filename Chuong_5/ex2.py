class NhanVienBase:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, diachi, he_so, luong_max):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.diachi = diachi
        
        if he_so > 0:
            self.he_so = he_so
        else:
            self.he_so = 1.0
            
        self.luong_max = luong_max

    def in_thong_tin(self):
        print("Ma NV:", self.ma_nv, "| Ho ten:", self.ho_ten, "| He so:", self.he_so)

class CongTacVien(NhanVienBase):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, diachi, he_so, luong_max, thoi_han, phu_cap_ld):
        NhanVienBase.__init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, diachi, he_so, luong_max)
        
        self.thoi_han = thoi_han
        self.phu_cap_ld = phu_cap_ld

    def in_thong_tin(self):
        NhanVienBase.in_thong_tin(self)
        print("Loai: Cong tac vien | Thoi han:", self.thoi_han, "| Phu cap:", self.phu_cap_ld)

class TruongPhong(NhanVienBase):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, diachi, he_so, luong_max, ngay_quan_ly, phu_cap_ql):
        NhanVienBase.__init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, diachi, he_so, luong_max)
        
        self.ngay_quan_ly = ngay_quan_ly
        self.phu_cap_ql = phu_cap_ql

    def in_thong_tin(self):
        NhanVienBase.in_thong_tin(self)
        print("Chuc vu: Truong phong | Ngay bat dau QL:", self.ngay_quan_ly, "| Phu cap QL:", self.phu_cap_ql)
