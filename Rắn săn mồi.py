import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ trò chơi
window_width = 600
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))

# Đặt tiêu đề cho cửa sổ
pygame.display.set_caption("Rắn săn mồi")

# Màu sắc
snake_color = (0, 255, 0)  # Xanh lá cây
food_color = (255, 0, 0)   # Đỏ

# Kích thước ô vuông (độ dài của mỗi đoạn thân rắn)
block_size = 10

# Tọa độ ban đầu của rắn
snake_x = window_width / 2
snake_y = window_height / 2

# Danh sách các tọa độ của các đoạn thân rắn (ban đầu chỉ có một đoạn)
snake_body = [(snake_x, snake_y)]

# Tạo tọa độ ngẫu nhiên cho thức ăn
food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

# Biến kiểm soát trò chơi
game_over = False

# Tốc độ của rắn
snake_speed = 15
snake_x_change = 0
snake_y_change = 0

# Khởi tạo font chữ
font_style = pygame.font.SysFont(None, 30)

# Vòng lặp chính của trò chơi
while not game_over:

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_x_change == 0:
                snake_x_change = -block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT and snake_x_change == 0:
                snake_x_change = block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP and snake_y_change == 0:
                snake_y_change = -block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN and snake_y_change == 0:
                snake_y_change = block_size
                snake_x_change = 0

    # Cập nhật vị trí của rắn
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Kiểm tra va chạm
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    # Kiểm tra nếu rắn tự ăn chính mình
    for block in snake_body[1:]:
        if snake_x == block[0] and snake_y == block[1]:
            game_over = True

    # Vẽ nền
    screen.fill((0, 0, 0))  # Màu đen
    
    # Vẽ rắn và thức ăn
    for x, y in snake_body:
        pygame.draw.rect(screen, snake_color, [x, y, block_size, block_size])

    pygame.draw.rect(screen, food_color, [food_x, food_y, block_size, block_size])

    # Hiển thị điểm số
    score = len(snake_body) - 1
    value = font_style.render("Điểm của bạn: " + str(score), True, (255, 255, 255))
    screen.blit(value, [0, 0])
    
    # Cập nhật màn hình
    pygame.display.update()

    # Kiểm tra nếu rắn ăn mồi
    if snake_x == food_x and snake_y == food_y:
        # Tạo vị trí mới cho thức ăn
        food_x = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
        # Tăng độ dài của rắn
        snake_body.append((0, 0))  # Thêm một đoạn mới vào cuối

    # Di chuyển rắn
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1][0]
        y = snake_body[i - 1][1]
        snake_body[i] = (x, y)

    # Cập nhật đầu rắn
    snake_body[0] = (snake_x, snake_y)

    # Điều khiển tốc độ chơi
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

# Kết thúc trò chơi
print("Game Over!")
pygame.quit()
quit()
