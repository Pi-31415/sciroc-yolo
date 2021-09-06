import torch
import json

def detect_duplicate(data):
    distance_threshold = 100
    double_detection = False
    double_detected_objects_raw = []
    final_output = []
    print("\n-------------------------------------------------")
    print("OBJECT DETECTION\nDetected Objects and their centre location are : ")
    for result in data:
        print("    "+result['name']+" - ("+str(round((result['xmin']+result['xmax'])/2)) + ", " + str(round((result['ymin']+result['ymax'])/2))+")")
    import math
    from collections import Counter
    item_names_raw = []
    for obj in data:
        item_names_raw.append(obj['name'])
    c = Counter(item_names_raw) 
    unique_items = list(c.keys())
    #print(unique_items)
    duplicate_items = []
    # Get the items occuring more than once from image
    for name in unique_items:
        if(c[name] > 1):
            if(name != 'human'):
                duplicate_items.append(name)
    if(len(duplicate_items) == 0):
        print("No double detection found. Object Detection Results are clear.")
    else:
        print("\nDuplicate Detection started ...")
        print("Items occuring more than once are : "+str(duplicate_items)+"\n")
        duplicate_item_detail = []
        for obj in data:
            for name in duplicate_items:
                if(obj['name'] == name):
                    duplicate_item_detail.append(obj)
        #Perform duplicate detection by comparing the distances
        #Calculate center point
        index_duplicate = 0
        duplicate_list_id = []
        duplicate_list_name = []
        duplicate_list_center_points_x = []
        duplicate_list_center_points_y = []
        for item in duplicate_item_detail:
            center_pointx = round((item['xmin'] + item['xmax'])/2)
            center_pointy = round((item['ymin'] + item['ymax'])/2)
            duplicate_list_name.append(item['name'])
            duplicate_list_center_points_x.append(center_pointx)
            duplicate_list_center_points_y.append(center_pointy)
            duplicate_list_id.append(index_duplicate)
            index_duplicate += 1
        #print("\n\n\n" + str(duplicate_list_name)  + "\n\n\n")
        #print(str(duplicate_list_id)  + "\n\n\n")
        #print(str(duplicate_list_center_points_x)  + "\n\n\n")
        #print(str(duplicate_list_center_points_y)  + "\n\n\n")
        #print("\nDistance Analysis started ... \n")
        for i in duplicate_list_id:
            for j in duplicate_list_id:
                if(i!=j): # Compare not against same index
                    if(duplicate_list_name[i] == duplicate_list_name[j]): # For same items only
                        Px = duplicate_list_center_points_x[i]
                        Py = duplicate_list_center_points_y[i]
                        Qx = duplicate_list_center_points_x[j]
                        Qy = duplicate_list_center_points_y[j]
                        # Calculate the Euclidean distance 
                        # between points P and Q
                        Distance = round(math.sqrt( pow((Px-Qx),2) + pow((Py-Qy),2)))
                        #print(duplicate_list_name[i] + "["+str(i)+"]  against " +duplicate_list_name[j]+"["+str(j)+"]   dist = " + str(Distance))
                        if(Distance <= distance_threshold):
                            double_detection = True
                            print(duplicate_list_name[i] + "[("+str(Px)+","+str(Py)+")] and " +duplicate_list_name[j]+"[("+str(Qx)+","+str(Qy)+")], distance = " + str(Distance))
                            double_detected_objects_raw.append(duplicate_list_name[i])
        if(double_detection == False):
            print("\n\nNo objects are detected twice.")
        else:
            print("\nIt is highly likely that the  objects above are the same object detected twice.")
            #Prepare for output
            d = Counter(double_detected_objects_raw)
            # Prepare for returning as list
            final_output = list(d.keys())
    print("\n-------------------------------------------------\n")
    #print(final_output)
    return(final_output)


# Model
model = torch.hub.load('./', 'custom', path='runs/train/exp10/weights/last.pt', source='local')  # local repo

# Images
img = 'left0055.jpg'  # or file, PIL, OpenCV, numpy, multiple

# Inference
results = model(img)

# Results
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
json_results = json.loads(results.pandas().xyxy[0].to_json(orient="records"))

for result in json_results:
    print(result)

RESSS = detect_duplicate(json_results)

print(RESSS)
