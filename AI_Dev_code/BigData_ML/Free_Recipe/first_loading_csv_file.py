import pandas as pd

#csv파일로 불러 올려했으나 utf-8 또는 cp949 유니코드 오류로 인해 엑셀파일로 변경 후 불러옴 ( 예상하는 바로는 특수문자 때문인듯....)
#그래픽 카드 성능 얼마나 빠를지 테스트 해보기
file_path = r'.\Data\remake_testing.xlsx'
df1 = pd.read_excel(file_path)
print(df1['CKG_DODF_NM'])