import pandas as pd
from konlpy.tag import Okt
from kss import split_sentences
from tqdm import tqdm
import re

# --- 1. 데이터 불러오기 ---
def load_csv_robustly(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        return df
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')
        return df

cheongju = load_csv_robustly("./crawled_data/merged_cheongju.csv")
other = load_csv_robustly("./crawled_data/merged_other.csv")

COLUMN_TO_ANALYZE = 'content_cleaned'

output_cheongju_path = "./crawled_data/merged_cheongju_analyzed_fnai.csv"
output_other_path = "./crawled_data/merged_other_analyzed_fnai.csv"

# --- 2. 분석 함수 정의 ---
okt = Okt()
category_keywords = {
    '음식': [
        '맛', '음식', '메뉴', '요리', '신선', '재료', '소스', '양', '식감', '퀄리티',
        '고기', '파스타', '피자', '초밥', '국물', '육수', '반찬', '디저트', '커피', '음료',
        '짜다', '싱겁다', '달다', '느끼다', '고소하다', '담백하다', '진하다', '매콤', '얼큰',
        '뜨겁다', '차갑다', '풍미', '구수하다', '바삭', '쫄깃', '부드럽다', '촉촉하다',
        '간', '양념', '토핑', '특제', '별미', '시그니처'
    ],
    '분위기': [
        '분위기', '인테리어', '디자인', '느낌', '뷰', '전망', '공간', '자리', '좌석',
        '조명', '음악', '데이트', '모임', '깔끔', '깨끗', '웨이팅', '대기',
        '아늑하다', '편안하다', '쾌적하다', '고급스럽다', '세련되다', '아기자기',
        '북적', '조용하다', '프라이빗', '개방감', '야경', '테라스', '분리', '오픈키친'
    ],
    '가격': [
        '가격', '가성비', '비용', '금액', '저렴', '비싸', '할인', '무료', '추가', '계산',
        '가심비', '만원', '합리적', '적당하다', '부담', '혜자', '세트', '코스', '포인트',
        '쿠폰', '배달비', '서비스 차지', '물가', '사치', '특가'
    ],
    '서비스': [
        '서비스', '직원', '사장님', '친절', '응대', '주차', '예약', '위치', '화장실',
        '리필', '주문', '서빙', '불만족', '빠르다', '느리다', '정성', '배려', '분위기메이커',
        '상냥하다', '불친절', '대응', '체계적', '혼잡', '깔끔', '소통', '센스', '매너'
    ]
}


def extract_sentences_by_category(text):
    text = str(text)
    category_sentences = {'음식_문장': [], '분위기_문장': [], '가격_문장': [], '서비스_문장': []}
    cleaned_text = re.sub(r"[^0-9가-힣?.!,¿]+", " ", text)

    try:
        # kss 설치시 emoji 작동 오류 (kss 삭제하고 emoji 다시 설치)
        # kss 문장 분리 (일반 cpu는 속도 빠른 mecab backend 사용)
        
        sentences = split_sentences(cleaned_text) # ,backend="mecab"
    except:
        pass

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        try:
            morphs = okt.pos(sentence, stem=True)
            words = [word for word, pos in morphs if pos in ['Noun', 'Verb', 'Adjective']]
        except:
            words = []
        
        for category, keywords in category_keywords.items():
            if any(keyword in words for keyword in keywords):
                if sentence not in category_sentences[f'{category}_문장']:
                    category_sentences[f'{category}_문장'].append(sentence)

    return category_sentences

# --- 3. tqdm으로 진행상황 표시 ---
def analyze_dataframe(df, name):
    print(f"{name} 데이터 분석 시작...")
    results = []
    for text in tqdm(df[COLUMN_TO_ANALYZE], desc=f"{name} 진행중"):
        results.append(extract_sentences_by_category(text))
        
    sentence_df = pd.json_normalize(results)
    final_df = pd.concat([df, sentence_df], axis=1)
    print(f"{name} 데이터 분석 완료.")
    return final_df

# --- 4. 청주 데이터 분석 ---
print("청주 데이터 분석 시작...")

cheongju_final = analyze_dataframe(cheongju, "청주")

cheongju_final.to_csv(output_cheongju_path, encoding='utf-8-sig', index=False)
print(f"청주 데이터 분석 결과가 '{output_cheongju_path}' 파일에 저장되었습니다.")


# --- 5. 다른 지역 데이터 분석 ---
print("다른 지역 데이터 분석 시작...")

other_final = analyze_dataframe(other, "다른 지역")

other_final.to_csv(output_other_path, encoding='utf-8-sig', index=False)
print(f"다른 지역 데이터 분석 결과가 '{output_other_path}' 파일에 저장되었습니다.")
print("모든 데이터 분석이 완료되었습니다.")