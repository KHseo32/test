# import os
# import glob
# import pandas as pd
# 지정된 경로에 파일들을 하나의 데이터 프레임으로 결합하여 되돌려주는 함수 생성
# 매개 변수 -> 경로, 확장자명
def data_load(_path,_end='csv'):
    # _path : 파일 경로
    # _end : 파일의 확장자명
    file_list = os.listdir(_path)
    result = pd.DataFrame()
    _path = _path+'/'
    for file in file_list:
        # file <- 파일명
        if file.endswith(_end):
            if _end == 'csv':
                df = pd.read_csv(_path + file)
            elif _end == 'json':
                df = pd.read_json(_path + file)
            elif _end == 'xml':
                df = pd.read_xml(_path + file)
            elif _end in ['xlsx', 'xls'] :
                df = pd.read_excel(_path + file)
            else:
                continue
        result = pd.concat([result, df],
                           axis=0, ignore_index=True)
    return result

def load_folder(folder):
    file_list = glob.glob(folder + '/*.*') 
    for file in file_list:
        folder_path, name = os.path.split(file)
        head, tail = os.path.splitext(name)
        if tail == '.csv':
            df = pd.read_csv(file)
        elif tail == '.json':
            df = pd.read_json(file)
        elif tail == '.xml':
            df = pd.read_xml(file)
        elif tail in ['.xlsx', '.xls']:
            df = pd.read_excel(file)
        else:
            print(f"지원되지 않는 확장자: {tail}")
            continue

        globals()[f'"{head}"'] = df.copy()
    print('Folder loaded')
