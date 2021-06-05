#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 19.  Написать программу, которая считывает текст из файла и выводит на экран предложения,
# содержащие минимальное количество знаков пунктуации.

import re

if __name__ == '__main__':
    file = 'text.txt'
    with open('text.txt', 'r', encoding='utf-8-sig') as f:
        sentences = f.read().split('. ')

    print(min(sentences, key=lambda x: re.subn(r'[,.;@#?!&$]+', '', x)[1]))