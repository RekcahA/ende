import random

First_dictionary =  {'\ufeff': 10675, '`': 10104, '1': 10862, '!': 10765, '2': 10107, '@': 10106, '3': 10549, '#': 10917, '4': 10290, '$': 10256, '5': 10319, '%': 10016, '6': 10267, '^': 10186, '7': 10001, '&': 10446, '8': 10260, '*': 10742, '9': 10721, '(': 10092, '0': 10451, ')': 10947, '-': 10252, '_': 10151, '=': 10940, '+': 10929, 'q': 10550, 'w': 10207, 'e': 10694, 'r': 10141, 't': 10968, 'y': 10656, 'u': 10635, 'i': 10986, 'o': 10309, 'p': 10786, '[': 10321, '{': 10660, '}': 10677, ']': 10743, 'a': 10159, 's': 10429, 'd': 10891, 'f': 10790, 'g': 10103, 'h': 10241, 'j': 10597, 'k': 10498, 'l': 10345, ';': 10023, "'": 10770, 'z': 10341, 'x': 10460, 'c': 10390, ':': 10297, '\\': 10184, 'v': 10823, 'b': 10412, 'n': 10278, 'm': 10045, ',': 10831, '<': 10435, '.': 10052, '>': 10191, '/': 10723, '?': 10813, 'Q': 10371, 'W': 10043, 'E': 10621, 'R': 10097, 'T': 10467, 'Y': 10984, 'U': 10552, 'I': 10619, 'O': 10298, 'P': 10731, 'A': 10166, 'S': 10219, 'D': 10662, 'F': 10366, 'G': 10919, 'H': 10488, 'J': 10170, 'K': 10771, 'L': 10017, 'M': 10061, 'N': 10481, 'B': 10455, 'V': 10796, 'C': 10653, 'X': 10489, 'Z': 10997, '~': 10840, '۱': 10775, '۲': 10132, '۳': 10282, '۴': 10418, '۵': 10558, '۶': 10058, '۷': 10240, '۸': 10626, '۹': 10697, '۰': 10982, 'ض': 10354, 'ص': 10726, 'ث': 10613, 'ق': 10203, 'ف': 10519, 'غ': 10952, 'ع': 10176, 'ه': 10158, 'خ': 10054, 'ح': 10719, 'ج': 10897, 'چ': 10490, 'ش': 10741, 'س': 10819, 'ی': 10413, 'ب': 10448, 'ل': 10849, 'ا': 10945, 'ت': 10116, 'ن': 10755, 'م': 10661, 'ک': 10658, 'گ': 10995, 'ظ': 10373, 'ط': 10860, 'ز': 10383, 'ر': 10205, 'ذ': 10625, 'د': 10843, 'پ': 10526, 'و': 10820, '؟': 10257, '\n': 10687, 'ْ': 10936, 'ٌ': 10588, 'ٍ': 10781, 'ً': 10485, 'ُ': 10528, 'ِ': 10285, 'َ': 10453, 'ّ': 10227, 'ؤ': 10063, 'ئ': 10062, 'ي': 10122, 'إ': 10832, 'أ': 10927, 'آ': 10996, 'ة': 10034, '»': 10343, '«': 10515, '؛': 10562, 'ك': 10998, 'ژ': 10561, 'ٰ': 10127, 'ٔ': 10595, 'ء': 10169, ' ': 10586, '\t': 10882, '"': 10464, '108': 10180}


def new_key_generator(file_name = '/bin/key.py'):

     encryption_dictionary = {}
     decryption_dictionary = {}
     used_numbers = []

     for letter in First_dictionary :

         while True :

             random_number = random.randint(10000,11000)
             if used_numbers.count(random_number) == False : break

         encryption_dictionary.update({letter:random_number})
         decryption_dictionary.update({random_number:letter})
         used_numbers.append(random_number)


     keys = open(file_name,'w')

     keys.write("\n\n# These are the base Dictionaries for encryption/decryption\n\nencryption_dictionary =  {}\n\ndecryption_dictionary =  {}\n\n".format(encryption_dictionary,decryption_dictionary))

     keys.close()