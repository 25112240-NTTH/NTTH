class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._gia = gia
    def hien_thi_thong_tin(self):
        print(f"Mã hàng: {self._ma_hang}")
        print(f"Tên hàng: {self._ten_hang}")
        print(f"Nhà sản xuất: {self._nha_sx}")
        print(f"Giá: {self._gia}")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_bao_hanh, dien_ap,cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._tg_bao_hanh = tg_bao_hanh
        self._dien_ap = dien_ap
        self._cong_suat = cong_suat
    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Thời gian bảo hành: {self._tg_bao_hanh} tháng")
        print(f"Điện áp: {self._dien_ap} V")
        print(f"Công suất: {self._cong_suat} W")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._loai_nguyen_lieu = loai_nguyen_lieu
    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Loại nguyên liệu: {self._loai_nguyen_lieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._ngay_sx = ngay_sx
        self._ngay_het_han = ngay_het_han
    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Ngày sản xuất: {self._ngay_sx}")
        print(f"Ngày hết hạn: {self._ngay_het_han}")