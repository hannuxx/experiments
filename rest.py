#!/bin/python3

import json
import requests
import math
import os
import random
import re
import sys

def getTotalGoals(team, year):
    total = 0
    headers = {'Content-Type': 'application/json'}
    totalPages = 1
    page = 1
    totalPages = 1
    while page <= totalPages:
        api_url1 = 'https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1={1}&page={2}'.format(year, team, page)
        response = requests.get(api_url1, headers=headers)
        resp = None
        d = {"page" : 0, "per_page" : 0, "total" : 0, "total_pages" : 0, "goals1": 0, "goals2": 0}
        if response.status_code == 200:
            resp = json.loads(response.content.decode('utf-8'))
            if (page == 1):
                page = int(resp['page'])
            totalPages = resp['total_pages']
            dd = resp['data']
            for dd in resp['data']:
                total += int(dd['team1goals'])
        page = page + 1
    page = 1
    totalPages = 1
    while page <= totalPages:
        api_url2 = 'https://jsonmock.hackerrank.com/api/football_matches?year={0}&team2={1}&page={2}'.format(year, team, page)
        response = requests.get(api_url2, headers=headers)
        resp = None
        d = {"page" : 0, "per_page" : 0, "total" : 0, "total_pages" : 0, "goals1": 0, "goals2": 0}
        if response.status_code == 200:
            resp = json.loads(response.content.decode('utf-8'))
            if (page == 1):
                page = int(resp['page'])
            totalPages = resp['total_pages']
            dd = resp['data']
            for dd in resp['data']:
                total += int(dd['team2goals'])
        page = page + 1
    return total

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("output.txt", 'w')

    #team = input()
    #year = int(input().strip())
    team = "Chelsea"
    year = 2014

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')
    sys.stdout.write(f'Result: {result}');

    fptr.close()
