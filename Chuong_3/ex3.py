class NhanVien:
    LUONG_MAX = 20000000.0

    def __init__(self, ten, luong_cb, he_so):
        self._tenNhanVien = ten
        self._luongCoBan = luong_cb
        self._heSoLuong = he_so

    def tinh_luong(self):
        luong = self._luongCoBan * self._heSoLuong
        return min(luong, NhanVien.LUONG_MAX)
    
    def hien_thi_thong_tin(self):
        print(f"Tên nhân viên: {self._tenNhanVien}")
        print(f"Lương cơ bản: {self._luongCoBan}")
        print(f"Hệ số lương: {self._heSoLuong}")

    def tang_luong(self, so_tien):
        self._luongCoBan += so_tien
        print(f"Lương cơ bản của {self._tenNhanVien} đã được tăng lên: {self._luongCoBan}")

    def doi_ten(self, ten_moi):
        self._tenNhanVien = ten_moi
        print(f"Tên nhân viên đã được đổi thành: {self._tenNhanVien}")
        