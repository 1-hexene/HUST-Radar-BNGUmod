from detect.Video import Video
from detect.Capture import Capture
import cv2
import time
from collections import deque
from ruamel.yaml import YAML


mode = "webcam" # "video" or "camera"
round = 11

if __name__ == '__main__':
    video_path = "videos/data/video.avi"
    detector_config_path = "configs/detector_config.yaml"
    binocular_camera_cfg_path = "configs/bin_cam_config.yaml"
    main_config_path = "configs/main_config.yaml"
    main_cfg = YAML().load(open(main_config_path, encoding='Utf-8', mode='r'))


    if mode == "video":
        capture = Video(video_path)
    elif mode == "webcam:":
        capture = cv2.VideoCapture(0)
    elif mode == "camera":
        capture = Capture(binocular_camera_cfg_path,"new_cam")

    # 使用mp4编码器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'camera0722_{round}.mp4', fourcc, 12, (capture.width,capture.height))  # 文件名，编码器，帧率，帧大小


    # fps计算
    N = 10
    fps_queue = deque(maxlen=N)
    start_time = time.time()


    # 主循环
    while True:

        frame = capture.get_frame()

        # 计算fps
        now = time.time()
        fps = 1 / (now - start_time)
        start_time = now
        fps_queue.append(fps)
        avg_fps = sum(fps_queue) / len(fps_queue)

        # 读图失败，推出
        if frame is None:
            print("no frame")
            break
        image = frame

        cv2.putText(image, "fps: {:.2f}".format(avg_fps), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 122),
                    2)

        out.write(image)
        # resize到1920*1080
        image = cv2.resize(image, (1920, 1280))
        cv2.imshow("frame", image)
        if cv2.waitKey(1) == ord('q'):
            break


    out.release()
    capture.release()

    cv2.destroyAllWindows()