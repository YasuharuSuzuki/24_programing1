import glob
import sys, os
import io
import neologdn
import subprocess
import pandas as pd

from collections import Counter

# XZで圧縮されたJSONファイル名
xz_filename = 'data/answer.csv.xz'

def try_all(exec_python_path):
    df_answer = pd.read_csv(xz_filename, index_col=0)
    answer_count = len(df_answer)
    error_count = 0
    for answer_index, in1, out1 in zip(df_answer.index, df_answer['in'], df_answer['out']):
        answer_input_string = '\n'.join(eval(in1))
        answer_outputs = eval(out1)
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

        # print(all_temp)
        # print(answer_outputs)
        for out_str1 in answer_outputs:
            stdout_str1 = neologdn.normalize(all_temp.pop(0)) # neologdnで正規化してから比較する
            out_str1 = neologdn.normalize(out_str1) # neologdnで正規化してから比較する
            if out_str1 != stdout_str1:
                print(f"Error! temp={stdout_str1}, answer={out_str1}, answer_index={answer_index} input_str={answer_input_string}")
                error_count += 1
            else:
                print(f"OK temp={stdout_str1}, answer={out_str1}")

    print(f"AC ({answer_count}/{answer_count})" if error_count == 0 else f"WA ({answer_count-error_count}/{answer_count} 正解率={100*(answer_count-error_count)/answer_count:.1f}%)")


if __name__ == "__main__":
    try_all(sys.argv[1])
