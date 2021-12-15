import matplotlib.pyplot as plt
import numpy as np
import cv2 # BGR
import sys

### Functions

def select_center_image(image_original):
    lenght_width = image_original.shape[1]/10
    length_height = image_original.shape[0]/10
    center = (image_original.shape[0]/2, image_original.shape[1]/2)
    image_center = image_original[int(center[0] - length_height):int(center[0] + length_height), int(center[1] - lenght_width):int(center[1] + lenght_width)]
    return image_center

def print_ratios_from_mean_pixels(image, max_value_intesity):
    ratios = [np.mean((image[:,:,1]/max_value_intesity)/(image[:,:,i]/max_value_intesity)) for i in range(0,3)]
    print(f"Ratio B/G: {ratios[0]}\nRatio G/G: {ratios[1]}\nRatio R/G: {ratios[2]}")
    return

def show_evolution_width_image_and_ratio_from_width(image, max_value_intesity):
    fig = plt.figure()
    ax = fig.add_subplot()
    x_axis = np.linspace(0, image.shape[1], image.shape[1])
    color = ["blue", "green", "red"]
    ratio = [np.mean((image[int(image.shape[0]/2), :,1]/max_value_intesity)/(image[int(image.shape[0]/2), :,i]/max_value_intesity)) for i in range(0,3)]
    ax.table(
        cellText=[[f"{ratio[0]:.5f}"],[f"{ratio[1]:.5f}"],[f"{ratio[2]:.5f}"]],
        cellLoc="center",
        colWidths=[0.3]*1,
        colLabels=["Ratio Channel/Green"],
        rowLabels=["Blue", "Green", "Red"],
        zorder=5,
        loc=0   
    )
    for i in range(0,3):
        ax.plot(x_axis, image[int(image.shape[0]/2), :,i]/max_value_intesity, color=color[i])
    ax.set_xlabel("width camera image (pixel)")
    ax.set_ylabel("Channels intensity (normalized)")
    ax.set_ylim([0,1])
    plt.show()
    return

### Parameters
max_value_intesity = 255 # 8bits

def main():
    try:
        image = cv2.imread(sys.argv[1])
    except:
        print("Please enter a valid image file as first argument. The second argument is a boolean to display the ratio along one line of the image")
        exit()
    if image is None:
        print("File name not valid. Need to give an image format. Please enter a valid image file as first argument.")
        exit()
    image_center = select_center_image(image)
    print_ratios_from_mean_pixels(image_center, max_value_intesity)
    if sys.argv[2] == "True":
        show_evolution_width_image_and_ratio_from_width(image_center, max_value_intesity)

if __name__ == "__main__":
    main()
