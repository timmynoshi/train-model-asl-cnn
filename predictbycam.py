import tensorflow as tf
import cv2
import numpy as np

# Tải mô hình từ file .keras
model = tf.keras.models.load_model("model_level_3.keras")


def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 128, 128, 1)
    return feature / 255.0


# Thiết lập camera
cap = cv2.VideoCapture(0)
label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'blank']

while True:
    _, frame = cap.read()
    cv2.rectangle(frame, (0, 40), (300, 300), (0, 165, 255), 1)

    # Lấy vùng ảnh để dự đoán
    crop_frame = frame[40:300, 0:300]
    crop_frame = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)
    crop_frame = cv2.resize(crop_frame, (128, 128))
    crop_frame = extract_features(crop_frame)

    # Dự đoán với mô hình đã tải
    pred = model.predict(crop_frame)
    prediction_label = label[pred.argmax()]

    # Hiển thị kết quả dự đoán trên màn hình
    cv2.rectangle(frame, (0, 0), (300, 40), (0, 165, 255), -1)
    if prediction_label == 'blank':
        cv2.putText(frame, " ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    else:
        accu = "{:.2f}".format(np.max(pred) * 100)
        cv2.putText(frame, f'{prediction_label}  {accu}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)

    cv2.imshow("Output", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(10) == 27:
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
