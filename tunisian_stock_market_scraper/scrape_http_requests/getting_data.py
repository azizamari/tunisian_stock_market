import requests
from io import StringIO
import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()



url = "https://www.ilboursa.com/marches/download/"


headers = {
  'authority': 'www.ilboursa.com',
  'method': 'POST',
  'scheme': 'https',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7,fr;q=0.6',
  'cache-control': 'max-age=0',
  'content-length': '295',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': os.getenv('COOKIE'),
  'origin': 'https://www.ilboursa.com',
  'referer': 'https://www.ilboursa.com/marches/download/MAG',
  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def get_data(ticker,dtFrom, dtTo):
    payload = f"dtFrom={dtFrom}&__Invariant=dtFrom&dtTo={dtTo}&__Invariant=dtTo&__RequestVerificationToken={os.getenv('__RequestVerificationToken')}"
    response = requests.request("POST", url+ticker, headers=headers, data=payload)
    if response.text.startswith("<!doctype html>"): return pd.DataFrame()
    csvStringIO = StringIO(response.text)
    df = pd.read_csv(csvStringIO, sep=";")
    return df


