import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import os
import shutil
import time
import json




def replace_json_part(file_path):
   
    with open(file_path, 'r') as file:
        json_data = json.load(file)

   
    json_data["reportName"] = "Dr. Garciabiomagnetism Website Report"
    with open(file_path, 'w') as file:
        json.dump(json_data, file)

def replace_css_data(file_path, search_data, replace_data):
    print(file_path)
    with open(file_path, 'r') as file:
        css_content = file.read()
    
    
    updated_css_content = css_content.replace(search_data, replace_data)
    
    with open("test.txt", "w") as f:
        f.write(updated_css_content)
    f.close()
    
    with open(file_path, 'w') as file:
        file.write(updated_css_content)
    file.close()

def replace_title(file_path, old_title, new_title):
    
    with open(file_path, 'r') as file:
        html_content = file.read()
    file.close()
    
    updated_html_content = html_content.replace(old_title, new_title)

    
    with open(file_path, 'w') as file:
        file.write(updated_html_content)
    file.close()

def replace_fav_icon():
    os.remove("docs/favicon.ico")
    os.system("cp Report_Modifier/favicon.ico docs")

def do_modification_on_report():
    file_path = "docs/widgets/summary.json"
    css_file = "docs/styles.css"
    html_file = "docs/index.html"

    logo1 = """background: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNTAwIDUwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczpieD0iaHR0cHM6Ly9ib3h5LXN2Zy5jb20iIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaW5ZTWluIj48cGF0aCBkPSJNMTQyLjE0MyAxNjcuMjE2Yy0xOC45NzEgMjQuNzEzLTI4LjEzOSA1My44NjUtMjguMTE4IDgyLjc4NEgzOC4xOTdjLS4wMzItNDUuMDQ3IDE0LjI0OC05MC40NTcgNDMuNzk4LTEyOC45NTNhMjEzLjg3IDIxMy44NyAwIDAxMTguMjMxLTIwLjgyMWw1My42MjIgNTMuNjIyYTEzNy4zNCAxMzcuMzQgMCAwMC0xMS43MDUgMTMuMzY4em0zMDUuOTAyIDI4Ni41OTZjLTE2LjE0MiAxMi43NzktNDAuMDU3IDkuNDYtNTMuNDE2LTcuNDE0LTQuODU1LTYuMTMzLTcuNjQ3LTEzLjIxNS04LjQ1OS0yMC4zNThoLS4yNjh2LTEzLjU2NmMtMzguNjk4IDMyLjQzNS04Ny4wODYgNDkuMjc5LTEzNS45MDIgNDkuMzE3di03NS44MjZjMzUuMjA0LS4wMjggNzAuMDYxLTEzLjY3MiA5Ni4xNDMtMzkuODIyTDQ1MS4xIDQ1MS4xYTM1Ljk2OCAzNS45NjggMCAwMS0zLjA1NSAyLjcxMnptLTI4MC44NC05NS45NjRjMjQuNzE2IDE4Ljk3MiA1My44NzIgMjguMTQgODIuNzk1IDI4LjExN3Y3NS44MjZjLTQ1LjA1MS4wMzUtOTAuNDY3LTE0LjI0NS0xMjguOTY2LTQzLjc5N2EyMTMuNzI0IDIxMy43MjQgMCAwMS0yMC44MDgtMTguMjJsNTMuNjIxLTUzLjYyMWExMzcuMzc1IDEzNy4zNzUgMCAwMDEzLjM1OCAxMS42OTV6bTIxOC42OTctMTA4LjUwNWguMDVjLS4xOTMtMzQuOTc5LTEzLjgyNS02OS41NjQtMzkuODEtOTUuNDg1bDUzLjYyMS01My42MjFjNDAuNTY3IDQwLjQ2OCA2MS44MDggOTQuNDk0IDYyLjAxOCAxNDkuMTA2aC4wMjJWMjUwaC03NS45MDF6bS01My4xMjctMTA3LjE4OWMtMjQuNzExLTE4Ljk2OC01My44NTktMjguMTM1LTgyLjc3NS0yOC4xMTdWMzguMjA4YzQ1LjA0NC0uMDMgOTAuNDUgMTQuMjUgMTI4Ljk0MiA0My43OTdhMjEzLjYyNiAyMTMuNjI2IDAgMDEyMC44MjEgMTguMjMybC01My42MjEgNTMuNjIxYTEzNy4yIDEzNy4yIDAgMDAtMTMuMzY3LTExLjcwNHptLTE3OC45MjcgMTEuNjk0bC01My42MjItNTMuNjIyQzE0MC44NTkgNTkuNDkzIDE5NS4xNjEgMzguMjQ1IDI1MCAzOC4yMDh2NzUuODI5Yy0zNS4yMDYuMDIzLTcwLjA2NiAxMy42NjMtOTYuMTUyIDM5LjgxMXptMjAzLjk4OSAxNzguOTM4YzE4LjEyNC0yMy42MTIgMjcuMzAxLTUxLjI3NSAyOC4wNjUtNzguOTE2VjI1MGg3NS45MDF2MTc2LjA0aC0uMDIyYy0uMjc2IDkuMy0zLjg5OSAxOC4zMTEtMTAuNjgxIDI1LjA2TDM0Ni4xNDMgMzQ2LjE0M2ExMzcuMzU0IDEzNy4zNTQgMCAwMDExLjY5NC0xMy4zNTd6TTM4LjE5NyAyNTBoNzUuODI4Yy4wMjUgMzUuMjA3IDEzLjY2OCA3MC4wNjggMzkuODIyIDk2LjE1M2wtNTMuNjIxIDUzLjYyMUM1OS40ODggMzU5LjE0MiAzOC4yMzcgMzA0Ljg0IDM4LjE5NyAyNTB6IiBmaWxsPSIjYWFhIi8+PHBhdGggZD0iTTk1OS43MTktMzQ4LjEwMmguMDVjLS4yMjQtNDAuNTU2LTE4LjUxNC04MC41ODMtNTMuMTc3LTEwNy4xODktNTkuNTY0LTQ1LjcyMS0xNDQuOTEzLTM0LjUtMTkwLjYzMiAyNS4wNjItNDUuNzIzIDU5LjU2Mi0zNC41MDIgMTQ0LjkxMSAyNS4wNjIgMTkwLjYzMiA1OS41NjIgNDUuNzIxIDE0NC45MTMgMzQuNSAxOTAuNjMyLTI1LjA2MiAxOC4xMjQtMjMuNjEyIDI3LjMwMS01MS4yNzUgMjguMDY1LTc4LjkxNnptNzUuOTAxIDB2MTc2LjY5N2gtLjAyMmMtLjMxNSAxMC42MS00Ljk4NiAyMC44NDUtMTMuNzM2IDI3Ljc3Mi0xNi4xNDIgMTIuNzc5LTQwLjA1NyA5LjQ2LTUzLjQxNi03LjQxNC00Ljg1NS02LjEzMy03LjY0Ny0xMy4yMTUtOC40NTktMjAuMzU4aC0uMjY4di0xMy41NjZjLTc0LjQxMiA2Mi4zNjgtMTg0LjY1MiA2Ny4wOTMtMjY0Ljg2OCA1LjUyLTkyLjc4LTcxLjIyLTExMC4yNTgtMjA0LjE2Ny0zOS4wMzktMjk2Ljk0NyA3MS4yMTgtOTIuNzgyIDIwNC4xNjktMTEwLjI2IDI5Ni45NDctMzkuMDQyIDU0LjA5OCA0MS41MjYgODIuNTk2IDEwNC4wMzggODIuODM5IDE2Ny4zMzh6IiBmaWxsPSIjOTdjYzY0Ii8+PHBhdGggc3Ryb2tlPSIjMDAwIiBkPSJNMzU3LjcwMiAzNTYuMjMzaDBNMzAxLjcxIDM0OC4wNmgwIi8+PHBhdGggZD0iTS03NzEuODY1IDEyODMuOTA4aC4wMjljLS4xMjgtMjMuMDY5LTEwLjUzMi00NS44MzctMzAuMjQ4LTYwLjk3MWE3Ny41MiA3Ny41MiAwIDAwLTE2LjE3Ni05LjU2MmwxNy40NjktMzkuNDQ2YTEyMC43NjIgMTIwLjc2MiAwIDAxMjQuOTY4IDE0Ljc5NGMzMC43NzIgMjMuNjIxIDQ2Ljk4MSA1OS4xNzkgNDcuMTE5IDk1LjE4NWguMDEzdjg1LjI3OGwtNTguMzg3LTM4LjgwOWM5LjgxMy0xMy4yMSAxNC43ODktMjguNTU4IDE1LjIxMy00My44OTR6IiBmaWxsPSIjOTdjYzY0Ii8+PHBhdGggZD0iTS05MjguNTcgMTI0NC41MDNjLTI2LjAwOCAzMy44OC0xOS42MjUgODIuNDI4IDE0LjI1NiAxMDguNDM1IDMzLjg4IDI2LjAwNyA4Mi40MjkgMTkuNjI0IDEwOC40MzQtMTQuMjU2LjI1NC0uMzMuNTA0LS42NjIuNzUyLS45OTZsNTguMzg2IDM4LjgwOXYxNS4yMzJoLS4wMTNjLS4xNzggNi4wMzUtMi44MzUgMTEuODU3LTcuODEyIDE1Ljc5Ny05LjE4MiA3LjI2OS0yMi43ODUgNS4zODEtMzAuMzg0LTQuMjE3LTIuNzYyLTMuNDg5LTQuMzUtNy41MTctNC44MTItMTEuNThoLS4xNTN2LTcuNzE3Yy00Mi4zMjYgMzUuNDc2LTEwNS4wMzQgMzguMTY0LTE1MC42NjEgMy4xNC01Mi43NzUtNDAuNTExLTYyLjcxNy0xMTYuMTM0LTIyLjIwNi0xNjguOTA5IDM0LjQ2My00NC44OTggOTQuMzQtNTguNzk1IDE0My45NDEtMzcuMDAybC0xNy40NjkgMzkuNDQ2Yy0zMS44MTQtMTMuODk5LTcwLjE2OS00Ljk2LTkyLjI1OSAyMy44MTh6IiBmaWxsPSIjOTdjYzY0Ii8+PHBhdGggZD0iTS00MzIuNzUzIDEwMjkuMDIzYTE3MS4zNzIgMTcxLjM3MiAwIDExLTczLjMyNy0yNTEuNTU5bC02OS4zOTMgMTU2LjY5NHoiIGJ4OnNoYXBlPSJwaWUgMzA1IDI4NSAwIDIwNC4xMyAxMjMuNjEyIDIzLjg4NiAxQDdkYjMyM2NiIiBmaWxsPSIjZmQ1YTNlIi8+PHBhdGggZD0iTS00OTYuMTM4IDkzMC4zMTFoLjAyOWMtLjEyOC0yMy4wNjktMTAuNTMyLTQ1LjgzNy0zMC4yNDgtNjAuOTcxLTMzLjg4MS0yNi4wMDctODIuNDI5LTE5LjYyNC0xMDguNDM1IDE0LjI1Ni0yNi4wMDggMzMuODgtMTkuNjI1IDgyLjQyOCAxNC4yNTYgMTA4LjQzNSAzMy44OCAyNi4wMDcgODIuNDI5IDE5LjYyNCAxMDguNDM0LTE0LjI1NiAxMC4zMS0xMy40MzEgMTUuNTI5LTI5LjE2NiAxNS45NjQtNDQuODg5em00My4xNzQgMHYxMDAuNTA5aC0uMDEzYy0uMTc4IDYuMDM1LTIuODM1IDExLjg1Ny03LjgxMiAxNS43OTctOS4xODIgNy4yNjktMjIuNzg1IDUuMzgxLTMwLjM4NC00LjIxNy0yLjc2Mi0zLjQ4OS00LjM1LTcuNTE3LTQuODEyLTExLjU4aC0uMTUzdi03LjcxN2MtNDIuMzI2IDM1LjQ3Ni0xMDUuMDM0IDM4LjE2NC0xNTAuNjYxIDMuMTQtNTIuNzc1LTQwLjUxMS02Mi43MTctMTE2LjEzNC0yMi4yMDYtMTY4LjkwOSA0MC41MS01Mi43NzYgMTE2LjEzNS02Mi43MTggMTY4LjkwOS0yMi4yMDggMzAuNzcyIDIzLjYyMSA0Ni45ODEgNTkuMTc5IDQ3LjExOSA5NS4xODV6IiBmaWxsPSIjOTdjYzY0Ii8+PHBhdGggZD0iTS01MDUuNTY0IDE0OTkuMDUyYTE3MS4zNzIgMTcxLjM3MiAwIDExMTE4LjY4NCA3OS42N2wyMi41MzUtMTM4Ljc2N2EzMC43ODYgMzAuNzg2IDAgMTAtMjEuMzIxLTE0LjMxM3oiIGJ4OnNoYXBlPSJwaWUgMzA1IDI4NSAzNi42NzEgMjA0LjEzIDIzOC41MjIgMTg5LjIyNCAxQGI5NzQ0OTBhIiBmaWxsPSIjZmQ1YTNlIi8+PHBhdGggZD0iTS0yODIuMTI5IDE0MDkuMDQ4aC4wMjljLS4xMjgtMjMuMDY5LTEwLjUzMi00NS44MzctMzAuMjQ4LTYwLjk3MS0zMy44ODEtMjYuMDA3LTgyLjQyOS0xOS42MjQtMTA4LjQzNSAxNC4yNTYtMjYuMDA4IDMzLjg4LTE5LjYyNSA4Mi40MjggMTQuMjU2IDEwOC40MzUgMzMuODggMjYuMDA3IDgyLjQyOSAxOS42MjQgMTA4LjQzNC0xNC4yNTYgMTAuMzEtMTMuNDMxIDE1LjUyOS0yOS4xNjYgMTUuOTY0LTQ0Ljg4OXptNDMuMTc0IDB2MTAwLjUwOWgtLjAxM2MtLjE3OCA2LjAzNS0yLjgzNSAxMS44NTctNy44MTIgMTUuNzk3LTkuMTgyIDcuMjY5LTIyLjc4NSA1LjM4MS0zMC4zODQtNC4yMTctMi43NjItMy40ODktNC4zNS03LjUxNy00LjgxMi0xMS41OGgtLjE1M3YtNy43MTdjLTQyLjMyNiAzNS40NzYtMTA1LjAzNCAzOC4xNjQtMTUwLjY2MSAzLjE0LTUyLjc3NS00MC41MTEtNjIuNzE3LTExNi4xMzQtMjIuMjA2LTE2OC45MDkgNDAuNTEtNTIuNzc2IDExNi4xMzUtNjIuNzE4IDE2OC45MDktMjIuMjA4IDMwLjc3MiAyMy42MjEgNDYuOTgxIDU5LjE3OSA0Ny4xMTkgOTUuMTg1ek0tODgwLjIwOCAxNzA2LjM2OHYxMDAuNTA5aC0uMDEzYy0uMTc4IDYuMDM1LTIuODM1IDExLjg1Ny03LjgxMiAxNS43OTctOS4xODIgNy4yNjktMjIuNzg1IDUuMzgxLTMwLjM4NC00LjIxNy0yLjc2Mi0zLjQ4OS00LjM1LTcuNTE3LTQuODEyLTExLjU4aC0uMTUzdi03LjcxN2MtNDIuMzI2IDM1LjQ3Ni0xMDUuMDM0IDM4LjE2NC0xNTAuNjYxIDMuMTQtMTUuOTYzLTEyLjI1My0yOC4wMDctMjcuNzE5LTM1LjkyMS00NC43OTNsMzguMzc4LTE3Ljc3M2MyNS4yODUgNTQuNTk2IDEwMC4xOTEgNjEuMzQ3IDEzNC44MzEgMTIuMTUxIDM0LjYzOS00OS4xOTUgMy4wMzMtMTE3LjQ0MS01Ni44OTItMTIyLjg0Mi0zMC4wMzQtMi43MDctNTguOTQ2IDEyLjEwNi03NC4yOTQgMzguMDYzbC0zNi41MTEtMjEuNTg4YTEyMS43OSAxMjEuNzkgMCAwMTguMjAzLTEyLjEyN2M0MC41MS01Mi43NzYgMTE2LjEzNS02Mi43MTggMTY4LjkwOS0yMi4yMDggMzAuNzcyIDIzLjYyMSA0Ni45ODEgNTkuMTc5IDQ3LjExOSA5NS4xODV6IiBmaWxsPSIjOTdjYzY0Ii8+PHBhdGggZD0iTS05MzMuNjA5IDkzMC4zMTFoLjAyOWMtLjEyOC0yMy4wNjktMTAuNTMyLTQ1LjgzNy0zMC4yNDgtNjAuOTcxLTE0Ljg4NC0xMS40MjUtMzIuNTk5LTE2LjU5OS00OS45OS0xNS45MzdsLTEuNjMtNDMuMTAxYzI3LjA5NC0xLjAzNSA1NC42OTMgNy4wMjUgNzcuODgxIDI0LjgyNCAzMC43NzIgMjMuNjIxIDQ2Ljk4MSA1OS4xNzkgNDcuMTE5IDk1LjE4NWguMDEzdjgwLjA1OGwtNTYuMDA0LTM2Ljk4MWE3Ni45MTYgNzYuOTE2IDAgMDAxMi44My00MC41MDJ6IiBmaWxsPSIjZmQ1YTNlIi8+PHBhdGggZD0iTS05NDkuNTc5IDk3Ny43OTlhNzkuMjMxIDc5LjIzMSAwIDAwMy4xMzQtNC4zODZsNTYuMDA0IDM2Ljk4djIwLjQ1MWgtLjAxM2MtLjE3OCA2LjAzNC0yLjgzNSAxMS44NTctNy44MTIgMTUuNzk3LTkuMTgyIDcuMjY4LTIyLjc4NSA1LjM4MS0zMC4zODQtNC4yMTctMi43NjItMy40ODktNC4zNS03LjUxNy00LjgxMi0xMS41OGgtLjE1M3YtNy43MTdjLTI3LjExIDIyLjcyMy02Mi41ODIgMzEuOTk0LTk2LjU3MiAyNi41Mmw2LjkxNS00Mi41ODFjMjcuMTUyIDQuMzY4IDU1Ljc3NC01LjkyMyA3My42OTMtMjkuMjY3eiIgZmlsbD0iI2ZmZDA1MCIvPjxwYXRoIGQ9Ik0tMTA1OC4wOCA5OTEuOTVjMTAuNTM1IDguMDg3IDIyLjQ4OCAxMy4wNDIgMzQuNzQxIDE1LjAxMmwtNi45MTUgNDIuNThjLTE5LjA3Ny0zLjA3Mi0zNy42ODctMTAuNzg5LTU0LjA4OS0yMy4zOC0xMi4wNC05LjI0Mi0yMS44NS0yMC4zMTEtMjkuMzQxLTMyLjUybDM2Ljc5My0yMi41MjhjNC44MDUgNy44MjIgMTEuMDk1IDE0LjkxMyAxOC44MTEgMjAuODM2eiIgZmlsbD0iI2FhYSIvPjxwYXRoIGQ9Ik0tMjcyLjQ4OCAxMTE4Ljc5N2ExNS43NzUgMTUuMjI0IDcxLjAyOCAxMDguNDM2LTguMTU3bDIuMDEgNS4zMjVhMTAuMDgzIDkuNzMxIDcxLjAyOCAxMS01LjM5MiA1LjIxNHoiIGJ4OnNoYXBlPSJwaWUgMzA1IDI4NSAxMzAuNDc5IDIwNC4xMyAzMTYuODExIDI3MS43NzIgMUBkYzU3YmZhNSIvPjxwYXRoIGQ9Ik0tMTA3Mi4yMTQgODgzLjY2MWMtMjAuMDU5IDI2LjEzLTIwLjg1IDYwLjk4NS00LjYxOSA4Ny40OTVsLS4wMTcuMDExLTM2Ljc3NiAyMi41MTdjLTI1LjI3OC00MS4yOTMtMjQuMDQ0LTk1LjU4NCA3LjE5OS0xMzYuMjg1IDIyLjcwOS0yOS41ODUgNTYuNDUzLTQ1LjcxIDkxLjAyLTQ3LjAzMmwxLjYzIDQzLjA4OS4wMDIuMDEyYy0yMi4xOTQuODQ3LTQzLjg1OSAxMS4xOTktNTguNDM5IDMwLjE5M3oiIGZpbGw9IiM5N2NjNjQiLz48cGF0aCBkPSJNLTMwOC4yNjIgMTEzNS43NTNoLjAwNmExNi44NzQgMTYuODc0IDAgMDAtNi42MS0xMy4zMjYgMTYuODQgMTYuODQgMCAwMC0xMC45MjYtMy40ODJsLS4zNTctOS40MmEyNi4yMjYgMjYuMjI2IDAgMDExNy4wMjMgNS40MjVjNi43MjQgNS4xNjMgMTAuMjY2IDEyLjkzNCAxMC4yOTcgMjAuODAzaC4wMDJ2MTcuNDk3bC0xMi4yMzktOC4wODJhMTYuODE1IDE2LjgxNSAwIDAwMi44MDQtOC44NTJ6IiBmaWxsPSIjZmQ1YTNlIi8+PHBhdGggZD0iTS0zMTEuNzUzIDExNDYuMTMyYy4yNDEtLjMxNC40Ny0uNjM0LjY4NS0uOTU5bDEyLjI0IDguMDgydjQuNDdoLS4wMDJjLS4wNCAxLjMxOS0uNjE5IDIuNTkxLTEuNzA4IDMuNDUyLTIuMDA3IDEuNTg5LTQuOTc5IDEuMTc3LTYuNjQxLS45MjFhNC45ODggNC45ODggMCAwMS0xLjA1MS0yLjUzMWgtLjAzNHYtMS42ODdjLTUuOTI1IDQuOTY2LTEzLjY3NyA2Ljk5My0yMS4xMDYgNS43OTdsMS41MTItOS4zMDdjNS45MzUuOTU1IDEyLjE5LTEuMjk0IDE2LjEwNS02LjM5NnoiIGZpbGw9IiNmZmQwNTAiLz48cGF0aCBkPSJNLTMzNS40NjUgMTE0OS4yMjVhMTYuODMgMTYuODMgMCAwMDcuNTkyIDMuMjgxbC0xLjUxMiA5LjMwNmEyNi4yMTYgMjYuMjE2IDAgMDEtMTEuODIxLTUuMTEgMjYuMjYgMjYuMjYgMCAwMS02LjQxMi03LjEwOGw4LjA0MS00LjkyM2ExNi44NjQgMTYuODY0IDAgMDA0LjExMiA0LjU1NHoiIGZpbGw9IiNhYWEiLz48cGF0aCBkPSJNLTMzOC41NTQgMTEyNS41NThjLTQuMzg1IDUuNzExLTQuNTU4IDEzLjMyNy0xLjAxIDE5LjEyMmwtLjAwNC4wMDItOC4wMzggNC45MjJjLTUuNTI0LTkuMDI1LTUuMjU1LTIwLjg5MSAxLjU3NC0yOS43ODYgNC45NjMtNi40NjYgMTIuMzM4LTkuOTkgMTkuODkzLTEwLjI3OWwuMzU2IDkuNDE3di4wMDJjLTQuODUxLjE4Ni05LjU4NiAyLjQ0OC0xMi43NzEgNi42eiIgZmlsbD0iIzk3Y2M2NCIvPjxwYXRoIGQ9Ik0xNjcuMjA1IDM1Ny44NDhjMjQuNzE2IDE4Ljk3MiA1My44NzIgMjguMTQgODIuNzk1IDI4LjExN3Y3NS44MjZjLTQ1LjA1MS4wMzUtOTAuNDY3LTE0LjI0NS0xMjguOTY2LTQzLjc5N2EyMTMuNzI0IDIxMy43MjQgMCAwMS0yMC44MDgtMTguMjJsNTMuNjIxLTUzLjYyMWExMzcuMzc1IDEzNy4zNzUgMCAwMDEzLjM1OCAxMS42OTV6IiBmaWxsPSIjYWFhIi8+PHBhdGggZD0iTTM4NS45MDIgMjQ5LjM0M2guMDVjLS4xOTMtMzQuOTc5LTEzLjgyNS02OS41NjQtMzkuODEtOTUuNDg1bDUzLjYyMS01My42MjFjNDAuNTY3IDQwLjQ2OCA2MS44MDggOTQuNDk0IDYyLjAxOCAxNDkuMTA2aC4wMjJWMjUwaC03NS45MDF6IiBmaWxsPSIjZDM1ZWJlIi8+PHBhdGggZD0iTTM4LjE5Ny01MTguODI3bC0yNTAgMjUwaDI1MHYtMjUweiIgZmlsbD0iIzU2NTJhNyIvPjxwYXRoIGQ9Ik0zMzIuNzc1IDE0Mi4xNTRjLTI0LjcxMS0xOC45NjgtNTMuODU5LTI4LjEzNS04Mi43NzUtMjguMTE3VjM4LjIwOGM0NS4wNDQtLjAzIDkwLjQ1IDE0LjI1IDEyOC45NDIgNDMuNzk3YTIxMy42MjYgMjEzLjYyNiAwIDAxMjAuODIxIDE4LjIzMmwtNTMuNjIxIDUzLjYyMWExMzcuMiAxMzcuMiAwIDAwLTEzLjM2Ny0xMS43MDR6IiBmaWxsPSIjZmQ1YTNlIi8+PHBhdGggZD0iTTM1Ny44MzcgMzMyLjc4NmMxOC4xMjQtMjMuNjEyIDI3LjMwMS01MS4yNzUgMjguMDY1LTc4LjkxNlYyNTBoNzUuOTAxdjE3Ni4wNGgtLjAyMmMtLjI3NiA5LjMtMy44OTkgMTguMzExLTEwLjY4MSAyNS4wNmEzNS45NjggMzUuOTY4IDAgMDEtMy4wNTUgMi43MTJjLTE2LjE0MiAxMi43NzktNDAuMDU3IDkuNDYtNTMuNDE2LTcuNDE0LTQuODU1LTYuMTMzLTcuNjQ3LTEzLjIxNS04LjQ1OS0yMC4zNThoLS4yNjh2LTEzLjU2NmMtMzguNjk4IDMyLjQzNS04Ny4wODYgNDkuMjc5LTEzNS45MDIgNDkuMzE3di03NS44MjZjMzUuMjA0LS4wMjggNzAuMDYxLTEzLjY3MiA5Ni4xNDMtMzkuODIyYTEzNy4zNTQgMTM3LjM1NCAwIDAwMTEuNjk0LTEzLjM1N3oiIGZpbGw9IiNmZmQwNTAiLz48cGF0aCBkPSJNMTUzLjg0NyAzNDYuMTUzbC01My42MjEgNTMuNjIxQzU5LjQ4OCAzNTkuMTQyIDM4LjIzNyAzMDQuODQgMzguMTk3IDI1MGMtLjAzMi00NS4wNDcgMTQuMjQ4LTkwLjQ1NyA0My43OTgtMTI4Ljk1M2EyMTMuODcgMjEzLjg3IDAgMDExOC4yMzEtMjAuODIxQzE0MC44NTkgNTkuNDkzIDE5NS4xNjEgMzguMjQ1IDI1MCAzOC4yMDh2NzUuODI5Yy0zNS4yMDYuMDIzLTcwLjA2NiAxMy42NjMtOTYuMTUyIDM5LjgxMWExMzcuMzQgMTM3LjM0IDAgMDAtMTEuNzA1IDEzLjM2OGMtMTguOTcxIDI0LjcxMy0yOC4xMzkgNTMuODY1LTI4LjExOCA4Mi43ODQuMDI1IDM1LjIwNyAxMy42NjggNzAuMDY4IDM5LjgyMiA5Ni4xNTN6IiBmaWxsPSIjOTdjYzY0Ii8+PC9zdmc+) no-repeat 0"""

    logo_name = """.side-nav__brand-text {
        padding-left: 16px
    }"""


    logo_url = """margin-right: 10px;
    border-radius: 20px;
    height: 90px;
    background: url(https://biomag.s3.us-east-2.amazonaws.com/logo-min.jpg);
    background-size: contain;
    background-repeat: no-repeat;"""


    logo_name_hidden = """.side-nav__brand-text {
        visibility: hidden;
        padding-left: 16px
    }
    """

    new_title = "<title>Dr. Garciabiomagnetism Report</title>"
    old_title = "<title>Allure Report</title>"


    replace_json_part(file_path)
    replace_css_data(css_file, logo1, logo_url)
    replace_css_data(css_file, logo_name, logo_name_hidden)
    replace_title(html_file,old_title,new_title)
    replace_fav_icon()


