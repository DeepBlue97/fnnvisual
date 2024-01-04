
import cv2

from fnnfunctor.utils.bbox import X1Y1WHRatioBBox, CXCYWHPixBBox, X1Y1WHPixBBox


def draw_bbox(image, bbox, color=(0, 255, 0), thickness=2):
    # if isinstance(bbox, X1Y1WHRatioBBox):
    #     # left_top_point = [bbox[0], bbox[1]]
    #     # right_buttom_point = [bbox[0]+bbox[2], bbox[1]+bbox[3]]
    #     left_top_point = [bbox.xy.x, bbox.xy.y]
    #     right_buttom_point = [bbox.xy.x+bbox.wh.x, bbox.xy.y+bbox.wh.y]
    if isinstance(bbox, CXCYWHPixBBox):
        # left_top_point = [bbox[0]-bbox[2]/2, bbox[1]-bbox[2]/2]
        # right_buttom_point = [bbox[0]+bbox[2]/2, bbox[1]+bbox[3]/2]
        left_top_point = [bbox.xy.x-bbox.wh.x/2, bbox.xy.y-bbox.wh.y/2]
        right_buttom_point = [bbox.xy.x+bbox.wh.x/2, bbox.xy.y+bbox.wh.y/2]
    elif isinstance(bbox, X1Y1WHPixBBox):
        # left_top_point = [bbox[0]-bbox[2]/2, bbox[1]-bbox[2]/2]
        # right_buttom_point = [bbox[0]+bbox[2]/2, bbox[1]+bbox[3]/2]
        left_top_point = [bbox.xy.x, bbox.xy.y]
        right_buttom_point = [bbox.xy.x+bbox.wh.x, bbox.xy.y+bbox.wh.y]
    else:
        print(f'unsupported bbox type: {type(bbox)}')
        return None
    left_top_point = [int(i) for i in left_top_point]
    right_buttom_point = [int(i) for i in right_buttom_point]

    image_with_rectangle = cv2.rectangle(image, left_top_point, right_buttom_point, color, thickness)

    return image_with_rectangle
