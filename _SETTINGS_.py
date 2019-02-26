# CÀI ĐẶT

# Nhạc nền
# Đặt tên file trong '' hoặc để None để tắt nhạc
BGMfile = None

# Số rùa/số đường đua
# Phải đảm bảo số này <= số con vật có trong set đã chọn
# (trong phần 'Hình dạng con rùa' bên dưới)
# và <= số màu có trong turtleColors
c = 4

# Số lượt đua (VD: 2 = có lượt đi lượt về)
raceCount = 3

# Đường đua
initX = -300
initY = 100
trackCount = c # số rùa = số đường đua
trackUnitLength = 20
trackUnitCount = [10, 20, 30] # 3 mức short, medium, long
trackWidth = 60
trackDivPadding = 10

# Rùa
turtleCount = c # số rùa = số đường đua
turtleColors = ['red', 'orange', 'green', 'blue', 'violet', 'purple', 'brown', 'black']
turtleMoveLength = [10, 15, 20]
turtleBackStopBias = 6 # giá trị trong khoảng 0 - 10

# Hình dạng con rùa
# Tên mỗi con vật trong set = tên file bỏ đuôi .GIF
# Tất cả con vật, bất kể set nào, đều phải được đặt trong ./Resources
Set1 = ['chicken', 'horse', 'pig', 'sheep']
Set2 = ['butterfly', 'grasshopper', 'turtle', 'unicorn', 'fish']
Set3 = []
Set4 = []
SetPepe = ['pepe1', 'pepe2', 'pepe3', 'pepe4']
# turtleShapes = chọn tên set con vật sẽ dùng
turtleShapes = SetPepe

# Bảng điểm
scoreboardPadding = 20