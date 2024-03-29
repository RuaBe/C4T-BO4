# from __future__ import unicode_literals
# import youtube_dl

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=FJlEkNVcVXc'])










# from youtube_dl import YoutubeDL
# import json
# import urllib.parse

# from youtube_dl.utils import (
#     DownloadError
# )

# def lambda_handler(event, context):
#     lambda_response =  {
#         "isBase64Encoded": False,
#         "statusCode": 200,
#         "headers": {"Content-Type": "application/json"},
#         "body": "{}"
#     }

#     if not 'url' in event['queryStringParameters'] or not event['queryStringParameters']['url']:
#         lambda_response['statusCode'] = 400
#         return lambda_response
    
#     url = urllib.parse.unquote(event['queryStringParameters']['url'])
    
#     ydl_opts = {
#         'skip_download': True,
#         'quiet': True,
#         'no_warnings': True
#     }
#     ydl = YoutubeDL(ydl_opts)
#     try:
#         download_url = ydl.extract_info(url)
#         lambda_response['body'] = json.dumps(download_url)
#     except DownloadError:
#         lambda_response['statusCode'] = 404
#     except:
#         lambda_response['statusCode'] = 500
#     return lambda_response

# def test(name, url, statuscode):
#     test_case = lambda_handler({'queryStringParameters': {'url': url}}, None)
#     if test_case['statusCode'] == statuscode:
#         print("[OK] '%s' passed" % name)
#     else:
#         print("[FAIL] '%s' failed, retured %d, %d expected" % (name, test_case['statusCode'], statuscode))

# print('Running unit tests...')
# test('extract info from Youtube', 'https://www.youtube.com/watch?v=FJlEkNVcVXc', 200)
# test('invalid url', 'https://www.youtube.com/watch?v=00000000000', 404)
# test('invalid extractor', 'https://www.example.com/', 404)
# test('no url', None, 400)






# from youtube_dl import YoutubeDL

# options = {
#     'default_search': 'ytsearch5'
# }

# ydl = YoutubeDL(options)
# search_result = ydl.extract_info('', False)
# print(search_result)


from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])