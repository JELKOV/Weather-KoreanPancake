import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

koreanPancake_2021 = "csvFile/2021_부침개_네이버_일간검색트렌드.csv"
koreanPancake_2022 = "csvFile/2022_부침개_네이버_일간검색트렌드.csv"
koreanPancake_2023 = "csvFile/2023_부침개_네이버_일간검색트렌드.csv"
koreanPancake_2024 = "csvFile/2024_부침개_네이버_일간검색트렌드.csv"
koreanPancakeCSVArr = [koreanPancake_2021,koreanPancake_2022,koreanPancake_2023,koreanPancake_2024]

koreanPancakeArr2021 = []
koreanPancakeArr2022 = []
koreanPancakeArr2023 = []
koreanPancakeArr2024 = []
koreanPancakeArr = [koreanPancakeArr2021,koreanPancakeArr2022,koreanPancakeArr2023,koreanPancakeArr2024]

# for i in range(len(koreanPancakeCSVArr)):
#     with open(koreanPancakeCSVArr[i], mode='r',encoding="UTF-8") as file :
#         reader = csv.reader(file)
#         header = next(reader)
#         for row in reader:
#             koreanPancakeArr[i].append(row)

def dateType(i,dateString):
    return pd.to_datetime(koreanPancakeArr[i][dateString])

#아래 for문을 하드코딩한
# koreanPancakeArr[0] = pd.read_csv(koreanPancakeCSVArr[0])
# koreanPancakeArr[1] = pd.read_csv(koreanPancakeCSVArr[1])
# koreanPancakeArr[2] = pd.read_csv(koreanPancakeCSVArr[2])
# koreanPancakeArr[3] = pd.read_csv(koreanPancakeCSVArr[3])
for i in range(len(koreanPancakeArr)):
    koreanPancakeArr[i] = pd.read_csv(koreanPancakeCSVArr[i])
    koreanPancakeArr[i]['period'] = dateType(i,'period')

plt.figure(figsize=(15,10))
plt.plot(koreanPancakeArr[0]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[0]['searchVolume'])
plt.plot(koreanPancakeArr[1]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[1]['searchVolume'])
plt.plot(koreanPancakeArr[2]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[2]['searchVolume'])
plt.plot(koreanPancakeArr[3]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[3]['searchVolume'])
plt.show()