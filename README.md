# Sơ lược các giai đoạn của TurtleRace

##Phát nhạc nền
CÀI ĐẶT: Đặt tên file nhạc làm switch: filename để phát nhạc, None để tắt nhạc

##Hỏi người dùng độ dài đường đua (1 = short, 2 = medium, 3 = long)
CÀI ĐẶT: Nhập mảng độ dài đường đua (trackUnitCount)
trackLength_Session = Tính độ dài ra (trackUnitCount * trackUnitLength)

##Vẽ đường đua

##t[] = tạo mảng, mỗi phần tử chứa 8 phần tử con:
0: Turtle()
1: thứ tự chạy
2: vị trí ban đầu
3: hình dáng
4: tổng số nước
5: số nước lùi
6: số nước dừng
7: đã thắng hay chưa]

##Hàm AddTurtles(mảng t):
Tạo rùa
Tạo thứ tự chạy
Tạo vị trí ban đầu, dựa theo độ rộng đường đua (KHÔNG DỰA THEO THỨ TỰ CHẠY)
Set hình dáng (hiện tại là màu)
moveCount = 0
backCount = 0
stopCount = 0
win = False
Trả về mảng t

##Thay đổi hình dáng, đưa từng con rùa tới vị trí xuất phát
Hiện tại chưa có hình nên mới chỉ đổi màu

##Hàm MakeMove(một con rùa trong mảng t, độ dài đường đua):
Cơ chế như MakeMove2
Trả về con rùa đó

##Đếm thời gian từng con rùa chạy
Báo thắng con nào có thời gian thấp nhất
Hiện tại chưa có cách đo thời gian nên lấy tổng số nước để so sánh thay thế

##Phát hiệu ứng chiến thắng
Vẫn chưa hình dung ra được :v
