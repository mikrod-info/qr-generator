import os
import qrcode
from PIL import Image

BASE_URL = "https://mikrod-info.github.io/carteles-accesibles/carteles"
OUTPUT_DIR = "output"
LOGO_PATH = "assets/PNG.png"
COLOR = "black"
BG_COLOR = "white"
LOGO_DIM = 0.2
START = 1
END = 20

def generate_qr(cartel_id):
    url = f"{BASE_URL}/cartel-{cartel_id:02}/"

    qr = qrcode.QRCode(
            version = None,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
            )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=COLOR, back_color=BG_COLOR).convert("RGB")

    if LOGO_PATH and os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH)

        qr_width, qr_height = img.size
        logo_size = int(qr_width * LOGO_DIM)


        logo = logo.resize((logo_size, logo_size))

        pos = (
                (qr_width - logo_size) // 2,
                (qr_height - logo_size) // 2
                )
        
        if logo.mode in ("RGBA", "LA"):
            img.paste(logo, pos, logo)
        else:
            img.paste(logo, pos)

    filename = f"qr-cartel-{cartel_id:02}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)

    img.save(filepath)
    print(f"[OK] {filename} -> {url}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for i in range (START, END + 1):
        generate_qr(i)

if __name__ == "__main__":
    main()