@pytest.fixture(scope= 'class')
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.page_load_strategy = 'eager'

    web_driver = uc.Chrome(use_subprocess= True, options= options, version_main= 113)
    web_wait = WebDriverWait(web_driver,10)

    request.cls.driver = web_driver
    request.cls.wait = web_wait

    yield
    web_driver.close()




@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
        report_dir = "Allure_Generated_Files"
        allure_dir = "docs"
        # shutil.rmtree(allure_dir, ignore_errors=True)
        allure_cmd = f"allure generate {report_dir} --clean"
        remove_docs_cmd = f"rm -rf docs"
        rename_allure_report = f"mv allure-report {allure_dir}"

        git_status = "git status"
        git_add = "git add ."
        git_commit = "git commit -m 'auto commit by pytest' "
        git_push = "git push origin2 master"
      
        os.system(allure_cmd)
        
        os.system(remove_docs_cmd)
        time.sleep(5)
        os.system(rename_allure_report)
        time.sleep(3)
        do_modification_on_report()
        os.system(git_status)
        os.system(git_add)
        os.system(git_commit)
        os.system(git_push)

       
        
        print("Report Hosted : https://drgarciabiomagnetismtesting.github.io/allure_report/")

def pytest_configure(config):
    
    print("Initializing pytest...")
    delete_allure_report = "rm -rf Allure_Generated_Files"
    create_allure_report = "mkdir Allure_Generated_Files"
    copy_system_environment = "cp Data_Files/environment.properties Allure_Generated_Files"
    os.system(delete_allure_report)
    time.sleep(5)
    os.system(create_allure_report)
    os.system(copy_system_environment)
    

