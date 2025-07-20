import boto3
import json 
import os
from botocore.exceptions import ClientError
import requests 
import pandas as pd
import re #regular expression
import logging
from typing import List, Dict, Any, Tuple
from tqdm import tqdm #progress bar
import jsonschema


#Sources : https://archive.org/details/bhagavadgitaasitisoriginal1972edition
#https://archive.org/details/bhagavadgitaorig0000unse
#https://gitapress.org/bookdetail/gita-shankarbhashya-hindi-10

CHAPTER_INFO = {
    "chapters": [
        {"number": 1, "name": "Arjuna Visada Yoga", "total_shlokas": 47},
        {"number": 2, "name": "Sankhya Yoga", "total_shlokas": 72},
        {"number": 3, "name": "Karma Yoga", "total_shlokas": 43},
        {"number": 4, "name": "Jnana Yoga", "total_shlokas": 42},
        {"number": 5, "name": "Karma Sanyasa Yoga", "total_shlokas": 29},
        {"number": 6, "name": "Dhyana Yoga", "total_shlokas": 47},
        {"number": 7, "name": "Jnana Vijnana Yoga", "total_shlokas": 30},
        {"number": 8, "name": "Aksara Brahma Yoga", "total_shlokas": 28},
        {"number": 9, "name": "Raja Vidya Yoga", "total_shlokas": 34},
        {"number": 10, "name": "Vibhuti Yoga", "total_shlokas": 42},
        {"number": 11, "name": "Visvarupa Darsana Yoga", "total_shlokas": 55},
        {"number": 12, "name": "Bhakti Yoga", "total_shlokas": 20},
        {"number": 13, "name": "Ksetra Ksetrajna Vibhaga Yoga", "total_shlokas": 35},
        {"number": 14, "name": "Gunatraya Vibhaga Yoga", "total_shlokas": 27},
        {"number": 15, "name": "Purusottama Yoga", "total_shlokas": 20},
        {"number": 16, "name": "Daivasura Sampad Vibhaga Yoga", "total_shlokas": 24},
        {"number": 17, "name": "Sraddhatraya Vibhaga Yoga", "total_shlokas": 28},
        {"number": 18, "name": "Moksa Sanyasa Yoga", "total_shlokas": 78}
    ]
}



