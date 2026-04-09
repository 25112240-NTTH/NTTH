from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f" Gia {gia} khong hop le")

class HangHoa(ABC):
    def __init__(self, ma, ten, nsx, gia):
        self.__ma, self.__ten, self.__nsx = ma, ten, nsx
        self.gia = gia
    @property
    def ma_hang(self): return self.__ma
    @property
    def ten_hang(self): return self.__ten
    @property
    def gia(self): return self.__gia
    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value)
        self.__gia = value
    @abstractmethod
    def loai_hang(self):
        pass
    def inTTin(self):
        return (f"[{self.loai_hang()}] {self.__ma}" f" | {self.__ten} | {self.__gia:,.0f}đ")
    def __str__(self):        return self.inTTin()
    def __eq__(self, o): return self.__ma == o.__ma
    def __lt__(self, o): return self.__gia < o.__gia
    def __hash__(self): return hash(self.__ma)

class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nsx, gia, bh, dap, cs):
        super().__init__(ma, ten, nsx, gia)
        self.__bh, self.__dap, self.__cs = bh, dap, cs
    def loai_hang(self): return "Điện máy"
    def inTTin(self):
        return (f"{super().inTTin()}" f" | BH: {self.__bh} tháng" f" | Điện áp: {self.__dap}V" f" | Công suất: {self.__cs}W")
    
