import pytesseract
import cv2 as cv
import json

def del_symbols(string):
    return string.replace('\x0c', '').replace('\n', ' ').replace('  ', '')

def get_text(img):
    protocol = del_symbols(pytesseract.image_to_string(img[30:110, 360:1000], lang='rus'))
    object_name = del_symbols(pytesseract.image_to_string(img[160:210, 360:970], lang='rus'))
    authors = del_symbols(pytesseract.image_to_string(img[210:250, 360:970], lang='rus'))
    organization = del_symbols(pytesseract.image_to_string(img[250:290, 360:970], lang='rus'))
    builder = del_symbols(pytesseract.image_to_string(img[290:335, 360:970], lang='rus'))
    referant = del_symbols(pytesseract.image_to_string(img[360:399, 360:970], lang='rus'))
    performers = del_symbols(pytesseract.image_to_string(img[430:480, 360:970]))
    if len(object_name) < 50:
        date = del_symbols(pytesseract.image_to_string(img[120:160, 230:380], lang='rus'))
        number = del_symbols(pytesseract.image_to_string(img[130:160, 620:720], lang='rus'))
        par = del_symbols(pytesseract.image_to_string(img[130:165, 950:1060], lang='rus'))
    else:
        date = del_symbols(pytesseract.image_to_string(img[110:150, 190:380], lang='rus'))
        number = del_symbols(pytesseract.image_to_string(img[120:140, 580:670], lang='rus'))
        par = del_symbols(pytesseract.image_to_string(img[120:145, 900:980], lang='rus'))

    return {
    'Выписка из протокола': protocol, 
    'дата' : date, 
    'номер': number,
    'пункт': par,
    'Наименование объекта': object_name, 
    'Авторы проекта': authors,
    'Генеральная проектная организация': organization,
    'Застройщик': builder,
    'Рассмотрение на рабочей комиссии': '',
    'Референт': referant,
    'Докладчик': '',
    'Выступили': performers
    }

def parse_dict_to_json(output_file, info):
    with open(output_file, 'w+') as f:
                json.dump(info, f, ensure_ascii=False)
