import cv2
import numpy as np
import os

def extract_hog_features(image):

    resized_image = cv2.resize(image, (64, 128))
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)


    hog = cv2.HOGDescriptor()
    features = hog.compute(gray)
    return features

def canny_edge_detection(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    v = np.median(gray)
    lower = int(max(0, 0.66 * v))
    upper = int(min(255, 1.33 * v))
    edges = cv2.Canny(gray, lower, upper)
    return edges

def hog_feature_matching(input_image, templates):

    input_hog_features = extract_hog_features(input_image)

    best_match = None
    best_score = float('inf')
    scores = []

    
    for template_path, label in templates:
        template = cv2.imread(template_path)

        if template is None:
            print(f"Error loading template: {template_path}")
            continue

        template_hog_features = extract_hog_features(template)


        distance = np.linalg.norm(input_hog_features - template_hog_features)

        scores.append((label, distance))
        if distance < best_score:
            best_score = distance
            best_match = label

    return best_match, scores

def main():

    input_image_path = r"C:\Users\srikar\Downloads\test5.png"
    templates = [
        (r"C:\Users\srikar\Downloads\STOPsign.jpg", "STOP"),
        (r"C:\Users\srikar\Downloads\GiveWay.jpg", "Give Way"),
        (r"C:\Users\srikar\Downloads\NoEntry.png", "No Entry"),
        (r"C:\Users\srikar\Downloads\SpeedLimit.png", "Speed Limit"),
        (r"C:\Users\srikar\Downloads\Uturn.png", "U turn Prohibited")
    ]


    input_image = cv2.imread(input_image_path)

    if input_image is None:
        print("Error: Input image not found!")
        return


    input_edges = canny_edge_detection(input_image)


    best_match, scores = hog_feature_matching(input_image, templates)


    print(f"Best Match: {best_match}")
    print("HOG Distance Scores:")
    for label, score in scores:
        print(f"{label}: {score:.4f}")


    cv2.imshow("Input Image", input_image)
    cv2.imshow("Canny Edges", input_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
