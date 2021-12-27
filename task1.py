import os


SOURCE_CSV_PATH = "source.csv"

DEFAULT_CARACTOR = ["ねずこ","たんじろう","ぎゆう","ぜんいつ","いのすけ"]

def read_source(csv_pass:str):
     if not os.path.exists(csv_pass):
        print(f"csv_path:{csv_path}が存在しません。")
        write_source(csv_path,DEFOULT_CARACTOR)
        with open(csv_path, mode='r',encoding ="utf-8_sig") as f:
            return f.read(),splitlines()
def write_source(csv_path:str,source:list):
    with open(csv_path,mode='w',encoding="utf-8_sig") as f:
        f.write("\n".join(source))
def search():
    source = read_source(SOURCE_CSV_PATH)
    while True:
        word = input("鬼滅の登場人物を入力 >>")
        if word in source:
            print(f"『{word}』は登録されています。")
        else:
            print(f"『{word}』は未登録です。")
            is_add = input("追加登録しますか？(n:しない y:する)>>")
            if is_add == "y":
                source.append(word)
        write_source(SOURCE_CSV_PATH,source = source)
if __name__ == "__main__":
    search()
            
        
