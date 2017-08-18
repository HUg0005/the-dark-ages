import socket
import json
import time
import threading
from termcolor import colored


def genmap(empty, tree, farm, water, stone, town_center):
    default_map = {
        "1,1": empty,
        "2,1": empty,
        "3,1": empty,
        "4,1": empty,
        "5,1": empty,
        "6,1": empty,
        "7,1": empty,
        "8,1": empty,
        "9,1": tree,
        "10,1": empty,
        "11,1": empty,
        "12,1": empty,
        "13,1": tree,
        "14,1": tree,
        "15,1": tree,
        "16,1": tree,
        "17,1": tree,
        "18,1": tree,
        "19,1": tree,
        "20,1": tree,
        "21,1": tree,
        "22,1": tree,
        "23,1": empty,
        "24,1": empty,
        "25,1": tree,
        "26,1": tree,
        "27,1": tree,
        "28,1": tree,
        "29,1": tree,
        "30,1": tree,
        "31,1": tree,
        "32,1": tree,
        "33,1": empty,
        "34,1": tree,
        "35,1": tree,
        "36,1": tree,
        "37,1": tree,
        "38,1": tree,
        "39,1": tree,
        "40,1": tree,
        "41,1": tree,
        "42,1": tree,
        "43,1": tree,
        "44,1": tree,
        "45,1": tree,
        "46,1": tree,
        "47,1": tree,
        "48,1": tree,
        "49,1": tree,
        "50,1": tree,
        "51,1": tree,
        "52,1": tree,
        "53,1": tree,
        "54,1": tree,
        "55,1": tree,
        "56,1": tree,
        "57,1": tree,
        "58,1": empty,
        "59,1": empty,
        "60,1": tree,
        "61,1": tree,
        "62,1": empty,
        "63,1": empty,
        "64,1": empty,
        "1,2": empty,
        "2,2": empty,
        "3,2": empty,
        "4,2": empty,
        "5,2": empty,
        "6,2": empty,
        "7,2": empty,
        "8,2": empty,
        "9,2": empty,
        "10,2": empty,
        "11,2": tree,
        "12,2": tree,
        "13,2": tree,
        "14,2": tree,
        "15,2": tree,
        "16,2": tree,
        "17,2": tree,
        "18,2": tree,
        "19,2": empty,
        "20,2": tree,
        "21,2": tree,
        "22,2": tree,
        "23,2": tree,
        "24,2": tree,
        "25,2": tree,
        "26,2": tree,
        "27,2": tree,
        "28,2": tree,
        "29,2": tree,
        "30,2": tree,
        "31,2": tree,
        "32,2": tree,
        "33,2": tree,
        "34,2": tree,
        "35,2": tree,
        "36,2": tree,
        "37,2": tree,
        "38,2": tree,
        "39,2": tree,
        "40,2": empty,
        "41,2": tree,
        "42,2": tree,
        "43,2": tree,
        "44,2": tree,
        "45,2": tree,
        "46,2": empty,
        "47,2": tree,
        "48,2": tree,
        "49,2": empty,
        "50,2": empty,
        "51,2": tree,
        "52,2": tree,
        "53,2": tree,
        "54,2": tree,
        "55,2": tree,
        "56,2": empty,
        "57,2": empty,
        "58,2": tree,
        "59,2": empty,
        "60,2": empty,
        "61,2": empty,
        "62,2": empty,
        "63,2": empty,
        "64,2": empty,
        "1,3": empty,
        "2,3": empty,
        "3,3": empty,
        "4,3": empty,
        "5,3": empty,
        "6,3": empty,
        "7,3": empty,
        "8,3": empty,
        "9,3": empty,
        "10,3": empty,
        "11,3": empty,
        "12,3": tree,
        "13,3": tree,
        "14,3": tree,
        "15,3": tree,
        "16,3": tree,
        "17,3": tree,
        "18,3": tree,
        "19,3": empty,
        "20,3": tree,
        "21,3": tree,
        "22,3": tree,
        "23,3": tree,
        "24,3": tree,
        "25,3": tree,
        "26,3": tree,
        "27,3": tree,
        "28,3": tree,
        "29,3": tree,
        "30,3": tree,
        "31,3": tree,
        "32,3": empty,
        "33,3": tree,
        "34,3": tree,
        "35,3": tree,
        "36,3": tree,
        "37,3": tree,
        "38,3": tree,
        "39,3": tree,
        "40,3": empty,
        "41,3": tree,
        "42,3": tree,
        "43,3": tree,
        "44,3": tree,
        "45,3": empty,
        "46,3": tree,
        "47,3": tree,
        "48,3": tree,
        "49,3": empty,
        "50,3": empty,
        "51,3": tree,
        "52,3": tree,
        "53,3": tree,
        "54,3": tree,
        "55,3": tree,
        "56,3": empty,
        "57,3": empty,
        "58,3": tree,
        "59,3": empty,
        "60,3": empty,
        "61,3": empty,
        "62,3": empty,
        "63,3": empty,
        "64,3": empty,
        "1,4": empty,
        "2,4": empty,
        "3,4": empty,
        "4,4": empty,
        "5,4": empty,
        "6,4": empty,
        "7,4": empty,
        "8,4": empty,
        "9,4": empty,
        "10,4": empty,
        "11,4": tree,
        "12,4": tree,
        "13,4": empty,
        "14,4": empty,
        "15,4": tree,
        "16,4": tree,
        "17,4": tree,
        "18,4": tree,
        "19,4": tree,
        "20,4": tree,
        "21,4": tree,
        "22,4": tree,
        "23,4": empty,
        "24,4": tree,
        "25,4": tree,
        "26,4": tree,
        "27,4": tree,
        "28,4": tree,
        "29,4": tree,
        "30,4": tree,
        "31,4": tree,
        "32,4": tree,
        "33,4": tree,
        "34,4": tree,
        "35,4": tree,
        "36,4": tree,
        "37,4": tree,
        "38,4": tree,
        "39,4": empty,
        "40,4": tree,
        "41,4": tree,
        "42,4": tree,
        "43,4": tree,
        "44,4": tree,
        "45,4": tree,
        "46,4": tree,
        "47,4": tree,
        "48,4": tree,
        "49,4": tree,
        "50,4": tree,
        "51,4": tree,
        "52,4": tree,
        "53,4": tree,
        "54,4": tree,
        "55,4": tree,
        "56,4": tree,
        "57,4": empty,
        "58,4": empty,
        "59,4": empty,
        "60,4": empty,
        "61,4": empty,
        "62,4": empty,
        "63,4": empty,
        "64,4": empty,
        "1,5": empty,
        "2,5": empty,
        "3,5": empty,
        "4,5": empty,
        "5,5": empty,
        "6,5": empty,
        "7,5": tree,
        "8,5": tree,
        "9,5": empty,
        "10,5": empty,
        "11,5": empty,
        "12,5": empty,
        "13,5": empty,
        "14,5": empty,
        "15,5": empty,
        "16,5": empty,
        "17,5": tree,
        "18,5": tree,
        "19,5": tree,
        "20,5": tree,
        "21,5": tree,
        "22,5": tree,
        "23,5": empty,
        "24,5": empty,
        "25,5": tree,
        "26,5": tree,
        "27,5": tree,
        "28,5": tree,
        "29,5": tree,
        "30,5": tree,
        "31,5": tree,
        "32,5": tree,
        "33,5": tree,
        "34,5": tree,
        "35,5": tree,
        "36,5": tree,
        "37,5": tree,
        "38,5": tree,
        "39,5": empty,
        "40,5": empty,
        "41,5": tree,
        "42,5": tree,
        "43,5": tree,
        "44,5": tree,
        "45,5": tree,
        "46,5": tree,
        "47,5": tree,
        "48,5": tree,
        "49,5": tree,
        "50,5": tree,
        "51,5": tree,
        "52,5": tree,
        "53,5": tree,
        "54,5": tree,
        "55,5": tree,
        "56,5": tree,
        "57,5": empty,
        "58,5": empty,
        "59,5": empty,
        "60,5": tree,
        "61,5": empty,
        "62,5": empty,
        "63,5": empty,
        "64,5": empty,
        "1,6": empty,
        "2,6": empty,
        "3,6": empty,
        "4,6": empty,
        "5,6": empty,
        "6,6": empty,
        "7,6": empty,
        "8,6": empty,
        "9,6": empty,
        "10,6": empty,
        "11,6": empty,
        "12,6": empty,
        "13,6": tree,
        "14,6": empty,
        "15,6": empty,
        "16,6": empty,
        "17,6": empty,
        "18,6": empty,
        "19,6": empty,
        "20,6": empty,
        "21,6": empty,
        "22,6": empty,
        "23,6": empty,
        "24,6": tree,
        "25,6": tree,
        "26,6": tree,
        "27,6": tree,
        "28,6": tree,
        "29,6": tree,
        "30,6": tree,
        "31,6": tree,
        "32,6": tree,
        "33,6": tree,
        "34,6": tree,
        "35,6": empty,
        "36,6": tree,
        "37,6": tree,
        "38,6": tree,
        "39,6": tree,
        "40,6": tree,
        "41,6": tree,
        "42,6": tree,
        "43,6": tree,
        "44,6": tree,
        "45,6": tree,
        "46,6": tree,
        "47,6": empty,
        "48,6": empty,
        "49,6": empty,
        "50,6": empty,
        "51,6": empty,
        "52,6": empty,
        "53,6": empty,
        "54,6": empty,
        "55,6": empty,
        "56,6": tree,
        "57,6": tree,
        "58,6": empty,
        "59,6": empty,
        "60,6": empty,
        "61,6": empty,
        "62,6": empty,
        "63,6": empty,
        "64,6": empty,
        "1,7": empty,
        "2,7": empty,
        "3,7": empty,
        "4,7": empty,
        "5,7": empty,
        "6,7": empty,
        "7,7": empty,
        "8,7": empty,
        "9,7": empty,
        "10,7": empty,
        "11,7": empty,
        "12,7": empty,
        "13,7": empty,
        "14,7": empty,
        "15,7": empty,
        "16,7": empty,
        "17,7": empty,
        "18,7": empty,
        "19,7": empty,
        "20,7": empty,
        "21,7": tree,
        "22,7": empty,
        "23,7": empty,
        "24,7": empty,
        "25,7": empty,
        "26,7": empty,
        "27,7": empty,
        "28,7": empty,
        "29,7": empty,
        "30,7": tree,
        "31,7": tree,
        "32,7": tree,
        "33,7": tree,
        "34,7": tree,
        "35,7": tree,
        "36,7": tree,
        "37,7": tree,
        "38,7": tree,
        "39,7": tree,
        "40,7": empty,
        "41,7": empty,
        "42,7": empty,
        "43,7": empty,
        "44,7": empty,
        "45,7": empty,
        "46,7": empty,
        "47,7": empty,
        "48,7": empty,
        "49,7": empty,
        "50,7": empty,
        "51,7": tree,
        "52,7": empty,
        "53,7": empty,
        "54,7": empty,
        "55,7": empty,
        "56,7": empty,
        "57,7": empty,
        "58,7": empty,
        "59,7": empty,
        "60,7": empty,
        "61,7": empty,
        "62,7": empty,
        "63,7": empty,
        "64,7": empty,
        "1,8": empty,
        "2,8": empty,
        "3,8": empty,
        "4,8": empty,
        "5,8": farm,
        "6,8": farm,
        "7,8": farm,
        "8,8": farm,
        "9,8": farm,
        "10,8": farm,
        "11,8": farm,
        "12,8": farm,
        "13,8": farm,
        "14,8": empty,
        "15,8": empty,
        "16,8": empty,
        "17,8": empty,
        "18,8": empty,
        "19,8": empty,
        "20,8": empty,
        "21,8": empty,
        "22,8": empty,
        "23,8": empty,
        "24,8": empty,
        "25,8": empty,
        "26,8": empty,
        "27,8": empty,
        "28,8": empty,
        "29,8": empty,
        "30,8": empty,
        "31,8": empty,
        "32,8": empty,
        "33,8": empty,
        "34,8": tree,
        "35,8": tree,
        "36,8": empty,
        "37,8": empty,
        "38,8": empty,
        "39,8": empty,
        "40,8": empty,
        "41,8": empty,
        "42,8": empty,
        "43,8": empty,
        "44,8": empty,
        "45,8": empty,
        "46,8": empty,
        "47,8": empty,
        "48,8": empty,
        "49,8": empty,
        "50,8": empty,
        "51,8": tree,
        "52,8": empty,
        "53,8": empty,
        "54,8": empty,
        "55,8": empty,
        "56,8": empty,
        "57,8": empty,
        "58,8": empty,
        "59,8": empty,
        "60,8": empty,
        "61,8": empty,
        "62,8": empty,
        "63,8": empty,
        "64,8": empty,
        "1,9": empty,
        "2,9": empty,
        "3,9": empty,
        "4,9": empty,
        "5,9": farm,
        "6,9": farm,
        "7,9": farm,
        "8,9": farm,
        "9,9": farm,
        "10,9": farm,
        "11,9": farm,
        "12,9": farm,
        "13,9": farm,
        "14,9": empty,
        "15,9": empty,
        "16,9": empty,
        "17,9": empty,
        "18,9": empty,
        "19,9": empty,
        "20,9": empty,
        "21,9": empty,
        "22,9": empty,
        "23,9": empty,
        "24,9": empty,
        "25,9": empty,
        "26,9": empty,
        "27,9": empty,
        "28,9": empty,
        "29,9": empty,
        "30,9": empty,
        "31,9": empty,
        "32,9": empty,
        "33,9": empty,
        "34,9": empty,
        "35,9": empty,
        "36,9": empty,
        "37,9": empty,
        "38,9": empty,
        "39,9": empty,
        "40,9": empty,
        "41,9": empty,
        "42,9": empty,
        "43,9": empty,
        "44,9": empty,
        "45,9": tree,
        "46,9": empty,
        "47,9": empty,
        "48,9": empty,
        "49,9": empty,
        "50,9": empty,
        "51,9": empty,
        "52,9": empty,
        "53,9": empty,
        "54,9": empty,
        "55,9": empty,
        "56,9": empty,
        "57,9": empty,
        "58,9": empty,
        "59,9": empty,
        "60,9": empty,
        "61,9": empty,
        "62,9": empty,
        "63,9": empty,
        "64,9": empty,
        "1,10": empty,
        "2,10": empty,
        "3,10": empty,
        "4,10": empty,
        "5,10": farm,
        "6,10": farm,
        "7,10": farm,
        "8,10": farm,
        "9,10": farm,
        "10,10": farm,
        "11,10": farm,
        "12,10": farm,
        "13,10": farm,
        "14,10": empty,
        "15,10": empty,
        "16,10": empty,
        "17,10": empty,
        "18,10": empty,
        "19,10": empty,
        "20,10": empty,
        "21,10": empty,
        "22,10": empty,
        "23,10": empty,
        "24,10": empty,
        "25,10": empty,
        "26,10": empty,
        "27,10": empty,
        "28,10": empty,
        "29,10": empty,
        "30,10": empty,
        "31,10": empty,
        "32,10": empty,
        "33,10": empty,
        "34,10": empty,
        "35,10": empty,
        "36,10": empty,
        "37,10": empty,
        "38,10": empty,
        "39,10": empty,
        "40,10": empty,
        "41,10": empty,
        "42,10": empty,
        "43,10": empty,
        "44,10": empty,
        "45,10": empty,
        "46,10": empty,
        "47,10": empty,
        "48,10": empty,
        "49,10": empty,
        "50,10": empty,
        "51,10": empty,
        "52,10": empty,
        "53,10": empty,
        "54,10": empty,
        "55,10": empty,
        "56,10": empty,
        "57,10": empty,
        "58,10": empty,
        "59,10": empty,
        "60,10": empty,
        "61,10": empty,
        "62,10": empty,
        "63,10": empty,
        "64,10": empty,
        "1,11": empty,
        "2,11": empty,
        "3,11": empty,
        "4,11": empty,
        "5,11": farm,
        "6,11": farm,
        "7,11": farm,
        "8,11": farm,
        "9,11": farm,
        "10,11": farm,
        "11,11": farm,
        "12,11": farm,
        "13,11": farm,
        "14,11": empty,
        "15,11": empty,
        "16,11": empty,
        "17,11": empty,
        "18,11": empty,
        "19,11": empty,
        "20,11": tree,
        "21,11": empty,
        "22,11": empty,
        "23,11": empty,
        "24,11": empty,
        "25,11": empty,
        "26,11": empty,
        "27,11": empty,
        "28,11": empty,
        "29,11": empty,
        "30,11": empty,
        "31,11": empty,
        "32,11": empty,
        "33,11": empty,
        "34,11": empty,
        "35,11": empty,
        "36,11": empty,
        "37,11": empty,
        "38,11": empty,
        "39,11": empty,
        "40,11": empty,
        "41,11": empty,
        "42,11": empty,
        "43,11": empty,
        "44,11": empty,
        "45,11": empty,
        "46,11": empty,
        "47,11": empty,
        "48,11": empty,
        "49,11": empty,
        "50,11": empty,
        "51,11": empty,
        "52,11": empty,
        "53,11": empty,
        "54,11": empty,
        "55,11": empty,
        "56,11": empty,
        "57,11": empty,
        "58,11": empty,
        "59,11": empty,
        "60,11": empty,
        "61,11": empty,
        "62,11": empty,
        "63,11": empty,
        "64,11": empty,
        "1,12": empty,
        "2,12": empty,
        "3,12": empty,
        "4,12": empty,
        "5,12": empty,
        "6,12": empty,
        "7,12": empty,
        "8,12": empty,
        "9,12": empty,
        "10,12": empty,
        "11,12": empty,
        "12,12": empty,
        "13,12": empty,
        "14,12": empty,
        "15,12": empty,
        "16,12": empty,
        "17,12": empty,
        "18,12": empty,
        "19,12": empty,
        "20,12": empty,
        "21,12": empty,
        "22,12": empty,
        "23,12": empty,
        "24,12": empty,
        "25,12": empty,
        "26,12": empty,
        "27,12": empty,
        "28,12": empty,
        "29,12": empty,
        "30,12": empty,
        "31,12": empty,
        "32,12": empty,
        "33,12": empty,
        "34,12": empty,
        "35,12": empty,
        "36,12": empty,
        "37,12": empty,
        "38,12": empty,
        "39,12": empty,
        "40,12": empty,
        "41,12": empty,
        "42,12": empty,
        "43,12": empty,
        "44,12": empty,
        "45,12": empty,
        "46,12": empty,
        "47,12": empty,
        "48,12": empty,
        "49,12": empty,
        "50,12": empty,
        "51,12": empty,
        "52,12": empty,
        "53,12": empty,
        "54,12": empty,
        "55,12": empty,
        "56,12": empty,
        "57,12": empty,
        "58,12": empty,
        "59,12": empty,
        "60,12": empty,
        "61,12": empty,
        "62,12": empty,
        "63,12": empty,
        "64,12": empty,
        "1,13": empty,
        "2,13": empty,
        "3,13": empty,
        "4,13": empty,
        "5,13": empty,
        "6,13": farm,
        "7,13": farm,
        "8,13": farm,
        "9,13": farm,
        "10,13": farm,
        "11,13": farm,
        "12,13": farm,
        "13,13": farm,
        "14,13": farm,
        "15,13": farm,
        "16,13": farm,
        "17,13": farm,
        "18,13": farm,
        "19,13": farm,
        "20,13": farm,
        "21,13": empty,
        "22,13": empty,
        "23,13": empty,
        "24,13": empty,
        "25,13": empty,
        "26,13": empty,
        "27,13": empty,
        "28,13": empty,
        "29,13": empty,
        "30,13": empty,
        "31,13": empty,
        "32,13": empty,
        "33,13": empty,
        "34,13": empty,
        "35,13": empty,
        "36,13": empty,
        "37,13": empty,
        "38,13": empty,
        "39,13": empty,
        "40,13": empty,
        "41,13": empty,
        "42,13": empty,
        "43,13": empty,
        "44,13": empty,
        "45,13": empty,
        "46,13": empty,
        "47,13": empty,
        "48,13": empty,
        "49,13": empty,
        "50,13": empty,
        "51,13": empty,
        "52,13": empty,
        "53,13": empty,
        "54,13": empty,
        "55,13": empty,
        "56,13": empty,
        "57,13": empty,
        "58,13": empty,
        "59,13": empty,
        "60,13": empty,
        "61,13": empty,
        "62,13": empty,
        "63,13": empty,
        "64,13": empty,
        "1,14": empty,
        "2,14": tree,
        "3,14": empty,
        "4,14": empty,
        "5,14": empty,
        "6,14": farm,
        "7,14": farm,
        "8,14": farm,
        "9,14": farm,
        "10,14": farm,
        "11,14": farm,
        "12,14": farm,
        "13,14": farm,
        "14,14": farm,
        "15,14": farm,
        "16,14": farm,
        "17,14": farm,
        "18,14": farm,
        "19,14": farm,
        "20,14": farm,
        "21,14": empty,
        "22,14": empty,
        "23,14": empty,
        "24,14": empty,
        "25,14": empty,
        "26,14": empty,
        "27,14": empty,
        "28,14": empty,
        "29,14": empty,
        "30,14": empty,
        "31,14": empty,
        "32,14": empty,
        "33,14": empty,
        "34,14": empty,
        "35,14": empty,
        "36,14": empty,
        "37,14": empty,
        "38,14": empty,
        "39,14": empty,
        "40,14": empty,
        "41,14": empty,
        "42,14": empty,
        "43,14": empty,
        "44,14": empty,
        "45,14": empty,
        "46,14": empty,
        "47,14": empty,
        "48,14": empty,
        "49,14": empty,
        "50,14": empty,
        "51,14": empty,
        "52,14": empty,
        "53,14": empty,
        "54,14": empty,
        "55,14": empty,
        "56,14": empty,
        "57,14": empty,
        "58,14": empty,
        "59,14": empty,
        "60,14": empty,
        "61,14": empty,
        "62,14": empty,
        "63,14": empty,
        "64,14": empty,
        "1,15": empty,
        "2,15": empty,
        "3,15": empty,
        "4,15": empty,
        "5,15": empty,
        "6,15": farm,
        "7,15": farm,
        "8,15": farm,
        "9,15": farm,
        "10,15": farm,
        "11,15": farm,
        "12,15": farm,
        "13,15": farm,
        "14,15": farm,
        "15,15": farm,
        "16,15": farm,
        "17,15": farm,
        "18,15": farm,
        "19,15": farm,
        "20,15": farm,
        "21,15": empty,
        "22,15": empty,
        "23,15": empty,
        "24,15": empty,
        "25,15": empty,
        "26,15": empty,
        "27,15": empty,
        "28,15": empty,
        "29,15": empty,
        "30,15": empty,
        "31,15": empty,
        "32,15": empty,
        "33,15": empty,
        "34,15": empty,
        "35,15": empty,
        "36,15": empty,
        "37,15": empty,
        "38,15": empty,
        "39,15": empty,
        "40,15": empty,
        "41,15": empty,
        "42,15": empty,
        "43,15": empty,
        "44,15": empty,
        "45,15": empty,
        "46,15": empty,
        "47,15": empty,
        "48,15": empty,
        "49,15": empty,
        "50,15": empty,
        "51,15": empty,
        "52,15": empty,
        "53,15": empty,
        "54,15": empty,
        "55,15": empty,
        "56,15": empty,
        "57,15": empty,
        "58,15": empty,
        "59,15": empty,
        "60,15": empty,
        "61,15": empty,
        "62,15": empty,
        "63,15": empty,
        "64,15": empty,
        "1,16": empty,
        "2,16": empty,
        "3,16": empty,
        "4,16": empty,
        "5,16": empty,
        "6,16": empty,
        "7,16": empty,
        "8,16": empty,
        "9,16": empty,
        "10,16": empty,
        "11,16": empty,
        "12,16": empty,
        "13,16": empty,
        "14,16": empty,
        "15,16": empty,
        "16,16": empty,
        "17,16": empty,
        "18,16": empty,
        "19,16": empty,
        "20,16": empty,
        "21,16": empty,
        "22,16": empty,
        "23,16": empty,
        "24,16": tree,
        "25,16": empty,
        "26,16": empty,
        "27,16": empty,
        "28,16": empty,
        "29,16": empty,
        "30,16": empty,
        "31,16": empty,
        "32,16": town_center,
        "33,16": empty,
        "34,16": empty,
        "35,16": empty,
        "36,16": empty,
        "37,16": empty,
        "38,16": empty,
        "39,16": empty,
        "40,16": empty,
        "41,16": empty,
        "42,16": empty,
        "43,16": empty,
        "44,16": empty,
        "45,16": empty,
        "46,16": empty,
        "47,16": empty,
        "48,16": empty,
        "49,16": empty,
        "50,16": empty,
        "51,16": empty,
        "52,16": empty,
        "53,16": empty,
        "54,16": empty,
        "55,16": empty,
        "56,16": empty,
        "57,16": empty,
        "58,16": empty,
        "59,16": empty,
        "60,16": empty,
        "61,16": empty,
        "62,16": empty,
        "63,16": empty,
        "64,16": empty,
        "1,17": empty,
        "2,17": farm,
        "3,17": farm,
        "4,17": farm,
        "5,17": farm,
        "6,17": farm,
        "7,17": farm,
        "8,17": farm,
        "9,17": empty,
        "10,17": empty,
        "11,17": empty,
        "12,17": empty,
        "13,17": empty,
        "14,17": empty,
        "15,17": empty,
        "16,17": empty,
        "17,17": empty,
        "18,17": empty,
        "19,17": empty,
        "20,17": empty,
        "21,17": empty,
        "22,17": empty,
        "23,17": empty,
        "24,17": empty,
        "25,17": empty,
        "26,17": empty,
        "27,17": empty,
        "28,17": empty,
        "29,17": empty,
        "30,17": empty,
        "31,17": empty,
        "32,17": empty,
        "33,17": empty,
        "34,17": empty,
        "35,17": empty,
        "36,17": empty,
        "37,17": empty,
        "38,17": empty,
        "39,17": empty,
        "40,17": empty,
        "41,17": empty,
        "42,17": empty,
        "43,17": empty,
        "44,17": empty,
        "45,17": empty,
        "46,17": empty,
        "47,17": empty,
        "48,17": empty,
        "49,17": empty,
        "50,17": empty,
        "51,17": empty,
        "52,17": empty,
        "53,17": empty,
        "54,17": empty,
        "55,17": empty,
        "56,17": empty,
        "57,17": empty,
        "58,17": empty,
        "59,17": empty,
        "60,17": empty,
        "61,17": empty,
        "62,17": empty,
        "63,17": empty,
        "64,17": empty,
        "1,18": empty,
        "2,18": farm,
        "3,18": farm,
        "4,18": farm,
        "5,18": farm,
        "6,18": farm,
        "7,18": farm,
        "8,18": farm,
        "9,18": empty,
        "10,18": empty,
        "11,18": empty,
        "12,18": farm,
        "13,18": farm,
        "14,18": farm,
        "15,18": farm,
        "16,18": farm,
        "17,18": farm,
        "18,18": farm,
        "19,18": farm,
        "20,18": farm,
        "21,18": farm,
        "22,18": farm,
        "23,18": farm,
        "24,18": farm,
        "25,18": farm,
        "26,18": farm,
        "27,18": farm,
        "28,18": farm,
        "29,18": empty,
        "30,18": empty,
        "31,18": empty,
        "32,18": empty,
        "33,18": empty,
        "34,18": empty,
        "35,18": empty,
        "36,18": empty,
        "37,18": empty,
        "38,18": empty,
        "39,18": empty,
        "40,18": empty,
        "41,18": empty,
        "42,18": empty,
        "43,18": empty,
        "44,18": empty,
        "45,18": empty,
        "46,18": empty,
        "47,18": empty,
        "48,18": empty,
        "49,18": empty,
        "50,18": empty,
        "51,18": empty,
        "52,18": empty,
        "53,18": empty,
        "54,18": empty,
        "55,18": empty,
        "56,18": empty,
        "57,18": empty,
        "58,18": empty,
        "59,18": empty,
        "60,18": empty,
        "61,18": empty,
        "62,18": empty,
        "63,18": empty,
        "64,18": empty,
        "1,19": empty,
        "2,19": farm,
        "3,19": farm,
        "4,19": farm,
        "5,19": farm,
        "6,19": farm,
        "7,19": farm,
        "8,19": farm,
        "9,19": empty,
        "10,19": empty,
        "11,19": empty,
        "12,19": farm,
        "13,19": farm,
        "14,19": farm,
        "15,19": farm,
        "16,19": farm,
        "17,19": farm,
        "18,19": farm,
        "19,19": farm,
        "20,19": farm,
        "21,19": farm,
        "22,19": farm,
        "23,19": farm,
        "24,19": farm,
        "25,19": farm,
        "26,19": farm,
        "27,19": farm,
        "28,19": farm,
        "29,19": empty,
        "30,19": empty,
        "31,19": empty,
        "32,19": empty,
        "33,19": empty,
        "34,19": empty,
        "35,19": empty,
        "36,19": empty,
        "37,19": empty,
        "38,19": empty,
        "39,19": empty,
        "40,19": empty,
        "41,19": empty,
        "42,19": empty,
        "43,19": empty,
        "44,19": empty,
        "45,19": empty,
        "46,19": empty,
        "47,19": empty,
        "48,19": empty,
        "49,19": empty,
        "50,19": empty,
        "51,19": empty,
        "52,19": empty,
        "53,19": empty,
        "54,19": empty,
        "55,19": empty,
        "56,19": empty,
        "57,19": empty,
        "58,19": stone,
        "59,19": stone,
        "60,19": empty,
        "61,19": empty,
        "62,19": empty,
        "63,19": empty,
        "64,19": empty,
        "1,20": empty,
        "2,20": farm,
        "3,20": farm,
        "4,20": farm,
        "5,20": farm,
        "6,20": farm,
        "7,20": farm,
        "8,20": farm,
        "9,20": empty,
        "10,20": empty,
        "11,20": empty,
        "12,20": farm,
        "13,20": farm,
        "14,20": farm,
        "15,20": farm,
        "16,20": farm,
        "17,20": farm,
        "18,20": farm,
        "19,20": farm,
        "20,20": farm,
        "21,20": farm,
        "22,20": farm,
        "23,20": farm,
        "24,20": farm,
        "25,20": farm,
        "26,20": farm,
        "27,20": farm,
        "28,20": farm,
        "29,20": empty,
        "30,20": empty,
        "31,20": empty,
        "32,20": empty,
        "33,20": empty,
        "34,20": empty,
        "35,20": empty,
        "36,20": empty,
        "37,20": empty,
        "38,20": empty,
        "39,20": empty,
        "40,20": empty,
        "41,20": empty,
        "42,20": empty,
        "43,20": empty,
        "44,20": empty,
        "45,20": empty,
        "46,20": empty,
        "47,20": empty,
        "48,20": empty,
        "49,20": empty,
        "50,20": empty,
        "51,20": empty,
        "52,20": empty,
        "53,20": empty,
        "54,20": empty,
        "55,20": empty,
        "56,20": stone,
        "57,20": stone,
        "58,20": stone,
        "59,20": stone,
        "60,20": empty,
        "61,20": empty,
        "62,20": empty,
        "63,20": empty,
        "64,20": empty,
        "1,21": empty,
        "2,21": farm,
        "3,21": farm,
        "4,21": farm,
        "5,21": farm,
        "6,21": farm,
        "7,21": farm,
        "8,21": farm,
        "9,21": empty,
        "10,21": empty,
        "11,21": empty,
        "12,21": empty,
        "13,21": empty,
        "14,21": empty,
        "15,21": empty,
        "16,21": empty,
        "17,21": empty,
        "18,21": empty,
        "19,21": empty,
        "20,21": empty,
        "21,21": empty,
        "22,21": empty,
        "23,21": empty,
        "24,21": empty,
        "25,21": empty,
        "26,21": empty,
        "27,21": empty,
        "28,21": empty,
        "29,21": empty,
        "30,21": empty,
        "31,21": empty,
        "32,21": empty,
        "33,21": empty,
        "34,21": empty,
        "35,21": empty,
        "36,21": empty,
        "37,21": empty,
        "38,21": empty,
        "39,21": empty,
        "40,21": empty,
        "41,21": empty,
        "42,21": empty,
        "43,21": empty,
        "44,21": empty,
        "45,21": empty,
        "46,21": empty,
        "47,21": empty,
        "48,21": empty,
        "49,21": empty,
        "50,21": empty,
        "51,21": empty,
        "52,21": empty,
        "53,21": empty,
        "54,21": stone,
        "55,21": stone,
        "56,21": stone,
        "57,21": stone,
        "58,21": stone,
        "59,21": stone,
        "60,21": stone,
        "61,21": empty,
        "62,21": empty,
        "63,21": empty,
        "64,21": empty,
        "1,22": empty,
        "2,22": farm,
        "3,22": farm,
        "4,22": farm,
        "5,22": farm,
        "6,22": farm,
        "7,22": farm,
        "8,22": farm,
        "9,22": empty,
        "10,22": empty,
        "11,22": empty,
        "12,22": empty,
        "13,22": tree,
        "14,22": empty,
        "15,22": empty,
        "16,22": empty,
        "17,22": empty,
        "18,22": empty,
        "19,22": empty,
        "20,22": empty,
        "21,22": empty,
        "22,22": empty,
        "23,22": empty,
        "24,22": empty,
        "25,22": empty,
        "26,22": empty,
        "27,22": empty,
        "28,22": empty,
        "29,22": empty,
        "30,22": empty,
        "31,22": empty,
        "32,22": empty,
        "33,22": empty,
        "34,22": empty,
        "35,22": empty,
        "36,22": empty,
        "37,22": empty,
        "38,22": empty,
        "39,22": empty,
        "40,22": empty,
        "41,22": empty,
        "42,22": empty,
        "43,22": empty,
        "44,22": empty,
        "45,22": empty,
        "46,22": empty,
        "47,22": empty,
        "48,22": empty,
        "49,22": empty,
        "50,22": empty,
        "51,22": empty,
        "52,22": stone,
        "53,22": stone,
        "54,22": stone,
        "55,22": stone,
        "56,22": stone,
        "57,22": stone,
        "58,22": stone,
        "59,22": stone,
        "60,22": empty,
        "61,22": empty,
        "62,22": empty,
        "63,22": empty,
        "64,22": empty,
        "1,23": empty,
        "2,23": farm,
        "3,23": farm,
        "4,23": farm,
        "5,23": farm,
        "6,23": farm,
        "7,23": farm,
        "8,23": farm,
        "9,23": empty,
        "10,23": empty,
        "11,23": empty,
        "12,23": empty,
        "13,23": tree,
        "14,23": empty,
        "15,23": empty,
        "16,23": empty,
        "17,23": empty,
        "18,23": empty,
        "19,23": empty,
        "20,23": empty,
        "21,23": empty,
        "22,23": empty,
        "23,23": empty,
        "24,23": empty,
        "25,23": empty,
        "26,23": empty,
        "27,23": empty,
        "28,23": empty,
        "29,23": empty,
        "30,23": empty,
        "31,23": tree,
        "32,23": empty,
        "33,23": empty,
        "34,23": empty,
        "35,23": empty,
        "36,23": empty,
        "37,23": empty,
        "38,23": empty,
        "39,23": empty,
        "40,23": empty,
        "41,23": empty,
        "42,23": empty,
        "43,23": empty,
        "44,23": empty,
        "45,23": empty,
        "46,23": empty,
        "47,23": empty,
        "48,23": empty,
        "49,23": empty,
        "50,23": empty,
        "51,23": empty,
        "52,23": empty,
        "53,23": stone,
        "54,23": stone,
        "55,23": stone,
        "56,23": stone,
        "57,23": stone,
        "58,23": stone,
        "59,23": stone,
        "60,23": empty,
        "61,23": empty,
        "62,23": empty,
        "63,23": empty,
        "64,23": empty,
        "1,24": empty,
        "2,24": empty,
        "3,24": empty,
        "4,24": empty,
        "5,24": empty,
        "6,24": empty,
        "7,24": empty,
        "8,24": empty,
        "9,24": empty,
        "10,24": empty,
        "11,24": empty,
        "12,24": empty,
        "13,24": empty,
        "14,24": empty,
        "15,24": empty,
        "16,24": empty,
        "17,24": empty,
        "18,24": empty,
        "19,24": empty,
        "20,24": empty,
        "21,24": empty,
        "22,24": empty,
        "23,24": empty,
        "24,24": empty,
        "25,24": empty,
        "26,24": empty,
        "27,24": empty,
        "28,24": empty,
        "29,24": empty,
        "30,24": empty,
        "31,24": empty,
        "32,24": empty,
        "33,24": empty,
        "34,24": empty,
        "35,24": empty,
        "36,24": empty,
        "37,24": empty,
        "38,24": empty,
        "39,24": empty,
        "40,24": empty,
        "41,24": empty,
        "42,24": empty,
        "43,24": empty,
        "44,24": empty,
        "45,24": empty,
        "46,24": empty,
        "47,24": empty,
        "48,24": empty,
        "49,24": empty,
        "50,24": empty,
        "51,24": empty,
        "52,24": empty,
        "53,24": empty,
        "54,24": empty,
        "55,24": stone,
        "56,24": stone,
        "57,24": stone,
        "58,24": stone,
        "59,24": stone,
        "60,24": stone,
        "61,24": stone,
        "62,24": empty,
        "63,24": empty,
        "64,24": empty,
        "1,25": empty,
        "2,25": empty,
        "3,25": empty,
        "4,25": empty,
        "5,25": empty,
        "6,25": empty,
        "7,25": empty,
        "8,25": empty,
        "9,25": empty,
        "10,25": empty,
        "11,25": empty,
        "12,25": empty,
        "13,25": water,
        "14,25": water,
        "15,25": water,
        "16,25": water,
        "17,25": water,
        "18,25": water,
        "19,25": water,
        "20,25": water,
        "21,25": water,
        "22,25": water,
        "23,25": water,
        "24,25": water,
        "25,25": water,
        "26,25": water,
        "27,25": water,
        "28,25": water,
        "29,25": empty,
        "30,25": empty,
        "31,25": empty,
        "32,25": empty,
        "33,25": empty,
        "34,25": empty,
        "35,25": empty,
        "36,25": water,
        "37,25": water,
        "38,25": water,
        "39,25": water,
        "40,25": water,
        "41,25": water,
        "42,25": empty,
        "43,25": empty,
        "44,25": empty,
        "45,25": empty,
        "46,25": empty,
        "47,25": empty,
        "48,25": empty,
        "49,25": empty,
        "50,25": empty,
        "51,25": empty,
        "52,25": empty,
        "53,25": empty,
        "54,25": empty,
        "55,25": empty,
        "56,25": empty,
        "57,25": stone,
        "58,25": stone,
        "59,25": stone,
        "60,25": stone,
        "61,25": stone,
        "62,25": stone,
        "63,25": empty,
        "64,25": empty,
        "1,26": water,
        "2,26": water,
        "3,26": water,
        "4,26": empty,
        "5,26": empty,
        "6,26": water,
        "7,26": water,
        "8,26": water,
        "9,26": water,
        "10,26": water,
        "11,26": water,
        "12,26": water,
        "13,26": water,
        "14,26": water,
        "15,26": water,
        "16,26": water,
        "17,26": water,
        "18,26": water,
        "19,26": water,
        "20,26": water,
        "21,26": water,
        "22,26": water,
        "23,26": water,
        "24,26": water,
        "25,26": water,
        "26,26": water,
        "27,26": water,
        "28,26": water,
        "29,26": water,
        "30,26": water,
        "31,26": water,
        "32,26": water,
        "33,26": water,
        "34,26": water,
        "35,26": water,
        "36,26": water,
        "37,26": water,
        "38,26": water,
        "39,26": water,
        "40,26": water,
        "41,26": water,
        "42,26": water,
        "43,26": water,
        "44,26": water,
        "45,26": water,
        "46,26": water,
        "47,26": water,
        "48,26": water,
        "49,26": water,
        "50,26": empty,
        "51,26": empty,
        "52,26": empty,
        "53,26": empty,
        "54,26": empty,
        "55,26": empty,
        "56,26": empty,
        "57,26": tree,
        "58,26": empty,
        "59,26": empty,
        "60,26": empty,
        "61,26": empty,
        "62,26": empty,
        "63,26": empty,
        "64,26": empty,
        "1,27": water,
        "2,27": water,
        "3,27": water,
        "4,27": water,
        "5,27": water,
        "6,27": water,
        "7,27": water,
        "8,27": water,
        "9,27": water,
        "10,27": water,
        "11,27": water,
        "12,27": water,
        "13,27": water,
        "14,27": water,
        "15,27": water,
        "16,27": water,
        "17,27": water,
        "18,27": water,
        "19,27": water,
        "20,27": water,
        "21,27": water,
        "22,27": water,
        "23,27": water,
        "24,27": water,
        "25,27": water,
        "26,27": water,
        "27,27": water,
        "28,27": water,
        "29,27": water,
        "30,27": water,
        "31,27": water,
        "32,27": water,
        "33,27": water,
        "34,27": water,
        "35,27": water,
        "36,27": water,
        "37,27": water,
        "38,27": water,
        "39,27": water,
        "40,27": water,
        "41,27": water,
        "42,27": water,
        "43,27": water,
        "44,27": water,
        "45,27": water,
        "46,27": water,
        "47,27": water,
        "48,27": water,
        "49,27": water,
        "50,27": water,
        "51,27": water,
        "52,27": empty,
        "53,27": empty,
        "54,27": empty,
        "55,27": empty,
        "56,27": empty,
        "57,27": empty,
        "58,27": empty,
        "59,27": empty,
        "60,27": empty,
        "61,27": empty,
        "62,27": empty,
        "63,27": tree,
        "64,27": empty,
        "1,28": water,
        "2,28": water,
        "3,28": water,
        "4,28": water,
        "5,28": water,
        "6,28": water,
        "7,28": water,
        "8,28": water,
        "9,28": water,
        "10,28": water,
        "11,28": water,
        "12,28": water,
        "13,28": water,
        "14,28": water,
        "15,28": water,
        "16,28": water,
        "17,28": water,
        "18,28": water,
        "19,28": water,
        "20,28": water,
        "21,28": water,
        "22,28": water,
        "23,28": water,
        "24,28": water,
        "25,28": water,
        "26,28": water,
        "27,28": water,
        "28,28": water,
        "29,28": water,
        "30,28": water,
        "31,28": water,
        "32,28": water,
        "33,28": water,
        "34,28": water,
        "35,28": water,
        "36,28": water,
        "37,28": water,
        "38,28": water,
        "39,28": water,
        "40,28": water,
        "41,28": water,
        "42,28": water,
        "43,28": water,
        "44,28": water,
        "45,28": water,
        "46,28": water,
        "47,28": water,
        "48,28": water,
        "49,28": water,
        "50,28": water,
        "51,28": water,
        "52,28": water,
        "53,28": water,
        "54,28": water,
        "55,28": empty,
        "56,28": empty,
        "57,28": empty,
        "58,28": empty,
        "59,28": empty,
        "60,28": empty,
        "61,28": empty,
        "62,28": empty,
        "63,28": empty,
        "64,28": empty,
        "1,29": water,
        "2,29": water,
        "3,29": water,
        "4,29": water,
        "5,29": water,
        "6,29": water,
        "7,29": water,
        "8,29": water,
        "9,29": water,
        "10,29": water,
        "11,29": water,
        "12,29": water,
        "13,29": empty,
        "14,29": empty,
        "15,29": empty,
        "16,29": tree,
        "17,29": empty,
        "18,29": empty,
        "19,29": empty,
        "20,29": empty,
        "21,29": tree,
        "22,29": empty,
        "23,29": empty,
        "24,29": empty,
        "25,29": tree,
        "26,29": empty,
        "27,29": empty,
        "28,29": empty,
        "29,29": water,
        "30,29": water,
        "31,29": water,
        "32,29": water,
        "33,29": water,
        "34,29": water,
        "35,29": water,
        "36,29": water,
        "37,29": water,
        "38,29": water,
        "39,29": water,
        "40,29": water,
        "41,29": water,
        "42,29": water,
        "43,29": water,
        "44,29": water,
        "45,29": water,
        "46,29": water,
        "47,29": water,
        "48,29": water,
        "49,29": water,
        "50,29": water,
        "51,29": water,
        "52,29": water,
        "53,29": water,
        "54,29": water,
        "55,29": water,
        "56,29": water,
        "57,29": empty,
        "58,29": empty,
        "59,29": empty,
        "60,29": tree,
        "61,29": empty,
        "62,29": empty,
        "63,29": empty,
        "64,29": empty,
        "1,30": empty,
        "2,30": empty,
        "3,30": water,
        "4,30": water,
        "5,30": water,
        "6,30": empty,
        "7,30": empty,
        "8,30": tree,
        "9,30": empty,
        "10,30": empty,
        "11,30": empty,
        "12,30": empty,
        "13,30": empty,
        "14,30": empty,
        "15,30": tree,
        "16,30": empty,
        "17,30": empty,
        "18,30": empty,
        "19,30": empty,
        "20,30": tree,
        "21,30": empty,
        "22,30": empty,
        "23,30": empty,
        "24,30": tree,
        "25,30": empty,
        "26,30": empty,
        "27,30": empty,
        "28,30": empty,
        "29,30": empty,
        "30,30": empty,
        "31,30": empty,
        "32,30": empty,
        "33,30": empty,
        "34,30": empty,
        "35,30": empty,
        "36,30": empty,
        "37,30": empty,
        "38,30": tree,
        "39,30": empty,
        "40,30": empty,
        "41,30": empty,
        "42,30": tree,
        "43,30": empty,
        "44,30": water,
        "45,30": water,
        "46,30": water,
        "47,30": water,
        "48,30": water,
        "49,30": water,
        "50,30": water,
        "51,30": water,
        "52,30": water,
        "53,30": water,
        "54,30": water,
        "55,30": water,
        "56,30": water,
        "57,30": water,
        "58,30": water,
        "59,30": empty,
        "60,30": empty,
        "61,30": empty,
        "62,30": empty,
        "63,30": empty,
        "64,30": empty,
        "1,31": empty,
        "2,31": empty,
        "3,31": tree,
        "4,31": empty,
        "5,31": empty,
        "6,31": empty,
        "7,31": empty,
        "8,31": tree,
        "9,31": empty,
        "10,31": empty,
        "11,31": tree,
        "12,31": empty,
        "13,31": empty,
        "14,31": empty,
        "15,31": empty,
        "16,31": empty,
        "17,31": empty,
        "18,31": empty,
        "19,31": empty,
        "20,31": tree,
        "21,31": empty,
        "22,31": empty,
        "23,31": tree,
        "24,31": empty,
        "25,31": empty,
        "26,31": empty,
        "27,31": empty,
        "28,31": empty,
        "29,31": empty,
        "30,31": empty,
        "31,31": tree,
        "32,31": empty,
        "33,31": empty,
        "34,31": tree,
        "35,31": empty,
        "36,31": empty,
        "37,31": empty,
        "38,31": empty,
        "39,31": tree,
        "40,31": empty,
        "41,31": empty,
        "42,31": empty,
        "43,31": empty,
        "44,31": empty,
        "45,31": water,
        "46,31": water,
        "47,31": water,
        "48,31": water,
        "49,31": water,
        "50,31": water,
        "51,31": water,
        "52,31": water,
        "53,31": water,
        "54,31": water,
        "55,31": water,
        "56,31": water,
        "57,31": water,
        "58,31": water,
        "59,31": water,
        "60,31": water,
        "61,31": water,
        "62,31": empty,
        "63,31": empty,
        "64,31": empty,
        "1,32": empty,
        "2,32": empty,
        "3,32": empty,
        "4,32": tree,
        "5,32": empty,
        "6,32": tree,
        "7,32": empty,
        "8,32": empty,
        "9,32": empty,
        "10,32": empty,
        "11,32": empty,
        "12,32": tree,
        "13,32": empty,
        "14,32": empty,
        "15,32": empty,
        "16,32": empty,
        "17,32": tree,
        "18,32": empty,
        "19,32": empty,
        "20,32": empty,
        "21,32": empty,
        "22,32": empty,
        "23,32": empty,
        "24,32": empty,
        "25,32": empty,
        "26,32": empty,
        "27,32": empty,
        "28,32": empty,
        "29,32": tree,
        "30,32": empty,
        "31,32": empty,
        "32,32": empty,
        "33,32": empty,
        "34,32": empty,
        "35,32": empty,
        "36,32": tree,
        "37,32": empty,
        "38,32": tree,
        "39,32": empty,
        "40,32": tree,
        "41,32": tree,
        "42,32": empty,
        "43,32": empty,
        "44,32": empty,
        "45,32": water,
        "46,32": water,
        "47,32": water,
        "48,32": water,
        "49,32": water,
        "50,32": water,
        "51,32": water,
        "52,32": water,
        "53,32": water,
        "54,32": water,
        "55,32": water,
        "56,32": water,
        "57,32": water,
        "58,32": water,
        "59,32": water,
        "60,32": water,
        "61,32": water,
        "62,32": water,
        "63,32": empty,
        "64,32": empty,
    }
    return default_map


