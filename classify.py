import glob
import datetime
import inference
import numpy as np
flist = []
def run_classifier():
        flist = []
        list1 = glob.glob("./images/*.jpg")
        list1.sort()
        print("Printing the time of Interesting Events.....\n\n")
        temp = str(inference.run_inference_on_image())
        for i in range(len(list1) - 1):
                inference.imagePath = list1[i]
                temp2 = str(inference.run_inference_on_image2())
                inference.imagePath = list1[i+1]
                temp = str(inference.run_inference_on_image2())
                if temp2 != temp:
                        print("Time : " + str(datetime.timedelta(seconds=(i*3))))
                        flist.extend([i*3])
                else:
                        print("." ,)
        d = np.array(flist)
        d.sort()

        diff = [y - x for x, y in zip(*[iter(d)] * 2)]
        avg = sum(diff) / len(diff)

        m = [[d[0]]]

        for x in d[1:]:
            if x - m[-1][0] < avg:
                m[-1].append(x)
            else:
                m.append([x])


#        print(m)
#        print(type(m))
        with open('list.txt' , 'w') as f:
            print("Writing to file\n")
        for i in range(0 , (len(m))):
            with open('list.txt' , 'a') as f:
                print("\n", file=f)
                print("start time : " + str(datetime.timedelta(seconds = int((m[i][0])) ))  , file=f)
                print("end time : " + str(datetime.timedelta(seconds = int((m[i][len(m[i]) - 1])) )) , file=f )
        print("\n\nFinished Analysis\n\n")
        print("The timestanps of all interesting events is stored in a File named list.txt ")
if __name__ == '__main__':
        run_classifier()

