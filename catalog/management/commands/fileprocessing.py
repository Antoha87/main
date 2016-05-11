# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from slugify import slugify
import xlrd
from decimal import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from catalog.models import FileProcessing, Goods, GoodsVariation, Location, Category
from pages.models import Brand


class Command(BaseCommand):

    def handle(self, *args, **options):
        fileprocessing = FileProcessing.objects.first()
        if fileprocessing:

            rb = xlrd.open_workbook(fileprocessing.fileprocessing.path, formatting_info=False)
            sheet = rb.sheet_by_index(0)
            for rownum in range(sheet.nrows):
                if not rownum == 0:
                    g = Goods()
                    b = Brand()
                    c = Category()
                    row = sheet.row_values(rownum)
                    try:
                        good = Goods.objects.get(model=row[0])
                        good.price = Decimal(row[11])
                        good.currence = row[15]
                        good.stock = row[10]
                        good.save()
                    except Goods.DoesNotExist:
                        g.model = row[0]
                        g.kod = row[1]
                        g.post = row[2]
                        try:
                            brand = Brand.objects.get(name=row[13])
                            g.brand = brand
                        except Brand.DoesNotExist:
                            b.name = row[13]
                            b.slug = slugify(row[13])
                            b.save()
                            g.brand = Brand.objects.get(name=row[13])

                        g.article = row[4]
                        g.soput = row[5]

                        cat_list = row[7].split("/")
                        for index, cat in enumerate(cat_list):
                            obj, created = Category.objects.get_or_create(
                                    name=cat,
                                    slug=slugify(cat),
                                    activate=True)
                            if index >= 1 and created:
                                prev_cat = Category.objects.get(name=cat_list[index - 1])
                                obj.move_to(prev_cat)


                        #cat_obj = Category.objects.get(name=cat_list[-1])

                        g.name = row[8]
                        g.torg = row[9]
                        g.stock = row[10]
                        g.price = Decimal(row[11])
                        g.diskont = int(row[12])
                        g.collection = row[14]
                        g.currence = row[15]
                        g.youtube_url = row[19]
                        g.description = row[20]
                        g.izm = row[23]
                        g.garanty = int(row[25])
                        g.krat = row[22]
                        g.gab = row[24]
                        g.ves = row[26]
                        g.type = row[27]
                        g.vid = row[28]
                        g.color = row[29]
                        g.save()
                        g.category.add(obj)
                        location_list = row[3].split(",")
                        for loc in location_list:
                            loc_obj = Location.objects.get(location=loc)
                            g.location.add(loc_obj)

