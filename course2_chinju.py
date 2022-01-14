from dronekit import VehicleMode, connect
import time

vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True, timeout = 60)

#アーミング可能かチェック
while not vehicle.is_armable:
    print("初期化待ちです")
    time.sleep(1)

#アーミング実行　・・フライトモードを「GUIDED]に変更、アームＯＮ
# vehicle.mode = VehicleMode("GUIDED")
vehicle.wait_for_mode("GUIDED")

# vehicle.armed = True
vehicle.arm()


#目標高度を設定
targetAltitude = 20

print("離陸！")
vehicle.simple_takeoff(targetAltitude)

while True:
    print("高度：", vehicle.location.global_relative_frame.alt)

    if vehicle.location.global_relative_frame.alt >= targetAltitude*0.95:
        print("目標高度に到着しました　≫着陸開始！")
        vehicle.wait_for_mode("LAND")
        break
    time.sleep(1)