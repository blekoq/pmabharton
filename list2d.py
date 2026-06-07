#data player game roblox dari tahun 2024-2026
dataRobloxGame=[[2,1,0.1],#SAB  
                [0.6,4,1.2,0.2],#Theforge
                [0.7,0.4,0.1]]#towerdefense
print("apakah pemain Theforge lebih banyak dari SAB di tahun 2025? ",dataRobloxGame[1][3],dataRobloxGame[0][2])
dataRobloxGame2={"SAB":{2024:2,2025:1,2026:0.1},
                 "Theforge":{2023:0.6,2024:4,2025:1.2,2026:0.2},
                 "towerdefense":{2024:0.7,2025:0.4,2026:0.1}}
print("apakah pemain Theforge lebih banyak dari SAB di tahun 2025? ",dataRobloxGame2["Theforge"][2023] > dataRobloxGame2["SAB"][2025])        