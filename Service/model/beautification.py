import cv2
import numpy as np
from Service.config import (  # Directly import from config
    DEFAULT_CONTRAST,
    DEFAULT_BRIGHTNESS,
    DEFAULT_SATURATION,
    DEFAULT_SHARPNESS,
    JPEG_QUALITY
)

class ImageEnhancer:
    @staticmethod
    def beautify_image(image_bytes: bytes) -> bytes:
        """Applies fixed enhancement settings to an image"""
        try:
            # Decode image
            img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
            if img is None:
                raise ValueError("Invalid image data")

            # Convert to float for processing
            img = img.astype(np.float32) / 255.0

            # 1. Apply contrast (0.8 makes image slightly softer)
            img = np.clip((img - 0.5) * DEFAULT_CONTRAST + 0.5, 0, 1)

            # 2. Apply brightness (+18/255)
            img = np.clip(img + DEFAULT_BRIGHTNESS/255, 0, 1)

            # 3. Apply saturation (1.35x boost)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hsv[:,:,1] = np.clip(hsv[:,:,1] * DEFAULT_SATURATION, 0, 1)
            img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

            # 4. Apply sharpness
            kernel = np.array([[-1,-1,-1], [-1,11,-1], [-1,-1,-1]]) / (DEFAULT_SHARPNESS * 2)  # 1.5 sharpness equivalent
            img = cv2.filter2D(img, -1, kernel)

            # Convert back to bytes
            img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
            _, jpeg_bytes = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
            
            return jpeg_bytes.tobytes()

        except Exception as e:
            raise ValueError(f"Enhancement failed: {str(e)}")