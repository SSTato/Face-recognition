import cv2
def read_video_write(videoName,a):
    '''
    读取视频并保存截帧

    cv2.imwrite(filename, frame)
    '''
    cap = cv2.VideoCapture(videoName)

    # 视频属性
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取原视频的宽
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取原视频的搞
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # 帧率
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))  # 视频的编码

    n, i = 0, 0  # 总的帧数，保存的第i张图片

    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            break
        if ret:
            n += 1
            if n % fps == 0:
                i += 1
                filename = '{:0>4}.png'.format(str(i))
                path = 'C:/Users/Administrator/Desktop/121/'
                filename = path+str(a)+filename
                cv2.imwrite(filename, frame)  # 存入快照
                cv2.imshow('frame', frame)
                key = cv2.waitKey(1) & 0xff
                if key == ord('q'):
                    break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    #read_video_write('D:/xl/Xmp/profiles/截图/NOR_0000000_000000_20220729_082137_000120228171421392.mp4')
    import os

    current_path = 'D:/xl/Xmp/profiles/截图/'

    filename_list = os.listdir(current_path)

    for filename in filename_list:
        a = filename_list.index(filename)
        filename = current_path+filename
        read_video_write(filename,a)