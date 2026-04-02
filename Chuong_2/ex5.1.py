import time 
total_seconds = time.time()
days_since_epoch = int(total_seconds // 86400)
remaining_seconds = total_seconds % 86400
hours = int(remaining_seconds // 3600)
minutes = int((remaining_seconds % 3600) // 60)
seconds = int(remaining_seconds % 60)

print("So ngay la:", days_since_epoch)
print(f"Thoi gian hien tai la: {hours} gio, {minutes} phut, {seconds} giay")