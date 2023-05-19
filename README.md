Group J - ECE 4300 - Computer Architecture

Benchmarking Yolov8 by Ultralytics and comparing performance across multiple architectires

RTX 2060 GPU
https://youtu.be/h88KjdwtcYc

Intel i7 8th Gen CPU
https://youtu.be/RTncXm8Vb6Q

Intel i7 10th Gen CPU
https://youtu.be/Uhghl5ojdRU

Yolov8 Jetson Nano
https://youtu.be/p3NhEqIWMww

               YOLOv8 Benchmark Poster
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/8633954/bba5ca10-d502-4959-bcfd-a048851cb8b9)

              Laptop: 8th Gen Intel i7 CPU
Using CPU version of Pytorch on Laptop 8th gen i7 - Spectre x360
![flamegraph2](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/026ab956-a142-4d44-91ec-c25b43683a78)

Htop while idle
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/0f060a2c-5dc9-45e7-8988-7b83766c72b7)

Htop while running object detection program for office.mp4
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/2d27a2a5-8eb6-4cad-bafb-698a64d4adf1)

![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/f61d0f04-5589-4f7c-b529-3d1c7b1d7321)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/643c9a2e-7739-4a36-83c2-3d08f905707b)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/ec6ed922-577b-469c-aa3c-efbdf7b31eca)


sudo perf stat python3 testpic.py -i
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/9ec50c25-0237-495a-9765-4db9c2813619)



__________________________________________________________________________________________________________________________________________________________________________________________________________________________________


                    Laptop: 10th Gen Intel i7 CPU
Using CPU version of Pytorch on laptop with 10th gen i7 Cpu , no GPU usage on office.mp4
![flamegraph](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/262784c4-e8b9-4c84-a042-d445eee2c6df)

perf reports
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/f19b390c-25f1-44d3-9632-e00b62ecd791)


![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/d48c8ff5-434a-49de-97f3-dce7e7953366)

![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/9dd09d7b-283f-452a-abc9-2956b2db8be9)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/5a5fbf64-ee71-478f-8711-52fff8c73f89)

Idle CPU measured with htop
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/19c5a561-b155-4cd0-b78e-b62bd76f0124)

Htop while running Yolo on office.mp4
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/5925d964-5418-4b13-9425-d8f03e195986)




__________________________________________________________________________________________________________________________________________________________________________________________________________________________________



                    Jetson Nano Arm CPU
   ![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/08bd65e9-c261-40af-8897-e1a7328437b4)
   ![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/35311a0b-7fd2-4944-a469-cdceae8e803e)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/5873e3a5-15e7-4daa-bb9f-29ae3f20c563)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/313efd7c-e8ab-417e-bf35-628e2d81dedb)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/6dfdc339-8c81-4340-accf-3d16b0dc9732)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/f315e70d-3851-4164-bd31-0285dd0e7636)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/3a899289-b521-42d6-b8a5-7f8311565394)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/4bde25d8-9f89-46b7-9eae-fa7a1ae92a6b)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/035d2e3b-1e33-4cf5-8441-4dcdc938037d)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/d290fe18-a52d-472e-93a8-bb64b382b264)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/68ccc1ae-83ef-4e57-af47-3b5991049f29)
![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/238342d1-9e85-41ad-a52f-1ec1cba00b3c)


  Baseline Jetson Performance
                    ![image](https://github.com/california-polytechnic-university/ECE4300_Spring_2023_02_J/assets/98286393/a45fddd5-67c2-449c-90ed-be69128e2b0d)
                    




