# T_BGM.py
Phát nhạc nền

#### Chức năng
Phát file âm thanh được định nghĩa trong `BGMfile` trong file `_SETTINGS_.py` dưới nền

#### Mô tả
Chức năng trên được thực hiện bởi `PlaySound()` trong thư viện `winsound`.

Flag đi kèm trong tham số thứ 2 của hàm bao gồm `SND_LOOP` (lặp lại file âm thanh này sau khi kết thúc) và `SND_ASYNC` ("không đồng bộ"; yêu cầu `PlaySound()` return lập tức để tránh chặn phần sau của chương trình không được chạy.)