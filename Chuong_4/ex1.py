class NhanVien:
    LUONG_MAX = 20000000.0

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self._tenNhanVien = tenNhanVien
        self._luongCoBan = luongCoBan
        self._heSoLuong = heSoLuong
    
    def tinh_luong(self):
        luong = self._luongCoBan * self._heSoLuong
        return min(luong, NhanVien.LUONG_MAX)
    
    def hien_thi_thong_tin(self):
        print(f"Tên nhân viên: {self._tenNhanVien}")
        print(f"Lương cơ bản: {self._luongCoBan}")
        print(f"Hệ số lương: {self._heSoLuong}")

    def tang_luong(self, delta):
        he_so_moi = self._heSoLuong + delta
        tong_luong_moi = self._luongCoBan * he_so_moi
        if tong_luong_moi > NhanVien.LUONG_MAX:
            print(f"Không thể tăng lương. Lương mới sẽ vượt quá mức tối đa: {NhanVien.LUONG_MAX}")
        else:
            self._heSoLuong = he_so_moi
            print(f"Hệ số lương của {self._tenNhanVien} đã được tăng lên: {self._heSoLuong}")
       