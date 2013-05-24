import subprocess
import lixian_commands.download

download_file = lixian_commands.download.download_file

def download_file_and_print(client, path, task, options):
    download_file(client, path, task, options)
    print 'finish'

lixian_commands.download.download_file = download_file_and_print
