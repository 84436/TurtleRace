# T_AddTurtles.py: Tạo rùa
Dưới đây là sơ lược các công việc mà hàm AddTurtles() sẽ thực hiện:

1. ___Tạo một mảng order chứa thứ tự chạy ngẫu nhiên của những con rùa___

2. ___Tạo các biến___:  
	- Những biến có giá trị ban đầu không đổi đối với tất cả con rùa sẽ được đặt ngoài vòng lặp for. Những biến này bao gồm:
		- Các bộ đếm: `moveCount` (tổng số nước đi), `backCount` (số nước lùi), `stopCount` (số nước dừng)
		- `win`: flag để kiểm tra rùa đã tới đích chưa
		- `runtime`: lưu thời gian chạy của rùa

	- Những biến có giá trị riêng biệt sẽ được đặt trong vòng lặp for. Những biến này bao gồm:  
		- `order`: thứ tự chạy của rùa
            > Thứ tự chạy của rùa sẽ được chọn lần lượt theo mảng order đã tạo trước đó thay vì tạo ngẫu nhiên kiểu randrange() để tránh hiện tượng 2 con rùa ngẫu nhiên chọn trùng thứ tự chạy.
            > 
		- `position`: vị trí ban đầu
		- `color`: màu nét vẽ của rùa (chọn ngẫu nhiên trong `turtleColors`)
		- `shape`: hình dáng con rùa (chọn ngẫu nhiên trong `turtleShapes`)

	- Sau khi các biến đã được tạo, mọi thứ cùng với con rùa chính nó sẽ được thêm vào mảng `t` dưới dạng một mảng con chứa 10 phần tử. Dưới đây là thứ tự các phần tử:

		  0: Turtle() <-- con rùa chính nó
          1: order			2: position
          3: shape			4: color
          5: moveCount		6: backCount
          7: stopCount		8: runtime
          9: win

      Khi đó, con rùa thứ i trong mảng (_Note: i bắt đầu từ 0_) có thể được truy cập bằng `t[i][0]`, và các thuộc tính của nó được truy cập bằng chỉ số tương ứng trong bảng thứ tự các phần tử trên.
      > VD1: `t[0][0].forward(100)` sẽ ra lệnh cho con rùa thứ 0 tiến 100 đơn vị  
      > VD2: `t[2][0].shape(t[2][3])` sẽ thay đổi hình dạng cho con rùa thứ 2, với tên hình dạng nằm trong thuộc tính của chính nó  
      > VD3: `t[1][0].color(t[3][4])` sẽ tô màu cho con rùa thứ 1, với tên màu của con rùa thứ 3  

3. ___Thay đổi màu nét vẽ, hình dạng và vị trí xuất hiện đầu tiên của rùa___:
	- Thay đổi vị trí xuất hiện đầu tiên để tránh việc rùa tự dưng xuất hiện giữa đường đua và đi tới vị trí xuất phát (nhìn hơi... kì kì `:v`)
	- Trong lúc thay đổi những thứ trên của rùa, ta sẽ tạm thời ẩn nó đi và chỉ cho xuất hiện lại sau khi đã hoàn tất