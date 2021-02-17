import matplotlib.pyplot as plt
import numpy as np
w = 0.1
sub = ["Introduction to Computing","Programming Fundamental","English Composition and Comprehensive","Applied Physics","Calculus"]
Ali_Amjad=[65,51,65,62,65]
# Muhammad_Zaid=[58,55,60,56,60]
# Hammad_Imran=[78,60,61,52,60]
# Syed_Hamza=[76,50,74,56,65]
# Ibrar_Bhatti=[71,60,50,59,50]
# Kanwal_Batool=[71,60,60,64,75]
# Abdul_Rafy=[68,51,52,57,75]
# Hamza_Mustafa=[86,85,60,80,80]
# Junaid_Rafique=[52,50,56,54,60]
# Husnain_Ali=[64,70,50,58,55]
# Muhammad_Basit =[56,50, 50,49,55]
# Muhammad_Numan=[79,55,67,62,75]
# Zartasha_Ahmad=[71,50,55,52,75]
# Junaid_Sultan=[59,50,50,57,55]
# Tayyab_Ghorsi=[60,50,55,57,53]
# Arslan_Raza=[70,80,60,60,60]
# Saveez_Muhammad=[60,50,60,52,55]
# Zain_Safdar_Dogar=[65,50,60,53,57]
# M_Hamza=[85,80,70,67,60]

bar1 = [0,1,2,3,4]
# bar3 =(i+w for i in bar2)
# bar4 =(i+w for i in bar3)
# bar5 =(i+w for i in bar4)
# bar6 =(i+w for i in bar5)
# bar7 =(i+w for i in bar6)
# bar8 =(i+w for i in bar7)
# bar9 =(i+w for i in bar8)
# bar10 =(i+w for i in bar9)
# bar11 =(i+w for i in bar10)
# bar12 =(i+w for i in bar11)
# bar13 =(i+w for i in bar12)
# bar14 =(i+w for i in bar13)
# bar15 =(i+w for i in bar14)
# bar16 =(i+w for i in bar15)
# bar17 =(i+w for i in bar16)
# bar18 =(i+w for i in bar17)
# bar19 =(i+w for i in bar18)

plt.bar(bar1,sub,Ali_Amjad,w,label="Ali Amjad(BDSM_F19_002)DataScience")
# plt.bar(bar2,sub,Muhammad_Zaid,w,label="Muhammad Zaid(BDSM_F19_004)DataScience")
# plt.bar(bar3,sub,Hammad_Imran,w,label="Hammad Imran(BDSM_F19_005),DataScience")
# plt.bar(bar4,sub,Syed_Hamza,w,label="Syed Hamza(BDSM_F19_008),DataScience")
# plt.bar(bar5,sub,Ibrar_Bhatti,w,label="Ibrar Bhatti(BDSM_F19_009),DataScience")
# plt.bar(bar6,sub,Kanwal_Batool,w,label="Kanwal Batool(BDSM_F19_010),DataScienc")
# plt.bar(bar7,sub,Abdul_Rafy,w,label="Abdul Rafy(BDSM_F19_012),DataScience")
# plt.bar(bar8,sub,Hamza_Mustafa,w,label="Hamza Mustafa(BDSM_F19_013),DataScience")
# plt.bar(bar9,sub,Junaid_Rafique,w,label="Junaid Rafique(BDSM_F19_014),DataScience")
# plt.bar(bar10,sub,Husnain_Ali,w,label="Husnain Ali(BDSM_F19_016),DataScience")
# plt.bar(bar11,sub,Muhammad_Basit,w,label="Muhammad Basit(BDSM_F19_018),Data Science")
# plt.bar(bar12,sub,Muhammad_Numan,w,label="Muhammad Numan(BDSM_F19_019),DataScience")
# plt.bar(bar13,sub,Zartasha_Ahmad,w,label="Zartasha Ahmed(BDSM_F19_020),DataScience")
# plt.bar(bar14,sub,Junaid_Sultan,w,label="Junaid Sultan(BDSM_F19_021),DataScience")
# plt.bar(bar15,sub,Tayyab_Ghorsi,w,label="Tayyab Ghorsi(BDSM_F19_022),DataScience")
# plt.bar(bar16,sub,Arslan_Raza,w,label="Arslan Raza(BAIM_F19_001),ArtificialIntelligence")
# plt.bar(bar17,sub,Saveez_Muhammad,w,label="Saveez Muhammad(BAIM_F19_003),ArtificialIntelligence")
# plt.bar(bar18,sub,Zain_Safdar_Dogar,w,label="Zain_Safdar_Dogar(BAIM_F19_004),ArtificialIntelligence")
# plt.bar(bar19,sub,M_Hamza,w,label="M Hamza(BAIM_F19_006),ArtificialIntelligence")


plt.xlabel(" Courses ")
plt.ylabel(" Marks")
plt.title("Student amoung Semester Courses")
plt.legend()
plt.show()