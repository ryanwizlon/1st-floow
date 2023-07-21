import cv2
import numpy as np
from pymander import Scene, Texture

class VideoTexture:
    def __init__(self, video_file):
        self.video_file = video_file
        self.cap = cv2.VideoCapture(self.video_file)
        self.texture = None

    def update_texture(self):
        ret, frame = self.cap.read()
        if ret:
            self.texture = Texture(frame)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def get_texture(self):
        if self.texture is None:
            self.update_texture()
        return self.texture

def apply_video_texture(scene: Scene, video_texture: VideoTexture):
    video_texture.update_texture()
    scene.set_texture(video_texture.get_texture())

def main():
    scene = Scene()
    video_texture = VideoTexture('video_file.mp4')
    apply_video_texture(scene, video_texture)

if __name__ == "__main__":
    main()