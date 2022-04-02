# import picamera
# import RPi.GPIO as GPIO
import cv2

from functions import decode_image, get_product, update_stock

# camera = picamera.PiCamera()
cap = cv2.VideoCapture(1)


def start_camera():
    # camera.preview_fullscreen=False
    # camera.preview_window = (0, 0, 320, 240)
    # camera.resolution=(640,480)
    # camera.start_preview()

    if not cap.isOpened():
        print("Can`t open the video file!\n");
        exit()

    while cap.isOpened():

        # reads frame from a camera
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('Camera', frame)

        # Wait for 25ms
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def scan():
    # image_file = './image.png'
    # camera.capture(image_file)
    # camera.stop_preview()
    cap.release()
    ret, frame = cap.read()

    # barcode = decode_image(image_file)
    barcode = decode_image(frame)
    return get_product(barcode)


def save_product(product, quantity, form, root, update_products):
    update_stock(product, quantity)
    products_list = root.get_child('top_frame').get_child('products_list')
    update_products(products_list)
    form.grid_forget()
    form.destroy()

