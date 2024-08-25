import cv2
import numpy as np
from sklearn.cluster import KMeans
from app.main.models import Color


def detect_colors() -> list[Color]:
    image_file = cv2.imread("app/main/flag.jpg")
    rgb_image = cv2.cvtColor(image_file, cv2.COLOR_BGR2RGB)

    pixels = rgb_image.reshape(-1, 3)

    # Number of popular colors to find
    cluster_count = 5

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
        color = {
            "red": int(color[0]),
            "green": int(color[1]),
            "blue": int(color[2]),
            "percentage": float(round(percentage, 2)),
            "hex_code": f"#{red:02x}{green:02x}{blue:02x}",
        }
        colors.append(
            color,
        )
    return colors
