import math

def calc_centroids():
    base_array = [[1,2,3,4,5],[5,4,3,2,1]]
    centroids = [[],[]]
    temp_array = []
    for row in range(0,len(base_array)) :
        for item in range(0,len(base_array)-1):
            print(calc_length(centroids[row,row+1],temp_array[row,row+1]))

def calc_length(self,centroid,element):
    centroid_x = self.centroid[0]
    centroid_y = self.centroid[1]
    element_x = self.element[0]
    element_y = self.element[1]
    function = math.sqrt(pow(element_x-centroid_x,2)+pow(element_y-centroid_y,2))
    return function


calc_centroids()