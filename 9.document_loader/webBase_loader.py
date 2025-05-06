from langchain_community.document_loaders import WebBaseLoader
import os
url = 'https://www.flipkart.com/apple-macbook-air-m2-8-gb-512-gb-ssd-mac-os-monterey-mlxx3hn-a/p/itmc2732c112aeb1?pid=COMGFB2GNWNN9DN8&lid=LSTCOMGFB2GNWNN9DN8OLT676&marketplace=FLIPKART&sattr[]=color&st=color&otracker=pp_reco_Similar%2525252BProducts_4_39.productCard.PMU_HORIZONTAL_Apple%2525252BMacBook%2525252BAIR%2525252BApple%2525252BM2%2525252B-%2525252B%25252525288%2525252BGB%252525252F512%2525252BGB%2525252BSSD%252525252FMac%2525252BOS%2525252BMonterey%2525252529%2525252BMLXX3HN%252525252FA_COMGFB2GNWNN9DN8_productRecommendation%2525252Fsimilar_3'
loader = WebBaseLoader(url)

os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


docs = loader.load()

# print(docs[0].page_content)
print(len(docs))