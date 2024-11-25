from alessandro_c_mod1_atsiskaitymas.web_crawler import  web_crawler

if __name__ == "__main__":
  #CSV
    web_crawler(url="https://www.gintarine.lt/maistas-ir-papildai-sportininkams", timeout=60, output_format="csv")

    # data = web_crawler(url="https://www.gintarine.lt/maistas-ir-papildai-sportininkams", timeout=60, output_format="dict")
    # print(data)