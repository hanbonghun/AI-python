import os

#파일 이름 입력하면 파일의 리스트를 반환하는 함수
def get_file_list(dir_name):
    return os.listdir(dir_name)  #listdir 폴더 안의 파일리스트 가져올 떄


#파일별로 내용 읽기
def get_contents(file_list):
    y_class = [] #각 text파일 분류
    X_text=[]   #각 text파일의 내용들 list에 저장
    class_dict = {
    1:"0", 2:"0", 3:"0", 4:"0",5:"1",6:"1",7:"1",8:"1"
    }

    for file_name in file_list:
        try:
            f = open(file_name,"r", encoding="cp949")
            category = int(file_name.split(os.sep)[1].split("_")[0])
            y_class.append(class_dict[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text,y_class

#의미 없는 문장 부호 제거
def get_cleaned_text(word):
    import re
    word= re.sub('\W+','',word.lower())
    return word

def get_corpus_dict(text):
    text = [sentence.split() for sentence in text]
    cleaned_words= [get_cleaned_text(word) for words in text for word in words]
    from collections import OrderedDict
    corpus_dict = OrderedDict() #값을 집어 넣은 순서대로 사용
    for i,v in enumerate(set(cleaned_words)): #set을 통해 동일 단어 없앤다
        corpus_dict[v]=i
    return corpus_dict

#문서별로 Bag of words vector 생성
def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    word_number_list =[[corpus[get_cleaned_text(word)] for word in words] for words in text]
    X_vector = [[0 for _ in range(len(corpus))]for x in range(len(text))]

    for i, text in enumerate(word_number_list):
        for word_number in text:
            X_vector[i][word_number]+=1

    return X_vector

#비교하기
import math
def get_cosine_similarity(v1,v2):
    sumxx,sumxy,sumyy =0,0,0
    for i in range(len(v1)):
        x=v1[i]; y= v2[i]
        sumxx+=x*x
        sumxy+=x*y
        sumyy+=y*y
    return sumxy/math.sqrt(sumxx*sumyy)

#비교결과 정리
def get_similarity_score(X_vector, source):
    source_vector = X_vector[source]
    similarity_list=[]
    for target_vector in X_vector:
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector)
        )
    return similarity_list

def get_top_n_similarity_news(similarity_score, n):
    import operator
    x ={i:v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))

    return list(reversed(sorted_x))[1:n+1]

def get_accuracy(similarity_list,y_class, source_news):
    source_class = y_class[source_news]

    return sum([source_class == y_class[i[0]]for i in  similarity_list])/len(similarity_list)
if __name__ == "__main__":  #인터프리터에서 직접 실행하는 경우에만 if문 안의 내용 실행
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
        #운영체제에 따라 디렉토리 접근 방식이 다르기 때문에 os의 path.join 사용

    X_text, y_class = get_contents(file_list)
    corpus = get_corpus_dict(X_text)
    print("Number of words : {0}".format(len(corpus)))

    X_vector = get_count_vector(X_text, corpus)
    source_number = 10

    result=[]

    for i in range(80):
        source_number =i

        similarity_score= get_similarity_score(X_vector, source_number)
        similariry_news = get_top_n_similarity_news(similarity_score,10)
        accuracy_score = get_accuracy(similariry_news,y_class, source_number)
        result.append(accuracy_score)
    print(sum(result)/80)
