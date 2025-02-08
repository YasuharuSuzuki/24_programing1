import glob
import sys, os
import io
import neologdn
import subprocess
import pandas as pd

from collections import Counter

# XZで圧縮されたJSONファイル名
xz_filename = 'data/answer.csv.xz'

def _preprocess(text):
    text = neologdn.normalize(text)  # 正規化
    text = text.replace(' ', '')  # 正規化
    return text

def try_all(exec_python_path):
    df_answer = pd.read_csv(xz_filename, index_col=0)
    answer_count = len(df_answer)
    error_count = 0
    for answer_index, in1, answer_output_string in zip(df_answer.index, df_answer['in'], df_answer['out']):
        answer_input_string = '\n'.join(eval(in1))
        answer_outputs = eval(answer_output_string)
        answer_outputs = [_preprocess(str(out1)) for out1 in  answer_outputs] # neologdnで正規化してから比較する
        # print("answer_input_string=",answer_input_string)
        # print("answer_outputs=",answer_outputs)
 
        # 標準入力を file に、標準出力を io.StringIO に結びつけてsubprocessで実行する
        proc = subprocess.Popen(['python', exec_python_path], encoding='utf-8', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate(answer_input_string)
        stdout_io = io.StringIO(stdout)

        all_temp = stdout_io.getvalue().split('\n')
        if len(all_temp[-1]) == 0:  # 出力結果の最後には\nが必ず存在するため、最終行に空文字列が入ってしまうので、チェックする
            all_temp = all_temp[:-1]  # 最終行の空文字列を削除
        if len(all_temp) == 0:  # 出力結果が空の時は
            all_temp = [""]  # 空文字列を入れておく
        all_temp = [_preprocess(out1) for out1 in  all_temp] # neologdnで正規化してから比較する

        # print(all_temp)
        # print(answer_outputs)
        error_outputs = []
        for out_index,out_str1 in enumerate(answer_outputs):
            stdout_str1 = all_temp[out_index]
            if out_str1 != stdout_str1:
                error_outputs.append(f"out[{out_index}]={stdout_str1}, answer={out_str1}")

        if len(error_outputs) == 0:
            print(f"OK out={all_temp}, answer={answer_outputs}")
        else:
            print("Error! answer[id={} input={}] error=[{}]".format(
                answer_index, answer_input_string, "\n".join(error_outputs)))
            error_count += 1

    print(f"AC ({answer_count}/{answer_count})" if error_count == 0 else f"WA ({answer_count-error_count}/{answer_count} 正解率={100*(answer_count-error_count)/answer_count:.1f}%)")


if __name__ == "__main__":
    try_all(sys.argv[1])
