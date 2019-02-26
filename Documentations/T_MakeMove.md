# T_MakeMove.py
Cho các con rùa tạo và thực hiện nước đi

Sơ lược các công việc `MakeMove()` thực hiện:

#### 1. Xét rùa đã hoàn thành các lượt đua của mình trước đó chưa.

Nếu có, không thực hiện công việc nào khác

#### 2. Xét rùa đã đến 1 trong 2 đích chưa
- Nếu lượt đua hiện tại là lượt đua đầu tiên, thứ 3, v.v. ("các lượt đi") , xét khoảng cách từ vị trí hiện tại của rùa đến vị trí ban đầu của nó có bằng (hoặc vượt qua chút đỉnh) độ dài đường đua chưa.
- Nếu lượt đua hiện tại là lượt đua thứ 2, thứ 4, v.v. ("các lượt về"), xét khoảng cách từ vị trí hiện tại đến vị trí về đích có bằng (hoặc vượt qua chút đỉnh) độ dài đường đua chưa.
Nếu 1 trong 2 test trên pass:
	* rùa sẽ quay đầu về sau và xóa nét vẽ trước đó của mình;
	* bộ đếm tổng số nước đi, số nước lùi, số nước dừng sẽ được đặt lại;
	* bộ đếm số lượt đua sẽ tăng thêm 1.

#### 3. Nếu cả 2 test trên đều fail, cho rùa tạo và thực hiện nước đi.
Lúc này, rùa sẽ thực hiện tuần tự các việc sau:
1. Chọn độ dài nước đi ngẫu nhiên (đã được định nghĩa trong `turtleMoveLength` trong `_SETTINGS_.py`)
2. Chọn ngẫu nhiên 1 trong 3 nước đi: lùi, dừng hoặc tiến.
3. Nếu chọn "lùi", xét bộ đếm tổng số nước đi và bộ đếm số nước lùi. Nếu trong 10 nước đi, nước hiện tại là nước đi thứ `turtleBackStopBias` trở đi, và tổng số nước lùi trong khoảng 10 nước đi đó chưa đạt đến giới hạn, cho phép con rùa lùi. Nếu test đã fail, chuyển sang bước 5.
> Thư viện `turtle` trong Python không hỗ trợ việc xoay hình dạng con vật nhập từ bên thứ 3 vào, nên `left()` hoặc `right()` khi đó chỉ thay đổi hướng đầu nét vẽ trỏ đến.
4. Nếu chọn "dừng", thực hiện các bước gần tương tự như bước 3.
5. `forward()` vô điều kiện.
6. Kiểm tra nếu đã qua 10 nước đi thì đặt lại bộ đếm số nước lùi/dừng.

---

Sau khi đã thực hiện xong các công việc trên, `MakeMove()` trả lại trạng thái mới của rùa (để có thể gán lại trong chương trình chính. Hình như Python không hỗ trợ "tham chiếu" .-.)
