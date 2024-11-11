import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# Tải mô hình đã lưu
model = load_model('model_128batch_100epoch.keras')

# Đường dẫn đến hình ảnh cần dự đoán
image_path = 'dataASL/predict/2.jpg'

# Đọc hình ảnh
image = cv2.imread(image_path)

# Tiền xử lý hình ảnh
image_orig = image.copy()  # Lưu bản gốc để hiển thị
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Chuyển đổi sang ảnh xám
image = cv2.resize(image, (128, 128))  # Kích thước phải khớp với kích thước đầu vào của mô hình
image = image.astype("float32") / 255.0  # Chuẩn hóa hình ảnh
image = img_to_array(image)  # Chuyển đổi hình ảnh thành mảng NumPy
image = np.expand_dims(image, axis=0)  # Thêm chiều cho batch size

# Dự đoán
predictions = model.predict(image)
predicted_class = np.argmax(predictions, axis=1)  # Lấy lớp có xác suất cao nhất

# Danh sách các lớp
class_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'blank'] # Thay đổi nếu bạn có thêm lớp khác
# Hiển thị kết quả
print(f'Dự đoán: {class_labels[predicted_class[0]]}')

# Hiển thị hình ảnh và dự đoán
plt.imshow(cv2.cvtColor(image_orig, cv2.COLOR_BGR2RGB))  # Chuyển đổi BGR sang RGB
plt.title(f'Dự đoán: {class_labels[predicted_class[0]]}')
plt.axis('off')  # Tắt trục
plt.show()

# alo