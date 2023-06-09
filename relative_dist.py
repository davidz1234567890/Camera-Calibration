# import numpy as np
# #import cv2 #newline
# import cv2 as cv
# #import glob
# # import vid
# # Load previously saved data
# with np.load('B.npz') as X:
#     mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
#     print(mtx)

# def draw(img, corners, imgpts):
#     corner = tuple(corners[0].ravel())
#     print(corner)
#     print(tuple(imgpts[0].ravel()))
#     print(tuple(imgpts[1].ravel()))
#     print(tuple(imgpts[2].ravel()))
#     print(corner[0])
#     print(corner[1])
#     print(tuple(imgpts[0].ravel())[0])
#     print(tuple(imgpts[0].ravel())[1])
#     img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(imgpts[0].ravel())[0]), int(tuple(imgpts[0].ravel())[1])), (255,0,0), 5)
#     img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(imgpts[1].ravel())[0]), int(tuple(imgpts[1].ravel())[1])), (0,255,0), 5)
#     img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(imgpts[2].ravel())[0]), int(tuple(imgpts[2].ravel())[1])), (0,0,255), 5)
#     return img
 
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# objp = np.zeros((7*10,3), np.float32)
# objp[:,:2] = np.mgrid[0:10,0:7].T.reshape(-1,2)
# axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)


# #for fname in glob.glob('images/*.png'): #changed the stuff inside of the quote
#     #changed above to png, not jpg
# cap = cv.VideoCapture(0)

# while cap.isOpened():

#     success, img = cap.read()
#     cv.imshow('img', img)
#     #ret, frame = vid.read()
#     #print(fname)
#     #img = cv.imread(fname)
#     gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', gray)
#     ret, corners = cv.findChessboardCorners(gray, (10,7),None)
#     if ret == True:
#         corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
#         # Find the rotation and translation vectors.
#         print(corners2)
#         ret,rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)
#         # project 3D points to image plane
#         imgpts, jac = cv.projectPoints(axis, rvecs, tvecs, mtx, dist)
#         img = draw(img,corners2,imgpts)
#         cv.imshow('img',img)
#         cv.waitKey(1)
#         # k = cv.waitKey(0) & 0xFF
#         # if k == ord('s'):
#         #     cv.imwrite(fname[:6]+'.png', img)
#     else:
#         print("not detected")

# cap.release()
# cv.destroyAllWindows()


# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()





import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

with np.load('B.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
    print(mtx)


criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((7*10,3), np.float32)
objp[:,:2] = np.mgrid[0:10,0:7].T.reshape(-1,2)
axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)

def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    # print(corner)
    # print(tuple(imgpts[0].ravel()))
    # print(tuple(imgpts[1].ravel()))
    # print(tuple(imgpts[2].ravel()))
    # print(corner[0])
    # print(corner[1])
    # print(tuple(imgpts[0].ravel())[0])
    # print(tuple(imgpts[0].ravel())[1])
    img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(imgpts[0].ravel())[0]), int(tuple(imgpts[0].ravel())[1])), (255,0,0), 5)
    img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(imgpts[1].ravel())[0]), int(tuple(imgpts[1].ravel())[1])), (0,255,0), 5)
    img = cv.line(img, (int(corner[0]), int(corner[1])), (int(tuple(imgpts[2].ravel())[0]), int(tuple(imgpts[2].ravel())[1])), (0,0,255), 5)
    return img


def randrange(n, vmin, vmax):
            return (vmax - vmin)*np.random.rand(n) + vmin
        # """
        # Helper function to make an array of random numbers having shape (n, )
        # with each number distributed Uniform(vmin, vmax).
        # """
          
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    #cv.imshow('frame', gray)


    success, corners = cv.findChessboardCorners(gray, (10,7),None) #new line
    if success == True: #new conditional
        corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        # Find the rotation and translation vectors.
        # print(corners2)
        ret,rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)
        distance = np.linalg.norm(tvecs)
        

        #Fixing random state for reproducibility
        # np.random.seed(19680801)

        
            
        # fig = plt.figure()
        # ax = fig.add_subplot(projection='3d')

        # # n = 100
        # # # For each set of style and range settings, plot n random points in the box
        # # # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
        # # for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
        # #     xs = randrange(n, 23, 32)
        # #     ys = randrange(n, 0, 100)
        # #     zs = randrange(n, zlow, zhigh)
        # #     ax.scatter(xs, ys, zs, marker=m)

        # ax.set_xlabel('X Label')
        # ax.set_ylabel('Y Label')
        # ax.set_zlabel('Z Label')

        # print(tvecs)
        # ax.scatter(tvecs[0], tvecs[1], tvecs[2], c='red', marker='.', s=10)
        # plt.show()


        #for relative distance
        cv.waitKey(1000)
        ret, frame = cap.read() #new
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        success, corners = cv.findChessboardCorners(gray, (10,7),None)
        if success == True:
            corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            ret,rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)
            d = np.linalg.norm(tvecs)
            print(tvecs)
            #ax.scatter(tvecs[0], tvecs[1], tvecs[2], c='red', marker='.', s=1000)

        # project 3D points to image plane
            imgpts, jac = cv.projectPoints(axis, rvecs, tvecs, mtx, dist)
            img = draw(frame,corners2,imgpts)
            img = cv.putText(img, str(d - distance), (10,50), cv.FONT_HERSHEY_SIMPLEX, 1, 
                 (0,0,255), 2, cv.LINE_AA, False)
            cv.imshow('img',img)
            cv.waitKey(1)
        # k = cv.waitKey(0) & 0xFF
        # if k == ord('s'):
        #     cv.imwrite(fname[:6]+'.png', img)
            #break #temporary
    else:
        cv.imshow('img',frame)
        cv.waitKey(1)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()