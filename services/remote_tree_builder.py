
def foo(id):
    for item in gds.drive_service.search_files_for_folder(id):
        if (item['mimeType'] == ''):
            foo(item['id'])
        else:
            print(item)


foo('root')