# Cau 1
pi = 3.14
r = 5
volume = (4/3) * pi * r**3
print(f"1.The tich hinh cau co ban kinh bang 5 la: {volume}")

# Cau 2
gia_bia = 24.95
gia_da_giam = gia_bia * (1 - 0.4)
phi_ship = 3 + 59 * 0.75 
tong_chi_phi = ( gia_da_giam * 60 ) + phi_ship
print(f"2.Tong chi phi cho 60 cuon sach la: {tong_chi_phi}")

# Cau 3
thoi_gian_chay_giay = (8 * 60 + 15) + 3*(7 * 60 + 12) + (8* 60 + 15)
phut_chay = thoi_gian_chay_giay // 60
giay_le = thoi_gian_chay_giay % 60

gio_ve = 6
phut_ve = 52 + phut_chay
gio_ve = gio_ve + (phut_ve // 60)
phut_ve = phut_ve % 60

print(f"3.Thoi gian ve den nha la: {gio_ve} gio, {phut_ve} phut, {giay_le} giay")


