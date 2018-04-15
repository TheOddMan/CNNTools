config_fromPath = "C:\\Users\\409LAB00\\Desktop\\Batik300"
config_toPath = "C:\\Users\\409LAB00\\Desktop\\NewBatikTrain\\DataSet"

config_rotation = "on"                                      #set 'on' will generate rotation images
config_rotation_amount = 40                                  #rotation images amount

config_shift = "on"                                        #set 'on' will generate shift images
config_shift_amount = 40                                    #shift images amount

config_zoom_out = "on"                                     #set 'on' will generate zoom out images
config_zoom_out_amount = 20                                 #zoom out images amount

config_zoom_in = "on"                                      #set 'on' will generate zoom in images
config_zoom_in_amount = 20                                  #zoom in images amount


# Conditio of usage : The sturcture in your 'config_fromPath' folder must be like
#                                B1     (folder)
#                                 |
#                                 |               |---------B1_1.jpg    (file)
#                                 | _______|---------B1_2.jpg    (file)
#                                                 |---------B1_3.jpg   ............
#                                B2     (folder)
#                                 |
#                                 |               |---------B2_1.jpg    (file)
#                                 | _______|---------B2_2.jpg    (file)
#                                                 |---------B2_3.jpg   ............
#                               。
#                               。
#                               。
#                               。
#                               。
#                                And your 'config_toPath' folder must have B1 folder,B2 folder,B3 folder........

