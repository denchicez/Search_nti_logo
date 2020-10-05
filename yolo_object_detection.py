import cv2                                                                                   # import libraries
import numpy as np                                                                           # 
import glob                                                                                  #
if __name__ == "__main__":                                                                   # Start main file
    net = cv2.dnn.readNet("yolov3_training_last.weights", "yolov3_testing.cfg")              # Read deep learning network  
    path = input()                                                                           # Introduce path of image
    layer_names = net.getLayerNames()                                                        # Download layers YOLO neural network
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]           # Convertation layers
    img = cv2.imread(path)                                                                   # Open image file
    img = cv2.resize(img, None, fx=0.4, fy=0.4)                                              # Resize image
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)      # Interpreter image
    net.setInput(blob)                                                                       # Set the new input value for the network.
    outs = net.forward(output_layers)                                                        # Compute output of layee
    for out in outs:                                                                         # Searsh in outs
        for detection in out:                                                                # 
            scores = detection[5:]                                                           # get results
            class_id = np.argmax(scores)                                                     # search max values accuracy
            accuracy = scores[class_id]                                                      # get max accuracy
            if accuracy > 0.3:                                                               # if accuracy>0.3
                print("kruzhok")                                                             # Withdraw "kruzhok"
                break                                                                        # end script
