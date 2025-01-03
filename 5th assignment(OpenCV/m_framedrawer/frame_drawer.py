import cv2
import numpy as np

class TeamAssigner:
    def __init__(self, frames, tracks):
        self.frames = frames
        self.tracks = tracks
        self.team_colors = {}
        self.player_team = {}
    
    def get_clustering_model(self, image):
        if image.size == 0:
            raise ValueError("Input image is empty. Cannot perform clustering.")
        
        image_1d = image.reshape(-1, 3).astype(np.float32)
        if image_1d.shape[0] == 0:
            raise ValueError("Reshaped image has no samples. Check input image dimensions.")
        
        # Clustering model to separate pixels into player jersey and background
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(image_1d, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        return labels, centers
    
    def get_player_color(self, frame, bbox):
        x1, y1, x2, y2 = bbox
        cropped_image = frame[int(y1):int(y2), int(x1):int(x2)]
        if cropped_image.size == 0:
            raise ValueError("Cropped image is empty. Check the bounding box dimensions.")
        
        top_half_image = cropped_image[0:(cropped_image.shape[0] // 2), :]
        if top_half_image.size == 0:
            raise ValueError("Top half of the image is empty. Check the bounding box dimensions.")
        
        labels, centers = self.get_clustering_model(top_half_image)
        
        # Getting labels and finding the dominant color for the player
        clustered_image = labels.reshape(top_half_image.shape[0], top_half_image.shape[1])
        corner_clusters = [clustered_image[0, 0], clustered_image[0, -1], clustered_image[-1, 0], clustered_image[-1, -1]]
        non_player_label = max(set(corner_clusters), key=corner_clusters.count)
        player_label = 1 - non_player_label  # Assuming two clusters: 0 and 1
        player_color = centers[player_label]
        return player_color
    
    def assign_team_colour(self, frame_no=0):
        frame = self.frames[frame_no]
        player_dict = self.tracks['players'][frame_no]
        player_colors = []
        
        for _, bbox in player_dict.items():
            try:
                player_color = self.get_player_color(frame, bbox)
                player_colors.append(player_color)
            except Exception as e:
                print(f"Error extracting player color: {e}. Skipping this player.")
        
        if len(player_colors) < 2:
            print("Not enough player colors for clustering. Assigning default team colors.")
            self.team_colors[1] = np.array([255, 0, 0])  # Default color for Team 1 (Red)
            self.team_colors[2] = np.array([0, 0, 255])  # Default color for Team 2 (Blue)
            self.kmeans = None
            return self.team_colors
        
        player_colors = np.array(player_colors).astype(np.float32)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(player_colors, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        self.team_colors[1] = tuple(map(int, centers[0]))
        self.team_colors[2] = tuple(map(int, centers[1]))
        self.kmeans = centers
        return self.team_colors
    
    def get_player_team(self, frame, player_bbox, player_id):
        try:
            player_color = self.get_player_color(frame, player_bbox)
            if self.kmeans is None:
                raise ValueError("KMeans model is not initialized. Assigning default team.")
            
            distances = np.linalg.norm(self.kmeans - player_color, axis=1)
            team_id = np.argmin(distances) + 1  # Team IDs start from 1
        except Exception as e:
            print(f"Error assigning team to player {player_id}: {e}. Assigning default team.")
            team_id = 1  # Default team ID if assignment fails
        
        
        return team_id
    
    def assign_all_player_team(self):
        for frame_no, player_track in enumerate(self.tracks['players']):
            for player_id, bbox in player_track.items():
                try:
                    self.get_player_team(self.frames[frame_no], bbox, player_id)
                except Exception as e:
                    print(f"Error processing player {player_id} in frame {frame_no}: {e}. Skipping this player.")
        return self.player_team

class Annotator:
    def __init__(self,tracks,framees):
        self.tracker_data=tracks
        self.frames=framees
        self.team_assigner=TeamAssigner(self.frames,tracks)
        self.team_color=self.team_assigner.assign_team_colour()

    def draw(self):
        output_video_frames=[]
        print('annotating \n')
        for frame_no,frame in enumerate(self.frames):
            current_frame=frame.copy()
            player_dict=self.tracker_data['players'][frame_no]
            referee_dict=self.tracker_data['referees'][frame_no]
            ball_dict=self.tracker_data['ball'][frame_no]
            player_no={1:0,2:0}

            for track_id,bbox in player_dict.items():
                player_team=self.team_assigner.get_player_team(frame,bbox,1)
                current_frame=self.draw_rectangle(current_frame,bbox,self.team_color[player_team],track_id=track_id)
                if player_team==1:
                    player_no[1]+=1
                if player_team==2:
                    player_no[2]+=1 
            for track_id,bbox in referee_dict.items():
                current_frame=self.draw_rectangle(current_frame,bbox,(0,255,255))
            for track_id,bbox in ball_dict.items():
                current_frame=self.draw_rectangle(current_frame,bbox,(0,0,255))
            current_frame=self.add_player_count(current_frame,player_no,self.team_color)
            output_video_frames.append(current_frame)
            progress_bar(len(output_video_frames),len(self.frames),task='Annotating')
        return output_video_frames

    def draw_rectangle(self, frame, bbox, color, track_id=None):
        x1, y1, x2, y2 = bbox
        x_center, _ = self.get_bbox_center(bbox)
        width = self.get_bbox_width(bbox)

        # Draw the bounding rectangle
        cv2.rectangle(
            frame,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            color,
            thickness=2
        )

        if track_id is not None:
            # Define rectangle for track_id display
            rectangle_width = 40
            rectangle_height = 20
            x1_rect = x_center - rectangle_width // 2
            x2_rect = x_center + rectangle_width // 2
            y1_rect = (y2 - rectangle_height // 2) + 15
            y2_rect = (y2 + rectangle_height // 2) + 15
        
            # Draw filled rectangle for the track_id
            cv2.rectangle(
                frame,
                (int(x1_rect), int(y1_rect)),
                (int(x2_rect), int(y2_rect)),
                color,
                cv2.FILLED
            )

            # Adjust text placement
            x1_text = x1_rect + 12
            if track_id > 99:
                x1_text -= 10

            # Draw the track_id text
            cv2.putText(
                frame,
                f"{track_id}",
                (int(x1_text), int(y1_rect + 15)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                self.choose_text_color(*color),
                2
            )

        return frame

    def luminance(self, r, g, b):
        # Normalize the RGB values to 0-1
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        # Calculate luminance using the formula
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    def choose_text_color(self, r, g, b):
        lum = self.luminance(r, g, b)
        return (0, 0, 0) if lum > 0.5 else (255, 255, 255) 


    def get_bbox_center(self,bbox):
        x1,y1,x2,y2=bbox
        return (x1+x2)/2,(y1+y2)/2
        
    def get_bbox_width(self,bbox):
        x1,y1,x2,y2=bbox
        return (x2-x1)

    def add_player_count(self,frame,team_no_of_player,team_color):
        clr_teamA=team_color[1]
        clr_teamB=team_color[2]

        text1 = f"Number of players team A: {team_no_of_player.get(1) if team_no_of_player.get(1)<=11 else 11}"
        text2 = f"Number of players team B: {team_no_of_player.get(2) if team_no_of_player.get(2)<=11 else 11}"
        position1 = (5, 30)  # Slight offset from the top-left corner for visibility
        position2 = (5, 60)
        font = cv2.FONT_HERSHEY_TRIPLEX
        font_scale = 1  # Adjust font size as neede
        thickness = 2  # Thin text for neatness
        outline_color = (0, 0, 0)
        frame = self.put_text_with_outline(frame, text1, position1, font, font_scale, clr_teamA, thickness, outline_color)
        frame = self.put_text_with_outline(frame, text2, position2, font, font_scale, clr_teamB, thickness, outline_color)
        return frame
    def put_text_with_outline(self,image, text, position, font, font_scale, color, thickness, outline_color):
         # Draw the outline by adding text at different offsets
        offsets = [(-1, -1), (1, -1), (-1, 1), (1, 1)]  # The outline offset directions
        for offset in offsets:
            x_offset, y_offset = offset
            image = cv2.putText(image, text, (position[0] + x_offset, position[1] + y_offset), font, font_scale, outline_color, thickness + 2)
            # Draw the main text on top
            image = cv2.putText(image, text, position, font, font_scale, color, thickness)
        return image
    
def progress_bar(progress, total, bar_length=50, task=' '):
    percent = (progress / float(total)) * 100
    filled_length = int(bar_length * progress // total)  
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    
    # Print the task and progress bar on the same line
    print(f'{task}: \r|{bar}| {percent:.2f}%', end='\r')

    # Move to the next line once progress is complete
    if progress == total:
        print()