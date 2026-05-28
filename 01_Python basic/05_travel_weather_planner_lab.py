distance_mi=1

is_raining= False

has_bike= True

has_car=True

has_ride_share_app=True

if (distance_mi == False):
    print("False")

elif(distance_mi<=1 and is_raining==False):
    print("True")
elif(distance_mi>1 and distance_mi<=6 and has_bike and is_raining==False):
    print("True")

elif(distance_mi > 6 and (has_car or has_ride_share_app)) :
    print("True") 

else:
    print("False")
