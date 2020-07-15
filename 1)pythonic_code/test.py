import os

#파일 내 문서들 리스트로 반환하는 함수
def get_file_list(dir_name):
    return os.listdir(dir_name)

#파일별로 내용 읽기
def get_contents(file_list):
    y_class = []
    X_text = []
    class_dict= {
        1:"0", 2:"0", 3:"0", 4:"0",5:"1",6:"1",7:"1",8:"1"
    }
    for file_name in file_list:
        try:
            f = open(file_list,'r', encoding ="cp949")
            category = int(file_name.split(os.sep)[1].split('_')[0])
            y_class.append(class_dict[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class

#의미 없는 문장 부호 제거
def get_cleaned_text(word):
    import re
    word = re.sub('\W+','',word.lower())
    return word

def get_corpus_dict(text):
    text = [sentence.split() for sentence in text]
    cleaned_words = [get_cleaned_text(words) for words in text for word in words]

    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i,v in enumerate(set(cleaned_words)):
        corpus_dict[v]=i
    return corpus_dict

#문서별로 bag of words vector 생성
def get_count_vector(text, courpus):
    text = [sentence.split() for sentence in text]
    word_number_list =pus[get_cleaned_text] [[cor]]
if __name__=="__main__":
    dir_name = "new_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path(dir_name,file_name) for file_name in file_list]

    X_text, y_class = get_contents(file_list)
