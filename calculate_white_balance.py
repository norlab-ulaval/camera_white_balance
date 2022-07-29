import matplotlib.pyplot as plt
import numpy as np
import cv2 # BGR
import sys

### Functions

def select_center_image(image_original):
    r = cv2.selectROI("ROI Selector", image_original, fromCenter=False)
    cv2.destroyAllWindows()
    image_cropped = image_original[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.imshow("Image Cropped", image_cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_cropped

def print_ratios_from_mean_pixels(image):
    ratios = [np.mean((image[:,:,1])/(image[:,:,i])) for i in range(0,3)]
    print(f"Ratio G/B: {ratios[0]}\nRatio G/G: {ratios[1]}\nRatio G/R: {ratios[2]}")
    return ratios

def show_evolution_width_image_and_ratio_from_width(image, ratios, value_max_channel):
    fig = plt.figure()
    ax = fig.add_subplot()
    x_axis = np.linspace(0, image.shape[1], image.shape[1])
    color = ["blue", "green", "red"]
    ax.table(
        cellText=[[f"{ratios[0]:.5f}"],[f"{ratios[1]:.5f}"],[f"{ratios[2]:.5f}"]],
        cellLoc="center",
        colWidths=[0.3]*1,
        colLabels=["Ratio Channel/Green"],
        rowLabels=["Blue", "Green", "Red"],
        zorder=5,
        loc=0   
    )
    for i in range(0,3):
        ax.plot(x_axis, image[int(image.shape[0]/2), :,i]/value_max_channel, color=color[i])
    ax.set_title("Ratio colors along width image.\nStraight lines if cropped image is valid for white balance")
    ax.set_xlabel("width camera image (pixel)")
    ax.set_ylabel("Channels intensity (normalized)")
    ax.set_ylim([0,1])
    plt.savefig("ratio_along_width.png")
    return


def main():
    max_value = 255 #8 bits
    try:
        image = cv2.imread(sys.argv[1])
    except:
        print("Please enter a valid image file as first argument. The second argument is a boolean to save a graph of the ratio along one line of the image")
        exit()
    if image is None:
        print("File name not valid. Need to give an image format. Please enter a valid image file as first argument.")
        exit()
    image_center = select_center_image(image)
    ratios = print_ratios_from_mean_pixels(image_center)
    if sys.argv[2] == "True":
        show_evolution_width_image_and_ratio_from_width(image_center, ratios, max_value)

if __name__ == "__main__":
    main()
