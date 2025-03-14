def tong_chi_phi(x, y):
    
    # Kiểm tra input hợp lệ
    if not (1 <= x <= 3260) or not (1 <= y <= 1000):
        return "invalid input"

    # Tính phí vận chuyển theo khoảng cách
    if x <= 50:  
        phi_van_chuyen = x * 10000  # Phí vận chuyển 10000 vnđ/km
    elif  50 < x <= 200:  
        phi_van_chuyen = x * 8000  # Phí vận chuyển 8000 vnđ/km
    else:  # 200 < x ≤ 1000
        phi_van_chuyen = x * 5000  # Phí vận chuyển 5000 vnđ/km

    # Tính phụ phí theo trọng lượng hàng hóa
    if y > 100:
        phu_phi = phi_van_chuyen * 0.1
    else: 
        phu_phi = 0

    return int(phi_van_chuyen + phu_phi)  # Trả về số nguyên (VNĐ không có phần lẻ)

# Ví dụ chạy thử
print(tong_chi_phi(0, 500))  # invalid input
print(tong_chi_phi(50, 200))  # 550000
print(tong_chi_phi(200, 200))  # 1760000
