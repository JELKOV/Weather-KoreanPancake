#=============== import 시작 =================
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import ToyProject1
#=============== import 끝 =================

#================= csv 데이터 -> 배열 변환 시작 ===================
################### 검색량 csv 파일 주소 ##################
#월별 폴더 주소
file_path_07 = "csvFile/07/"
koreanPancakeCSVArr07 = [file_path_07+"2021_부침개_네이버_일간검색트렌드.csv",file_path_07+"2022_부침개_네이버_일간검색트렌드.csv"
    ,file_path_07+"2023_부침개_네이버_일간검색트렌드.csv",file_path_07+"2024_부침개_네이버_일간검색트렌드.csv"]
file_path_rain07 = file_path_07+"기상청_강수량.csv"

#월별 폴더 주소
file_path_09  = "csvFile/09/"
koreanPancakeCSVArr09 = [file_path_09 +"2021_부침개_네이버_일간검색트렌드.csv",file_path_09 +"2022_부침개_네이버_일간검색트렌드.csv"
    ,file_path_09 +"2023_부침개_네이버_일간검색트렌드.csv",file_path_09 +"2024_부침개_네이버_일간검색트렌드.csv"]
file_path_rain09 = file_path_09 +"기상청_강수량.csv"

################### 기상청 csv 파일 주소 ###################



################### 기상청 dataFrame 데이터 생성 ###################
weatherArr07 = pd.DataFrame(pd.read_csv(file_path_rain07,encoding="cp949"))
weatherArr09 = pd.DataFrame(pd.read_csv(file_path_rain09,encoding="cp949"))
#================= csv 데이터 -> 배열 변환 끝 ===================

#================= 날짜 배열 생성 시작 =================
yearDate = [2021,2022,2023,2024]# 그래프 출력

ToyProject1.plotKoreanPancake(koreanPancakeCSVArr07, weatherArr07, yearDate)
ToyProject1.plotKoreanPancake(koreanPancakeCSVArr09, weatherArr09, yearDate)
plt.show()