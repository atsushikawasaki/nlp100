# coding: utf-8

import re
from q25 import get_basic_info
from q26 import remove_emphasis_expression
from q27 import remove_link_expression

def remove_tag(text):
    return re.sub(r'<.+?>', '', text)

if __name__ == '__main__':
    with open('britain.txt', 'r') as f:
        text = f.read()

    d = get_basic_info(text)
    res = {k: remove_tag(remove_link_expression(remove_emphasis_expression(v))) for k, v in d.items()}

    print(res)
