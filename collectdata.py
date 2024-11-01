import os
import cv2


directory = 'dataASL/'
def TaoFolder(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    if not os.path.exists(f'{directory}/blank'):
        os.mkdir(f'{directory}/blank') # tạo thư mục rỗng (chứa ảnh nền)

    for i in range(97, 123):
        letter = chr(i)
        if not os.path.exists(f'{directory}/{letter}'):
            os.mkdir(f'{directory}/{letter}') # tạo từng thư mục chữ cái

TaoFolder(directory)
# ----------------------------------------------------------

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    count = {
        'a': len(os.listdir(directory + "/a")),
        'b': len(os.listdir(directory + "/b")),
        'c': len(os.listdir(directory + "/c")),
        'd': len(os.listdir(directory + "/d")),
        'e': len(os.listdir(directory + "/e")),
        'f': len(os.listdir(directory + "/f")),
        'g': len(os.listdir(directory + "/g")),
        'h': len(os.listdir(directory + "/h")),
        'i': len(os.listdir(directory + "/i")),
        'j': len(os.listdir(directory + "/j")),
        'k': len(os.listdir(directory + "/k")),
        'l': len(os.listdir(directory + "/l")),
        'm': len(os.listdir(directory + "/m")),
        'n': len(os.listdir(directory + "/n")),
        'o': len(os.listdir(directory + "/o")),
        'p': len(os.listdir(directory + "/p")),
        'q': len(os.listdir(directory + "/q")),
        'r': len(os.listdir(directory + "/r")),
        's': len(os.listdir(directory + "/s")),
        't': len(os.listdir(directory + "/t")),
        'u': len(os.listdir(directory + "/u")),
        'v': len(os.listdir(directory + "/v")),
        'w': len(os.listdir(directory + "/w")),
        'x': len(os.listdir(directory + "/x")),
        'y': len(os.listdir(directory + "/y")),
        'z': len(os.listdir(directory + "/z")),
        'blank': len(os.listdir(directory + "/blank")),
        'predict': len(os.listdir(directory + "/predict"))
    }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame, (40, 40), (300, 300), (255, 255, 255), 2)
    cv2.imshow("main", frame)
    frame = frame[40:300, 40:300]
    cv2.imshow("cut", frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (128, 128))
    interrupt = cv2.waitKey(10)

    if interrupt == 27: # ESC để thoát
        break
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory + 'a/' + str(count['a'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory + 'b/' + str(count['b'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory + 'c/' + str(count['c'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory + 'd/' + str(count['d'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory + 'e/' + str(count['e'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(directory + 'f/' + str(count['f'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory + 'g/' + str(count['g'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(directory + 'h/' + str(count['h'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory + 'i/' + str(count['i'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(directory + 'j/' + str(count['j'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(directory + 'k/' + str(count['k'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(directory + 'l/' + str(count['l'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(os.path.join(directory + 'm/' + str(count['m'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(os.path.join(directory + 'n/' + str(count['n'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(os.path.join(directory + 'o/' + str(count['o'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(os.path.join(directory + 'p/' + str(count['p'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(os.path.join(directory + 'q/' + str(count['q'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(os.path.join(directory + 'r/' + str(count['r'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(directory + 's/' + str(count['s'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(directory + 't/' + str(count['t'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(os.path.join(directory + 'u/' + str(count['u'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(directory + 'v/' + str(count['v'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory + 'w/' + str(count['w'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(os.path.join(directory + 'x/' + str(count['x'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(directory + 'y/' + str(count['y'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(os.path.join(directory + 'z/' + str(count['z'])) + '.jpg', frame)
    if interrupt & 0xFF == ord('.'):
        cv2.imwrite(os.path.join(directory + 'blank/' + str(count['blank'])) + '.jpg', frame)
    if interrupt & 0xFF == ord(','):
        cv2.imwrite(os.path.join(directory + 'predict/' + str(count['predict'])) + '.jpg', frame)


cap.release()
cv2.destroyAllWindows()
