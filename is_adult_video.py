import sys
sys.path.insert(1, './netnude/nudenet')
from nudenet.detector import Detector as NudeDetector

detector = NudeDetector()

"""
    use stop_label array to stop whenever script found it
"""
hasil = detector.detect_video(
    "/Volumes/DATAEX/OneDrive/Movies/nsfw/_5QId8tdUHviAGyZ.mp4",
    show_progress=True,
    mode='fast',
    stop_label=['EXPOSED_BREAST_F', 'EXPOSED_GENITALIA_F',
                'EXPOSED_GENITALIA_M', 'EXPOSED_ANUS'],
    stop_value=0.70)

sexy = 0
nude = 0
count = 0
for key in hasil['preds']:
    for box in hasil['preds'][key]:
        print(box['label']+" "+str(box['score']))
        if box['label'] == 'EXPOSED_BREAST_F':
            if box['score'] >0.70:
                nude += 1
            else:
                count += 1
        if box['label'] == 'EXPOSED_GENITALIA_F':
            if box['score'] >0.70:
                nude += 1
            else:
                count += 1
        if box['label'] == 'EXPOSED_GENITALIA_M':
            if box['score'] >0.70:
                nude += 1
            else:
                count += 1
        if box['label'] == 'COVERED_GENITALIA_F':
            if box['score'] >0.70:
                sexy += 1
            else:
                count += 1
        if box['label'] == 'COVERED_BREAST_F':
            if box['score'] >0.70:
                sexy += 1
            else:
                count += 1
        if box['label'] == 'COVERED_BUTTOCKS':
            if box['score'] >0.70:
                sexy += 1
            else:
                count += 1
        if box['label'] == 'EXPOSED_BUTTOCKS':
            if box['score'] >0.70:
                sexy += 1
            else:
                count += 1
        if box['label'] == 'EXPOSED_BELLY':
            if box['score'] >0.70:
                sexy += 1
            else:
                count += 1
        if box['label'] == 'EXPOSED_ANUS':
            if box['score'] >0.70:
                nude += 1
            else:
                count += 1
print("nude: "+str(nude))
print("sexy: "+str(sexy))
print("Count: "+str(count))
