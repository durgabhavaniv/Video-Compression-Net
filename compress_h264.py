from pathlib import Path
import os
suffix = ".png"
input_path= Path.home() / "ai_video_compression/Video-Compression-Net/demo/input"
file_paths= [subp for subp in input_path.rglob('*') if  suffix == subp.suffix]
file_paths.sort()

output_path =  Path.home() / "ai_video_compression/Video-Compression-Net/demo/h264_compressed"
output_path.mkdir(parents=True, exist_ok=True)


for file_p in file_paths:
    input = str(file_p)
    output = str(  output_path / file_p.name  )
    command = f"ffmpeg -i {input} -vcodec libx264 -y {output}"
    os.system(command)
