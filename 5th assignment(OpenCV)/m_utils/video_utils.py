import cv2 
def progress_bar(progress, total, bar_length=50, task=' '):
    percent = (progress / float(total)) * 100
    filled_length = int(bar_length * progress // total)  
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    
    # Print the task and progress bar on the same line
    print(f'{task}: \r|{bar}| {percent:.2f}%', end='\r')

    # Move to the next line once progress is complete
    if progress == total:
        print()

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    print("Readed ",len(frames)," Frames!")  
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    print('saving \n')
    # Write each frame to the video
    for i,frame in enumerate(output_video_frames):
        out.write(frame)
        progress_bar(i,len(output_video_frames),task='Saving video:')
    
    # Release the video writer
    out.release()
    progress_bar(1,1,task='Saving video:')
    print('\n')
    print(f"Video sucessfully saved to {output_video_path}")