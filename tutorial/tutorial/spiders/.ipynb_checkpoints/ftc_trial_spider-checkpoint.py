import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'https://www.regulations.gov/document?D=EPA-HQ-OPP-2019-0066-0035',
            'https://www.regulations.gov/document?D=EPA-HQ-OPP-2019-0066-0007',
            'https://www.regulations.gov/document?D=EPA-HQ-OPP-2019-0066-0026',]
    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})


    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").get(),
                'author': quote.css("small.author::text").get(),
                'tags': quote.css("div.tags a.tag::text").getall(),
            }