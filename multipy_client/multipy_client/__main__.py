from .client import retrieve
from time import sleep


def main():
    while True:
        data = retrieve()
        print(data)

        sleep(1)