def print_game_map(map):
    while printmap == 1:
        printmap_unit_data = unit_data.copy()
        printmap_game_map = map.copy()

        for key in printmap_game_map:
            if printmap_game_map[key] == "empty":
                printmap_game_map[key] = " "
            elif printmap_game_map[key] == "tree":
                printmap_game_map[key] = colored("@", "green")
            elif printmap_game_map[key] == "farm":
                printmap_game_map[key] = colored(";", "yellow")
            elif printmap_game_map[key] == "water":
                printmap_game_map[key] = colored("~", "cyan")
            elif printmap_game_map[key] == "stone":
                printmap_game_map[key] = "o"

        for unit_name in printmap_unit_data:
            if printmap_unit_data[unit_name] != "deleted":
                if printmap_unit_data[unit_name][5] == "militia_" + enemy_num \
                    or printmap_unit_data[unit_name][5] == "archer_" \
                    + enemy_num or printmap_unit_data[unit_name] == "knight_" \
                    + enemy_num or \
                        printmap_unit_data[unit_name][5] == "ram_" + enemy_num:
                    printmap_game_map[list(printmap_game_map.keys())[list(
                        printmap_game_map.values()).index(unit_name)]] = \
                        colored(str(printmap_unit_data[unit_name][0]), "red")
                    printmap_unit_data[unit_name] = "deleted"
            else:
                printmap_game_map[list(printmap_game_map.keys())[list(
                    printmap_game_map.values()).index(unit_name)]] = \
                    str(printmap_unit_data[unit_name][0])
                printmap_unit_data[unit_name] = "deleted"

        while "deleted" in printmap_unit_data.values():
            printmap_unit_data.pop(list(printmap_unit_data.keys())[
                list(printmap_unit_data.values()).index("deleted")])

        # Print map
        print(" " + " " + "|" + "0" + "0" + "0" + "0" + "0" + "0" + "0" + "0" +
              "0" + "1" + "1" + "1" + "1" + "1" + "1" + "1" + "1" + "1" +
              "1" + "2" + "2" + "2" + "2" +
              "2" + "2" + "2" + "2" + "2" + "2" + "3" + "3" + "3" + "3" +
              "3" + "3" + "3" + "3" + "3" + "3" + "4" +
              "4" + "4" + "4" + "4" + "4" + "4" + "4" + "4" + "4" + "5" +
              "5" + "5" + "5" + "5" + "5" + "5" + "5" + "5" + "5" + "6" +
              "6" + "6" + "6" + "6")
        print(" " + " " + "|" + "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" +
              "9" + "0" + "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" +
              "9" + "0" + "1" + "2" + "3" +
              "4" + "5" + "6" + "7" + "8" + "9" + "0" + "1" + "2" + "3" +
              "4" + "5" + "6" + "7" + "8" + "9" + "0" +
              "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "0" +
              "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "0" +
              "1" + "2" + "3" + "4")
        print("-" + "-" + "|" +
              "-------------------------------------------------------------" +
              "---"
              )
        print("01" + "|" +
              printmap_game_map["1,1"] + printmap_game_map["2,1"] +
              printmap_game_map["3,1"] + printmap_game_map[
                  "4,1"] +
              printmap_game_map["5,1"] + printmap_game_map["6,1"] +
              printmap_game_map["7,1"] + printmap_game_map["8,1"] +
              printmap_game_map["9,1"] + printmap_game_map[
                  "10,1"] +
              printmap_game_map["11,1"] + printmap_game_map[
                  "12,1"] + printmap_game_map["13,1"] + printmap_game_map[
                  "14,1"] + printmap_game_map["15,1"] +
              printmap_game_map["16,1"] + printmap_game_map["17,1"] +
              printmap_game_map["18,1"] + printmap_game_map["19,1"] +
              printmap_game_map["20,1"] + printmap_game_map[
                  "21,1"] + printmap_game_map["22,1"] + printmap_game_map[
                  "23,1"] + printmap_game_map["24,1"] + printmap_game_map[
                  "25,1"] + printmap_game_map["26,1"] +
              printmap_game_map["27,1"] + printmap_game_map["28,1"] +
              printmap_game_map["29,1"] + printmap_game_map["30,1"] +
              printmap_game_map["31,1"] + printmap_game_map[
                  "32,1"] + printmap_game_map["33,1"] + printmap_game_map[
                  "34,1"] + printmap_game_map["35,1"] + printmap_game_map[
                  "36,1"] + printmap_game_map["37,1"] +
              printmap_game_map["38,1"] + printmap_game_map["39,1"] +
              printmap_game_map["40,1"] + printmap_game_map["41,1"] +
              printmap_game_map["42,1"] + printmap_game_map[
                  "43,1"] + printmap_game_map["44,1"] + printmap_game_map[
                  "45,1"] + printmap_game_map["46,1"] + printmap_game_map[
                  "47,1"] + printmap_game_map["48,1"] +
              printmap_game_map["49,1"] + printmap_game_map["50,1"] +
              printmap_game_map["51,1"] + printmap_game_map["52,1"] +
              printmap_game_map["53,1"] +
              printmap_game_map["54,1"] + printmap_game_map["55,1"] +
              printmap_game_map["56,1"] + printmap_game_map[
                  "57,1"] + printmap_game_map["58,1"] + printmap_game_map[
                  "59,1"] + printmap_game_map["60,1"] + printmap_game_map[
                  "61,1"] + printmap_game_map["62,1"] +
              printmap_game_map["63,1"] + printmap_game_map["64,1"])
        print(
            "02" + "|" +
            printmap_game_map["1,2"] + printmap_game_map["2,2"] +
            printmap_game_map["3,2"] + printmap_game_map["4,2"] +
            printmap_game_map["5,2"] + printmap_game_map["6,2"] +
            printmap_game_map["7,2"] + printmap_game_map["8,2"] +
            printmap_game_map["9,2"] + printmap_game_map["10,2"] +
            printmap_game_map["11,2"] + printmap_game_map[
                "12,2"] + printmap_game_map["13,2"] + printmap_game_map[
                "14,2"] + printmap_game_map["15,2"] +
            printmap_game_map["16,2"] + printmap_game_map["17,2"] +
            printmap_game_map["18,2"] + printmap_game_map["19,2"] +
            printmap_game_map["20,2"] +
            printmap_game_map["21,2"] +
            printmap_game_map["22,2"] + printmap_game_map[
                "23,2"] + printmap_game_map["24,2"] + printmap_game_map[
                "25,2"] + printmap_game_map["26,2"] +
            printmap_game_map["27,2"] + printmap_game_map["28,2"] +
            printmap_game_map["29,2"] + printmap_game_map["30,2"] +
            printmap_game_map["31,2"] +
            printmap_game_map["32,2"] +
            printmap_game_map["33,2"] + printmap_game_map[
                "34,2"] + printmap_game_map["35,2"] + printmap_game_map[
                "36,2"] + printmap_game_map["37,2"] +
            printmap_game_map["38,2"] + printmap_game_map["39,2"] +
            printmap_game_map["40,2"] + printmap_game_map["41,2"] +
            printmap_game_map["42,2"] +
            printmap_game_map["43,2"] + printmap_game_map["44,2"] +
            printmap_game_map[
                "45,2"] + printmap_game_map["46,2"] + printmap_game_map[
                "47,2"] + printmap_game_map["48,2"] +
            printmap_game_map["49,2"] + printmap_game_map["50,2"] +
            printmap_game_map["51,2"] + printmap_game_map["52,2"] +
            printmap_game_map["53,2"] +
            printmap_game_map["54,2"] + printmap_game_map["55,2"] +
            printmap_game_map["56,2"] +
            printmap_game_map["57,2"] +
            printmap_game_map["58,2"] + printmap_game_map[
                "59,2"] + printmap_game_map["60,2"] + printmap_game_map[
                "61,2"] + printmap_game_map["62,2"] +
            printmap_game_map["63,2"] + printmap_game_map["64,2"])
        print(
            "03" + "|" +
            printmap_game_map["1,3"] + printmap_game_map["2,3"] +
            printmap_game_map["3,3"] + printmap_game_map["4,3"] +
            printmap_game_map["5,3"] + printmap_game_map["6,3"] +
            printmap_game_map["7,3"] + printmap_game_map["8,3"] +
            printmap_game_map["9,3"] + printmap_game_map["10,3"] +
            printmap_game_map["11,3"] + printmap_game_map[
                "12,3"] + printmap_game_map["13,3"] + printmap_game_map[
                "14,3"] + printmap_game_map["15,3"] +
            printmap_game_map["16,3"] + printmap_game_map["17,3"] +
            printmap_game_map["18,3"] + printmap_game_map["19,3"] +
            printmap_game_map["20,3"] +
            printmap_game_map["21,3"] +
            printmap_game_map["22,3"] + printmap_game_map[
                "23,3"] + printmap_game_map["24,3"] + printmap_game_map[
                "25,3"] + printmap_game_map["26,3"] +
            printmap_game_map["27,3"] + printmap_game_map["28,3"] +
            printmap_game_map["29,3"] + printmap_game_map["30,3"] +
            printmap_game_map["31,3"] +
            printmap_game_map["32,3"] +
            printmap_game_map["33,3"] + printmap_game_map[
                "34,3"] + printmap_game_map["35,3"] + printmap_game_map[
                "36,3"] + printmap_game_map["37,3"] +
            printmap_game_map["38,3"] + printmap_game_map["39,3"] +
            printmap_game_map["40,3"] + printmap_game_map["41,3"] +
            printmap_game_map["42,3"] +
            printmap_game_map["43,3"] +
            printmap_game_map["44,3"] + printmap_game_map[
                "45,3"] + printmap_game_map["46,3"] + printmap_game_map[
                "47,3"] + printmap_game_map["48,3"] +
            printmap_game_map["49,3"] + printmap_game_map["50,3"] +
            printmap_game_map["51,3"] + printmap_game_map["52,3"] +
            printmap_game_map["53,3"] +
            printmap_game_map["54,3"] + printmap_game_map["55,3"] +
            printmap_game_map["56,3"] +
            printmap_game_map["57,3"] +
            printmap_game_map["58,3"] + printmap_game_map[
                "59,3"] + printmap_game_map["60,3"] + printmap_game_map[
                "61,3"] + printmap_game_map["62,3"] +
            printmap_game_map["63,3"] + printmap_game_map["64,3"])
        print(
            "04" + "|" +
            printmap_game_map["1,4"] + printmap_game_map["2,4"] +
            printmap_game_map["3,4"] + printmap_game_map["4,4"] +
            printmap_game_map["5,4"] + printmap_game_map["6,4"] +
            printmap_game_map["7,4"] + printmap_game_map["8,4"] +
            printmap_game_map["9,4"] + printmap_game_map["10,4"] +
            printmap_game_map["11,4"] + printmap_game_map[
                "12,4"] + printmap_game_map["13,4"] + printmap_game_map[
                "14,4"] + printmap_game_map["15,4"] +
            printmap_game_map["16,4"] + printmap_game_map["17,4"] +
            printmap_game_map["18,4"] + printmap_game_map["19,4"] +
            printmap_game_map["20,4"] +
            printmap_game_map["21,4"] +
            printmap_game_map["22,4"] + printmap_game_map[
                "23,4"] + printmap_game_map["24,4"] + printmap_game_map[
                "25,4"] + printmap_game_map["26,4"] +
            printmap_game_map["27,4"] + printmap_game_map["28,4"] +
            printmap_game_map["29,4"] + printmap_game_map["30,4"] +
            printmap_game_map["31,4"] +
            printmap_game_map["32,4"] +
            printmap_game_map["33,4"] + printmap_game_map[
                "34,4"] + printmap_game_map["35,4"] + printmap_game_map[
                "36,4"] + printmap_game_map["37,4"] +
            printmap_game_map["38,4"] + printmap_game_map["39,4"] +
            printmap_game_map["40,4"] + printmap_game_map["41,4"] +
            printmap_game_map["42,4"] +
            printmap_game_map["43,4"] +
            printmap_game_map["44,4"] + printmap_game_map[
                "45,4"] + printmap_game_map["46,4"] + printmap_game_map[
                "47,4"] + printmap_game_map["48,4"] +
            printmap_game_map["49,4"] + printmap_game_map["50,4"] +
            printmap_game_map["51,4"] + printmap_game_map["52,4"] +
            printmap_game_map["53,4"] +
            printmap_game_map["54,4"] + printmap_game_map["55,4"] +
            printmap_game_map["56,4"] +
            printmap_game_map["57,4"] +
            printmap_game_map["58,4"] + printmap_game_map[
                "59,4"] + printmap_game_map["60,4"] + printmap_game_map[
                "61,4"] + printmap_game_map["62,4"] +
            printmap_game_map["63,4"] + printmap_game_map["64,4"])
        print(
            "05" + "|" +
            printmap_game_map["1,5"] + printmap_game_map["2,5"] +
            printmap_game_map["3,5"] + printmap_game_map["4,5"] +
            printmap_game_map["5,5"] + printmap_game_map["6,5"] +
            printmap_game_map["7,5"] + printmap_game_map["8,5"] +
            printmap_game_map["9,5"] + printmap_game_map["10,5"] +
            printmap_game_map["11,5"] + printmap_game_map[
                "12,5"] + printmap_game_map["13,5"] + printmap_game_map[
                "14,5"] + printmap_game_map["15,5"] +
            printmap_game_map["16,5"] + printmap_game_map["17,5"] +
            printmap_game_map["18,5"] + printmap_game_map["19,5"] +
            printmap_game_map["20,5"] +
            printmap_game_map["21,5"] +
            printmap_game_map["22,5"] + printmap_game_map[
                "23,5"] + printmap_game_map["24,5"] + printmap_game_map[
                "25,5"] + printmap_game_map["26,5"] +
            printmap_game_map["27,5"] + printmap_game_map["28,5"] +
            printmap_game_map["29,5"] + printmap_game_map["30,5"] +
            printmap_game_map["31,5"] +
            printmap_game_map["32,5"] +
            printmap_game_map["33,5"] + printmap_game_map[
                "34,5"] + printmap_game_map["35,5"] + printmap_game_map[
                "36,5"] + printmap_game_map["37,5"] +
            printmap_game_map["38,5"] + printmap_game_map["39,5"] +
            printmap_game_map["40,5"] + printmap_game_map["41,5"] +
            printmap_game_map["42,5"] +
            printmap_game_map["43,5"] +
            printmap_game_map["44,5"] + printmap_game_map[
                "45,5"] + printmap_game_map["46,5"] + printmap_game_map[
                "47,5"] + printmap_game_map["48,5"] +
            printmap_game_map["49,5"] + printmap_game_map["50,5"] +
            printmap_game_map["51,5"] + printmap_game_map["52,5"] +
            printmap_game_map["53,5"] +
            printmap_game_map["54,5"] + printmap_game_map["55,5"] +
            printmap_game_map["56,5"] +
            printmap_game_map["57,5"] +
            printmap_game_map["58,5"] + printmap_game_map[
                "59,5"] + printmap_game_map["60,5"] + printmap_game_map[
                "61,5"] + printmap_game_map["62,5"] +
            printmap_game_map["63,5"] + printmap_game_map["64,5"])
        print(
            "06" + "|" +
            printmap_game_map["1,6"] + printmap_game_map["2,6"] +
            printmap_game_map["3,6"] + printmap_game_map["4,6"] +
            printmap_game_map["5,6"] + printmap_game_map["6,6"] +
            printmap_game_map["7,6"] + printmap_game_map["8,6"] +
            printmap_game_map["9,6"] + printmap_game_map["10,6"] +
            printmap_game_map["11,6"] + printmap_game_map[
                "12,6"] + printmap_game_map["13,6"] + printmap_game_map[
                "14,6"] + printmap_game_map["15,6"] +
            printmap_game_map["16,6"] + printmap_game_map["17,6"] +
            printmap_game_map["18,6"] + printmap_game_map["19,6"] +
            printmap_game_map["20,6"] +
            printmap_game_map["21,6"] +
            printmap_game_map["22,6"] + printmap_game_map[
                "23,6"] + printmap_game_map["24,6"] + printmap_game_map[
                "25,6"] + printmap_game_map["26,6"] +
            printmap_game_map["27,6"] + printmap_game_map["28,6"] +
            printmap_game_map["29,6"] + printmap_game_map["30,6"] +
            printmap_game_map["31,6"] +
            printmap_game_map["32,6"] +
            printmap_game_map["33,6"] + printmap_game_map[
                "34,6"] + printmap_game_map["35,6"] + printmap_game_map[
                "36,6"] + printmap_game_map["37,6"] +
            printmap_game_map["38,6"] + printmap_game_map["39,6"] +
            printmap_game_map["40,6"] + printmap_game_map["41,6"] +
            printmap_game_map["42,6"] +
            printmap_game_map["43,6"] +
            printmap_game_map["44,6"] + printmap_game_map[
                "45,6"] + printmap_game_map["46,6"] + printmap_game_map[
                "47,6"] + printmap_game_map["48,6"] +
            printmap_game_map["49,6"] + printmap_game_map["50,6"] +
            printmap_game_map["51,6"] + printmap_game_map["52,6"] +
            printmap_game_map["53,6"] +
            printmap_game_map["54,6"] + printmap_game_map["55,6"] +
            printmap_game_map["56,6"] +
            printmap_game_map["57,6"] +
            printmap_game_map["58,6"] + printmap_game_map[
                "59,6"] + printmap_game_map["60,6"] + printmap_game_map[
                "61,6"] + printmap_game_map["62,6"] +
            printmap_game_map["63,6"] + printmap_game_map["64,6"])
        print(
            "07" + "|" +
            printmap_game_map["1,7"] + printmap_game_map["2,7"] +
            printmap_game_map["3,7"] + printmap_game_map["4,7"] +
            printmap_game_map["5,7"] + printmap_game_map["6,7"] +
            printmap_game_map["7,7"] + printmap_game_map["8,7"] +
            printmap_game_map["9,7"] + printmap_game_map["10,7"] +
            printmap_game_map["11,7"] + printmap_game_map[
                "12,7"] + printmap_game_map["13,7"] + printmap_game_map[
                "14,7"] + printmap_game_map["15,7"] +
            printmap_game_map["16,7"] + printmap_game_map["17,7"] +
            printmap_game_map["18,7"] + printmap_game_map["19,7"] +
            printmap_game_map["20,7"] +
            printmap_game_map["21,7"] +
            printmap_game_map["22,7"] + printmap_game_map[
                "23,7"] + printmap_game_map["24,7"] + printmap_game_map[
                "25,7"] + printmap_game_map["26,7"] +
            printmap_game_map["27,7"] + printmap_game_map["28,7"] +
            printmap_game_map["29,7"] + printmap_game_map["30,7"] +
            printmap_game_map["31,7"] +
            printmap_game_map["32,7"] +
            printmap_game_map["33,7"] + printmap_game_map[
                "34,7"] + printmap_game_map["35,7"] + printmap_game_map[
                "36,7"] + printmap_game_map["37,7"] +
            printmap_game_map["38,7"] + printmap_game_map["39,7"] +
            printmap_game_map["40,7"] + printmap_game_map["41,7"] +
            printmap_game_map["42,7"] +
            printmap_game_map["43,7"] +
            printmap_game_map["44,7"] + printmap_game_map[
                "45,7"] + printmap_game_map["46,7"] + printmap_game_map[
                "47,7"] + printmap_game_map["48,7"] +
            printmap_game_map["49,7"] + printmap_game_map["50,7"] +
            printmap_game_map["51,7"] + printmap_game_map["52,7"] +
            printmap_game_map["53,7"] +
            printmap_game_map["54,7"] + printmap_game_map["55,7"] +
            printmap_game_map["56,7"] +
            printmap_game_map["57,7"] +
            printmap_game_map["58,7"] + printmap_game_map[
                "59,7"] + printmap_game_map["60,7"] + printmap_game_map[
                "61,7"] + printmap_game_map["62,7"] +
            printmap_game_map["63,7"] + printmap_game_map["64,7"])
        print(
            "09" + "|" +
            printmap_game_map["1,8"] + printmap_game_map["2,8"] +
            printmap_game_map["3,8"] + printmap_game_map["4,8"] +
            printmap_game_map["5,8"] + printmap_game_map["6,8"] +
            printmap_game_map["7,8"] + printmap_game_map["8,8"] +
            printmap_game_map["9,8"] + printmap_game_map["10,8"] +
            printmap_game_map["11,8"] + printmap_game_map[
                "12,8"] + printmap_game_map["13,8"] + printmap_game_map[
                "14,8"] + printmap_game_map["15,8"] +
            printmap_game_map["16,8"] + printmap_game_map["17,8"] +
            printmap_game_map["18,8"] + printmap_game_map["19,8"] +
            printmap_game_map["20,8"] +
            printmap_game_map["21,8"] +
            printmap_game_map["22,8"] + printmap_game_map[
                "23,8"] + printmap_game_map["24,8"] + printmap_game_map[
                "25,8"] + printmap_game_map["26,8"] +
            printmap_game_map["27,8"] + printmap_game_map["28,8"] +
            printmap_game_map["29,8"] + printmap_game_map["30,8"] +
            printmap_game_map["31,8"] +
            printmap_game_map["32,8"] +
            printmap_game_map["33,8"] + printmap_game_map[
                "34,8"] + printmap_game_map["35,8"] + printmap_game_map[
                "36,8"] + printmap_game_map["37,8"] +
            printmap_game_map["38,8"] + printmap_game_map["39,8"] +
            printmap_game_map["40,8"] + printmap_game_map["41,8"] +
            printmap_game_map["42,8"] +
            printmap_game_map["43,8"] +
            printmap_game_map["44,8"] + printmap_game_map[
                "45,8"] + printmap_game_map["46,8"] + printmap_game_map[
                "47,8"] + printmap_game_map["48,8"] +
            printmap_game_map["49,8"] + printmap_game_map["50,8"] +
            printmap_game_map["51,8"] + printmap_game_map["52,8"] +
            printmap_game_map["53,8"] +
            printmap_game_map["54,8"] + printmap_game_map["55,8"] +
            printmap_game_map["56,8"] +
            printmap_game_map["57,8"] +
            printmap_game_map["58,8"] + printmap_game_map[
                "59,8"] + printmap_game_map["60,8"] + printmap_game_map[
                "61,8"] + printmap_game_map["62,8"] +
            printmap_game_map["63,8"] + printmap_game_map["64,8"])
        print(
            "10" + "|" +
            printmap_game_map["1,9"] + printmap_game_map["2,9"] +
            printmap_game_map["3,9"] + printmap_game_map["4,9"] +
            printmap_game_map["5,9"] + printmap_game_map["6,9"] +
            printmap_game_map["7,9"] + printmap_game_map["8,9"] +
            printmap_game_map["9,9"] + printmap_game_map["10,9"] +
            printmap_game_map["11,9"] + printmap_game_map[
                "12,9"] + printmap_game_map["13,9"] + printmap_game_map[
                "14,9"] + printmap_game_map["15,9"] +
            printmap_game_map["16,9"] + printmap_game_map["17,9"] +
            printmap_game_map["18,9"] + printmap_game_map["19,9"] +
            printmap_game_map["20,9"] +
            printmap_game_map["21,9"] +
            printmap_game_map["22,9"] + printmap_game_map[
                "23,9"] + printmap_game_map["24,9"] + printmap_game_map[
                "25,9"] + printmap_game_map["26,9"] +
            printmap_game_map["27,9"] + printmap_game_map["28,9"] +
            printmap_game_map["29,9"] + printmap_game_map["30,9"] +
            printmap_game_map["31,9"] +
            printmap_game_map["32,9"] +
            printmap_game_map["33,9"] + printmap_game_map[
                "34,9"] + printmap_game_map["35,9"] + printmap_game_map[
                "36,9"] + printmap_game_map["37,9"] +
            printmap_game_map["38,9"] + printmap_game_map["39,9"] +
            printmap_game_map["40,9"] + printmap_game_map["41,9"] +
            printmap_game_map["42,9"] +
            printmap_game_map["43,9"] +
            printmap_game_map["44,9"] + printmap_game_map[
                "45,9"] + printmap_game_map["46,9"] + printmap_game_map[
                "47,9"] + printmap_game_map["48,9"] +
            printmap_game_map["49,9"] + printmap_game_map["50,9"] +
            printmap_game_map["51,9"] + printmap_game_map["52,9"] +
            printmap_game_map["53,9"] +
            printmap_game_map["54,9"] + printmap_game_map["55,9"] +
            printmap_game_map["56,9"] +
            printmap_game_map["57,9"] +
            printmap_game_map["58,9"] + printmap_game_map[
                "59,9"] + printmap_game_map["60,9"] + printmap_game_map[
                "61,9"] + printmap_game_map["62,9"] +
            printmap_game_map["63,9"] + printmap_game_map["64,9"])
        print(
            "11" + "|" +
            printmap_game_map["1,10"] + printmap_game_map["2,10"] +
            printmap_game_map["3,10"] +
            printmap_game_map["4,10"] +
            printmap_game_map["5,10"] + printmap_game_map[
                "6,10"] + printmap_game_map["7,10"] + printmap_game_map[
                "8,10"] + printmap_game_map["9,10"] +
            printmap_game_map["10,10"] + printmap_game_map["11,10"] +
            printmap_game_map["12,10"] + printmap_game_map["13,10"] +
            printmap_game_map["14,10"] + printmap_game_map[
                "15,10"] + printmap_game_map["16,10"] +
            printmap_game_map["17,10"] + printmap_game_map["18,10"] +
            printmap_game_map["19,10"] + printmap_game_map[
                "20,10"] + printmap_game_map["21,10"] +
            printmap_game_map["22,10"] + printmap_game_map["23,10"] +
            printmap_game_map["24,10"] + printmap_game_map[
                "25,10"] + printmap_game_map["26,10"] +
            printmap_game_map["27,10"] + printmap_game_map["28,10"] +
            printmap_game_map["29,10"] + printmap_game_map[
                "30,10"] + printmap_game_map["31,10"] +
            printmap_game_map["32,10"] + printmap_game_map["33,10"] +
            printmap_game_map["34,10"] + printmap_game_map[
                "35,10"] + printmap_game_map["36,10"] +
            printmap_game_map["37,10"] + printmap_game_map["38,10"] +
            printmap_game_map["39,10"] + printmap_game_map[
                "40,10"] + printmap_game_map["41,10"] +
            printmap_game_map["42,10"] + printmap_game_map["43,10"] +
            printmap_game_map["44,10"] + printmap_game_map[
                "45,10"] + printmap_game_map["46,10"] +
            printmap_game_map["47,10"] + printmap_game_map["48,10"] +
            printmap_game_map["49,10"] + printmap_game_map[
                "50,10"] + printmap_game_map["51,10"] +
            printmap_game_map["52,10"] + printmap_game_map["53,10"] +
            printmap_game_map["54,10"] + printmap_game_map["55,10"] +
            printmap_game_map["56,10"] + printmap_game_map[
                "57,10"] + printmap_game_map["58,10"] +
            printmap_game_map["59,10"] + printmap_game_map["60,10"] +
            printmap_game_map["61,10"] + printmap_game_map[
                "62,10"] + printmap_game_map["63,10"] +
            printmap_game_map["64,10"])
        print(
            "12" + "|" +
            printmap_game_map["1,11"] + printmap_game_map["2,11"] +
            printmap_game_map["3,11"] +
            printmap_game_map["4,11"] +
            printmap_game_map["5,11"] + printmap_game_map[
                "6,11"] + printmap_game_map["7,11"] + printmap_game_map[
                "8,11"] + printmap_game_map["9,11"] +
            printmap_game_map["10,11"] + printmap_game_map["11,11"] +
            printmap_game_map["12,11"] + printmap_game_map["13,11"] +
            printmap_game_map["14,11"] + printmap_game_map[
                "15,11"] + printmap_game_map["16,11"] +
            printmap_game_map["17,11"] + printmap_game_map["18,11"] +
            printmap_game_map["19,11"] + printmap_game_map[
                "20,11"] + printmap_game_map["21,11"] +
            printmap_game_map["22,11"] + printmap_game_map["23,11"] +
            printmap_game_map["24,11"] + printmap_game_map[
                "25,11"] + printmap_game_map["26,11"] +
            printmap_game_map["27,11"] + printmap_game_map["28,11"] +
            printmap_game_map["29,11"] + printmap_game_map[
                "30,11"] + printmap_game_map["31,11"] +
            printmap_game_map["32,11"] + printmap_game_map["33,11"] +
            printmap_game_map["34,11"] + printmap_game_map[
                "35,11"] + printmap_game_map["36,11"] +
            printmap_game_map["37,11"] + printmap_game_map["38,11"] +
            printmap_game_map["39,11"] + printmap_game_map[
                "40,11"] + printmap_game_map["41,11"] +
            printmap_game_map["42,11"] + printmap_game_map["43,11"] +
            printmap_game_map["44,11"] + printmap_game_map[
                "45,11"] + printmap_game_map["46,11"] +
            printmap_game_map["47,11"] + printmap_game_map["48,11"] +
            printmap_game_map["49,11"] + printmap_game_map[
                "50,11"] + printmap_game_map["51,11"] +
            printmap_game_map["52,11"] + printmap_game_map["53,11"] +
            printmap_game_map["54,11"] + printmap_game_map["55,11"] +
            printmap_game_map["56,11"] + printmap_game_map[
                "57,11"] + printmap_game_map["58,11"] +
            printmap_game_map["59,11"] + printmap_game_map["60,11"] +
            printmap_game_map["61,11"] + printmap_game_map[
                "62,11"] + printmap_game_map["63,11"] +
            printmap_game_map["64,11"])
        print(
            "12" + "|" +
            printmap_game_map["1,12"] + printmap_game_map["2,12"] +
            printmap_game_map["3,12"] +
            printmap_game_map["4,12"] +
            printmap_game_map["5,12"] + printmap_game_map[
                "6,12"] + printmap_game_map["7,12"] + printmap_game_map[
                "8,12"] + printmap_game_map["9,12"] +
            printmap_game_map["10,12"] + printmap_game_map["11,12"] +
            printmap_game_map["12,12"] + printmap_game_map["13,12"] +
            printmap_game_map["14,12"] + printmap_game_map[
                "15,12"] + printmap_game_map["16,12"] +
            printmap_game_map["17,12"] + printmap_game_map["18,12"] +
            printmap_game_map["19,12"] + printmap_game_map[
                "20,12"] + printmap_game_map["21,12"] +
            printmap_game_map["22,12"] + printmap_game_map["23,12"] +
            printmap_game_map["24,12"] + printmap_game_map[
                "25,12"] + printmap_game_map["26,12"] +
            printmap_game_map["27,12"] + printmap_game_map["28,12"] +
            printmap_game_map["29,12"] + printmap_game_map[
                "30,12"] + printmap_game_map["31,12"] +
            printmap_game_map["32,12"] + printmap_game_map["33,12"] +
            printmap_game_map["34,12"] + printmap_game_map[
                "35,12"] + printmap_game_map["36,12"] +
            printmap_game_map["37,12"] + printmap_game_map["38,12"] +
            printmap_game_map["39,12"] + printmap_game_map[
                "40,12"] + printmap_game_map["41,12"] +
            printmap_game_map["42,12"] + printmap_game_map["43,12"] +
            printmap_game_map["44,12"] + printmap_game_map[
                "45,12"] + printmap_game_map["46,12"] +
            printmap_game_map["47,12"] + printmap_game_map["48,12"] +
            printmap_game_map["49,12"] + printmap_game_map[
                "50,12"] + printmap_game_map["51,12"] +
            printmap_game_map["52,12"] + printmap_game_map["53,12"] +
            printmap_game_map["54,12"] + printmap_game_map["55,12"] +
            printmap_game_map["56,12"] + printmap_game_map[
                "57,12"] + printmap_game_map["58,12"] +
            printmap_game_map["59,12"] + printmap_game_map["60,12"] +
            printmap_game_map["61,12"] + printmap_game_map[
                "62,12"] + printmap_game_map["63,12"] +
            printmap_game_map["64,12"])
        print(
            "13" + "|" +
            printmap_game_map["1,13"] + printmap_game_map["2,13"] +
            printmap_game_map["3,13"] +
            printmap_game_map["4,13"] +
            printmap_game_map["5,13"] + printmap_game_map[
                "6,13"] + printmap_game_map["7,13"] + printmap_game_map[
                "8,13"] + printmap_game_map["9,13"] +
            printmap_game_map["10,13"] + printmap_game_map["11,13"] +
            printmap_game_map["12,13"] + printmap_game_map["13,13"] +
            printmap_game_map["14,13"] + printmap_game_map[
                "15,13"] + printmap_game_map["16,13"] +
            printmap_game_map["17,13"] + printmap_game_map["18,13"] +
            printmap_game_map["19,13"] + printmap_game_map[
                "20,13"] + printmap_game_map["21,13"] +
            printmap_game_map["22,13"] + printmap_game_map["23,13"] +
            printmap_game_map["24,13"] + printmap_game_map[
                "25,13"] + printmap_game_map["26,13"] +
            printmap_game_map["27,13"] + printmap_game_map["28,13"] +
            printmap_game_map["29,13"] + printmap_game_map[
                "30,13"] + printmap_game_map["31,13"] +
            printmap_game_map["32,13"] + printmap_game_map["33,13"] +
            printmap_game_map["34,13"] + printmap_game_map[
                "35,13"] + printmap_game_map["36,13"] +
            printmap_game_map["37,13"] + printmap_game_map["38,13"] +
            printmap_game_map["39,13"] + printmap_game_map[
                "40,13"] + printmap_game_map["41,13"] +
            printmap_game_map["42,13"] + printmap_game_map["43,13"] +
            printmap_game_map["44,13"] + printmap_game_map[
                "45,13"] + printmap_game_map["46,13"] +
            printmap_game_map["47,13"] + printmap_game_map["48,13"] +
            printmap_game_map["49,13"] + printmap_game_map[
                "50,13"] + printmap_game_map["51,13"] +
            printmap_game_map["52,13"] + printmap_game_map["53,13"] +
            printmap_game_map["54,13"] + printmap_game_map["55,13"] +
            printmap_game_map["56,13"] + printmap_game_map[
                "57,13"] + printmap_game_map["58,13"] +
            printmap_game_map["59,13"] + printmap_game_map["60,13"] +
            printmap_game_map["61,13"] + printmap_game_map[
                "62,13"] + printmap_game_map["63,13"] +
            printmap_game_map["64,13"])
        print(
            "14" + "|" +
            printmap_game_map["1,14"] + printmap_game_map["2,14"] +
            printmap_game_map["3,14"] +
            printmap_game_map["4,14"] +
            printmap_game_map["5,14"] + printmap_game_map[
                "6,14"] + printmap_game_map["7,14"] + printmap_game_map[
                "8,14"] + printmap_game_map["9,14"] +
            printmap_game_map["10,14"] + printmap_game_map["11,14"] +
            printmap_game_map["12,14"] + printmap_game_map["13,14"] +
            printmap_game_map["14,14"] + printmap_game_map[
                "15,14"] + printmap_game_map["16,14"] +
            printmap_game_map["17,14"] + printmap_game_map["18,14"] +
            printmap_game_map["19,14"] + printmap_game_map[
                "20,14"] + printmap_game_map["21,14"] +
            printmap_game_map["22,14"] + printmap_game_map["23,14"] +
            printmap_game_map["24,14"] + printmap_game_map[
                "25,14"] + printmap_game_map["26,14"] +
            printmap_game_map["27,14"] + printmap_game_map["28,14"] +
            printmap_game_map["29,14"] + printmap_game_map[
                "30,14"] + printmap_game_map["31,14"] +
            printmap_game_map["32,14"] + printmap_game_map["33,14"] +
            printmap_game_map["34,14"] + printmap_game_map[
                "35,14"] + printmap_game_map["36,14"] +
            printmap_game_map["37,14"] + printmap_game_map["38,14"] +
            printmap_game_map["39,14"] + printmap_game_map[
                "40,14"] + printmap_game_map["41,14"] +
            printmap_game_map["42,14"] + printmap_game_map["43,14"] +
            printmap_game_map["44,14"] + printmap_game_map[
                "45,14"] + printmap_game_map["46,14"] +
            printmap_game_map["47,14"] + printmap_game_map["48,14"] +
            printmap_game_map["49,14"] + printmap_game_map[
                "50,14"] + printmap_game_map["51,14"] +
            printmap_game_map["52,14"] + printmap_game_map["53,14"] +
            printmap_game_map["54,14"] + printmap_game_map["55,14"] +
            printmap_game_map["56,14"] + printmap_game_map[
                "57,14"] + printmap_game_map["58,14"] +
            printmap_game_map["59,14"] + printmap_game_map["60,14"] +
            printmap_game_map["61,14"] + printmap_game_map[
                "62,14"] + printmap_game_map["63,14"] +
            printmap_game_map["64,14"])
        print(
            "15" + "|" +
            printmap_game_map["1,15"] + printmap_game_map["2,15"] +
            printmap_game_map["3,15"] +
            printmap_game_map["4,15"] +
            printmap_game_map["5,15"] + printmap_game_map[
                "6,15"] + printmap_game_map["7,15"] + printmap_game_map[
                "8,15"] + printmap_game_map["9,15"] +
            printmap_game_map["10,15"] + printmap_game_map["11,15"] +
            printmap_game_map["12,15"] + printmap_game_map["13,15"] +
            printmap_game_map["14,15"] + printmap_game_map[
                "15,15"] + printmap_game_map["16,15"] +
            printmap_game_map["17,15"] + printmap_game_map["18,15"] +
            printmap_game_map["19,15"] + printmap_game_map[
                "20,15"] + printmap_game_map["21,15"] +
            printmap_game_map["22,15"] + printmap_game_map["23,15"] +
            printmap_game_map["24,15"] + printmap_game_map[
                "25,15"] + printmap_game_map["26,15"] +
            printmap_game_map["27,15"] + printmap_game_map["28,15"] +
            printmap_game_map["29,15"] + printmap_game_map[
                "30,15"] + printmap_game_map["31,15"] +
            printmap_game_map["32,15"] + printmap_game_map["33,15"] +
            printmap_game_map["34,15"] + printmap_game_map[
                "35,15"] + printmap_game_map["36,15"] +
            printmap_game_map["37,15"] + printmap_game_map["38,15"] +
            printmap_game_map["39,15"] + printmap_game_map[
                "40,15"] + printmap_game_map["41,15"] +
            printmap_game_map["42,15"] + printmap_game_map["43,15"] +
            printmap_game_map["44,15"] + printmap_game_map[
                "45,15"] + printmap_game_map["46,15"] +
            printmap_game_map["47,15"] + printmap_game_map["48,15"] +
            printmap_game_map["49,15"] + printmap_game_map[
                "50,15"] + printmap_game_map["51,15"] +
            printmap_game_map["52,15"] + printmap_game_map["53,15"] +
            printmap_game_map["54,15"] + printmap_game_map["55,15"] +
            printmap_game_map["56,15"] + printmap_game_map[
                "57,15"] + printmap_game_map["58,15"] +
            printmap_game_map["59,15"] + printmap_game_map["60,15"] +
            printmap_game_map["61,15"] + printmap_game_map[
                "62,15"] + printmap_game_map["63,15"] +
            printmap_game_map["64,15"])
        print(
            "16" + "|" +
            printmap_game_map["1,16"] + printmap_game_map["2,16"] +
            printmap_game_map["3,16"] +
            printmap_game_map["4,16"] +
            printmap_game_map["5,16"] + printmap_game_map[
                "6,16"] + printmap_game_map["7,16"] + printmap_game_map[
                "8,16"] + printmap_game_map["9,16"] +
            printmap_game_map["10,16"] + printmap_game_map["11,16"] +
            printmap_game_map["12,16"] + printmap_game_map["13,16"] +
            printmap_game_map["14,16"] + printmap_game_map[
                "15,16"] + printmap_game_map["16,16"] +
            printmap_game_map["17,16"] + printmap_game_map["18,16"] +
            printmap_game_map["19,16"] + printmap_game_map[
                "20,16"] + printmap_game_map["21,16"] +
            printmap_game_map["22,16"] + printmap_game_map["23,16"] +
            printmap_game_map["24,16"] + printmap_game_map[
                "25,16"] + printmap_game_map["26,16"] +
            printmap_game_map["27,16"] + printmap_game_map["28,16"] +
            printmap_game_map["29,16"] + printmap_game_map[
                "30,16"] + printmap_game_map["31,16"] +
            printmap_game_map["32,16"] + printmap_game_map["33,16"] +
            printmap_game_map["34,16"] + printmap_game_map[
                "35,16"] + printmap_game_map["36,16"] +
            printmap_game_map["37,16"] + printmap_game_map["38,16"] +
            printmap_game_map["39,16"] + printmap_game_map[
                "40,16"] + printmap_game_map["41,16"] +
            printmap_game_map["42,16"] + printmap_game_map["43,16"] +
            printmap_game_map["44,16"] + printmap_game_map[
                "45,16"] + printmap_game_map["46,16"] +
            printmap_game_map["47,16"] + printmap_game_map["48,16"] +
            printmap_game_map["49,16"] + printmap_game_map[
                "50,16"] + printmap_game_map["51,16"] +
            printmap_game_map["52,16"] + printmap_game_map["53,16"] +
            printmap_game_map["54,16"] + printmap_game_map["55,16"] +
            printmap_game_map["56,16"] + printmap_game_map[
                "57,16"] + printmap_game_map["58,16"] +
            printmap_game_map["59,16"] + printmap_game_map["60,16"] +
            printmap_game_map["61,16"] + printmap_game_map[
                "62,16"] + printmap_game_map["63,16"] +
            printmap_game_map["64,16"])
        print(
            "17" + "|" +
            printmap_game_map["1,17"] + printmap_game_map["2,17"] +
            printmap_game_map["3,17"] +
            printmap_game_map["4,17"] +
            printmap_game_map["5,17"] + printmap_game_map[
                "6,17"] + printmap_game_map["7,17"] + printmap_game_map[
                "8,17"] + printmap_game_map["9,17"] +
            printmap_game_map["10,17"] + printmap_game_map["11,17"] +
            printmap_game_map["12,17"] + printmap_game_map["13,17"] +
            printmap_game_map["14,17"] + printmap_game_map[
                "15,17"] + printmap_game_map["16,17"] +
            printmap_game_map["17,17"] + printmap_game_map["18,17"] +
            printmap_game_map["19,17"] + printmap_game_map[
                "20,17"] + printmap_game_map["21,17"] +
            printmap_game_map["22,17"] + printmap_game_map["23,17"] +
            printmap_game_map["24,17"] + printmap_game_map[
                "25,17"] + printmap_game_map["26,17"] +
            printmap_game_map["27,17"] + printmap_game_map["28,17"] +
            printmap_game_map["29,17"] + printmap_game_map[
                "30,17"] + printmap_game_map["31,17"] +
            printmap_game_map["32,17"] + printmap_game_map["33,17"] +
            printmap_game_map["34,17"] + printmap_game_map[
                "35,17"] + printmap_game_map["36,17"] +
            printmap_game_map["37,17"] + printmap_game_map["38,17"] +
            printmap_game_map["39,17"] + printmap_game_map[
                "40,17"] + printmap_game_map["41,17"] +
            printmap_game_map["42,17"] + printmap_game_map["43,17"] +
            printmap_game_map["44,17"] + printmap_game_map[
                "45,17"] + printmap_game_map["46,17"] +
            printmap_game_map["47,17"] + printmap_game_map["48,17"] +
            printmap_game_map["49,17"] + printmap_game_map[
                "50,17"] + printmap_game_map["51,17"] +
            printmap_game_map["52,17"] + printmap_game_map["53,17"] +
            printmap_game_map["54,17"] + printmap_game_map["55,17"] +
            printmap_game_map["56,17"] + printmap_game_map[
                "57,17"] + printmap_game_map["58,17"] +
            printmap_game_map["59,17"] + printmap_game_map["60,17"] +
            printmap_game_map["61,17"] + printmap_game_map[
                "62,17"] + printmap_game_map["63,17"] +
            printmap_game_map["64,17"])
        print(
            "18" + "|" +
            printmap_game_map["1,18"] + printmap_game_map["2,18"] +
            printmap_game_map["3,18"] +
            printmap_game_map["4,18"] +
            printmap_game_map["5,18"] + printmap_game_map[
                "6,18"] + printmap_game_map["7,18"] + printmap_game_map[
                "8,18"] + printmap_game_map["9,18"] +
            printmap_game_map["10,18"] + printmap_game_map["11,18"] +
            printmap_game_map["12,18"] + printmap_game_map["13,18"] +
            printmap_game_map["14,18"] + printmap_game_map[
                "15,18"] + printmap_game_map["16,18"] +
            printmap_game_map["17,18"] + printmap_game_map["18,18"] +
            printmap_game_map["19,18"] + printmap_game_map[
                "20,18"] + printmap_game_map["21,18"] +
            printmap_game_map["22,18"] + printmap_game_map["23,18"] +
            printmap_game_map["24,18"] + printmap_game_map[
                "25,18"] + printmap_game_map["26,18"] +
            printmap_game_map["27,18"] + printmap_game_map["28,18"] +
            printmap_game_map["29,18"] + printmap_game_map[
                "30,18"] + printmap_game_map["31,18"] +
            printmap_game_map["32,18"] + printmap_game_map["33,18"] +
            printmap_game_map["34,18"] + printmap_game_map[
                "35,18"] + printmap_game_map["36,18"] +
            printmap_game_map["37,18"] + printmap_game_map["38,18"] +
            printmap_game_map["39,18"] + printmap_game_map[
                "40,18"] + printmap_game_map["41,18"] +
            printmap_game_map["42,18"] + printmap_game_map["43,18"] +
            printmap_game_map["44,18"] + printmap_game_map[
                "45,18"] + printmap_game_map["46,18"] +
            printmap_game_map["47,18"] + printmap_game_map["48,18"] +
            printmap_game_map["49,18"] + printmap_game_map[
                "50,18"] + printmap_game_map["51,18"] +
            printmap_game_map["52,18"] + printmap_game_map["53,18"] +
            printmap_game_map["54,18"] + printmap_game_map["55,18"] +
            printmap_game_map["56,18"] + printmap_game_map[
                "57,18"] + printmap_game_map["58,18"] +
            printmap_game_map["59,18"] + printmap_game_map["60,18"] +
            printmap_game_map["61,18"] + printmap_game_map[
                "62,18"] + printmap_game_map["63,18"] +
            printmap_game_map["64,18"])
        print(
            "19" + "|" +
            printmap_game_map["1,19"] + printmap_game_map["2,19"] +
            printmap_game_map["3,19"] +
            printmap_game_map["4,19"] +
            printmap_game_map["5,19"] + printmap_game_map[
                "6,19"] + printmap_game_map["7,19"] + printmap_game_map[
                "8,19"] + printmap_game_map["9,19"] +
            printmap_game_map["10,19"] + printmap_game_map["11,19"] +
            printmap_game_map["12,19"] + printmap_game_map["13,19"] +
            printmap_game_map["14,19"] + printmap_game_map[
                "15,19"] + printmap_game_map["16,19"] +
            printmap_game_map["17,19"] + printmap_game_map["18,19"] +
            printmap_game_map["19,19"] + printmap_game_map[
                "20,19"] + printmap_game_map["21,19"] +
            printmap_game_map["22,19"] + printmap_game_map["23,19"] +
            printmap_game_map["24,19"] + printmap_game_map[
                "25,19"] + printmap_game_map["26,19"] +
            printmap_game_map["27,19"] + printmap_game_map["28,19"] +
            printmap_game_map["29,19"] + printmap_game_map[
                "30,19"] + printmap_game_map["31,19"] +
            printmap_game_map["32,19"] + printmap_game_map["33,19"] +
            printmap_game_map["34,19"] + printmap_game_map[
                "35,19"] + printmap_game_map["36,19"] +
            printmap_game_map["37,19"] + printmap_game_map["38,19"] +
            printmap_game_map["39,19"] + printmap_game_map[
                "40,19"] + printmap_game_map["41,19"] +
            printmap_game_map["42,19"] + printmap_game_map["43,19"] +
            printmap_game_map["44,19"] + printmap_game_map[
                "45,19"] + printmap_game_map["46,19"] +
            printmap_game_map["47,19"] + printmap_game_map["48,19"] +
            printmap_game_map["49,19"] + printmap_game_map[
                "50,19"] + printmap_game_map["51,19"] +
            printmap_game_map["52,19"] + printmap_game_map["53,19"] +
            printmap_game_map["54,19"] + printmap_game_map["55,19"] +
            printmap_game_map["56,19"] + printmap_game_map[
                "57,19"] + printmap_game_map["58,19"] +
            printmap_game_map["59,19"] + printmap_game_map["60,19"] +
            printmap_game_map["61,19"] + printmap_game_map[
                "62,19"] + printmap_game_map["63,19"] +
            printmap_game_map["64,19"])
        print(
            "20" + "|" +
            printmap_game_map["1,20"] + printmap_game_map["2,20"] +
            printmap_game_map["3,20"] +
            printmap_game_map["4,20"] +
            printmap_game_map["5,20"] + printmap_game_map[
                "6,20"] + printmap_game_map["7,20"] + printmap_game_map[
                "8,20"] + printmap_game_map["9,20"] +
            printmap_game_map["10,20"] + printmap_game_map["11,20"] +
            printmap_game_map["12,20"] + printmap_game_map["13,20"] +
            printmap_game_map["14,20"] + printmap_game_map[
                "15,20"] + printmap_game_map["16,20"] +
            printmap_game_map["17,20"] + printmap_game_map["18,20"] +
            printmap_game_map["19,20"] + printmap_game_map[
                "20,20"] + printmap_game_map["21,20"] +
            printmap_game_map["22,20"] + printmap_game_map["23,20"] +
            printmap_game_map["24,20"] + printmap_game_map[
                "25,20"] + printmap_game_map["26,20"] +
            printmap_game_map["27,20"] + printmap_game_map["28,20"] +
            printmap_game_map["29,20"] + printmap_game_map[
                "30,20"] + printmap_game_map["31,20"] +
            printmap_game_map["32,20"] + printmap_game_map["33,20"] +
            printmap_game_map["34,20"] + printmap_game_map[
                "35,20"] + printmap_game_map["36,20"] +
            printmap_game_map["37,20"] + printmap_game_map["38,20"] +
            printmap_game_map["39,20"] + printmap_game_map[
                "40,20"] + printmap_game_map["41,20"] +
            printmap_game_map["42,20"] + printmap_game_map["43,20"] +
            printmap_game_map["44,20"] + printmap_game_map[
                "45,20"] + printmap_game_map["46,20"] +
            printmap_game_map["47,20"] + printmap_game_map["48,20"] +
            printmap_game_map["49,20"] + printmap_game_map[
                "50,20"] + printmap_game_map["51,20"] +
            printmap_game_map["52,20"] + printmap_game_map["53,20"] +
            printmap_game_map["54,20"] + printmap_game_map["55,20"] +
            printmap_game_map["56,20"] + printmap_game_map[
                "57,20"] + printmap_game_map["58,20"] +
            printmap_game_map["59,20"] + printmap_game_map["60,20"] +
            printmap_game_map["61,20"] + printmap_game_map[
                "62,20"] + printmap_game_map["63,20"] +
            printmap_game_map["64,20"])
        print(
            "21" + "|" +
            printmap_game_map["1,21"] + printmap_game_map["2,21"] +
            printmap_game_map["3,21"] +
            printmap_game_map["4,21"] +
            printmap_game_map["5,21"] + printmap_game_map[
                "6,21"] + printmap_game_map["7,21"] + printmap_game_map[
                "8,21"] + printmap_game_map["9,21"] +
            printmap_game_map["10,21"] + printmap_game_map["11,21"] +
            printmap_game_map["12,21"] + printmap_game_map["13,21"] +
            printmap_game_map["14,21"] + printmap_game_map[
                "15,21"] + printmap_game_map["16,21"] +
            printmap_game_map["17,21"] + printmap_game_map["18,21"] +
            printmap_game_map["19,21"] + printmap_game_map[
                "20,21"] + printmap_game_map["21,21"] +
            printmap_game_map["22,21"] + printmap_game_map["23,21"] +
            printmap_game_map["24,21"] + printmap_game_map[
                "25,21"] + printmap_game_map["26,21"] +
            printmap_game_map["27,21"] + printmap_game_map["28,21"] +
            printmap_game_map["29,21"] + printmap_game_map[
                "30,21"] + printmap_game_map["31,21"] +
            printmap_game_map["32,21"] + printmap_game_map["33,21"] +
            printmap_game_map["34,21"] + printmap_game_map[
                "35,21"] + printmap_game_map["36,21"] +
            printmap_game_map["37,21"] + printmap_game_map["38,21"] +
            printmap_game_map["39,21"] + printmap_game_map[
                "40,21"] + printmap_game_map["41,21"] +
            printmap_game_map["42,21"] + printmap_game_map["43,21"] +
            printmap_game_map["44,21"] + printmap_game_map[
                "45,21"] + printmap_game_map["46,21"] +
            printmap_game_map["47,21"] + printmap_game_map["48,21"] +
            printmap_game_map["49,21"] + printmap_game_map[
                "50,21"] + printmap_game_map["51,21"] +
            printmap_game_map["52,21"] + printmap_game_map["53,21"] +
            printmap_game_map["54,21"] + printmap_game_map["55,21"] +
            printmap_game_map["56,21"] + printmap_game_map[
                "57,21"] + printmap_game_map["58,21"] +
            printmap_game_map["59,21"] + printmap_game_map["60,21"] +
            printmap_game_map["61,21"] + printmap_game_map[
                "62,21"] + printmap_game_map["63,21"] +
            printmap_game_map["64,21"])
        print(
            "22" + "|" +
            printmap_game_map["1,22"] + printmap_game_map["2,22"] +
            printmap_game_map["3,22"] +
            printmap_game_map["4,22"] +
            printmap_game_map["5,22"] + printmap_game_map[
                "6,22"] + printmap_game_map["7,22"] + printmap_game_map[
                "8,22"] + printmap_game_map["9,22"] +
            printmap_game_map["10,22"] + printmap_game_map["11,22"] +
            printmap_game_map["12,22"] + printmap_game_map["13,22"] +
            printmap_game_map["14,22"] + printmap_game_map[
                "15,22"] + printmap_game_map["16,22"] +
            printmap_game_map["17,22"] + printmap_game_map["18,22"] +
            printmap_game_map["19,22"] + printmap_game_map[
                "20,22"] + printmap_game_map["21,22"] +
            printmap_game_map["22,22"] + printmap_game_map["23,22"] +
            printmap_game_map["24,22"] + printmap_game_map[
                "25,22"] + printmap_game_map["26,22"] +
            printmap_game_map["27,22"] + printmap_game_map["28,22"] +
            printmap_game_map["29,22"] + printmap_game_map[
                "30,22"] + printmap_game_map["31,22"] +
            printmap_game_map["32,22"] + printmap_game_map["33,22"] +
            printmap_game_map["34,22"] + printmap_game_map[
                "35,22"] + printmap_game_map["36,22"] +
            printmap_game_map["37,22"] + printmap_game_map["38,22"] +
            printmap_game_map["39,22"] + printmap_game_map[
                "40,22"] + printmap_game_map["41,22"] +
            printmap_game_map["42,22"] + printmap_game_map["43,22"] +
            printmap_game_map["44,22"] + printmap_game_map[
                "45,22"] + printmap_game_map["46,22"] +
            printmap_game_map["47,22"] + printmap_game_map["48,22"] +
            printmap_game_map["49,22"] + printmap_game_map[
                "50,22"] + printmap_game_map["51,22"] +
            printmap_game_map["52,22"] + printmap_game_map["53,22"] +
            printmap_game_map["54,22"] + printmap_game_map["55,22"] +
            printmap_game_map["56,22"] + printmap_game_map[
                "57,22"] + printmap_game_map["58,22"] +
            printmap_game_map["59,22"] + printmap_game_map["60,22"] +
            printmap_game_map["61,22"] + printmap_game_map[
                "62,22"] + printmap_game_map["63,22"] +
            printmap_game_map["64,22"])
        print(
            "23" + "|" +
            printmap_game_map["1,23"] + printmap_game_map["2,23"] +
            printmap_game_map["3,23"] +
            printmap_game_map["4,23"] +
            printmap_game_map["5,23"] + printmap_game_map[
                "6,23"] + printmap_game_map["7,23"] + printmap_game_map[
                "8,23"] + printmap_game_map["9,23"] +
            printmap_game_map["10,23"] + printmap_game_map["11,23"] +
            printmap_game_map["12,23"] + printmap_game_map["13,23"] +
            printmap_game_map["14,23"] + printmap_game_map[
                "15,23"] + printmap_game_map["16,23"] +
            printmap_game_map["17,23"] + printmap_game_map["18,23"] +
            printmap_game_map["19,23"] + printmap_game_map[
                "20,23"] + printmap_game_map["21,23"] +
            printmap_game_map["22,23"] + printmap_game_map["23,23"] +
            printmap_game_map["24,23"] + printmap_game_map[
                "25,23"] + printmap_game_map["26,23"] +
            printmap_game_map["27,23"] + printmap_game_map["28,23"] +
            printmap_game_map["29,23"] + printmap_game_map[
                "30,23"] + printmap_game_map["31,23"] +
            printmap_game_map["32,23"] + printmap_game_map["33,23"] +
            printmap_game_map["34,23"] + printmap_game_map[
                "35,23"] + printmap_game_map["36,23"] +
            printmap_game_map["37,23"] + printmap_game_map["38,23"] +
            printmap_game_map["39,23"] + printmap_game_map[
                "40,23"] + printmap_game_map["41,23"] +
            printmap_game_map["42,23"] + printmap_game_map["43,23"] +
            printmap_game_map["44,23"] + printmap_game_map[
                "45,23"] + printmap_game_map["46,23"] +
            printmap_game_map["47,23"] + printmap_game_map["48,23"] +
            printmap_game_map["49,23"] + printmap_game_map[
                "50,23"] + printmap_game_map["51,23"] +
            printmap_game_map["52,23"] + printmap_game_map["53,23"] +
            printmap_game_map["54,23"] + printmap_game_map["55,23"] +
            printmap_game_map["56,23"] + printmap_game_map[
                "57,23"] + printmap_game_map["58,23"] +
            printmap_game_map["59,23"] + printmap_game_map["60,23"] +
            printmap_game_map["61,23"] + printmap_game_map[
                "62,23"] + printmap_game_map["63,23"] +
            printmap_game_map["64,23"])
        print(
            "24" + "|" +
            printmap_game_map["1,24"] + printmap_game_map["2,24"] +
            printmap_game_map["3,24"] +
            printmap_game_map["4,24"] +
            printmap_game_map["5,24"] + printmap_game_map[
                "6,24"] + printmap_game_map["7,24"] + printmap_game_map[
                "8,24"] + printmap_game_map["9,24"] +
            printmap_game_map["10,24"] + printmap_game_map["11,24"] +
            printmap_game_map["12,24"] + printmap_game_map["13,24"] +
            printmap_game_map["14,24"] + printmap_game_map[
                "15,24"] + printmap_game_map["16,24"] +
            printmap_game_map["17,24"] + printmap_game_map["18,24"] +
            printmap_game_map["19,24"] + printmap_game_map[
                "20,24"] + printmap_game_map["21,24"] +
            printmap_game_map["22,24"] + printmap_game_map["23,24"] +
            printmap_game_map["24,24"] + printmap_game_map[
                "25,24"] + printmap_game_map["26,24"] +
            printmap_game_map["27,24"] + printmap_game_map["28,24"] +
            printmap_game_map["29,24"] + printmap_game_map[
                "30,24"] + printmap_game_map["31,24"] +
            printmap_game_map["32,24"] + printmap_game_map["33,24"] +
            printmap_game_map["34,24"] + printmap_game_map[
                "35,24"] + printmap_game_map["36,24"] +
            printmap_game_map["37,24"] + printmap_game_map["38,24"] +
            printmap_game_map["39,24"] + printmap_game_map[
                "40,24"] + printmap_game_map["41,24"] +
            printmap_game_map["42,24"] + printmap_game_map["43,24"] +
            printmap_game_map["44,24"] + printmap_game_map[
                "45,24"] + printmap_game_map["46,24"] +
            printmap_game_map["47,24"] + printmap_game_map["48,24"] +
            printmap_game_map["49,24"] + printmap_game_map[
                "50,24"] + printmap_game_map["51,24"] +
            printmap_game_map["52,24"] + printmap_game_map["53,24"] +
            printmap_game_map["54,24"] + printmap_game_map["55,24"] +
            printmap_game_map["56,24"] + printmap_game_map[
                "57,24"] + printmap_game_map["58,24"] +
            printmap_game_map["59,24"] + printmap_game_map["60,24"] +
            printmap_game_map["61,24"] + printmap_game_map[
                "62,24"] + printmap_game_map["63,24"] +
            printmap_game_map["64,24"])
        print(
            "25" + "|" +
            printmap_game_map["1,25"] + printmap_game_map["2,25"] +
            printmap_game_map["3,25"] +
            printmap_game_map["4,25"] +
            printmap_game_map["5,25"] + printmap_game_map[
                "6,25"] + printmap_game_map["7,25"] + printmap_game_map[
                "8,25"] + printmap_game_map["9,25"] +
            printmap_game_map["10,25"] + printmap_game_map["11,25"] +
            printmap_game_map["12,25"] + printmap_game_map["13,25"] +
            printmap_game_map["14,25"] + printmap_game_map[
                "15,25"] + printmap_game_map["16,25"] +
            printmap_game_map["17,25"] + printmap_game_map["18,25"] +
            printmap_game_map["19,25"] + printmap_game_map[
                "20,25"] + printmap_game_map["21,25"] +
            printmap_game_map["22,25"] + printmap_game_map["23,25"] +
            printmap_game_map["24,25"] + printmap_game_map[
                "25,25"] + printmap_game_map["26,25"] +
            printmap_game_map["27,25"] + printmap_game_map["28,25"] +
            printmap_game_map["29,25"] + printmap_game_map[
                "30,25"] + printmap_game_map["31,25"] +
            printmap_game_map["32,25"] + printmap_game_map["33,25"] +
            printmap_game_map["34,25"] + printmap_game_map[
                "35,25"] + printmap_game_map["36,25"] +
            printmap_game_map["37,25"] + printmap_game_map["38,25"] +
            printmap_game_map["39,25"] + printmap_game_map[
                "40,25"] + printmap_game_map["41,25"] +
            printmap_game_map["42,25"] + printmap_game_map["43,25"] +
            printmap_game_map["44,25"] + printmap_game_map[
                "45,25"] + printmap_game_map["46,25"] +
            printmap_game_map["47,25"] + printmap_game_map["48,25"] +
            printmap_game_map["49,25"] + printmap_game_map[
                "50,25"] + printmap_game_map["51,25"] +
            printmap_game_map["52,25"] + printmap_game_map["53,25"] +
            printmap_game_map["54,25"] + printmap_game_map["55,25"] +
            printmap_game_map["56,25"] + printmap_game_map[
                "57,25"] + printmap_game_map["58,25"] +
            printmap_game_map["59,25"] + printmap_game_map["60,25"] +
            printmap_game_map["61,25"] + printmap_game_map[
                "62,25"] + printmap_game_map["63,25"] +
            printmap_game_map["64,25"])
        print(
            "26" + "|" +
            printmap_game_map["1,26"] + printmap_game_map["2,26"] +
            printmap_game_map["3,26"] +
            printmap_game_map["4,26"] +
            printmap_game_map["5,26"] + printmap_game_map[
                "6,26"] + printmap_game_map["7,26"] + printmap_game_map[
                "8,26"] + printmap_game_map["9,26"] +
            printmap_game_map["10,26"] + printmap_game_map["11,26"] +
            printmap_game_map["12,26"] + printmap_game_map["13,26"] +
            printmap_game_map["14,26"] + printmap_game_map[
                "15,26"] + printmap_game_map["16,26"] +
            printmap_game_map["17,26"] + printmap_game_map["18,26"] +
            printmap_game_map["19,26"] + printmap_game_map[
                "20,26"] + printmap_game_map["21,26"] +
            printmap_game_map["22,26"] + printmap_game_map["23,26"] +
            printmap_game_map["24,26"] + printmap_game_map[
                "25,26"] + printmap_game_map["26,26"] +
            printmap_game_map["27,26"] + printmap_game_map["28,26"] +
            printmap_game_map["29,26"] + printmap_game_map[
                "30,26"] + printmap_game_map["31,26"] +
            printmap_game_map["32,26"] + printmap_game_map["33,26"] +
            printmap_game_map["34,26"] + printmap_game_map[
                "35,26"] + printmap_game_map["36,26"] +
            printmap_game_map["37,26"] + printmap_game_map["38,26"] +
            printmap_game_map["39,26"] + printmap_game_map[
                "40,26"] + printmap_game_map["41,26"] +
            printmap_game_map["42,26"] + printmap_game_map["43,26"] +
            printmap_game_map["44,26"] + printmap_game_map[
                "45,26"] + printmap_game_map["46,26"] +
            printmap_game_map["47,26"] + printmap_game_map["48,26"] +
            printmap_game_map["49,26"] + printmap_game_map[
                "50,26"] + printmap_game_map["51,26"] +
            printmap_game_map["52,26"] + printmap_game_map["53,26"] +
            printmap_game_map["54,26"] + printmap_game_map["55,26"] +
            printmap_game_map["56,26"] + printmap_game_map[
                "57,26"] + printmap_game_map["58,26"] +
            printmap_game_map["59,26"] + printmap_game_map["60,26"] +
            printmap_game_map["61,26"] + printmap_game_map[
                "62,26"] + printmap_game_map["63,26"] +
            printmap_game_map["64,26"])
        print(
            "27" + "|" +
            printmap_game_map["1,27"] + printmap_game_map["2,27"] +
            printmap_game_map["3,27"] +
            printmap_game_map["4,27"] +
            printmap_game_map["5,27"] + printmap_game_map[
                "6,27"] + printmap_game_map["7,27"] + printmap_game_map[
                "8,27"] + printmap_game_map["9,27"] +
            printmap_game_map["10,27"] + printmap_game_map["11,27"] +
            printmap_game_map["12,27"] + printmap_game_map["13,27"] +
            printmap_game_map["14,27"] + printmap_game_map[
                "15,27"] + printmap_game_map["16,27"] +
            printmap_game_map["17,27"] + printmap_game_map["18,27"] +
            printmap_game_map["19,27"] + printmap_game_map[
                "20,27"] + printmap_game_map["21,27"] +
            printmap_game_map["22,27"] + printmap_game_map["23,27"] +
            printmap_game_map["24,27"] + printmap_game_map[
                "25,27"] + printmap_game_map["26,27"] +
            printmap_game_map["27,27"] + printmap_game_map["28,27"] +
            printmap_game_map["29,27"] + printmap_game_map[
                "30,27"] + printmap_game_map["31,27"] +
            printmap_game_map["32,27"] + printmap_game_map["33,27"] +
            printmap_game_map["34,27"] + printmap_game_map[
                "35,27"] + printmap_game_map["36,27"] +
            printmap_game_map["37,27"] + printmap_game_map["38,27"] +
            printmap_game_map["39,27"] + printmap_game_map[
                "40,27"] + printmap_game_map["41,27"] +
            printmap_game_map["42,27"] + printmap_game_map["43,27"] +
            printmap_game_map["44,27"] + printmap_game_map[
                "45,27"] + printmap_game_map["46,27"] +
            printmap_game_map["47,27"] + printmap_game_map["48,27"] +
            printmap_game_map["49,27"] + printmap_game_map[
                "50,27"] + printmap_game_map["51,27"] +
            printmap_game_map["52,27"] + printmap_game_map["53,27"] +
            printmap_game_map["54,27"] + printmap_game_map["55,27"] +
            printmap_game_map["56,27"] + printmap_game_map[
                "57,27"] + printmap_game_map["58,27"] +
            printmap_game_map["59,27"] + printmap_game_map["60,27"] +
            printmap_game_map["61,27"] + printmap_game_map[
                "62,27"] + printmap_game_map["63,27"] +
            printmap_game_map["64,27"])
        print(
            "28" + "|" +
            printmap_game_map["1,28"] + printmap_game_map["2,28"] +
            printmap_game_map["3,28"] +
            printmap_game_map["4,28"] +
            printmap_game_map["5,28"] + printmap_game_map[
                "6,28"] + printmap_game_map["7,28"] + printmap_game_map[
                "8,28"] + printmap_game_map["9,28"] +
            printmap_game_map["10,28"] + printmap_game_map["11,28"] +
            printmap_game_map["12,28"] + printmap_game_map["13,28"] +
            printmap_game_map["14,28"] + printmap_game_map[
                "15,28"] + printmap_game_map["16,28"] +
            printmap_game_map["17,28"] + printmap_game_map["18,28"] +
            printmap_game_map["19,28"] + printmap_game_map[
                "20,28"] + printmap_game_map["21,28"] +
            printmap_game_map["22,28"] + printmap_game_map["23,28"] +
            printmap_game_map["24,28"] + printmap_game_map[
                "25,28"] + printmap_game_map["26,28"] +
            printmap_game_map["27,28"] + printmap_game_map["28,28"] +
            printmap_game_map["29,28"] + printmap_game_map[
                "30,28"] + printmap_game_map["31,28"] +
            printmap_game_map["32,28"] + printmap_game_map["33,28"] +
            printmap_game_map["34,28"] + printmap_game_map[
                "35,28"] + printmap_game_map["36,28"] +
            printmap_game_map["37,28"] + printmap_game_map["38,28"] +
            printmap_game_map["39,28"] + printmap_game_map[
                "40,28"] + printmap_game_map["41,28"] +
            printmap_game_map["42,28"] + printmap_game_map["43,28"] +
            printmap_game_map["44,28"] + printmap_game_map[
                "45,28"] + printmap_game_map["46,28"] +
            printmap_game_map["47,28"] + printmap_game_map["48,28"] +
            printmap_game_map["49,28"] + printmap_game_map[
                "50,28"] + printmap_game_map["51,28"] +
            printmap_game_map["52,28"] + printmap_game_map["53,28"] +
            printmap_game_map["54,28"] + printmap_game_map["55,28"] +
            printmap_game_map["56,28"] + printmap_game_map[
                "57,28"] + printmap_game_map["58,28"] +
            printmap_game_map["59,28"] + printmap_game_map["60,28"] +
            printmap_game_map["61,28"] + printmap_game_map[
                "62,28"] + printmap_game_map["63,28"] +
            printmap_game_map["64,28"])
        print(
            "29" + "|" +
            printmap_game_map["1,29"] + printmap_game_map["2,29"] +
            printmap_game_map["3,29"] +
            printmap_game_map["4,29"] +
            printmap_game_map["5,29"] + printmap_game_map[
                "6,29"] + printmap_game_map["7,29"] + printmap_game_map[
                "8,29"] + printmap_game_map["9,29"] +
            printmap_game_map["10,29"] + printmap_game_map["11,29"] +
            printmap_game_map["12,29"] + printmap_game_map["13,29"] +
            printmap_game_map["14,29"] + printmap_game_map[
                "15,29"] + printmap_game_map["16,29"] +
            printmap_game_map["17,29"] + printmap_game_map["18,29"] +
            printmap_game_map["19,29"] + printmap_game_map[
                "20,29"] + printmap_game_map["21,29"] +
            printmap_game_map["22,29"] + printmap_game_map["23,29"] +
            printmap_game_map["24,29"] + printmap_game_map[
                "25,29"] + printmap_game_map["26,29"] +
            printmap_game_map["27,29"] + printmap_game_map["28,29"] +
            printmap_game_map["29,29"] + printmap_game_map[
                "30,29"] + printmap_game_map["31,29"] +
            printmap_game_map["32,29"] + printmap_game_map["33,29"] +
            printmap_game_map["34,29"] + printmap_game_map[
                "35,29"] + printmap_game_map["36,29"] +
            printmap_game_map["37,29"] + printmap_game_map["38,29"] +
            printmap_game_map["39,29"] + printmap_game_map[
                "40,29"] + printmap_game_map["41,29"] +
            printmap_game_map["42,29"] + printmap_game_map["43,29"] +
            printmap_game_map["44,29"] + printmap_game_map[
                "45,29"] + printmap_game_map["46,29"] +
            printmap_game_map["47,29"] + printmap_game_map["48,29"] +
            printmap_game_map["49,29"] + printmap_game_map[
                "50,29"] + printmap_game_map["51,29"] +
            printmap_game_map["52,29"] + printmap_game_map["53,29"] +
            printmap_game_map["54,29"] + printmap_game_map["55,29"] +
            printmap_game_map["56,29"] + printmap_game_map[
                "57,29"] + printmap_game_map["58,29"] +
            printmap_game_map["59,29"] + printmap_game_map["60,29"] +
            printmap_game_map["61,29"] + printmap_game_map[
                "62,29"] + printmap_game_map["63,29"] +
            printmap_game_map["64,29"])
        print(
            "30" + "|" +
            printmap_game_map["1,30"] + printmap_game_map["2,30"] +
            printmap_game_map["3,30"] +
            printmap_game_map["4,30"] +
            printmap_game_map["5,30"] + printmap_game_map[
                "6,30"] + printmap_game_map["7,30"] + printmap_game_map[
                "8,30"] + printmap_game_map["9,30"] +
            printmap_game_map["10,30"] + printmap_game_map["11,30"] +
            printmap_game_map["12,30"] + printmap_game_map["13,30"] +
            printmap_game_map["14,30"] + printmap_game_map[
                "15,30"] + printmap_game_map["16,30"] +
            printmap_game_map["17,30"] + printmap_game_map["18,30"] +
            printmap_game_map["19,30"] + printmap_game_map[
                "20,30"] + printmap_game_map["21,30"] +
            printmap_game_map["22,30"] + printmap_game_map["23,30"] +
            printmap_game_map["24,30"] + printmap_game_map[
                "25,30"] + printmap_game_map["26,30"] +
            printmap_game_map["27,30"] + printmap_game_map["28,30"] +
            printmap_game_map["29,30"] + printmap_game_map[
                "30,30"] + printmap_game_map["31,30"] +
            printmap_game_map["32,30"] + printmap_game_map["33,30"] +
            printmap_game_map["34,30"] + printmap_game_map[
                "35,30"] + printmap_game_map["36,30"] +
            printmap_game_map["37,30"] + printmap_game_map["38,30"] +
            printmap_game_map["39,30"] + printmap_game_map[
                "40,30"] + printmap_game_map["41,30"] +
            printmap_game_map["42,30"] + printmap_game_map["43,30"] +
            printmap_game_map["44,30"] + printmap_game_map[
                "45,30"] + printmap_game_map["46,30"] +
            printmap_game_map["47,30"] + printmap_game_map["48,30"] +
            printmap_game_map["49,30"] + printmap_game_map[
                "50,30"] + printmap_game_map["51,30"] +
            printmap_game_map["52,30"] + printmap_game_map["53,30"] +
            printmap_game_map["54,30"] + printmap_game_map["55,30"] +
            printmap_game_map["56,30"] + printmap_game_map[
                "57,30"] + printmap_game_map["58,30"] +
            printmap_game_map["59,30"] + printmap_game_map["60,30"] +
            printmap_game_map["61,30"] + printmap_game_map[
                "62,30"] + printmap_game_map["63,30"] +
            printmap_game_map["64,30"])
        print(
            "31" + "|" +
            printmap_game_map["1,31"] + printmap_game_map["2,31"] +
            printmap_game_map["3,31"] +
            printmap_game_map["4,31"] +
            printmap_game_map["5,31"] + printmap_game_map[
                "6,31"] + printmap_game_map["7,31"] + printmap_game_map[
                "8,31"] + printmap_game_map["9,31"] +
            printmap_game_map["10,31"] + printmap_game_map["11,31"] +
            printmap_game_map["12,31"] + printmap_game_map["13,31"] +
            printmap_game_map["14,31"] + printmap_game_map[
                "15,31"] + printmap_game_map["16,31"] +
            printmap_game_map["17,31"] + printmap_game_map["18,31"] +
            printmap_game_map["19,31"] + printmap_game_map[
                "20,31"] + printmap_game_map["21,31"] +
            printmap_game_map["22,31"] + printmap_game_map["23,31"] +
            printmap_game_map["24,31"] + printmap_game_map[
                "25,31"] + printmap_game_map["26,31"] +
            printmap_game_map["27,31"] + printmap_game_map["28,31"] +
            printmap_game_map["29,31"] + printmap_game_map[
                "30,31"] + printmap_game_map["31,31"] +
            printmap_game_map["32,31"] + printmap_game_map["33,31"] +
            printmap_game_map["34,31"] + printmap_game_map[
                "35,31"] + printmap_game_map["36,31"] +
            printmap_game_map["37,31"] + printmap_game_map["38,31"] +
            printmap_game_map["39,31"] + printmap_game_map[
                "40,31"] + printmap_game_map["41,31"] +
            printmap_game_map["42,31"] + printmap_game_map["43,31"] +
            printmap_game_map["44,31"] + printmap_game_map[
                "45,31"] + printmap_game_map["46,31"] +
            printmap_game_map["47,31"] + printmap_game_map["48,31"] +
            printmap_game_map["49,31"] + printmap_game_map[
                "50,31"] + printmap_game_map["51,31"] +
            printmap_game_map["52,31"] + printmap_game_map["53,31"] +
            printmap_game_map["54,31"] + printmap_game_map["55,31"] +
            printmap_game_map["56,31"] + printmap_game_map[
                "57,31"] + printmap_game_map["58,31"] +
            printmap_game_map["59,31"] + printmap_game_map["60,31"] +
            printmap_game_map["61,31"] + printmap_game_map[
                "62,31"] + printmap_game_map["63,31"] +
            printmap_game_map["64,31"])
        print(
            "32" + "|" +
            printmap_game_map["1,32"] + printmap_game_map["2,32"] +
            printmap_game_map["3,32"] +
            printmap_game_map["4,32"] +
            printmap_game_map["5,32"] + printmap_game_map[
                "6,32"] + printmap_game_map["7,32"] + printmap_game_map[
                "8,32"] + printmap_game_map["9,32"] +
            printmap_game_map["10,32"] + printmap_game_map["11,32"] +
            printmap_game_map["12,32"] + printmap_game_map["13,32"] +
            printmap_game_map["14,32"] + printmap_game_map[
                "15,32"] + printmap_game_map["16,32"] +
            printmap_game_map["17,32"] + printmap_game_map["18,32"] +
            printmap_game_map["19,32"] + printmap_game_map[
                "20,32"] + printmap_game_map["21,32"] +
            printmap_game_map["22,32"] + printmap_game_map["23,32"] +
            printmap_game_map["24,32"] + printmap_game_map[
                "25,32"] + printmap_game_map["26,32"] +
            printmap_game_map["27,32"] + printmap_game_map["28,32"] +
            printmap_game_map["29,32"] + printmap_game_map[
                "30,32"] + printmap_game_map["31,32"] +
            printmap_game_map["32,32"] + printmap_game_map["33,32"] +
            printmap_game_map["34,32"] + printmap_game_map[
                "35,32"] + printmap_game_map["36,32"] +
            printmap_game_map["37,32"] + printmap_game_map["38,32"] +
            printmap_game_map["39,32"] + printmap_game_map[
                "40,32"] + printmap_game_map["41,32"] +
            printmap_game_map["42,32"] + printmap_game_map["43,32"] +
            printmap_game_map["44,32"] + printmap_game_map[
                "45,32"] + printmap_game_map["46,32"] +
            printmap_game_map["47,32"] + printmap_game_map["48,32"] +
            printmap_game_map["49,32"] + printmap_game_map[
                "50,32"] + printmap_game_map["51,32"] +
            printmap_game_map["52,32"] + printmap_game_map["53,32"] +
            printmap_game_map["54,32"] + printmap_game_map["55,32"] +
            printmap_game_map["56,32"] + printmap_game_map[
                "57,32"] + printmap_game_map["58,32"] +
            printmap_game_map["59,32"] + printmap_game_map["60,32"] +
            printmap_game_map["61,32"] + printmap_game_map[
                "62,32"] + printmap_game_map["63,32"] +
            printmap_game_map["64,32"])
    time.sleep(1)


