import cv2
import os


def save_frames_batch(frames, folder_frame_dir, start_frame):#将一批视频帧保存到指定文件夹中，文件名以起始帧号进行10位数字填充命名
    for i, frame in enumerate(frames):
        frame_name = str(start_frame + i).zfill(10) + ".jpg"
        frame_path = os.path.join(folder_frame_dir, frame_name)
        cv2.imwrite(frame_path, frame)


def split_full_video(video_name, output_dir, batch_size=100): #将输入视频分割为帧，并按批次和子文件夹保存。
    # video_path = os.path.join("videos", video_name)
    video_path = video_name
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Cannot open video file: {video_path}")
        return

    current_frame = 0
    frames_batch = []
    i = 0
    while True:
        i = i + 1
        ret, frame = cap.read()

        if not ret:
            # Save any remaining frames in the batch # 视频读取完毕，保存剩余帧
            if frames_batch:
                save_frames_batch(frames_batch, folder_frame_dir, current_frame - len(frames_batch))
            print(f"Video {video_name} has been split.")
            break

        if i < 60: # 每处理1帧后跳过后续14帧（共15帧取1帧）
            continue
        else:
            i = 0
        # 将当前帧加入批次
        frames_batch.append(frame)

        # Every 1000 frames, create a new folder每处理1000帧创建一个新子文件夹
        if current_frame % 1000 == 0:
            folder_frame_dir = os.path.join(output_dir, str(current_frame).zfill(10))
            os.makedirs(folder_frame_dir, exist_ok=True)

        # Once batch is full, save it to disk# 批次达到大小时保存帧
        if len(frames_batch) >= batch_size:
            save_frames_batch(frames_batch, folder_frame_dir, current_frame - len(frames_batch) + 1)
            frames_batch = []# 清空缓存

        print(f"Frame {current_frame} in video {video_name} has been saved.")
        current_frame += 1# 更新已处理帧计数
    # 释放视频资源SS
    cap.release()


if __name__ == '__main__':
    video_name =  r"E:\2025\thesis\CLF\360bike\20\20250415_night.mp4"# 输入视频路径
    output_dir = os.path.join("frames", video_name[:-4])
    split_full_video(video_name, output_dir)
