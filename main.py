from alessandro_c_mod1_atsiskaitymas.web_crawler import  web_crawler, save_to_csv

if __name__ == "__main__":
  #CSV
    data = web_crawler()
    save_to_csv(data)

  #DICT
    # data = web_crawler(url="https://www.gintarine.lt/maistas-ir-papildai-sportininkams", timeout=60, output_format="dict")
    # print(data)