import os
import re

import telebot
import time
import docx
from docx.shared import Pt
from docx import Document
import chardet




#(((  БЛОК КОД DRF )))
def main1(transcripts):
    import gspread
    from openai import OpenAI
    count = 1
    for i in range(2):
        transcript_name = f"transcript{count}"
        client = OpenAI(api_key="")
        B = "Каждый критерий оценивается так 0 если критерий является не верным и 1 если критерий является верным ,1) Приветствие клиента по имени. ( 0 или 1 ) балл 2) Представление себя и агентства. ( 0 или 1 ) балл 3)Активное слушание и выяснение потребностей клиента. ( 0 или 1 ) балл 4) Четкое изложение того, как агентство может помочь клиенту. ( 0 или 1 ) балл 5) Уточнение, какие услуги интересны клиенту. ( 0 или 1 ) балл 6) Инструкции по необходимым документам и информации для успешного сотрудничества. ( 0 или 1 ) балл 7) Объяснение процесса работы с агентством. ( 0 или 1 ) балл 8) Выявление готовности клиента к личной встрече. ( 0 или 1 ) балл 9) Предложение уточнить детали встречи. ( 0 или 1 ) балл Обработка вопросов и возражений: 10) Умение аргументировать преимущества сотрудничества. ( 0 или 1 ) балл 11) Решение возможных вопросов и опровержение возражений. ( 0 или 1 ) балл Согласование Дальнейших Шагов: 12) Благодарность за время и внимание клиента. ( 0 или 1 ) балл  13) Запись основных моментов разговора. ( 0 или 1 ) балл 14) Получение обратной связи от клиента. ( 0 или 1 ) балл"
        promt = "я тебе даю эти критерии оценки качества обслуживания клиента (" + B + ") при помощи них оцени переписку между менеджером и клиентом (" + transcripts[transcript_name] + ") дай ответ очень кратко без каких либо слов только баллы например так 1) 1 2) 0 3) 0 итд, твоя оценка должна быть очень объективной "
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": promt}
            ]
        )
        lQ = completion.choices[0].message.content
        print(lQ)
        count += 1
        print(transcripts[transcript_name]*10)
        # Разделить строку на отдельные части
        parts = lQ.split()
        # Инициализировать переменные
        variables = [int(parts[i + 1]) for i in range(0, len(parts), 2)]
        # Вывести значения переменных
        for i, value in enumerate(variables, start=1):
            print(f"var{i} =", value)
        print(variables[0]*10)

        sa = gspread.service_account(filename="service_account.json")
        sh = sa.open("StudentsTest")
        wks = sh.worksheet("list1")
        wks.update(f'A{count}', variables[0])
        wks.update(f'B{count}', variables[1])
        wks.update(f'C{count}', variables[2])
        wks.update(f'D{count}', variables[3])
        wks.update(f'E{count}', variables[4])
        wks.update(f'F{count}', variables[5])
        wks.update(f'G{count}', variables[6])
        wks.update(f'H{count}', variables[7])
        wks.update(f'I{count}', variables[8])
        wks.update(f'J{count}', variables[9])
        wks.update(f'K{count}', variables[10])
        wks.update(f'L{count}', variables[11])
        wks.update(f'M{count}', variables[12])
        wks.update(f'N{count}', variables[13])




        return lQ
