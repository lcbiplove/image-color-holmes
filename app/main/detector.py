import webcolors
import cv2
import numpy as np
from sklearn.cluster import KMeans


def detect_colors(filename, cluster_count=5) -> list[dict]:
    image_file = cv2.imread(filename)
    rgb_image = cv2.cvtColor(image_file, cv2.COLOR_BGR2RGB)

    pixels = rgb_image.reshape(-1, 3)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=cluster_count, random_state=0)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_

    counts = np.bincount(labels)

    sorted_indices = np.argsort(counts)[::-1]
    sorted_colors = colors[sorted_indices]
    sorted_counts = counts[sorted_indices]

    total_pixels = len(labels)
    color_percentages = sorted_counts / total_pixels * 100

    colors = []
    for color, percentage in zip(sorted_colors, color_percentages):
        red = int(color[0])
        green = int(color[1])
        blue = int(color[2])
        actual_color, closest_colour = get_colour_name((red, green, blue))
        hex_code = f"#{red:02x}{green:02x}{blue:02x}"
        color = {
            "red": int(color[0]),
            "green": int(color[1]),
            "blue": int(color[2]),
            "percentage": float(round(percentage, 2)),
            "hex_code": hex_code,
            "color_name": actual_color if actual_color else closest_colour,
        }
        colors.append(
            color,
        )
    return colors


def closest_colour(requested_colour):
    min_colours = {}
    for name in webcolors.names("css3"):
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name
