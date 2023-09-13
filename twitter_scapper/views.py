from django.shortcuts import render
from django.http import JsonResponse
from twitter.scraper import Scraper

def api_response_result(result_code, data=None):
    if data is not None:
        response = JsonResponse({'result': result_code, 'data': data}, status=200)
    else:
        response = JsonResponse({'result': result_code}, status=200)

    return response

def get_twitter_user_info(request):
    ids = request.GET.get("ids", '').split(',')

    if not ids:
        return api_response_result('error', {"error": "error_params"})

    scraper = Scraper('baohogia0015@gmail.com', 'DepBao53560', '0942521337bao')

    users = scraper.users_by_ids([int(x) for x in ids])

    if not users:
        return api_response_result('error', {"error": "invalid_id"})

    return api_response_result('success',  users)
 