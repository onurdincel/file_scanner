import os
import requests
import asyncio
import concurrent.futures
import const
import json

class FileHandler():
    def __init__(self):
        self.file_list = set(os.listdir(const.WATCH_DIRECTORY))
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    def get_existing_files(self):
        return set(os.listdir(const.WATCH_DIRECTORY))

    def get_file_path(self, file_name):
        return os.path.join(const.WATCH_DIRECTORY, file_name)

    def get_report(session, id):
        try:
            url = f'https://www.virustotal.com/api/v3/analyses/{id}'
            response = requests.get(url, headers = const.HEADERS)
            data = response.json()
            return data
        except Exception as e:
            return {'error': str(e)}

    def scan_file(self, file_path):
        with open(file_path, 'rb') as file:
            response = requests.post(const.SCAN_URL, headers = const.HEADERS, files = { "file": file})

            if response.status_code == 200:
                result = response.json()
                id = result['data']['id']
                return self.get_report(id)
            else:
                return None

    def save_scan_result(self, file_name, result):
        print(f"{file_name} Dosyasinin Raporu {const.OUTPUT_DIRECTORY} uzerinde olusturuldu.", flush=True)
        report_filename = os.path.join(const.OUTPUT_DIRECTORY, f"{file_name}_report.txt")
        with open(report_filename, "w") as report_file:
            json.dump(result, report_file, indent = 4)

    async def watch_directory(self):
        while True:
            current_files = self.get_existing_files()
            new_files = current_files - self.file_list

            for file in new_files:
                print(f"Yeni Dosya Tespit Edildi: {file}", flush=True)
                file_path = self.get_file_path(file)
                asyncio.create_task(self.handle_scan(file_path))

            self.file_list = current_files
            await asyncio.sleep(5)

    async def handle_scan(self, file_path):
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(self.executor, self.scan_file, file_path)

        if result:
            file_name = os.path.basename(file_path)
            self.save_scan_result(file_name, result)

if __name__ == "__main__":
    print('Program Calismaya Basladi', flush=True)
    watcher = FileHandler()
    asyncio.run(watcher.watch_directory())

