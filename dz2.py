# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def get_directory_size(directory):
    total_size = 0
    for path, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)
    return total_size

def traverse_directory(directory):
    results = []
    for path, dirs, files in os.walk(directory):
        for subdir in dirs:
            subdir_path = os.path.join(path, subdir)
            size = get_directory_size(subdir_path)
            results.append({"path": subdir_path, "type": "directory", "size": size})
        
        for file in files:
            file_path = os.path.join(path, file)
            size = os.path.getsize(file_path)
            results.append({"path": file_path, "type": "file", "size": size})

    return results

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as file:
        json.dump(results, file)

def save_results_to_csv(results, output_file):
    header = ["path", "type", "size"]
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as file:
        pickle.dump(results, file)

directory = "test1"

results = traverse_directory(directory)

save_results_to_json(results, "output.json")
save_results_to_csv(results, "output.csv")
save_results_to_pickle(results, "output.pickle")