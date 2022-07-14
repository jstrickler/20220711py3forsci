#!/usr/bin/env python
import openpyxl as px

def main():
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb['US Presidents']  # <.>
    headers = next(ws.values)   # <.>
    # print("headers: {}".format(headers))

    for row in ws.values:  # <.>
        print(row)   # <.>


if __name__ == '__main__':
    main()
