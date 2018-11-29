clip.greyscale()
bilinearresize(clip.Width * 320 / clip.Height,320)
trim(clip.FrameCount / 2 - 500, clip.FrameCount / 2 + 500)
