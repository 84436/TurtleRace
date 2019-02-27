# CÀI ĐẶT

# Nhạc nền
# Đặt file trong thư mục "Audio" và ghi tên file (bỏ đuôi .gif) trong dấu nháy đơn
# Đặt None để tắt nhạc
Audio_BGM = 'ProtectorsOfTheEarth'
Audio_Win = 'win'

# Hình nền
# Đặt file trong thư mục "Backgrounds" và ghi tên file (bỏ đuôi .gif) trong dấu nháy đơn
# Đặt None để bỏ hình nền
## 800x800
BGPfile = 'bg2'

# Số rùa/số đường đua
# Phải đảm bảo số này <= số con vật có trong set đã chọn
# (trong phần "Hình dạng con rùa" bên dưới)
# và <= số màu có trong turtleColors
c = 4

# Số lượt đua
# (1=1đi, 2=1đi+1về, 3=2đi+1về, 4 =2đi+2về, v.v.)
raceCount = 2

# Đường đua
initX = -300
initY = 100
trackCount = c
trackUnitLength = 20
trackUnitCount = [10, 20, 30] # 3 mức short, medium, long
trackWidth = 60
trackDivPadding = 10

# Rùa
turtleCount = c
turtleColors = ['red', 'orange', 'green', 'blue', 'violet', 'purple', 'brown', 'black']
turtleMoveLength = [10, 15, 20]
turtleBackStopBias = 6 # giá trị trong khoảng 0 - 10

# Hình dạng con rùa
# Đặt tất cả các file trong thư mục "Characters" và ghi các tên file (bỏ đuôi .gif) vào một set
Set1 = ['chicken', 'horse', 'pig', 'sheep']
Set2 = ['butterfly', 'grasshopper', 'turtle', 'unicorn', 'fish']
Set3 = ['Meu2', 'Penguin2', 'Tho2', 'Pikachu']
Set4 = ['Moe_OwO', 'Tho_OwO', 'ThoConCho', 'Jerry', 'Totoro']
# turtleShapes = chọn tên set con vật sẽ dùng
turtleShapes = Set4

# Bảng điểm
rankInitX = -250
rankInitY = -150
rankWidth = 100