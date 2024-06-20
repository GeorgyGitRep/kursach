import pandas as pd

# Чтение данных из текстового файла
file_path = '1.txt'
data = pd.read_csv(file_path, delimiter='\s+', header=None, names=['Column1', 'Column2'])  # Измените разделитель, если он отличается от пробела

# Запись данных в файл Excel
excel_file_path = 'output.xlsx'
data.to_excel(excel_file_path, index=False)

print(f'Данные успешно записаны в файл {excel_file_path}')