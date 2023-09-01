# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'https://www.nintendo.com/es-mx/store/games/nintendo-switch-games/#sort=df',
    ]

    def parse(self, response): 
        for game in response.css('div.difXoz > div'):
            yield {
            	'image' : game.css('div.hKftmL > a > div > div > div > div > img::attr(src)').extract_first(),
            	#'image2' : game.css('div.PjcqG > img::attr(src)').extract_first(),
                #'image3' : game.css('img::attr(src)').extract_first(),
                'platform' : game.css('div.dttZIF > div > span::text').extract_first(),
                'price'	: game.css('span.dexgmS::text').extract_first(),
                'release'	: game.css('div.YnCBi::text').extract_first(),
				'title' : game.css('h2.bKKnvO::text').extract_first(),
            	'link'  : game.css("a.cjBJsu::attr(href)").extract_first(),
            }

"""            for game in response.xpath('//*[class="difXoz"]/div'):
                   	yield {
						#'image3' : game.xpath('//div[5]/div/a/div[1]/div/div/div/img/@src').extract_first(),
						#'platform' : game.xpath('//div[1]/div/a/div[2]/div/div[4]/div/span/text()').extract_first(),
						#'price'	: game.xpath('//div[1]/div/a/div[2]/div/div[3]/div/div/span/text()').extract_first(),
						#'release'	: game.xpath('//div[1]/div/a/div[2]/div/div[1]/div/text()').extract_first(),
						'title' : game.xpath('//div[1]/div/a/div[2]/div/div[1]/h2/text()').extract_first(),
						#'link'  : game.xpath('//div[1]/div/a/@href').extract_first(),
					} """