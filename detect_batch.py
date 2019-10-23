# *******************************************************************
# Detecting faces in images and clipping the face in separate folder
# 


import sys
import os
from glob import glob
from utils import *

#output-dir = 'outputs/'
#model-weights = './model-weights/yolov3-wider_16000.weights'
    
        

model_cfg = './cfg/yolov3-face.cfg'
model_weights = './model-weights/yolov3-wider_16000.weights'
net = cv2.dnn.readNetFromDarknet(model_cfg, model_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        

def _main():
    #wind_name = 'face detection using YOLOv3'
    #cv2.namedWindow(wind_name, cv2.WINDOW_NORMAL)
    det = 0
    
    output_file = 'outputs/'
    for img_file in glob("./images/*.jpg"):
        cap = cv2.imread(img_file)
        output_file = img_file[:-4].rsplit('/')[-1] + '_yoloface.jpg'
        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(cap, 1 / 255, (IMG_WIDTH, IMG_HEIGHT),
                                         [0, 0, 0], 1, crop=False)
        # Sets the input to the network
        net.setInput(blob)
        # Runs the forward pass to get output of the output layers
        outs = net.forward(get_outputs_names(net))
        # Remove the bounding boxes with low confidence
        faces = post_process(cap, outs, CONF_THRESHOLD, NMS_THRESHOLD)
        det = det + len(faces)
        fil = "faces/"
        ct = 0
        for face in faces:
           ct += 1
           x,y,w,h = face
           clip = cap[y:y+h,x:x+w]
           cv2.imwrite((os.path.join(fil))+str(ct)+".jpg",clip)
            
            
            
        
        
        
        print('[i] ==> # detected faces: {}'.format(len(faces)))
        with open("detected_faces.txt","a+") as f:
            if len(faces)  >= 1:
                f.write("found "+str(len(faces))+"  Total faces ="+str(det)+"\n")
        
        #print('#' * 60)
        # initialize the set of information we'll displaying on the frame
        info = [('number of faces detected', '{}'.format(len(faces)))
            ]
        for (i, (txt, val)) in enumerate(info):
            text = '{}: {}'.format(txt, val)
            cv2.putText(cap, text, (10, (i * 20) + 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR_RED, 2)

            # Save the output video to file
            #if img_file:
                #cv2.imwrite(os.path.join(output_file), cap.astype(np.uint8))
            #else:
                #video_writer.write(frame.astype(np.uint8))

            #cv2.imshow(wind_name, cap)

            #key = cv2.waitKey(1)
            #if key == 27 or key == ord('q'):
                #print('[i] ==> Interrupted by user!')
                #break

        #cap.release()
        cv2.destroyAllWindows()

        #print('==> All done!')
        #print('***********************************************************')


if __name__ == '__main__':
    _main()
