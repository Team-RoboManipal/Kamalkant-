from m_utils import read_video,save_video
from m_tracker import Tracker
from m_framedrawer import Annotator
import time
def main():
    start_time = time.time()
    frames=read_video('input_video/sample.mp4')
    #Detection and Tracking
    tracker=Tracker('model/dnn_model.cfg','model/dnn_weights.weights','model/classes.names')
    tracks=tracker.get_object_track(frames)
    #Annotating
    annotater=Annotator(tracks,frames)
    output_video_frames=annotater.draw()
    save_video(output_video_frames,'output_video/sample.mp4')
    
    end_time = time.time()
    total_time = end_time - start_time
    fps = len(frames) / total_time
    print(f"FPS: {fps:.2f}")

if __name__=='__main__':
    main()
