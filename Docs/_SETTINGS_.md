# \_SETTINGS\_.py
File các cài đặt cho chương trình

#### Quy ước
Tất cả các file tài nguyên được đặt trong thư mục `Resources`
và đường dẫn đến file được ghi như đã chú thích trong `_SETTINGS_.py`

#### Nhạc nền/Hình nền
- `BGMfile`: Chỉ định tên file nhạc nền
- `BGPfile`: Chỉ định tên file hình nền

#### Số rùa/số đường đua
Cả 2 thuộc tính này được quy định bằng biến `c` chung.

#### Số lượt đua
Số lần mỗi con rùa phải đi hết cả đường chạy trong game
> VD: Số lượt = 2 nghĩa là mỗi con rùa có lượt đi lượt về (chạy hết đường chạy 2 lần)

#### Vẽ đường đua

* `initX`, `initY`: tọa độ ban đầu để vẽ đường đua. Cũng được dùng để xác định vị trí ban đầu của rùa, xác định vị trí vẽ bảng điểm và v.v.
* `trackUnitLength`: độ dài cố định của một đoạn đường đua. Dùng cho `trackUnitCount`
* `trackUnitCount`: mảng 3 phần tử chứa số đoạn có độ dài `trackUnitLength` cần vẽ, tương ứng với 3 mức `short`, `medium` và `long` khi mới bắt đầu game
* `trackWidth`: độ rộng đường đua
* `trackDivPadding`: phần khoảng trống "đệm" cho mỗi vạch dọc trên đường đua


#### Cài đặt rùa

* `turtleColors`: một mảng các màu rùa có thể chọn ngẫu nhiên. Chỉ ảnh hưởng đến màu nét vẽ của rùa trên đường đua. Phải có số phần tử lớn hơn hoặc bằng số phần tử đã định ở `c`.
* `turtleMoveLength`: một mảng các độ dài nước đi rùa có thể chọn ngẫu nhiên. Dùng cho `MakeMove()`. Phải có số phần tử lớn hơn 0.
* `turtleBackStopBias`: một giá trị "thiên vị" cho việc chọn nước đi lùi/dừng của rùa trong `MakeMove()`. Mức bias có giá trị trong khoảng `0 - 10`; những giá trị khác ngoài khoảng này có thể dẫn đến hành vi không xác định.
	> Thực chất mức bias này là một phần trong câu điều kiện "nếu trong 10 nước đi, nước hiện tại là nước thứ `turtleBackStopBias` trở lên thì rùa được phép đi lùi/dừng" trong `MakeMove()`.

#### Hình dạng rùa
Các set hình dạng rùa được định nghĩa như đã chú thích trong `_SETTINGS_.py`.
`turtleShapes` chỉ định set hình dạng nào được dùng trong game.