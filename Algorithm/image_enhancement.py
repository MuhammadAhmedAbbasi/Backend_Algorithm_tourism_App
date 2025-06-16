from diffusers import StableVideoDiffusionPipeline
import torch

pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt",
    torch_dtype=torch.float16,
    variant="fp16",
)
pipe.to("cuda")

# Load an image (e.g., PIL format)
from PIL import Image
image = Image.open(r"D:\backend_algorithm_blind_person_guidance\other_materials\test2.jpg")

# Generate video (no prompt required, but can be added)
frames = pipe(image, decode_chunk_size=8).frames[0]
frames[0].save("output.gif", save_all=True, append_images=frames[1:], loop=0)