def recvData(required_data):
    data, addr = s.recvfrom(1024)
    if str(required_data) == (data.decode().split(" ", 1))[0]:
        return (data.decode().split(" ", 1))[0]


def getClient(clienttype, playernum):
    message = "request clients"
    s.sendto(message.encode(), server)
    clients = json.loads(recvData("client_list"))
    return tuple(clients[str(clienttype + playernum)])


def checkCoords(coords):
    return player_map[coords]


def checkExists(unit):
    if unit in player_map.values():
        return "yes"
    else:
        return "no"


def getPos(unit_name):
    return list(player_map.keys())[list(player_map.values()).index(
        unit_name)]


def getEnemyNumber():
    if player_num == "1":
        return "2"
    elif player_num == "2":
        return "1"


host = input("Server IP: ")
port = int(input("Server Port: "))
player_num = input("Player Number: ")
enemy_num = getEnemyNumber()
server = (host, port)
printmap = 1
current_map = "player"

# Connect to Server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("localhost", 0))
    clientid = "map" + player_num
    s.sendto(clientid.encode(), server)
except:
    print("Cannot find server!")

# Gen Map
player_map = genmap("empty", "tree", "farm", "water", "stone",
                    "town_center")
unit_data = {
    "town_center": ["X", 1000, 0, 0,
                    "town_center_" + player_num, "None", "None"
                    ]
}
print(player_map)
print("Waiting for game to start...")
start, addr = s.recvfrom(1024)
if start.decode() == "start":
    threading._start_new_thread(print_game_map, (player_map, ))

while True:
    data = (s.recvfrom(1024)).decode()

if data[0] == "checkCoords":
    coords_message = "checkCoordsData" + " " + checkCoords(data[1])
    s.sendto(coords_message.encode(), addr)

elif data[0] == "checkExist":
    exists_message = "checkExistData" + " " + checkExists(data[1])
    s.sendto(exists_message.encode(), addr)

elif data[0] == "getPos":
    pos_message = "getPosData" + " " + (data[1])
    s.sendto(pos_message.encode(), addr)

elif data[0] == "set":
    player_map[data[1]] = data[2]

elif data[0] == "unitData":
    unit_data_data, addr = s.recvfrom(1024)
    unit_data = dict(json.loads(unit_data_data.decode()))

elif data[0] == "stop":
    printmap = 0
elif data[0] == "start":
    printmap = 1
